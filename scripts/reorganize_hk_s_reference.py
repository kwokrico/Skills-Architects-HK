#!/usr/bin/env python3
"""Reorganize hk_s_reference: rename CS files, move sources to source_reference/, report gaps."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
HK_REF = ROOT / "hk_s_reference"
DOC_EXTS = {".pdf", ".md", ".doc", ".docx", ".txt"}
AMENDMENT_RE = re.compile(r"amendment|_amend|amend\d", re.I)
_PNAP_NOTE_RE = re.compile(r"\b(APP|ADM|ADV)[-_\s]?0*(\d+)\b", re.I)


REPORT_FILES = {"DOCUMENTS_WITHOUT_CS.md", "_CS_INVENTORY.md"}


def is_cs_file(path: Path) -> bool:
    name = path.name
    if name in REPORT_FILES:
        return False
    return "Architect Critical Summary" in name or name.endswith("_CS.md")


_LAYOUT_DIRS = {"summaries", "source_md", "source_reference"}


def topic_dir(path: Path) -> Path:
    """Topic folder that owns both summaries/ and the sibling source_reference/."""
    if path.parent.name in _LAYOUT_DIRS:
        return path.parent.parent
    return path.parent


def cs_parent_for_doc(doc: Path) -> Path:
    """Parent folder that owns a source document (handles source_reference/ subfolder)."""
    return topic_dir(doc)


def topic_dir_for_cs(cs: CsEntry) -> Path:
    """Folder a CS covers. A file in summaries/ covers the sibling source_reference/."""
    return topic_dir(cs.path)


def is_index_table(path: Path) -> bool:
    """Topic index tables are not source documents that need their own CS."""
    name = path.name
    return name.endswith("_Table_English.md") or name.endswith("_Table_Traditional_Chinese.md")


_GAP_NOTE_NAMES = {
    "STATUTORY_GAPS.md",
    "STATUTORY_READING_GUIDE.md",
    "critical summary prompt.md",
}


def _is_gap_exempt(path: Path) -> bool:
    """Indexes, compilations, and working notes do not need their own CS."""
    if path.name in REPORT_FILES or path.name in _GAP_NOTE_NAMES:
        return True
    if is_index_table(path) or "_extract_tmp" in path.parts:
        return True
    name = path.name
    if name.endswith("_Technical_Summaries.md") or "TOC" in name:
        return True
    return (
        name.startswith("batch_")
        and name.endswith(".md")
        and "Practice Notes for Authorized Persons (PNAP)" in path.parts
        and "source_reference" in path.parts
    )


def _pnap_note_id(name: str) -> tuple[str, int] | None:
    """APP/ADM/ADV number, ignoring leading zeros. APP-005 and APP-5 are one note."""
    match = _PNAP_NOTE_RE.search(Path(name).stem)
    if not match:
        return None
    return match.group(1).upper(), int(match.group(2))


def _topic_owning_source(path: Path) -> Path | None:
    """Topic folder for a file under source_reference/, including nested series folders."""
    for parent in path.parents:
        if parent.name == "source_reference":
            return parent.parent
    return None


def doc_matches_cs_entry(doc: Path, cs: CsEntry) -> bool:
    if cs_parent_for_doc(doc) != topic_dir_for_cs(cs):
        return False
    # A base-code CS must not swallow a later amendment PDF. An amendment CS may.
    if is_amendment(doc.name) and not is_amendment(cs.path.name):
        return False
    dkey = norm_key(doc.name)
    if dkey == cs.key or dkey.startswith(cs.key) or cs.key.startswith(dkey):
        return True
    if len(cs.key) > 10 and cs.key in dkey:
        return True
    doc_cap = cap_prefix(doc.name)
    cs_cap = cap_prefix(cs.title)
    if doc_cap and cs_cap and doc_cap == cs_cap:
        return True
    doc_circ = circular_key(doc.name)
    cs_circ = circular_key(cs.title)
    if doc_circ and cs_circ and doc_circ == cs_circ:
        return True
    doc_jpn = jpn_key(doc.name)
    cs_jpn = jpn_key(cs.title)
    if doc_jpn and cs_jpn and doc_jpn == cs_jpn:
        return True
    doc_pnrc = _pnrc_key(doc.name)
    cs_pnrc = _pnrc_key(cs.title)
    if doc_pnrc and cs_pnrc and doc_pnrc == cs_pnrc:
        return True
    return False


def cs_title(path: Path) -> str:
    name = path.name
    if "Architect Critical Summary" in name:
        return re.sub(r"\s+Architect Critical Summary.*", "", name.replace(".md", ""))
    return name.replace("_CS.md", "")


def rename_cs_filename(name: str) -> str:
    if name.endswith("_CS.md"):
        return name
    if not name.endswith(".md"):
        return name
    base = name[:-3]
    match = re.match(r"^(.*?)\s+Architect Critical Summary(?:\s+(\([^)]+\)))?$", base)
    if not match:
        return name
    title, extra = match.group(1), match.group(2) or ""
    return f"{title} {extra}_CS.md".strip() if extra else f"{title}_CS.md"


def norm_key(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+architect critical summary.*", "", text)
    text = re.sub(r"_cs$", "", text)
    text = re.sub(r"\.(pdf|md)$", "", text)
    text = re.sub(r"\s+consolidated version.*", "", text)
    text = re.sub(r"\s+\([^)]*english[^)]*\)", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def is_amendment(name: str) -> bool:
    return bool(AMENDMENT_RE.search(name))


def circular_key(name: str) -> tuple[str, str] | None:
    match = re.search(r"no\.\s*(\d+)-(\d{4})", name, re.I)
    if match:
        return match.group(1), match.group(2)
    return None


def jpn_key(name: str) -> str | None:
    match = re.search(r"joint practice note no\.?\s*(\d+)", name, re.I)
    return match.group(1) if match else None


def cap_prefix(name: str) -> str | None:
    match = re.search(r"(cap\s+\d+[a-z]?)", name, re.I)
    return norm_key(match.group(1)) if match else None


@dataclass
class CsEntry:
    path: Path
    title: str
    key: str
    parent: Path


def collect_cs_files() -> list[CsEntry]:
    entries: list[CsEntry] = []
    for path in sorted(HK_REF.rglob("*")):
        if path.is_file() and is_cs_file(path):
            title = cs_title(path)
            entries.append(
                CsEntry(path=path, title=title, key=norm_key(title), parent=path.parent)
            )
    return entries


def doc_matches_cs(doc: Path, cs: CsEntry) -> bool:
    return doc_matches_cs_entry(doc, cs)


def find_moves(cs_entries: list[CsEntry]) -> list[tuple[Path, Path]]:
    moves: list[tuple[Path, Path]] = []
    seen: set[Path] = set()
    for cs in cs_entries:
        sr = cs.parent / "source_reference"
        for doc in cs.parent.iterdir():
            if not doc.is_file():
                continue
            if doc.suffix.lower() not in DOC_EXTS:
                continue
            if is_cs_file(doc):
                continue
            if doc in seen:
                continue
            if doc_matches_cs(doc, cs):
                target = sr / doc.name
                if doc.parent == sr:
                    continue
                moves.append((doc, target))
                seen.add(doc)
    return moves


def git_tracked(path: Path) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def move_file(src: Path, dst: Path, execute: bool) -> None:
    if not execute:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise FileExistsError(f"Target already exists: {dst}")
    if git_tracked(src):
        result = subprocess.run(
            ["git", "mv", str(src), str(dst)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return
    shutil.move(str(src), str(dst))


def rename_file(src: Path, dst: Path, execute: bool) -> None:
    if not execute:
        return
    if dst.exists():
        raise FileExistsError(f"Target already exists: {dst}")
    if git_tracked(src):
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT, check=True)
    else:
        src.rename(dst)


def match_doc_to_any_cs(doc: Path, cs_entries: list[CsEntry]) -> bool:
    if doc.name in REPORT_FILES:
        return False
    return any(doc_matches_cs_entry(doc, cs) for cs in cs_entries)


def _covered_source_files(cs: CsEntry, text: str) -> list[Path]:
    """Files this CS accounts for.

    Backtick names in ### Source cover cryptic amendment PDFs and PDFs nested
    under source_reference/. A companion named elsewhere in the CS does not.
    A folder-level link (more than _MAX_MATCH_HITS) does not cover every PDF.
    A markdown or text extract with the same stem as a named PDF is included.
    Matcher hits still refuse an unnamed amendment/base cross-pair.
    """
    sr = nearest_source_dir(cs)
    named_in_source = _named_source_files(text, sr)
    if named_in_source:
        return _with_text_twins(named_in_source, sr)
    explicit = _explicit_filename_source(cs, text)
    if explicit is not None:
        return [explicit]
    docs = _listable_docs(sr)
    if not docs:
        return []
    hits = _matcher_hits(cs, docs, sr)
    if 1 <= len(hits) <= _MAX_MATCH_HITS:
        return hits
    ident = _id_hit(cs.title, docs)
    if ident is not None:
        return [ident]
    stemmed = _stem_hit(cs.title, docs)
    if stemmed is not None:
        return [stemmed]
    return []


def collect_without_cs(cs_entries: list[CsEntry]) -> list[Path]:
    named: set[Path] = set()
    note_ids: dict[Path, set[tuple[str, int]]] = defaultdict(set)
    for cs in cs_entries:
        text = _read_cs(cs.path)
        named.update(_covered_source_files(cs, text))
        ident = _pnap_note_id(cs.path.name)
        if ident is not None:
            note_ids[topic_dir_for_cs(cs)].add(ident)
    without: list[Path] = []
    for path in sorted(HK_REF.rglob("*")):
        if not path.is_file() or _is_gap_exempt(path):
            continue
        if path.suffix.lower() not in {".pdf", ".md"}:
            continue
        if is_cs_file(path):
            continue
        if path in named or match_doc_to_any_cs(path, cs_entries):
            continue
        if _note_extract_covered(path, note_ids):
            continue
        without.append(path)
    return without


def _note_extract_covered(path: Path, note_ids: dict[Path, set[tuple[str, int]]]) -> bool:
    """Cover a text extract whose APP/ADM/ADV number matches a CS in that topic.

    A PDF is not covered by number alone. The summary has to name that filename.
    """
    if path.suffix.lower() not in {".md", ".txt"} or "source_reference" not in path.parts:
        return False
    ident = _pnap_note_id(path.name)
    if ident is None:
        return False
    topic = _topic_owning_source(path)
    return topic is not None and ident in note_ids.get(topic, ())


_URL_RE = re.compile(r"https?://[^\s)>\]]+")
_BACKTICK_RE = re.compile(r"`([^`]+)`")
_STEM_NOISE_RE = re.compile(
    r"\b(brochure|english|chinese|traditional|edition|fifth|fourth|third|second|first|with|eurocodes)\b",
    re.I,
)
_PNBI_RE = re.compile(r"\bpnbi[-_\s]?0*(\d+)\b", re.I)
_PNRC_RE = re.compile(r"\bpnrc[-_\s]?0*(\d+)\b", re.I)
_PRACTICE_NOTE_RE = re.compile(
    r"(?:practice note no\.?\s+(?:apsrse\s+)?|pn\s*)(\d+)\s*[-_]\s*(\d{2,4})([a-z])?",
    re.I,
)
_PRACTICE_NOTE_REV_RE = re.compile(r"^(?:2k|(\d{4}))([a-z])?[-_](\d+)([a-z])?$", re.I)
_APSR_RE = re.compile(r"^(\d{2})(\d{2})apsr$", re.I)
_INV_EXTS = DOC_EXTS | {".rtf"}
_MAX_MATCH_HITS = 5


def nearest_source_dir(cs: CsEntry) -> Path:
    """source_reference next to the CS, or sibling of summaries/source_md."""
    if cs.path.parent.name in {"source_md", "summaries"}:
        return cs.path.parent.parent / "source_reference"
    return cs.path.parent / "source_reference"


def _md_path(path: Path, label: str | None = None) -> str:
    rel = path.relative_to(HK_REF).as_posix()
    text = (label if label is not None else path.name).replace("|", "\\|")
    return f"[{text}]({quote(rel, safe='/')})"


def _md_url(url: str) -> str:
    safe = url.replace("|", "%7C")
    return f"[{safe}]({safe})"


def _read_cs(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


_SOURCE_TREE_CACHE: dict[Path, list[Path]] = {}


def _source_tree_files(sr: Path) -> list[Path]:
    """Every file under source_reference/, including series subfolders such as PNAP_APPa_e."""
    cached = _SOURCE_TREE_CACHE.get(sr)
    if cached is None:
        cached = [path for path in sr.rglob("*") if path.is_file()] if sr.is_dir() else []
        _SOURCE_TREE_CACHE[sr] = cached
    return cached


def _files_by_basename(sr: Path) -> dict[str, list[Path]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in _source_tree_files(sr):
        grouped[path.name.lower()].append(path)
    return grouped


def _basename_hits(grouped: dict[str, list[Path]], token: str) -> list[Path]:
    token = token.strip().replace("\\", "/")
    if not token or "*" in token:
        return []
    hits = grouped.get(Path(token).name.lower(), [])
    if "/" not in token.strip("/"):
        return hits
    suffix = token.lower().rstrip("/")
    narrowed = [path for path in hits if path.as_posix().lower().endswith(suffix)]
    return narrowed or hits


def _with_text_twins(named: list[Path], sr: Path) -> list[Path]:
    """Markdown or text extracts that share a stem with a PDF named in ### Source."""
    stems = {path.stem.lower() for path in named if path.suffix.lower() == ".pdf"}
    if not stems:
        return named
    found = list(named)
    seen = set(named)
    for path in _source_tree_files(sr):
        if path in seen or path.suffix.lower() not in {".md", ".txt"}:
            continue
        if path.stem.lower() in stems:
            seen.add(path)
            found.append(path)
    return found


def _cited_files(text: str, sr: Path) -> list[Path]:
    if not sr.is_dir():
        return []
    grouped = _files_by_basename(sr)
    found: list[Path] = []
    seen: set[Path] = set()
    for line in text.splitlines():
        if "source_reference" not in line.replace("\\", "/"):
            continue
        for token in _BACKTICK_RE.findall(line):
            for hit in _basename_hits(grouped, token):
                if hit not in seen:
                    seen.add(hit)
                    found.append(hit)
    return found


def _listable_docs(sr: Path) -> list[Path]:
    if not sr.is_dir():
        return []
    return [
        p
        for p in sr.iterdir()
        if p.is_file() and p.suffix.lower() in _INV_EXTS and not is_amendment(p.name)
    ]


def _matcher_hits(cs: CsEntry, docs: list[Path], sr: Path) -> list[Path]:
    entry = CsEntry(path=cs.path, title=cs.title, key=cs.key, parent=sr.parent)
    hits = [doc for doc in docs if doc_matches_cs_entry(doc, entry)]
    cap = cap_prefix(cs.title)
    if cap:
        tight = [doc for doc in hits if cap_prefix(doc.name) == cap]
        if tight:
            return tight
    return hits


def _full_year(year: int) -> int:
    if year >= 100:
        return year
    return 1900 + year if year >= 70 else 2000 + year


def _label_stem(name: str) -> str:
    """Drop a real file extension. Leave titles whose dot is 'No.' alone."""
    suffix = Path(name).suffix.lower()
    if suffix in _INV_EXTS or suffix == ".md":
        return Path(name).stem
    return name


def _practice_note_key(name: str) -> tuple[int, int, str] | None:
    stem = _label_stem(name)
    match = _PRACTICE_NOTE_RE.search(stem)
    if match:
        suffix = match.group(3) or ""
        if suffix.lower() == "e":
            suffix = ""
        return int(match.group(1)), _full_year(int(match.group(2))), suffix.lower()
    match = _APSR_RE.match(stem)
    if match:
        return int(match.group(2)), _full_year(int(match.group(1))), ""
    match = _PRACTICE_NOTE_REV_RE.match(stem)
    if not match:
        return None
    year = 2000 if match.group(1) is None else int(match.group(1))
    suffix = (match.group(2) or match.group(4) or "").lower()
    if suffix == "e":
        suffix = ""
    return int(match.group(3)), year, suffix


def _pnbi_key(name: str) -> str | None:
    match = _PNBI_RE.search(name)
    return str(int(match.group(1))) if match else None


def _pnrc_key(name: str) -> str | None:
    match = _PNRC_RE.search(name)
    return str(int(match.group(1))) if match else None


def _id_hit(title: str, docs: list[Path]) -> Path | None:
    pnbi = _pnbi_key(title)
    if pnbi:
        hits = [doc for doc in docs if _pnbi_key(doc.name) == pnbi]
        if len(hits) == 1:
            return hits[0]
    pnrc = _pnrc_key(title)
    if pnrc:
        hits = [doc for doc in docs if _pnrc_key(doc.name) == pnrc]
        if len(hits) == 1:
            return hits[0]
    note = _practice_note_key(title)
    if note:
        hits = [doc for doc in docs if _practice_note_key(doc.name) == note]
        if len(hits) == 1:
            return hits[0]
    return None


def _loose_stem(name: str) -> str:
    text = _STEM_NOISE_RE.sub(" ", _label_stem(name).lower())
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text).split())


def _rejects_other_circular(title: str, doc_name: str) -> bool:
    """Shared words must not pair two different 'No. N-YYYY' circulars."""
    cs_circ = circular_key(title)
    doc_circ = circular_key(doc_name)
    return bool(cs_circ and doc_circ and cs_circ != doc_circ)


def _stem_hit(title: str, docs: list[Path]) -> Path | None:
    cs_key = _loose_stem(title)
    if len(cs_key) < 12:
        return None
    contained = [
        doc
        for doc in docs
        if not _rejects_other_circular(title, doc.name)
        and (cs_key in (dk := _loose_stem(doc.name)) or dk in cs_key)
    ]
    if len(contained) == 1:
        return contained[0]
    if contained:
        return None
    cs_tokens = [tok for tok in cs_key.split() if len(tok) >= 3]
    scored: list[tuple[int, Path]] = []
    for doc in docs:
        if _rejects_other_circular(title, doc.name):
            continue
        doc_tokens = set(_loose_stem(doc.name).split())
        doc_tokens |= {tok[:-1] for tok in doc_tokens if tok.endswith("s") and len(tok) > 4}
        shared = [
            tok
            for tok in cs_tokens
            if tok in doc_tokens or (tok.endswith("s") and len(tok) > 4 and tok[:-1] in doc_tokens)
        ]
        long = sum(1 for tok in shared if len(tok) >= 5)
        if len(shared) < 2 or (long < 1 and len(shared) < 3):
            continue
        scored.append((len(shared), doc))
    if not scored:
        return None
    scored.sort(key=lambda item: (-item[0], item[1].name.lower()))
    if len(scored) > 1 and scored[0][0] == scored[1][0]:
        return None
    return scored[0][1]


def _opening_url(text: str) -> str | None:
    head = "\n".join(text.splitlines()[:20])
    match = _URL_RE.search(head)
    return match.group(0).rstrip(".,;") if match else None


def _source_section(text: str) -> str:
    match = re.search(r"(?m)^### Source\s*$", text)
    if not match:
        return ""
    rest = text[match.end() :]
    nxt = re.search(r"(?m)^#{1,6} ", rest)
    return rest[: nxt.start()] if nxt else rest


def _filename_mentioned(section: str, name: str) -> bool:
    """True when name appears as its own filename, not inside a longer filename."""
    low = section.lower()
    needle = name.lower()
    start = 0
    while True:
        index = low.find(needle, start)
        if index < 0:
            return False
        before = low[index - 1] if index else ""
        if before.isalnum() or before in "._-":
            start = index + 1
            continue
        return True


def _named_source_files(text: str, sr: Path) -> list[Path]:
    """Filenames in ### Source that exist anywhere under this source_reference/.

    A PDF in a series subfolder counts. The file does not have to sit directly
    in source_reference/. Backticks win. A bare filename is accepted when it
    is not glued to a longer name, so 'Chapter 10 (English).pdf' pairs and
    '1.pdf' does not hide inside 'Chapter 11 (English).pdf'.
    """
    if not sr.is_dir():
        return []
    files = _source_tree_files(sr)
    grouped = _files_by_basename(sr)
    found: list[Path] = []
    seen: set[Path] = set()
    section = _source_section(text)
    for token in _BACKTICK_RE.findall(section):
        for hit in _basename_hits(grouped, token):
            if hit not in seen:
                seen.add(hit)
                found.append(hit)
    # Longer names first so a short filename cannot claim a longer one's text.
    for path in sorted(files, key=lambda item: len(item.name), reverse=True):
        if path in seen or len(path.name) < 8:
            continue
        if path.suffix.lower() not in _INV_EXTS and path.suffix.lower() != ".pdf":
            continue
        if _filename_mentioned(section, path.name):
            seen.add(path)
            found.append(path)
    return found


def _explicit_filename_source(cs: CsEntry, text: str) -> Path | None:
    """Filename the CS names, when title matching is missing or ambiguous.

    A unique 1..5 title hit stays in charge so an extra backtick cannot
    replace an already-correct pair.
    """
    sr = nearest_source_dir(cs)
    if _cited_files(text, sr):
        return None
    docs = _listable_docs(sr)
    hits = _matcher_hits(cs, docs, sr) if docs else []
    if 1 <= len(hits) <= _MAX_MATCH_HITS:
        return None
    named = _named_source_files(text, sr)
    return named[0] if len(named) == 1 else None


def _source_cell(cs: CsEntry, text: str, sole: bool) -> tuple[str, bool]:
    sr = nearest_source_dir(cs)
    cited = _cited_files(text, sr)
    if cited:
        return "<br>".join(_md_path(path) for path in cited), True
    explicit = _explicit_filename_source(cs, text)
    if explicit is not None:
        return _md_path(explicit), True
    docs = _listable_docs(sr)
    hits = _matcher_hits(cs, docs, sr) if docs else []
    if len(hits) > _MAX_MATCH_HITS:
        return _md_path(sr, "source_reference/"), True
    if hits:
        ordered = sorted(hits, key=lambda path: path.name.lower())
        return "<br>".join(_md_path(path) for path in ordered), True
    ident = _id_hit(cs.title, docs) if docs else None
    if ident is not None:
        return _md_path(ident), True
    stemmed = _stem_hit(cs.title, docs) if docs else None
    if stemmed is not None:
        return _md_path(stemmed), True
    url = _opening_url(text)
    if url:
        return _md_url(url), True
    if sole and sr.is_dir() and any(path.is_file() for path in sr.iterdir()):
        return _md_path(sr, "source_reference/"), True
    return "—", False


def _assert_inventory_samples(cells: dict[str, str]) -> None:
    """ponytail: fails regeneration if a known CS/source pair stops resolving."""
    samples = {
        "BEAM Plus Assessment Tools/BEAM Plus New Buildings V2.0_CS.md": "BEAM Plus New Buildings V2.0 Brochure.pdf",
        "Building Department (BD)/Cap 123 Building Ordience/Cap 123 (01-03-2026)_Buildings Ordinance_CS.md": "Cap 123 Consolidated",
        "Fire Department (FSD)/summaries/FSD Circular Letter No. 1-1997 Fire Services Requirements for Refuge Floors_CS.md": "1-1997",
        "Fire Department (FSD)/summaries/FSD Circular Letter No. 1-2011 Delisting of Fire Extinguishers Containing Scheduled Substances_CS.md": "2011_01.pdf",
        "Fire Department (FSD)/summaries/FSD Circular Letter No. 2-2007 Certification of FSI under Fire Safety Buildings Ordinance Cap 572_CS.md": "2007_02.pdf",
        "Building Department (BD)/BD Website/Alterations and additions/Alterations and additions_CS.md": "bd.gov.hk/en/building-works/alterations-and-additions",
        "Land Department (LandD)/LACO Circular Memorandum/summaries/LACO Circular Memorandum No. 72 (26-04-2013)_CS.md": "72.pdf",
        "Planning Department (PlanD)/Cap 131 Town Planning Ordinance/Cap 131 (02-11-2023)_CS.md": "—",
    }
    for rel, needle in samples.items():
        cell = cells.get(rel, "")
        if needle not in cell:
            raise AssertionError(f"{rel} source cell missing {needle!r}: {cell}")
    cap = cells[
        "Building Department (BD)/Cap 123 Building Ordience/Cap 123 (01-03-2026)_Buildings Ordinance_CS.md"
    ]
    if "Cap 123A" in cap:
        raise AssertionError(f"Cap 123 row also linked Cap 123A: {cap}")


def _assert_gap_pairing(without: list[Path]) -> None:
    """A summaries/*_CS.md covers its source PDF, including one nested under source_reference/."""
    rels = {path.relative_to(HK_REF).as_posix() for path in without}
    covered = [
        "Joint Practice Notes (JPN)/source_reference/Joint Practice Note No. 1 Green and Innovative Buildings.pdf",
        "Joint Practice Notes (JPN)/JPN_Table_English.md",
        "Building Department (BD)/Codes of Practice and Design Manuals/Structure/source_reference/CoP_SUC2013e_amendment202306.pdf",
        "Building Department (BD)/Codes of Practice and Design Manuals/Structure/Structure_Table_English.md",
        "Building Department (BD)/Practice Notes for Registered Contractors (PNRC)/source_reference/Pnrc02.pdf",
        "Planning Department (PlanD)/Hong Kong Planning Standards and Guidelines/source_reference/Chapter 10 (English).pdf",
        "Building Department (BD)/Codes of Practice and Design Manuals/Miscellaneous/source_reference/CoP MBIS MWIS 2012 (2023 Edition).pdf",
        "Building Department (BD)/Codes of Practice and Design Manuals/Structure/source_reference/EMSUOS2011e.pdf",
        "Building Department (BD)/Codes of Practice and Design Manuals/Structure/source_reference/ExplanatoryNotesWindEffects2019e.pdf",
        "Building Department (BD)/Practice Notes for Authorized Persons (PNAP)/source_reference/PNAP_APPa_e/APP-005 Height of Storeys - Regulations 3(3) & 24 of Building (Planning).pdf",
        "Building Department (BD)/Practice Notes for Authorized Persons (PNAP)/source_reference/PNAP_APPb_e/_extracted_txt/APP-101 Podium Height Restriction under Building (Planning).md",
    ]
    still = [item for item in covered if item in rels]
    if still:
        raise AssertionError("expected these to leave the gap list:\n" + "\n".join(still))
    still_open: list[str] = [
        "Building Department (BD)/Minor Works (MWCS)/Additional Documents/MW33 Submission of Supplementary Documents or Information.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Change Cessation of Appointment of Prescribed Building Professional Contractor/MW07 Notice of Change in Appointment of RSE RGE or PRC.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Change Cessation of Appointment of Prescribed Building Professional Contractor/MW08 Notice of Change in Appointment of AP or RI.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Change Cessation of Appointment of Prescribed Building Professional Contractor/MW09 Notice of Nomination of Temporary PBP.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Change Cessation of Appointment of Prescribed Building Professional Contractor/MW10 Notice of Cessation of Appointment of PRC.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Change Cessation of Appointment of Prescribed Building Professional Contractor/MW31 Notice of PBP Ceasing to be Appointed or Nominated.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class I Minor Works/MW01 Notice of Commencement of Minor Works (with PBP Appointed).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class I Minor Works/MW02 Certificate of Completion of Minor Works (with PBP Appointed).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class I Minor Works/MW11 Notice of Commencement of Additional Class I Minor Works (with PBP).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class II Minor Works/MW03 Notice of Commencement of Minor Works (without PBP).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class II Minor Works/MW04 Certificate of Completion of Minor Works (without PBP).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class II Minor Works/MW12 Notice of Commencement of Additional Class II Minor Works (without PBP).pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class III Minor Works/MW05 Notice and Certificate of Completion of Class III Minor Works.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Class III Minor Works/MW32 Request for Submission Number for Class III Signboard.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Household Minor Works Validation Scheme/MW06-3 Certificate for Household Minor Works Validation Scheme.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Minor Amenity Feature Validation Scheme/MW06-1 Certificate of Completion of Associated Alteration or Strengthening Works Class I.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Minor Amenity Feature Validation Scheme/MW06-2 Certificate of Completion of Associated Alteration or Strengthening Works Class II.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Minor Amenity Feature Validation Scheme/MW06-3 Certificate of Completion of Associated Alteration or Strengthening Works Class III.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR1 Attachment of Photographs.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR2 Attachment of A3 Plans.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR3 Attachment of A4 Plans.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR4 Attachment of Structural Calculations.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR5 Attachment of Supervision Plan Class I.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/PR6 Attachment of Safety Inspection Report or Related Documents.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/SP Supervision Plan.pdf",
        "Building Department (BD)/Minor Works (MWCS)/Supporting Information/VSR Safety Inspection Checklist for Validation Scheme.pdf",
        "Water Authority (WSD)/Figure.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P1.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P2.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P3.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P4.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P4A.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P4B.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P5.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/P5A.pdf",
        "Environmental Protection Department (EPD)/Cap. 311 Air Pollution Control Ordinance/source_reference/document_1.pdf",
        "Environmental Protection Department (EPD)/Cap. 358 Water Pollution Control Ordinance/source_reference/document_1.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P1.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P2.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P3.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P4.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P5.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/P6.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/document_1.pdf",
        "Environmental Protection Department (EPD)/Cap. 400 Noise Control Ordinance/source_reference/sch0.pdf",
    ]
    missing = [item for item in still_open if item not in rels]
    if missing:
        raise AssertionError("expected these to stay on the gap list:\n" + "\n".join(missing))


def write_cs_inventory(cs_entries: list[CsEntry]) -> Path:
    out = HK_REF / "_CS_INVENTORY.md"
    texts = {cs.path: _read_cs(cs.path) for cs in cs_entries}
    sr_counts: dict[Path, int] = defaultdict(int)
    for cs in cs_entries:
        sr_counts[nearest_source_dir(cs)] += 1

    rows: dict[str, list[tuple[str, str, str, bool]]] = defaultdict(list)
    cells: dict[str, str] = {}
    for cs in cs_entries:
        folder = cs.path.parent.relative_to(HK_REF).as_posix()
        if folder == ".":
            folder = ""
        cell, resolved = _source_cell(cs, texts[cs.path], sr_counts[nearest_source_dir(cs)] == 1)
        rel = cs.path.relative_to(HK_REF).as_posix()
        cells[rel] = cell
        rows[folder].append((cs.path.name, _md_path(cs.path), cell, resolved))

    _assert_inventory_samples(cells)

    lines = [
        "# Critical Summary Inventory",
        "",
        f"Total: **{len(cs_entries)}** files",
        "",
        "| Folder | CS | With source |",
        "|---|---:|---:|",
    ]
    for folder in sorted(rows):
        items = rows[folder]
        label = folder or "(root)"
        lines.append(f"| {label} | {len(items)} | {sum(1 for item in items if item[3])} |")
    lines.append("")

    for folder in sorted(rows):
        items = sorted(rows[folder], key=lambda item: item[0].lower())
        heading = folder or "(root)"
        lines.append(f"## {heading} ({len(items)})")
        lines.append("")
        lines.append("| CS | Source |")
        lines.append("|---|---|")
        for _name, cs_link, cell, _resolved in items:
            lines.append(f"| {cs_link} | {cell} |")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_without_cs_report(without: list[Path]) -> Path:
    out = HK_REF / "DOCUMENTS_WITHOUT_CS.md"
    by_dept: dict[str, list[str]] = defaultdict(list)
    for path in without:
        rel = path.relative_to(HK_REF)
        dept = rel.parts[0] if rel.parts else "."
        by_dept[dept].append(str(rel).replace("\\", "/"))

    lines = [
        "# Documents Without Critical Summary",
        "",
        f"Total: **{len(without)}** files (PDF and MD)",
        "",
        "## Summary by department",
        "",
        "| Department | Count |",
        "|------------|------:|",
    ]
    for dept in sorted(by_dept, key=lambda d: (-len(by_dept[d]), d)):
        lines.append(f"| {dept} | {len(by_dept[dept])} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    for dept in sorted(by_dept):
        items = sorted(by_dept[dept])
        lines.append(f"## {dept} ({len(items)})")
        lines.append("")
        for item in items:
            lines.append(f"- `{item}`")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def run(execute: bool, report_only: bool) -> int:
    cs_entries = collect_cs_files()
    print(f"Found {len(cs_entries)} Critical Summary files")

    if not report_only:
        renames = [
            (cs.path, cs.path.parent / rename_cs_filename(cs.path.name))
            for cs in cs_entries
            if cs.path.name != rename_cs_filename(cs.path.name)
        ]
        moves = find_moves(cs_entries)
        sr_dirs = sorted({dst.parent for _, dst in moves})

        print(f"Renames: {len(renames)}")
        print(f"Moves to source_reference/: {len(moves)}")
        print(f"source_reference/ dirs to create: {len(sr_dirs)}")

        for src, dst in renames:
            print(f"  RENAME: {src.relative_to(HK_REF)} -> {dst.name}")
            rename_file(src, dst, execute)

        if execute:
            for sr in sr_dirs:
                sr.mkdir(parents=True, exist_ok=True)

        for src, dst in moves:
            print(f"  MOVE: {src.relative_to(HK_REF)} -> {dst.relative_to(HK_REF)}")
            move_file(src, dst, execute)

        # Refresh CS paths after rename for accurate reporting
        if execute and renames:
            cs_entries = collect_cs_files()

    without = collect_without_cs(cs_entries)
    _assert_gap_pairing(without)
    inv = write_cs_inventory(cs_entries)
    report = write_without_cs_report(without)
    print(f"Wrote {inv.relative_to(ROOT)}")
    print(f"Wrote {report.relative_to(ROOT)} ({len(without)} docs without CS)")

    remaining = [
        p for p in HK_REF.rglob("*") if p.is_file() and "Architect Critical Summary" in p.name
    ]
    if remaining:
        print(f"WARNING: {len(remaining)} files still contain 'Architect Critical Summary' in name")
        for p in remaining[:5]:
            print(f"  {p.relative_to(HK_REF)}")
        return 1

    mode = "EXECUTED" if execute else "DRY-RUN"
    print(f"\n{mode} complete.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Apply renames and moves (default: dry-run, reports always written)",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Only regenerate inventory and without-CS reports",
    )
    args = parser.parse_args()
    sys.exit(run(execute=args.execute, report_only=args.report_only))


if __name__ == "__main__":
    main()
