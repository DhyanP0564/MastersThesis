#!/usr/bin/env python3
"""thesis_lint: check the thesis .tex against the Standing Facts and the controlled vocabulary.

Usage (Python >= 3.11 for tomllib, stdlib only: `conda activate pihm` has it), from the repository root:
  python tools/thesis_lint.py                        lint the default file set ([settings] in lint_rules.toml)
  python tools/thesis_lint.py --files 5_descriptor   one chapter (a glob; a bare word matches as a substring)
  python tools/thesis_lint.py --rule as-printed,spell-*   only these rules (comma-separated ids or globs)
  python tools/thesis_lint.py --severity info        also show info hits (default: warn and error)
  python tools/thesis_lint.py --strict               warnings fail too;  --list prints every rule
Output: hits grouped by file as `line:col severity rule-id`, the rule's message on its first hit in each
file, and a ~80-character excerpt with the hit in «guillemets»; then a count by rule and severity.
Exit status: 0 clean, 1 if any error (or any warning with --strict), 2 for a bad rule file or usage.
Rules live in tools/lint_rules.toml (fields documented at its top): add or edit a rule there, not here.
Before matching, comments are stripped (\\% respected) and, per the rule's `view`, reference keys
(\\res, \\label, \\Cref, \\cite, ...) and then maths are masked; line and column numbers are kept.
Suppress a hit with `% lint-allow: <rule-id>[, <rule-id>]` on its line; prefer tightening the rule.
"""
from __future__ import annotations

import argparse
import bisect
import fnmatch
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    print("thesis_lint: needs Python >= 3.11 for tomllib (try `conda activate pihm`)", file=sys.stderr)
    sys.exit(2)

SEVERITIES = ("info", "warn", "error")
VIEWS = ("raw", "text", "prose")
SCOPES = ("sentence", "line")
RULE_FIELDS = {"id", "regex", "severity", "message", "view", "scope", "also", "unless", "exclude",
               "not_after", "files", "allow_files", "allow_scopes"}
SCOPE_FIELDS = {"files", "section", "paragraph"}
MASK = "\x1a"  # neither a word character nor whitespace, so masked spans never join two words
ALLOW_RE = re.compile(r"lint-allow:\s*([\w*?\-]+(?:\s*,\s*[\w*?\-]+)*)")
SECTION_RE = re.compile(r"\\(part|chapter|section|subsection|subsubsection)\*?\s*[\[{]")
SECTION_LEVEL = {"part": -1, "chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3}
LABEL_RE = re.compile(r"\\label\s*\{([^}]*)\}")
TOKEN_RE = re.compile(r"\\(?:([A-Za-z]+)\*?|.)", re.S)
ABBREVIATIONS = {"al", "e.g", "i.e", "cf", "vs", "Fig", "Figs", "Eq", "Eqs", "Ref", "Refs", "Sec", "Secs",
                 "Ch", "App", "approx", "resp", "No", "Tab", "etc", "Prof", "Dr", "viz", "ca", "Thm", "Prop"}


class ConfigError(Exception):
    pass


@dataclass
class Rule:
    id: str
    regex: re.Pattern
    severity: str
    message: str
    view: str = "prose"
    scope: str = "sentence"
    also: re.Pattern | None = None
    unless: re.Pattern | None = None
    exclude: re.Pattern | None = None
    not_after: re.Pattern | None = None
    files: list[str] = field(default_factory=list)
    allow_files: list[str] = field(default_factory=list)
    allow_scopes: list[dict] = field(default_factory=list)


@dataclass
class Config:
    rules: list[Rule]
    files: list[str]
    exclude: list[str]
    excerpt: int
    keys: dict[str, int]
    prose: dict[str, int]
    env_args: dict[str, int]
    code_envs: list[str]
    math_envs: list[str]


@dataclass
class Hit:
    path: str
    line: int
    col: int
    rule: Rule
    excerpt: str


# ---------------------------------------------------------------- configuration

def load_config(path: Path) -> Config:
    try:
        data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ConfigError(f"{path}: {exc}") from exc
    defs = data.get("defs", {})
    settings = data.get("settings", {})
    mask = data.get("mask", {})

    def compile_(pattern, where, anchor_end=False):
        if pattern is None:
            return None
        if not isinstance(pattern, str):
            raise ConfigError(f"{where}: a pattern must be a string")

        def sub(m):
            if m[1] not in defs:
                raise ConfigError(f"{where}: unknown <<{m[1]}>> (define it under [defs])")
            return defs[m[1]]

        pattern = re.sub(r"<<(\w+)>>", sub, pattern)
        if anchor_end:  # keep leading global flags such as (?i) in front
            flags = re.match(r"(?:\(\?[aiLmsux]+\))*", pattern).group(0)
            pattern = f"{flags}(?:{pattern[len(flags):]})\\Z"
        try:
            return re.compile(pattern, re.M)
        except re.error as exc:
            raise ConfigError(f"{where}: bad regex ({exc}): {pattern}") from exc

    rules, seen = [], set()
    for k, entry in enumerate(data.get("rule", [])):
        rid = entry.get("id", f"#{k + 1}")
        where = f"rule {rid}"
        unknown = set(entry) - RULE_FIELDS
        if unknown:
            raise ConfigError(f"{where}: unknown field(s) {sorted(unknown)}")
        for req in ("id", "regex", "severity", "message"):
            if req not in entry:
                raise ConfigError(f"{where}: missing `{req}`")
        if rid in seen:
            raise ConfigError(f"{where}: duplicate id")
        seen.add(rid)
        if entry["severity"] not in SEVERITIES:
            raise ConfigError(f"{where}: severity must be one of {SEVERITIES}")
        if entry.get("view", "prose") not in VIEWS:
            raise ConfigError(f"{where}: view must be one of {VIEWS}")
        if entry.get("scope", "sentence") not in SCOPES:
            raise ConfigError(f"{where}: scope must be one of {SCOPES}")
        scopes = []
        for s in entry.get("allow_scopes", []):
            if not isinstance(s, dict) or not s or set(s) - SCOPE_FIELDS:
                raise ConfigError(f"{where}: each allow_scopes entry is a table of {sorted(SCOPE_FIELDS)}")
            scopes.append({"files": s.get("files"), "section": s.get("section"),
                           "paragraph": compile_(s.get("paragraph"), where)})
        rules.append(Rule(
            id=rid, regex=compile_(entry["regex"], where), severity=entry["severity"],
            message=entry["message"].strip(), view=entry.get("view", "prose"),
            scope=entry.get("scope", "sentence"), also=compile_(entry.get("also"), where),
            unless=compile_(entry.get("unless"), where), exclude=compile_(entry.get("exclude"), where),
            not_after=compile_(entry.get("not_after"), where, anchor_end=True),
            files=list(entry.get("files", [])), allow_files=list(entry.get("allow_files", [])),
            allow_scopes=scopes))
    if not rules:
        raise ConfigError(f"{path}: no [[rule]] entries")
    return Config(rules=rules, files=list(settings.get("files", ["**/*.tex"])),
                  exclude=list(settings.get("exclude", [])), excerpt=int(settings.get("excerpt", 80)),
                  keys=dict(mask.get("keys", {})), prose=dict(mask.get("prose", {})),
                  env_args=dict(mask.get("env_args", {})), code_envs=list(mask.get("code_envs", [])),
                  math_envs=list(mask.get("math_envs", [])))


# ---------------------------------------------------------------- views

def strip_comment(line: str) -> tuple[str, str]:
    """Split a line into its code and its comment, respecting \\% (and \\\\%, a comment)."""
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\":
            i += 2
            continue
        if c == "%":
            return line[:i], line[i + 1:]
        i += 1
    return line, ""


def group_end(s: str, i: int, close: str) -> int:
    """s[i] opens a group ('{' or '['); return the index past its close, or -1."""
    depth, j = 0, i + 1
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "\n" and s.startswith("\n\n", j):
            return -1  # a group never crosses a blank line
        if c == "{":
            depth += 1
        elif c == "}":
            if close == "}" and depth == 0:
                return j + 1
            depth -= 1
        elif c == close and depth == 0:
            return j + 1
        j += 1
    return -1


def fill(buf: list, a: int, b: int) -> None:
    for i in range(a, b):
        if buf[i] != "\n":
            buf[i] = MASK


def mask_macros(s: str, buf: list, spec: dict[str, int], env_args: dict[str, int]) -> None:
    """Mask every optional argument and the first `spec[name]` mandatory ones of each listed macro."""
    for m in TOKEN_RE.finditer(s):
        name = m.group(1)
        if not name or name not in spec:
            continue
        j = m.end()
        if name in ("verb", "lstinline") and j < len(s) and s[j] not in "{[":
            end = s.find(s[j], j + 1) if j < len(s) else -1
            if end > 0:
                fill(buf, j, end + 1)
            continue
        wanted = spec[name]
        env = None
        while True:
            k = j
            while k < len(s) and s[k] in " \t":
                k += 1
            if k < len(s) and s[k] == "[":
                end = group_end(s, k, "]")
                if end < 0:
                    break
                fill(buf, k, end)
                j = end
                continue
            if wanted > 0 and k < len(s) and s[k] == "{":
                end = group_end(s, k, "}")
                if end < 0:
                    break
                if name == "begin" and env is None:
                    env = s[k + 1:end - 1].strip()
                    wanted += env_args.get(env, 0)
                fill(buf, k + 1, end - 1)
                wanted -= 1
                j = end
                continue
            break


def mask_envs(s: str, buf: list, envs: list[str]) -> None:
    if not envs:
        return
    names = "|".join(re.escape(e) for e in sorted(envs, key=len, reverse=True))
    for m in re.finditer(r"\\begin\s*\{(" + names + r")\}", s):
        end = s.find("\\end{" + m.group(1) + "}", m.end())
        if end >= 0:
            fill(buf, m.start(), end + len(m.group(1)) + 6)


def mask_inline_math(s: str, buf: list) -> None:
    """Mask $...$, $$...$$, \\(...\\) and \\[...\\]; s already has its maths environments masked."""
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            nxt = s[i + 1:i + 2]
            if nxt in ("(", "["):
                end = s.find("\\" + (")" if nxt == "(" else "]"), i + 2)
                if end >= 0:
                    fill(buf, i, end + 2)
                    i = end + 2
                    continue
            i += 2
            continue
        if c == "$":
            width = 2 if s.startswith("$$", i) else 1
            j = i + width
            while j < n:
                if s[j] == "\\":
                    j += 2
                    continue
                if s[j] == "$" or s.startswith("\n\n", j):
                    break
                j += 1
            if j < n and s[j] == "$":
                end = j + width
                fill(buf, i, end)
                i = end
                continue
        i += 1


class Source:
    """One file: its comment-stripped lines, comments, masked views and section labels."""

    def __init__(self, path: str, text: str, config: Config):
        self.path, self.config = path, config
        lines = text.split("\n")
        split = [strip_comment(line) for line in lines]
        self.code_lines = [c for c, _ in split]
        self.comments = [m for _, m in split]
        self.raw = "\n".join(self.code_lines)
        self.starts = [0]
        for line in self.code_lines[:-1]:
            self.starts.append(self.starts[-1] + len(line) + 1)
        self._views: dict[str, str] = {"raw": self.raw}
        self._labels: list[frozenset] | None = None
        self._display: set[int] | None = None

    def view(self, name: str) -> str:
        if name not in self._views:
            cfg, s = self.config, self.raw
            text = list(s)
            mask_macros(s, text, cfg.keys, cfg.env_args)
            mask_envs(s, text, cfg.code_envs)
            self._views["text"] = "".join(text)
            prose = list(text)
            mask_macros(s, prose, cfg.prose, {})
            math = list(s)
            mask_envs(s, math, cfg.math_envs + cfg.code_envs)
            env_masked = "".join(math)
            mask_envs(s, prose, cfg.math_envs)
            mask_inline_math(env_masked, prose)
            for m in re.finditer(r"\\[A-Za-z]+|``[^`'\n]*''", s):  # macro names; quoted (verbatim) text
                fill(prose, m.start(), m.end())
            self._views["prose"] = "".join(prose)
        return self._views[name]

    def locate(self, offset: int) -> tuple[int, int]:
        k = bisect.bisect_right(self.starts, offset) - 1
        return k, offset - self.starts[k]

    def labels(self, k: int) -> frozenset:
        """The labels of the sections enclosing line index k (a section's first \\label, if it
        comes before any other content after the sectioning command)."""
        if self._labels is None:
            stack, out = [], []
            for line in self.code_lines:
                m = SECTION_RE.search(line)
                if m:
                    level = SECTION_LEVEL[m.group(1)]
                    stack = [e for e in stack if e[0] < level] + [[level, None, True]]
                label = LABEL_RE.search(line)
                if stack and stack[-1][2]:
                    if label and stack[-1][1] is None:
                        stack[-1][1] = label.group(1)
                    elif line.strip() and not m and not label:
                        stack[-1][2] = False
                out.append(frozenset(e[1] for e in stack if e[1]))
            self._labels = out
        return self._labels[k]

    def display_lines(self) -> set[int]:
        """Indices of lines inside a display-maths environment."""
        if self._display is None:
            buf = list(self.raw)
            mask_envs(self.raw, buf, self.config.math_envs)
            masked = "".join(buf)
            self._display = {k for k, a in enumerate(self.starts)
                             if MASK in masked[a:a + len(self.code_lines[k]) + 1]
                             and masked[a:a + len(self.code_lines[k])].strip(MASK + " \t") == ""
                             and self.code_lines[k].strip()}
        return self._display

    def sentence(self, k: int, col_a: int, col_b: int) -> str:
        """The sentence(s) of line k covering columns [col_a, col_b), heuristically split; for a
        line of displayed maths, its whole paragraph (the block of non-blank lines around it)."""
        if k in self.display_lines():
            a = b = k
            while a > 0 and self.code_lines[a - 1].strip():
                a -= 1
            while b + 1 < len(self.code_lines) and self.code_lines[b + 1].strip():
                b += 1
            return "\n".join(self.code_lines[a:b + 1])
        line = self.code_lines[k]
        start, end = 0, len(line)
        for m in re.finditer(r"[.!?][)\]}'\"]*\s+", line):
            word = re.search(r"([\w.]*)$", line[:m.start()]).group(1)
            nxt = line[m.end():m.end() + 1]
            if word in ABBREVIATIONS or re.fullmatch(r"[A-Z]", word) or (nxt and nxt.islower()):
                continue
            if m.end() <= col_a:
                start = m.end()
            elif m.start() >= col_b:
                end = m.start() + 1
                break
        return line[start:end]


# ---------------------------------------------------------------- linting

def glob_any(path: str, patterns) -> bool:
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


def scope_allows(src: Source, k: int, scopes: list[dict]) -> bool:
    for s in scopes:
        if s["files"] and not fnmatch.fnmatchcase(src.path, s["files"]):
            continue
        if s["section"] and s["section"] not in src.labels(k):
            continue
        if s["paragraph"] and not s["paragraph"].search(src.code_lines[k]):
            continue
        return True
    return False


def excerpt(line: str, a: int, b: int, width: int) -> str:
    side = max(10, (width - (b - a)) // 2)
    pre, hit, post = line[max(0, a - side):a], line[a:b], line[b:b + side]
    norm = lambda t: re.sub(r"\s+", " ", t)
    return ("…" if a - side > 0 else "") + norm(pre) + "«" + norm(hit) + "»" + norm(post) + \
        ("…" if b + side < len(line) else "")


def lint_source(path: str, text: str, config: Config, rules: list[Rule] | None = None) -> list[Hit]:
    src = Source(path, text, config)
    hits = []
    for rule in rules if rules is not None else config.rules:
        if rule.files and not glob_any(path, rule.files):
            continue
        if rule.allow_files and glob_any(path, rule.allow_files):
            continue
        view = src.view(rule.view)
        for m in rule.regex.finditer(view):
            if m.end() == m.start():
                continue
            k, col = src.locate(m.start())
            line = src.code_lines[k]
            col_end = min(col + (m.end() - m.start()), len(line))
            if rule.exclude and rule.exclude.fullmatch(src.raw[m.start():m.end()]):
                continue
            if rule.not_after and rule.not_after.search(line[:col]):
                continue
            if rule.also or rule.unless:
                region = line if rule.scope == "line" else src.sentence(k, col, col_end)
                if rule.also and not rule.also.search(region):
                    continue
                if rule.unless and rule.unless.search(region):
                    continue
            allowed = ALLOW_RE.search(src.comments[k])
            if allowed and glob_any(rule.id, [a.strip() for a in allowed.group(1).split(",")]):
                continue
            if rule.allow_scopes and scope_allows(src, k, rule.allow_scopes):
                continue
            hits.append(Hit(path, k + 1, col + 1, rule, excerpt(line, col, col_end, config.excerpt)))
    hits.sort(key=lambda h: (h.line, h.col, h.rule.id))
    return hits


def collect_files(root: Path, config: Config, selectors: list[str]) -> list[str]:
    found = set()
    for pattern in config.files:
        found.update(p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file())
    files = sorted(f for f in found if not glob_any(f, config.exclude))
    if not selectors:
        return files
    pats = [p if any(ch in p for ch in "*?[") else f"*{p}*" for p in selectors]
    chosen = [f for f in files if glob_any(f, pats)]
    if not chosen:  # an explicit path outside the default set, e.g. main.tex
        chosen = sorted({p.relative_to(root).as_posix() for s in selectors for p in root.glob(s)
                         if p.is_file() and p.suffix == ".tex"})
    return chosen


def main(argv=None) -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Lint the thesis against the Standing Facts and vocabulary.")
    ap.add_argument("--config", type=Path, default=here / "lint_rules.toml")
    ap.add_argument("--root", type=Path, default=here.parent, help="repository root (default: tools/..)")
    ap.add_argument("--files", action="append", default=[], help="glob (repeatable, comma-separated)")
    ap.add_argument("--rule", action="append", default=[], help="rule id or glob (repeatable, comma-separated)")
    ap.add_argument("--severity", choices=SEVERITIES, default="warn", help="lowest severity shown")
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    ap.add_argument("--list", action="store_true", help="list the rules and exit")
    args = ap.parse_args(argv)

    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"thesis_lint: {exc}", file=sys.stderr)
        return 2
    wanted = [r.strip() for spec in args.rule for r in spec.split(",") if r.strip()]
    rules = [r for r in config.rules if not wanted or glob_any(r.id, wanted)]
    if wanted and not rules:
        print(f"thesis_lint: no rule matches {wanted} (see --list)", file=sys.stderr)
        return 2
    if args.list:
        for r in rules:
            print(f"{r.severity:5}  {r.id:28} [{r.view}] {r.message}")
        return 0

    root = args.root.resolve()
    selectors = [s.strip() for spec in args.files for s in spec.split(",") if s.strip()]
    files = collect_files(root, config, selectors)
    if not files:
        print(f"thesis_lint: no files match {selectors or config.files}", file=sys.stderr)
        return 2

    t0 = time.perf_counter()
    floor = SEVERITIES.index(args.severity)
    shown, hidden = [], 0
    for f in files:
        for h in lint_source(f, (root / f).read_text(encoding="utf-8"), config, rules):
            if SEVERITIES.index(h.rule.severity) >= floor:
                shown.append(h)
            else:
                hidden += 1
    elapsed = time.perf_counter() - t0

    current, explained = None, set()
    for h in shown:
        if h.path != current:
            current, explained = h.path, set()
            print(f"\n{h.path}")
        print(f"  {h.line}:{h.col}  {h.rule.severity:5}  {h.rule.id}")
        if h.rule.id not in explained:
            explained.add(h.rule.id)
            print(f"      ⟶ {h.rule.message}")
        print(f"      {h.excerpt}")

    counts: dict[tuple[str, str], int] = {}
    for h in shown:
        counts[(h.rule.severity, h.rule.id)] = counts.get((h.rule.severity, h.rule.id), 0) + 1
    by_sev = {s: sum(n for (sev, _), n in counts.items() if sev == s) for s in SEVERITIES}
    failing = by_sev["error"] + (by_sev["warn"] if args.strict else 0)
    tail = f" ({hidden} below --severity {args.severity} hidden)" if hidden else ""
    if not shown:
        print(f"thesis_lint: clean, {len(files)} files, {len(rules)} rules, {elapsed:.2f} s{tail}")
        return 0
    print(f"\nsummary ({len(files)} files, {len(rules)} rules, {elapsed:.2f} s)")
    for (sev, rid), n in sorted(counts.items(), key=lambda kv: (-SEVERITIES.index(kv[0][0]), kv[0][1])):
        print(f"  {sev:5}  {n:4}  {rid}")
    print(f"  {by_sev['error']} error, {by_sev['warn']} warn, {by_sev['info']} info{tail}"
          f" -> {'FAIL' if failing else 'pass'}")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
