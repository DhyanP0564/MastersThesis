#!/usr/bin/env python3
"""Audit the thesis bibliography against the publishers (stdlib only).

    python3 tools/bib_audit.py --cache-dir <scratch>/bib_cache            # full audit
    python3 tools/bib_audit.py --offline                                  # inventory only

Step 1 (offline): cited-but-missing / defined-but-uncited keys (build/main.bcf and a scan of
the .tex sources), duplicates (DOI, arXiv id, near-identical titles), fields missing for the
entry type, malformed DOIs, http URLs, unprotected capitals in titles.
Step 2 (network): Crossref /works/<doi> (DataCite on a Crossref 404), the arXiv API for every
arXiv id (journal_ref and DOI), and a Crossref title search for entries with neither.
Step 3: a field-by-field diff written to review/bib_audit.md, grouped as wrong, preprint now
published, missing field, cosmetic. Text between the MANUAL markers in an existing report is
kept across reruns.

Every response is cached as JSON/XML in --cache-dir, so a rerun makes no requests.
"""

import argparse
import difflib
import hashlib
import json
import re
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "bib-audit/0.1 (bibliography metadata check; python-urllib)"
SLEEP = 1.0
MANUAL_BEGIN = "<!-- BEGIN MANUAL -->"
MANUAL_END = "<!-- END MANUAL -->"

# --------------------------------------------------------------------------------------------
# .bib parser
# --------------------------------------------------------------------------------------------


class Entry:
    def __init__(self, etype, key, fields, line):
        self.type = etype.lower()
        self.key = key
        self.fields = fields  # lower-case name -> raw value (outer delimiters removed)
        self.line = line

    def get(self, *names):
        for n in names:
            if n in self.fields and self.fields[n].strip():
                return self.fields[n].strip()
        return None


def _read_value(text, i):
    """Read one field value starting at text[i]; return (value, next index)."""
    parts = []
    while True:
        while text[i].isspace():
            i += 1
        c = text[i]
        if c == "{":
            depth, j = 0, i
            while True:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            parts.append(text[i + 1 : j])
            i = j + 1
        elif c == '"':
            depth, j = 0, i + 1
            while not (text[j] == '"' and depth == 0):
                if text[j] == "\\":
                    j += 2
                    continue
                depth += {"{": 1, "}": -1}.get(text[j], 0)
                j += 1
            parts.append(text[i + 1 : j])
            i = j + 1
        else:
            m = re.match(r"[^\s,#}]+", text[i:])
            parts.append(m.group(0))
            i += m.end()
        while text[i].isspace():
            i += 1
        if text[i] == "#":
            i += 1
            continue
        return "".join(parts), i


def parse_bib(path):
    text = path.read_text(encoding="utf-8")
    entries, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == "%":  # comment line outside an entry
            i = text.find("\n", i)
            i = n if i < 0 else i
            continue
        if c != "@":
            i += 1
            continue
        m = re.match(r"@(\w+)\s*([{(])", text[i:])
        if not m:
            i += 1
            continue
        etype, line = m.group(1), text.count("\n", 0, i) + 1
        close = "}" if m.group(2) == "{" else ")"
        i += m.end()
        if etype.lower() in ("comment", "preamble", "string"):
            depth = 1
            while depth:
                depth += {"{": 1, "(": 1, "}": -1, ")": -1}.get(text[i], 0)
                i += 1
            continue
        km = re.match(r"\s*([^,\s]+)\s*,", text[i:])
        key = km.group(1)
        i += km.end()
        fields = {}
        while True:
            while text[i].isspace() or text[i] == ",":
                i += 1
            if text[i] == close:
                i += 1
                break
            fm = re.match(r"([\w:.+-]+)\s*=\s*", text[i:])
            name = fm.group(1).lower()
            i += fm.end()
            value, i = _read_value(text, i)
            fields[name] = value
        entries.append(Entry(etype, key, fields, line))
    return entries


# --------------------------------------------------------------------------------------------
# Normalisation
# --------------------------------------------------------------------------------------------

_ACCENTS = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303",
            "=": "\u0304", ".": "\u0307", "u": "\u0306", "v": "\u030c", "H": "\u030b",
            "c": "\u0327", "k": "\u0328", "r": "\u030a"}
_SYMBOLS = {"o": "ø", "O": "Ø", "i": "ı", "j": "ȷ", "l": "ł", "L": "Ł", "ss": "ß",
            "aa": "å", "AA": "Å", "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "Œ", "&": "&", "%": "%"}


def delatex(s):
    """LaTeX source -> plain Unicode (accents composed, braces and commands dropped)."""
    s = re.sub(r"\\([" + re.escape("'`^\"~=.") + r"])\s*\{?\\?([A-Za-z])\}?",
               lambda m: m.group(2) + _ACCENTS[m.group(1)], s)
    s = re.sub(r"\\([uvHckr])\s*\{\\?([A-Za-z])\}|\\([uvHckr])\s+\\?([A-Za-z])",
               lambda m: (m.group(2) or m.group(4)) + _ACCENTS[m.group(1) or m.group(3)], s)
    s = re.sub(r"\\(ss|aa|AA|ae|AE|oe|OE|[oOijlL&%])(?![A-Za-z])",
               lambda m: _SYMBOLS[m.group(1)], s)
    s = s.replace("---", "\u2014").replace("--", "\u2013").replace("~", " ")
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", s)).strip()


def strip_markup(s):
    """Publisher metadata often carries JATS/MathML/HTML tags and entities."""
    s = re.sub(r"<[^>]+>", "", s or "")
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def fold(s):
    """Case- and accent-free form used for every comparison."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("ı", "i").replace("ø", "o").replace("Ø", "o").replace("ł", "l").replace("ß", "ss")
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2010", "-").replace("\u2212", "-")
    return re.sub(r"\s+", " ", s.lower()).strip()


def norm_title(s, latex=True):
    s = fold(delatex(s) if latex else strip_markup(s))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def alnum(s):
    return re.sub(r"[\W_]+", "", s)


def sim(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


_PARTICLES = {"van", "der", "de", "von", "del", "la", "le", "da", "di", "den", "du", "dos"}


def family_key(name):
    toks = [t for t in re.split(r"[\s\-]+", fold(name)) if t]
    toks = [t for t in toks if t not in _PARTICLES and t.strip(",") not in _SUFFIX] or toks
    return alnum(" ".join(toks))


def split_authors(field):
    """Split a bib name list on ' and ' at brace depth 0."""
    names, depth, cur, i = [], 0, "", 0
    while i < len(field):
        c = field[i]
        depth += {"{": 1, "}": -1}.get(c, 0)
        if depth == 0 and field[i : i + 5].lower() == " and ":
            names.append(cur.strip())
            cur, i = "", i + 5
            continue
        cur += c
        i += 1
    names.append(cur.strip())
    return [n for n in names if n]


_SUFFIX = {"jr", "jr.", "sr", "ii", "iii", "iv"}


def bib_people(field):
    """(family, given) per name, in order; 'others' ends a truncated list (returned as the flag)."""
    people, truncated = [], False
    for name in split_authors(field):
        if name.lower() == "others":
            truncated = True
            continue
        if name.startswith("{") and name.endswith("}"):  # corporate author
            people.append((delatex(name), ""))
            continue
        parts = [p.strip() for p in name.split(",")]
        if len(parts) >= 2:  # "von Last, First" or "von Last, Jr, First"
            fam, given = parts[0], parts[-1]
        else:
            toks = parts[0].split()
            # "First von Last": the family starts at the first lower-case particle, else last token.
            start = next((k for k, t in enumerate(toks[:-1]) if t[:1].islower()), len(toks) - 1)
            fam, given = " ".join(toks[start:]), " ".join(toks[:start])
        people.append((delatex(fam), delatex(given)))
    return people, truncated


def bib_families(field):
    people, truncated = bib_people(field)
    return [family_key(f) for f, _ in people], truncated


def norm_pages(s):
    s = fold(delatex(s or "")).replace(" ", "")
    s = re.sub(r"-+", "-", s)
    return s


# --------------------------------------------------------------------------------------------
# Identifiers
# --------------------------------------------------------------------------------------------

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV_NEW = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
ARXIV_OLD = re.compile(r"^[a-z\-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$")


def entry_doi(e):
    d = e.get("doi")
    if d:
        return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", d.strip(), flags=re.I)
    return None


def entry_arxiv(e):
    """The arXiv id from eprint (with an arXiv eprinttype), or from a url/howpublished link."""
    ep = e.get("eprint")
    kind = (e.get("eprinttype", "archiveprefix") or "arxiv").lower()
    if ep and kind == "arxiv":
        return re.sub(r"^arxiv:", "", ep.strip(), flags=re.I)
    for f in ("url", "howpublished", "note"):
        v = e.get(f)
        if v:
            m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})", v)
            if m:
                return m.group(1)
    return None


# --------------------------------------------------------------------------------------------
# Step 1: inventory
# --------------------------------------------------------------------------------------------

REQUIRED = {
    "article": [("journal", "journaltitle"), ("year", "date"), ("volume",), ("pages", "eid"), ("doi",)],
    "misc-arxiv": [("eprint",), ("eprinttype", "archiveprefix"), ("eprintclass", "primaryclass")],
    "book": [("publisher",), ("year", "date")],
    "inproceedings": [("booktitle",), ("year", "date"), ("pages",)],
    "online": [("url",), ("urldate",)],
}

PROPER = ["Hamiltonian", "Chebyshev", "Carleman", "Navier", "Stokes", "Fourier", "Burgers",
          "Schrödinger", "Schrodinger", "Lanczos", "Grover", "Rudolph", "Hilbert", "Pauli",
          "Hermite", "Legendre", "Gegenbauer", "Jacobi", "Krylov", "Galerkin", "Taylor",
          "Green", "Riemann", "Euler", "Lagrange", "Newton", "MATLAB", "Python", "Toffoli",
          "Gram", "Kronecker", "Laplace", "Poisson", "Heisenberg", "Dirac", "Bloch", "Ising"]


def unprotected_words(title):
    """Words at brace depth 0 that a sentence-casing style would lowercase wrongly."""
    out, depth, cur = [], 0, []
    for c in title + " ":
        if c == "{":
            depth += 1
            continue
        if c == "}":
            depth -= 1
            continue
        cur.append(c if depth == 0 else "\0")
    flat = "".join(cur)
    words = re.findall(r"[^\s\0]+", flat)
    for k, w in enumerate(words):
        core = re.sub(r"^[^\w]+|[^\w]+$", "", w)
        if not core:
            continue
        caps = sum(ch.isupper() for ch in core)
        if caps >= 2 or (caps == 1 and not core[0].isupper()):
            out.append(core)  # acronym or mixed case: PDE, SU(2), NumPy
        elif k > 0 and core[0].isupper() and any(fold(core).startswith(fold(p)) for p in PROPER):
            out.append(core)
    # proper nouns written in lower case (e.g. "fourier") are lost whatever the style does
    for p in PROPER:
        for m in re.finditer(r"(?<![\w\\])" + p.lower() + r"\w*", flat):
            out.append(m.group(0) + " (lower-case proper noun)")
    return sorted(set(out))


def cited_keys_bcf(bcf):
    if not bcf.exists():
        return None
    keys = re.findall(r"<bcf:citekey[^>]*>([^<]+)</bcf:citekey>", bcf.read_text(encoding="utf-8"))
    return set(keys)


def cited_keys_tex(root):
    keys = set()
    cite = re.compile(r"\\[A-Za-z]*cite[A-Za-z]*\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]*)\}")
    for tex in root.rglob("*.tex"):
        if "build" in tex.parts:
            continue
        for line in tex.read_text(encoding="utf-8", errors="replace").splitlines():
            code = re.split(r"(?<!\\)%", line, 1)[0]
            for m in cite.finditer(code):
                keys.update(k.strip() for k in m.group(1).split(",") if k.strip())
    return keys


def inventory(entries, bib_path, root, bcf):
    rows, info = [], {}
    keys = [e.key for e in entries]
    defined = set(keys)
    info["duplicate_keys"] = sorted({k for k in keys if keys.count(k) > 1})
    bcf_keys = cited_keys_bcf(bcf)
    tex_keys = cited_keys_tex(root)
    cited = (bcf_keys or set()) | tex_keys
    info["cited_missing"] = sorted(cited - defined)
    info["uncited"] = sorted(defined - cited)
    info["bcf_only"] = sorted((bcf_keys or set()) - tex_keys)
    info["tex_only"] = sorted(tex_keys - (bcf_keys or set()))
    info["n_cited"] = len(cited & defined)

    dups = []
    by_doi, by_arxiv = {}, {}
    for e in entries:
        d, a = entry_doi(e), entry_arxiv(e)
        if d:
            by_doi.setdefault(d.lower(), []).append(e.key)
        if a:
            by_arxiv.setdefault(re.sub(r"v\d+$", "", a), []).append(e.key)
    dups += [("DOI " + d, ks) for d, ks in by_doi.items() if len(ks) > 1]
    dups += [("arXiv " + a, ks) for a, ks in by_arxiv.items() if len(ks) > 1]
    titles = [(e.key, norm_title(e.get("title") or "")) for e in entries]
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            a, b = titles[i][1], titles[j][1]
            if a and b and sim(a, b) >= 0.9:
                dups.append((f"title similarity {sim(a, b):.2f}", [titles[i][0], titles[j][0]]))
    info["duplicates"] = dups

    for e in entries:
        src = f"{bib_path.name}:{e.line}"
        arx = entry_arxiv(e)
        kind = e.type
        if kind == "misc" and arx:
            kind = "misc-arxiv"
        for alts in REQUIRED.get(kind, []):
            if not e.get(*alts):
                note = ""
                if alts[0] == "eprintclass" and arx and ARXIV_OLD.match(arx):
                    note = " (class implicit in old-style id)"
                if alts[0] == "eprint" and arx:
                    note = f" (arXiv:{arx} only in {'howpublished' if e.get('howpublished') else 'url'})"
                if alts[0] == "doi" and e.get("eprint"):
                    note = " (arXiv eprint present)"
                rows.append(dict(group="missing", key=e.key, field=alts[0],
                                 ours="(absent)" + note, theirs="", source=src))
        if e.type == "misc" and not arx and not e.get("doi", "url"):
            rows.append(dict(group="missing", key=e.key, field="eprint/doi/url",
                             ours="(absent)", theirs="", source=src))
        if e.type not in ("misc", "online") and arx and e.get("eprint") and not e.get("eprintclass", "primaryclass") and not ARXIV_OLD.match(arx):
            rows.append(dict(group="cosmetic", key=e.key, field="eprintclass",
                             ours="(absent)", theirs="", source=src))
        d = e.get("doi")
        if d and not DOI_RE.match(d.strip()):
            rows.append(dict(group="wrong", key=e.key, field="doi", ours=d,
                             theirs="malformed DOI", source=src))
        for f in ("url", "howpublished", "note", "doi"):
            v = e.get(f)
            if v and re.search(r"http://", v):
                rows.append(dict(group="cosmetic", key=e.key, field=f, ours=v,
                                 theirs="use https", source=src))
        if e.get("howpublished") and re.match(r"https?://", e.get("howpublished")):
            rows.append(dict(group="cosmetic", key=e.key, field="howpublished",
                             ours=e.get("howpublished"), theirs="a link belongs in url/eprint",
                             source=src))
        mo = e.get("month")
        if mo and not re.fullmatch(r"\d{1,2}|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec", mo.strip().lower()):
            rows.append(dict(group="cosmetic", key=e.key, field="month", ours=mo,
                             theirs="biblatex wants an integer (or date = {YYYY-MM-DD})", source=src))
        t = e.get("title")
        if t:
            bad = unprotected_words(t)
            if bad:
                rows.append(dict(group="cosmetic", key=e.key, field="title (case)", ours=", ".join(bad),
                                 theirs="unprotected: a sentence-casing style would lowercase these",
                                 source=src))
        if not e.get("author", "editor") and e.type != "online":
            rows.append(dict(group="missing", key=e.key, field="author",
                             ours="(absent)", theirs="", source=src))
    return rows, info


# --------------------------------------------------------------------------------------------
# Step 2: network with cache
# --------------------------------------------------------------------------------------------


class Fetcher:
    def __init__(self, cache_dir, offline=False):
        self.dir = Path(cache_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.offline = offline
        self.requests = 0
        self.last = 0.0

    def get(self, url):
        """Return (status, body text); status 0 means not fetched (offline or network error)."""
        h = hashlib.sha1(url.encode()).hexdigest()[:20]
        path = self.dir / f"{h}.json"
        if path.exists():
            rec = json.loads(path.read_text(encoding="utf-8"))
            return rec["status"], rec["body"]
        if self.offline:
            return 0, ""
        wait = SLEEP - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        status, body = 0, ""
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    status, body = r.status, r.read().decode("utf-8", errors="replace")
                break
            except urllib.error.HTTPError as err:
                status, body = err.code, ""
                if err.code not in (429, 500, 502, 503, 504):
                    break
            except (urllib.error.URLError, OSError) as err:  # socket.timeout is an OSError on 3.9
                status, body = 0, str(err)
            time.sleep(3 * (attempt + 1))
        self.last = time.time()
        self.requests += 1
        if status in (200, 404):
            path.write_text(json.dumps({"url": url, "status": status, "body": body}), encoding="utf-8")
        return status, body


def crossref_work(fx, doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/:;()")
    st, body = fx.get(url)
    if st == 200:
        return crossref_record(json.loads(body)["message"]), url
    if st == 404:  # not a Crossref DOI: try DataCite (Zenodo, arXiv, many datasets)
        durl = "https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe="")
        st2, body2 = fx.get(durl)
        if st2 == 200:
            return datacite_record(json.loads(body2)["data"]["attributes"]), durl
        return {"error": f"DOI not found at Crossref or DataCite (HTTP {st}/{st2})"}, url
    return {"error": f"HTTP {st}"}, url


def _year(parts):
    try:
        y = parts["date-parts"][0][0]
    except (KeyError, IndexError, TypeError):
        return None
    return str(y) if y else None


def crossref_record(m):
    authors = [(a.get("family") or a.get("name") or "", a.get("given") or "") for a in m.get("author", [])]
    years = {k: _year(m.get(k, {})) for k in ("issued", "published-print", "published-online")}
    ct = m.get("container-title") or []
    sct = m.get("short-container-title") or []
    title = strip_markup(" ".join(m.get("title") or []))
    sub = strip_markup(" ".join(m.get("subtitle") or []))
    return dict(
        type=m.get("type"), title=title, subtitle=sub, authors=authors,
        year=years.get("issued"), years={v for v in years.values() if v},
        journal=strip_markup(ct[0]) if ct else "", journal_alt=[strip_markup(x) for x in ct[1:] + sct],
        volume=m.get("volume"), issue=m.get("issue"), page=m.get("page"),
        article_number=m.get("article-number"), doi=m.get("DOI"), publisher=m.get("publisher"),
        url="https://doi.org/" + m.get("DOI", ""),
    )


def datacite_record(a):
    authors = [(c.get("familyName") or c.get("name") or "", c.get("givenName") or "") for c in a.get("creators", [])]
    title = strip_markup((a.get("titles") or [{}])[0].get("title", ""))
    return dict(type=(a.get("types") or {}).get("resourceTypeGeneral"), title=title, subtitle="",
                authors=authors, year=str(a.get("publicationYear") or ""),
                years={str(a.get("publicationYear") or "")}, journal="", journal_alt=[],
                volume=None, issue=None, page=None, article_number=None, doi=a.get("doi"),
                publisher=a.get("publisher") if isinstance(a.get("publisher"), str) else (a.get("publisher") or {}).get("name"),
                url="https://doi.org/" + (a.get("doi") or ""))


ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def _arxiv_entry(ent):
    aid = (ent.findtext("a:id", "", ATOM) or "").rsplit("/abs/", 1)[-1]
    title = re.sub(r"\s+", " ", ent.findtext("a:title", "", ATOM)).strip()
    if not aid or title == "Error":
        return None
    base = re.sub(r"v\d+$", "", aid)
    pc = ent.find("arxiv:primary_category", ATOM)
    return dict(
        id=base, version=aid, title=title,
        authors=[re.sub(r"\s+", " ", a.findtext("a:name", "", ATOM)).strip()
                 for a in ent.findall("a:author", ATOM)],
        published=(ent.findtext("a:published", "", ATOM) or "")[:10],
        updated=(ent.findtext("a:updated", "", ATOM) or "")[:10],
        journal_ref=re.sub(r"\s+", " ", ent.findtext("arxiv:journal_ref", "", ATOM) or "").strip(),
        doi=(ent.findtext("arxiv:doi", "", ATOM) or "").strip(),
        primary=pc.get("term") if pc is not None else "",
        url=f"https://arxiv.org/abs/{base}",
    )


def arxiv_records(fx, ids):
    """arXiv metadata per id. Each parsed record is cached on its own, so only ids not yet
    seen are requested (20 per request)."""
    out, todo = {}, []
    for i in sorted(set(ids)):
        path = fx.dir / ("arxiv_" + i.replace("/", "_") + ".json")
        if path.exists():
            out[i] = json.loads(path.read_text(encoding="utf-8"))
        else:
            todo.append(i)
    for k in range(0, len(todo), 20):
        chunk = todo[k : k + 20]
        url = ("https://export.arxiv.org/api/query?max_results=50&id_list="
               + ",".join(urllib.parse.quote(i, safe="/.") for i in chunk))
        st, body = fx.get(url)
        if st != 200:
            for i in chunk:
                out[i] = {"error": f"HTTP {st} (not cached; rerun)"}
            continue
        for ent in ET.fromstring(body).findall("a:entry", ATOM):
            rec = _arxiv_entry(ent)
            if rec and rec["id"] in chunk:
                out[rec["id"]] = rec
                (fx.dir / ("arxiv_" + rec["id"].replace("/", "_") + ".json")).write_text(json.dumps(rec), encoding="utf-8")
        for i in chunk:
            out.setdefault(i, {"error": "not returned by the arXiv API"})
    return out


def crossref_search(fx, e, rows=5):
    title = delatex(e.get("title") or "")
    q = {"query.bibliographic": title, "rows": str(rows),
         "select": "DOI,title,subtitle,author,issued,published-print,published-online,container-title,short-container-title,volume,issue,page,article-number,type,publisher"}
    fams, _ = bib_families(e.get("author") or "")
    if e.get("author") and fams:
        q["query.author"] = delatex(split_authors(e.get("author"))[0].split(",")[0])
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(q)
    st, body = fx.get(url)
    if st != 200:
        return [], url
    items = json.loads(body)["message"].get("items", [])
    return [crossref_record(i) for i in items], url


# --------------------------------------------------------------------------------------------
# Step 3: diff
# --------------------------------------------------------------------------------------------


def split_full_name(full):
    """arXiv gives 'First Middle von Last'; return (family, given)."""
    toks = full.split()
    if not toks:
        return "", ""
    start = len(toks) - 1
    if start > 0 and fold(toks[start]).strip(".,") in _SUFFIX:
        start -= 1
    while start > 0 and toks[start - 1].lower() in _PARTICLES:
        start -= 1
    return " ".join(toks[start:]), " ".join(toks[:start])


def given_mismatch(ours, theirs):
    """Compare given names token by token: spelled-out names must agree, initials by letter."""
    a = [t for t in re.split(r"[\s.\-]+", fold(ours)) if t]
    b = [t for t in re.split(r"[\s.\-]+", fold(theirs)) if t]
    for x, y in zip(a, b):
        if len(x) > 1 and len(y) > 1:
            if alnum(x) != alnum(y):
                return True
        elif x[0] != y[0]:
            return True
    return False


def compare_authors(e, pub_people):
    """Rows (group, field, ours, theirs) comparing family names in order, then given initials."""
    rows = []
    if not e.get("author"):
        return rows
    people, truncated = bib_people(e.get("author"))
    ours = [family_key(f) for f, _ in people]
    theirs = [family_key(f) for f, _ in pub_people if f]
    if not theirs:
        return rows
    if truncated and theirs[: len(ours)] != ours:
        rows.append(("wrong", "author", ", ".join(ours) + " et al.", ", ".join(theirs[: len(ours) + 2]) + " …"))
        return rows
    if not truncated and ours != theirs:
        if theirs[: len(ours)] == ours and people and people[-1][1] == "" and len(ours) < len(theirs):
            rows.append(("cosmetic", "author (group)", f"{len(ours)} names ending in a group author",
                         f"{len(theirs)} names: the record expands the group"))
        elif sorted(ours) == sorted(theirs):
            rows.append(("wrong", "author (order)", ", ".join(ours), ", ".join(theirs)))
            return rows
        elif len(ours) != len(theirs):
            miss = [t for t in theirs if t not in ours]
            extra = [o for o in ours if o not in theirs]
            rows.append(("wrong", "author (count)", f"{len(ours)}: " + ", ".join(ours),
                         f"{len(theirs)}: " + ", ".join(theirs)
                         + (f" [missing {', '.join(miss)}]" if miss else "")
                         + (f" [extra {', '.join(extra)}]" if extra else "")))
            return rows
        else:
            diffs = [(o, t) for o, t in zip(ours, theirs) if o != t]
            close = all(sim(o, t) >= 0.75 or o in t or t in o for o, t in diffs)
            rows.append(("cosmetic" if close else "wrong", "author (spelling)",
                         ", ".join(o for o, _ in diffs), ", ".join(t for _, t in diffs)))
            if not close:
                return rows
    # given names, position by position where the family names agree
    bad = []
    for (of, og), (tf, tg) in zip(people, pub_people):
        if family_key(of) == family_key(tf) and og and tg and given_mismatch(og, tg):
            bad.append((f"{og} {of}", f"{tg} {tf}"))
    if bad:
        rows.append(("wrong", "author (given name)", "; ".join(o for o, _ in bad), "; ".join(t for _, t in bad)))
    return rows


def has_math(s):
    return "$" in s or "<mml:" in s or "\\" in s and re.search(r"\\(mu|nu|alpha|beta|partial)", s) is not None


def compare_title(ours_raw, theirs, theirs_sub=""):
    o = norm_title(ours_raw)
    t = norm_title(theirs, latex=False)
    ts = norm_title(theirs + (" " + theirs_sub if theirs_sub else ""), latex=False)
    if o in (t, ts) or alnum(o) in (alnum(t), alnum(ts)):
        return None
    shown = theirs + (": " + theirs_sub if theirs_sub else "")
    if "$" in ours_raw:
        return ("cosmetic", "title (math)", delatex(ours_raw) + " [math in source]", shown)
    if ts and o.startswith(ts) and len(o) > len(ts):
        return ("cosmetic", "title", delatex(ours_raw), shown + " [record omits the subtitle]")
    if o and ts.startswith(o) and len(ts) > len(o):
        return ("wrong", "title (truncated)", delatex(ours_raw), shown)
    s = max(sim(o, t), sim(o, ts))
    return ("cosmetic" if s >= 0.93 else "wrong", "title", delatex(ours_raw), shown)


def norm_journal(s, latex=True):
    s = norm_title(s, latex)
    s = re.sub(r"\bthe\b", "", s)
    return re.sub(r"\s+", " ", s).strip()


def pages_str(rec):
    return " / ".join(dict.fromkeys(x for x in (rec.get("page"), rec.get("article_number")) if x))


def compare_record(e, rec, src_url, via, identity_only=False):
    """Field-by-field diff of a bib entry against a publisher record."""
    out = []

    def add(group, field, ours, theirs):
        out.append(dict(group=group, key=e.key, field=field, ours=ours or "(absent)",
                        theirs=theirs or "(absent)", source=src_url, via=via))

    if e.get("title") and rec.get("title"):
        r = compare_title(e.get("title"), rec["title"], rec.get("subtitle", ""))
        if r:
            add(*r)
    for g, f, o, t in compare_authors(e, rec.get("authors", [])):
        add(g, f, o, t)
    if identity_only:
        return out
    y = e.get("year") or (e.get("date") or "")[:4]
    if y and rec.get("years") and y not in rec["years"]:
        add("wrong", "year", y, " / ".join(sorted(rec["years"])) + " (issued / print / online)")
    rtype = rec.get("type")
    jour = e.get("journal", "journaltitle")
    if rtype == "journal-article":
        if jour and rec.get("journal"):
            oj = norm_journal(jour)
            cands = [norm_journal(rec["journal"], False)] + [norm_journal(x, False) for x in rec.get("journal_alt", [])]
            if oj not in cands and alnum(oj) not in [alnum(c) for c in cands]:
                s = max(sim(oj, c) for c in cands)
                contained = any(oj in c or c in oj for c in cands if c)
                add("cosmetic" if (s >= 0.8 or contained) else "wrong", "journal", delatex(jour), rec["journal"])
        elif not jour and rec.get("journal"):
            add("missing", "journal", None, rec["journal"])
        v = e.get("volume")
        if rec.get("volume") and fold(v or "") != fold(rec["volume"]):
            add("wrong" if v else "missing", "volume", v, rec["volume"])
        n = e.get("number", "issue")
        iss = rec.get("issue")
        if iss and iss != "0" and fold(n or "") != fold(iss):
            add("wrong" if n else "missing", "number", n, iss)
    if rtype in ("journal-article", "proceedings-article", "book-chapter"):
        p = norm_pages(e.get("pages", "eid") or "")
        cand = [norm_pages(x) for x in (rec.get("page"), rec.get("article_number")) if x]
        if cand and p not in cand:
            first = lambda s: s.split("-")[0]
            if not p:
                add("missing", "pages", None, pages_str(rec))
            elif any(first(p) == first(c) for c in cand):
                add("missing" if "-" not in p else "cosmetic", "pages", e.get("pages", "eid"), pages_str(rec))
            elif "-" not in p and any(c.startswith("1-") for c in cand):
                add("cosmetic", "pages (article number)", e.get("pages", "eid"),
                    pages_str(rec) + " [no article number in the record; check the landing page]")
            else:
                add("wrong", "pages", e.get("pages", "eid"), pages_str(rec))
    d = entry_doi(e)
    if rec.get("doi"):
        if not d:
            add("missing", "doi", None, rec["doi"])
        elif d.lower() != rec["doi"].lower():
            add("wrong", "doi", d, rec["doi"])
    return out


def match_strength(e, rec):
    """Title similarity, and whether the first authors' family names agree."""
    o = norm_title(e.get("title") or "")
    t = norm_title(rec.get("title", ""), latex=False)
    ts = norm_title(rec.get("title", "") + " " + rec.get("subtitle", ""), latex=False)
    s = max(sim(o, t), sim(o, ts))
    ours, _ = bib_families(e.get("author") or "")
    theirs = [family_key(f) for f, _ in rec.get("authors", []) if f]
    first_ok = bool(ours and theirs and ours[0] == theirs[0])
    return s, first_ok


def fmt_published(rec):
    bits = [rec.get("journal") or rec.get("publisher") or rec.get("type") or ""]
    if rec.get("volume"):
        bits.append(rec["volume"] + (f"({rec['issue']})" if rec.get("issue") else ""))
    pg = rec.get("article_number") or rec.get("page")
    if pg:
        bits.append(pg)
    if rec.get("year"):
        bits.append(f"({rec['year']})")
    if rec.get("doi"):
        bits.append("doi:" + rec["doi"])
    return " ".join(b for b in bits if b)


PUBLISHED_TYPES = ("journal-article", "proceedings-article", "book-chapter")


def audit_network(entries, fx):
    """Resolve each entry to its publisher record (its DOI; else the DOI on its arXiv record;
    else, for @article/@inproceedings, an exact title-and-first-author Crossref match), diff
    against that, and fall back to the arXiv record only when there is no publisher record."""
    rows, candidates, records = [], [], {}
    arx_ids = {e.key: entry_arxiv(e) for e in entries}
    arx = arxiv_records(fx, [re.sub(r"v\d+$", "", a) for a in arx_ids.values() if a])

    def row(group, e, field, ours, theirs, source, via):
        rows.append(dict(group=group, key=e.key, field=field, ours=ours, theirs=theirs, source=source, via=via))

    for e in entries:
        doi = entry_doi(e)
        aid = arx_ids[e.key]
        ar = arx.get(re.sub(r"v\d+$", "", aid)) if aid else None
        if ar and "error" in ar:
            row("wrong", e, "eprint", aid, ar["error"], f"https://arxiv.org/abs/{aid}", "arxiv")
            ar = None
        pub, url, via = None, None, None
        if doi and DOI_RE.match(doi):
            pub, url = crossref_work(fx, doi)
            via = "doi"
            if "error" in pub:
                row("wrong", e, "doi", doi, pub["error"], url, via)
                pub = None
        if pub is None and ar and ar.get("doi"):
            p2, u2 = crossref_work(fx, ar["doi"])
            if "error" not in p2:
                pub, url, via = p2, u2, "arxiv doi"
        if pub is None and not doi and e.type in ("article", "inproceedings"):
            found, surl = crossref_search(fx, e)
            for c in found:
                s, first_ok = match_strength(e, c)
                if s >= 0.97 and first_ok and c.get("type") in PUBLISHED_TYPES:
                    pub, url, via = c, c["url"], "title search (exact title, first author)"
                    break
            else:
                for c in found[:3]:
                    s, _ = match_strength(e, c)
                    if s >= 0.6:
                        candidates.append(dict(key=e.key, reason=f"@{e.type} without DOI", score=s, rec=c, source=c["url"]))
        records[e.key] = dict(publisher=pub, arxiv=ar)

        if ar and doi and ar.get("doi") and doi.lower() != ar["doi"].lower():
            row("wrong", e, "doi", doi, ar["doi"] + " (DOI on the arXiv record)", ar["url"], "arxiv")
        if ar:
            pc = e.get("eprintclass", "primaryclass")
            if pc and ar.get("primary") and pc != ar["primary"]:
                row("cosmetic", e, "eprintclass", pc, ar["primary"], ar["url"], "arxiv")

        preprint_entry = e.type in ("misc", "online", "unpublished")
        if pub is not None:
            if preprint_entry and (pub.get("type") in PUBLISHED_TYPES or (pub.get("journal") and pub.get("page"))):
                row("published", e, "entry type", f"@{e.type} arXiv:{aid}" if aid else f"@{e.type}",
                    fmt_published(pub), url, via)
                rows.extend(compare_record(e, pub, url, via, identity_only=True))
            else:
                rows.extend(compare_record(e, pub, url, via))
            continue
        if ar:
            r = compare_title(e.get("title") or "", ar["title"])
            if r:
                row(r[0], e, r[1], r[2], r[3], ar["url"], "arxiv")
            for g, f, o, t in compare_authors(e, [split_full_name(a) for a in ar["authors"]]):
                row(g, e, f, o, t, ar["url"], "arxiv")
            if preprint_entry and (e.get("year") or "") != ar["published"][:4]:
                row("wrong", e, "year", e.get("year"), f"{ar['published'][:4]} (v1 {ar['published']})", ar["url"], "arxiv")
            if preprint_entry and ar.get("journal_ref"):
                row("published", e, "entry type", f"@{e.type} arXiv:{aid}", "journal_ref: " + ar["journal_ref"],
                    ar["url"], "arxiv journal_ref")
            elif preprint_entry:
                # arXiv records are often not updated after publication: search Crossref by title.
                found, surl = crossref_search(fx, e)
                for c in found:
                    s, first_ok = match_strength(e, c)
                    if s >= 0.85 and first_ok and c.get("type") in PUBLISHED_TYPES:
                        candidates.append(dict(key=e.key, reason="arXiv-only: possible published version",
                                               score=s, rec=c, source=c["url"]))
        if not doi and not aid:
            found, surl = crossref_search(fx, e)
            shown = 0
            for c in found:
                s, _ = match_strength(e, c)
                if s >= 0.6 and shown < 3:
                    candidates.append(dict(key=e.key, reason="no DOI or arXiv id", score=s, rec=c, source=c["url"]))
                    shown += 1
            if not shown:
                candidates.append(dict(key=e.key, reason="no DOI or arXiv id", score=0.0, rec=None, source=surl))
    return rows, candidates, records, arx


# --------------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------------

GROUPS = [("wrong", "Wrong"), ("published", "Preprint now published"),
          ("missing", "Missing field"), ("cosmetic", "Cosmetic")]


def cell(s):
    s = str(s if s is not None else "")
    return s.replace("|", "\\|").replace("\n", " ")


def write_report(path, bib_rel, entries, inv_rows, info, net_rows, candidates, fx, offline):
    old_manual = ""
    if path.exists():
        txt = path.read_text(encoding="utf-8")
        if MANUAL_BEGIN in txt and MANUAL_END in txt:
            old_manual = txt.split(MANUAL_BEGIN, 1)[1].split(MANUAL_END, 1)[0]
    found = {(r["key"], r["field"]) for r in net_rows}
    rows = [r for r in inv_rows if (r["key"], r["field"]) not in found] + net_rows
    seen, uniq = set(), []
    for r in rows:
        k = (r["group"], r["key"], r["field"], str(r["ours"]), str(r["theirs"]))
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    order = {e.key: i for i, e in enumerate(entries)}
    L = [f"# Bibliography audit: `{bib_rel}`", "",
         f"Generated by `tools/bib_audit.py` ({len(entries)} entries; {info['n_cited']} cited). "
         f"{'Offline: no publisher data. ' if offline else ''}"
         "Comparisons fold case, accents, LaTeX escapes and punctuation, so a row is a real "
         "difference. `via` says which record the row was compared against.", "",
         MANUAL_BEGIN + (old_manual if old_manual else "\n_(hand-check notes go here; kept across reruns)_\n") + MANUAL_END, "",
         "## Inventory", ""]
    L.append(f"- Cited but not defined: {', '.join(info['cited_missing']) or 'none'}")
    L.append(f"- Defined but not cited ({len(info['uncited'])}): {', '.join(info['uncited']) or 'none'}")
    if info["bcf_only"] or info["tex_only"]:
        L.append(f"- In `main.bcf` but not found in a `.tex` scan: {', '.join(info['bcf_only']) or 'none'}; "
                 f"in `.tex` but not in `main.bcf` (rebuild needed?): {', '.join(info['tex_only']) or 'none'}")
    L.append(f"- Duplicate keys: {', '.join(info['duplicate_keys']) or 'none'}")
    if info["duplicates"]:
        L.append("- Possible duplicate entries:")
        for why, ks in info["duplicates"]:
            L.append(f"  - {why}: {', '.join(ks)}")
    else:
        L.append("- Possible duplicate entries: none (same DOI, same arXiv id, title similarity ≥ 0.90)")
    L.append("")
    for g, title in GROUPS:
        rs = sorted((r for r in uniq if r["group"] == g), key=lambda r: (order.get(r["key"], 999), r["field"]))
        L += [f"## {title} ({len(rs)})", ""]
        if not rs:
            L += ["None.", ""]
            continue
        L += ["| key | field | ours | publisher's | source |", "|---|---|---|---|---|"]
        for r in rs:
            src = r["source"]
            src = f"[{r.get('via', 'link')}]({src})" if src.startswith("http") else f"`{src}`"
            L.append(f"| `{r['key']}` | {cell(r['field'])} | {cell(r['ours'])} | {cell(r['theirs'])} | {src} |")
        L.append("")
    L += ["## Title-search candidates (for review, not matches)", "",
          "Crossref bibliographic search on the title (and first author). Nothing here was used in the diff.", ""]
    if candidates:
        L += ["| key | why searched | score | candidate | source |", "|---|---|---|---|---|"]
        for c in sorted(candidates, key=lambda c: (order.get(c["key"], 999), -c["score"])):
            rec = c["rec"]
            desc = "no candidate above 0.6" if rec is None else (
                f"{rec['title']} — {', '.join(f for f, _ in rec['authors'][:3])}{' et al.' if len(rec['authors']) > 3 else ''}; "
                f"{rec.get('type')}; {fmt_published(rec)}")
            L.append(f"| `{c['key']}` | {c['reason']} | {c['score']:.2f} | {cell(desc)} | [link]({c['source']}) |")
    else:
        L.append("None.")
    L += ["", f"_Requests this run: {fx.requests} (the rest from the cache)._", ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bib", default=str(ROOT / "3_footer" / "ref.bib"))
    ap.add_argument("--bcf", default=str(ROOT / "build" / "main.bcf"))
    ap.add_argument("--out", default=str(ROOT / "review" / "bib_audit.md"))
    ap.add_argument("--cache-dir", default=str(Path(tempfile.gettempdir()) / "bib_audit_cache"))
    ap.add_argument("--offline", action="store_true", help="inventory only; use cached responses if any")
    ap.add_argument("--dump", help="write the fetched records as JSON here (for hand checks)")
    args = ap.parse_args()

    bib = Path(args.bib)
    entries = parse_bib(bib)
    inv_rows, info = inventory(entries, bib, ROOT, Path(args.bcf))
    fx = Fetcher(args.cache_dir, offline=args.offline)
    net_rows, candidates, records, arx = ([], [], {}, {})
    if not args.offline:
        net_rows, candidates, records, arx = audit_network(entries, fx)
    try:
        bib_rel = bib.resolve().relative_to(ROOT)
    except ValueError:
        bib_rel = bib
    write_report(Path(args.out), bib_rel, entries, inv_rows, info, net_rows, candidates, fx, args.offline)
    if args.dump:
        Path(args.dump).write_text(json.dumps({"records": records, "arxiv": arx}, indent=1, default=list), encoding="utf-8")
    counts = {g: sum(1 for r in inv_rows + net_rows if r["group"] == g) for g, _ in GROUPS}
    print(f"{len(entries)} entries, {info['n_cited']} cited, {len(info['uncited'])} uncited, "
          f"{len(info['cited_missing'])} missing; rows: {counts}; candidates: {len(candidates)}; "
          f"requests: {fx.requests}; report: {args.out}")


if __name__ == "__main__":
    sys.exit(main())
