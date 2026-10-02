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
        if not match_doc_to_any_cs(path, cs_entries):
            without.append(path)
    return without


def write_cs_inventory(cs_entries: list[CsEntry]) -> Path:
    out = HK_REF / "_CS_INVENTORY.md"
    by_folder: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for cs in cs_entries:
        folder = str(cs.path.parent.relative_to(HK_REF))
        old_name = cs.path.name
        new_name = rename_cs_filename(old_name)
        by_folder[folder].append((old_name, new_name))

    lines = [
        "# Critical Summary Inventory",
        "",
        f"Total: **{len(cs_entries)}** files",
        "",
    ]
    for folder in sorted(by_folder):
        items = by_folder[folder]
        lines.append(f"## {folder} ({len(items)})")
        lines.append("")
        for old, new in sorted(items):
            if old == new:
                lines.append(f"- `{new}`")
            else:
                lines.append(f"- `{old}` → `{new}`")
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
