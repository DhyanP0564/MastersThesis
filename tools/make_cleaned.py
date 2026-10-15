#!/usr/bin/env python3
"""Build a shareable copy of the thesis source with every LaTeX comment removed.

Usage (from the project root, or anywhere):
    python3 tools/make_cleaned.py            # writes ./cleaned/
    python3 tools/make_cleaned.py -o OUTDIR  # writes OUTDIR/

Copies main.tex, latexmkrc, the 0_*, 1_*, 2_*, 3_* folders and the figures in Figs/
(not their scripts) into the output directory, which is deleted and rebuilt on every run.
In .tex files, full-line comments are deleted and trailing comments are cut; a `%` that
directly follows non-space text is kept bare, so its end-of-line space suppression still
holds. In .bib files only full-line comments are deleted. Runs of blank lines collapse to
one. Markdown notes (e.g. 0_results/README.md) and OS clutter are left out.
"""

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIRS = ("0_results", "1_header", "2_body", "3_footer")
TOP_FILES = ("main.tex", "latexmkrc")
FIG_EXTS = {".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg"}
SKIP_NAMES = {".DS_Store", "__pycache__"}
SKIP_EXTS = {".md", ".pyc"}

VERBATIM_BEGIN = re.compile(r"\\begin\{(verbatim\*?|lstlisting|minted|Verbatim)\}")
VERBATIM_END = re.compile(r"\\end\{(verbatim\*?|lstlisting|minted|Verbatim)\}")


def comment_start(line: str) -> int:
    """Index of the first unescaped `%`, or -1. A `%` is escaped by an odd run of backslashes."""
    for i, ch in enumerate(line):
        if ch == "%":
            backslashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                return i
    return -1


def strip_tex(text: str) -> str:
    out = []
    in_verbatim = False
    for line in text.splitlines():
        if in_verbatim:
            out.append(line)
            if VERBATIM_END.search(line):
                in_verbatim = False
            continue
        if VERBATIM_BEGIN.search(line):
            in_verbatim = True
            out.append(line)
            continue

        i = comment_start(line)
        if i < 0:
            out.append(line.rstrip())
            continue
        code = line[:i]
        if code.strip() == "":
            continue  # full-line comment: the line contributes nothing to TeX
        if code[-1] in " \t":
            out.append(code.rstrip())
        else:
            out.append(code + "%")  # keep the bare % that suppresses the end-of-line space
    return collapse_blank_lines(out)


def strip_bib(text: str) -> str:
    lines = [l.rstrip() for l in text.splitlines() if not l.lstrip().startswith("%")]
    return collapse_blank_lines(lines)


def collapse_blank_lines(lines: list[str]) -> str:
    cleaned = []
    for line in lines:
        if line == "" and (not cleaned or cleaned[-1] == ""):
            continue
        cleaned.append(line)
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return "\n".join(cleaned) + "\n" if cleaned else ""


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix == ".tex":
        dst.write_text(strip_tex(src.read_text(encoding="utf-8")), encoding="utf-8")
    elif src.suffix == ".bib":
        dst.write_text(strip_bib(src.read_text(encoding="utf-8")), encoding="utf-8")
    else:
        shutil.copy2(src, dst)


def wanted(path: Path) -> bool:
    return not (set(path.parts) & SKIP_NAMES) and path.suffix not in SKIP_EXTS


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-o", "--outdir", default=str(ROOT / "cleaned"), help="output directory (default: ./cleaned)")
    args = parser.parse_args()
    outdir = Path(args.outdir).resolve()
    if outdir == ROOT or ROOT.is_relative_to(outdir):
        raise SystemExit(f"refusing to overwrite {outdir}")

    if outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True)

    count = 0
    for name in TOP_FILES:
        copy_file(ROOT / name, outdir / name)
        count += 1
    for d in SOURCE_DIRS:
        for src in sorted((ROOT / d).rglob("*")):
            if src.is_file() and wanted(src.relative_to(ROOT)):
                copy_file(src, outdir / src.relative_to(ROOT))
                count += 1
    for src in sorted((ROOT / "Figs").iterdir()):
        if src.is_file() and src.suffix.lower() in FIG_EXTS:
            copy_file(src, outdir / "Figs" / src.name)
            count += 1

    print(f"wrote {count} files to {outdir}")


if __name__ == "__main__":
    main()
