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


REPORT_FILES = {"DOCUMENTS_WITHOUT_CS.md", "_CS_INVENTORY.md"}


def is_cs_file(path: Path) -> bool:
    name = path.name
    if name in REPORT_FILES:
        return False
    return "Architect Critical Summary" in name or name.endswith("_CS.md")


def cs_parent_for_doc(doc: Path) -> Path:
    """Parent folder that owns a source document (handles source_reference/ subfolder)."""
    if doc.parent.name == "source_reference":
        return doc.parent.parent
    return doc.parent


def doc_matches_cs_entry(doc: Path, cs: CsEntry) -> bool:
    if cs_parent_for_doc(doc) != cs.parent:
        return False
    if is_amendment(doc.name):
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


def collect_without_cs(cs_entries: list[CsEntry]) -> list[Path]:
    named: set[Path] = set()
    for cs in cs_entries:
        hit = _explicit_filename_source(cs, _read_cs(cs.path))
        if hit is not None:
            named.add(hit)
    without: list[Path] = []
    for path in sorted(HK_REF.rglob("*")):
        if not path.is_file():
            continue
        if path.name in REPORT_FILES:
            continue
        if path.suffix.lower() not in {".pdf", ".md"}:
            continue
        if is_cs_file(path):
            continue
        if path in named or match_doc_to_any_cs(path, cs_entries):
            continue
        without.append(path)
    return without


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


def _cited_files(text: str, sr: Path) -> list[Path]:
    if not sr.is_dir():
        return []
    by_name = {p.name.lower(): p for p in sr.iterdir() if p.is_file()}
    found: list[Path] = []
    seen: set[Path] = set()
    for line in text.splitlines():
        if "source_reference" not in line.replace("\\", "/"):
            continue
        for token in _BACKTICK_RE.findall(line):
            token = token.strip().replace("\\", "/")
            if not token or "*" in token:
                continue
            hit = by_name.get(token.split("/")[-1].lower())
            if hit is not None and hit not in seen:
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


def _named_source_files(text: str, sr: Path) -> list[Path]:
    """Backtick filenames in ### Source that exist in this source_reference/."""
    if not sr.is_dir():
        return []
    by_name = {path.name.lower(): path for path in sr.iterdir() if path.is_file()}
    found: list[Path] = []
    seen: set[Path] = set()
    for token in _BACKTICK_RE.findall(_source_section(text)):
        token = token.strip().replace("\\", "/")
        if not token or "*" in token:
            continue
        hit = by_name.get(Path(token).name.lower())
        if hit is not None and hit not in seen:
            seen.add(hit)
            found.append(hit)
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
