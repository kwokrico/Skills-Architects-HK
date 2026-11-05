#!/usr/bin/env python3
"""Build a Gemini upload zip for hk-architect-master.

Reads hk-architect-master and writes dist/gemini/hk-architect-master.zip.
Does not write into hk-architect-master or hk_architect_skills.
Statutory folders, linked reference sheets, and templates are concatenated
inside the zip. Calculator wording that points at main.py is rewritten
only inside the zip.
"""

from __future__ import annotations

import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = ROOT / "hk-architect-master"
ZIP_PATH = ROOT / "dist" / "gemini" / "hk-architect-master.zip"
FOLDER = "hk-architect-master"
SIZE_LIMIT = 100 * 1024 * 1024
DESCRIPTION_LIMIT = 1024
ENTERPRISE_FILE_CAP = 100
# 47 subskills + 28 catalogues + 5 loose references + SKILL.md + calculators.py
# + 10 statutory bundles + linked-sheets.md + templates.md
EXPECTED_FILES = 94
BUNDLE_INTRO = "Sections below are the original files; use the heading as the filename."

ALLOWED_EXTENSIONS = {
    ".txt",
    ".md",
    ".rst",
    ".rtf",
    ".tex",
    ".log",
    ".py",
    ".sh",
    ".json",
    ".yaml",
    ".csv",
    ".toml",
    ".xml",
    ".env",
    ".sql",
    ".html",
    ".css",
    ".svg",
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".tif",
    ".tiff",
}
ALLOWED_NAMES = {"Makefile", "Dockerfile"}
NETWORK_MARKERS = ("http", "socket", "urllib")

STATUTORY_COLLECTIONS = (
    "beam-plus",
    "fsd-circulars",
    "hkia",
    "lands-circulars",
    "lands-practice-notes",
    "minor-works",
    "ozp-notes",
    "pnap",
    "pnbi",
    "pnrc",
)
KEPT_REFERENCE_FILES = {
    "compliance.md",
    "config.json",
    "domain_terms.json",
    "foundation.md",
    "operational.md",
}
LINKED_SHEETS = (
    "hia-starter-checklist.md",
    "hk-common-material-dimensions.md",
    "hk-construction-sequence-swimlanes.md",
    "hk-construction-stakeholder-register.md",
    "hk-human-scale-dimensions.md",
    "hk-ofca-licensed-works.md",
    "hk-pow-stages-0-7.md",
    "hk-procurement-routes-comparison.md",
    "hk-site-establishment-checklist.md",
    "hk-td-submission-types.md",
    "hk-typhoon-eot-by-procurement.md",
)

SKILL_CALC_OLD = """Run a check through the package entry:

```bash
echo '{"tool":"run_hk_calculator","arguments":{"calc_type":"gfa_aggregator","data":{"floors":[{"area":500,"is_exempt":false}]}}}' | python hk-architect-master/main.py
```
"""
SKILL_CALC_NEW = (
    "Apply these three checks from "
    "[scripts/calculators.py](scripts/calculators.py) in the reply: "
    "`egress_1004_7`, `gfa_aggregator`, and `layout_sort`. Do not run `main.py`.\n"
)
CALC_TOPIC = Path("subskills/hk-architect-calculator/hk-architect-calculator.md")
CALC_TOPIC_REPLACEMENTS = (
    (
        "Markdown formulas above are for reasoning; numeric checks use `main.py`:",
        "Markdown formulas above are for reasoning; numeric checks use `scripts/calculators.py`:",
    ),
    (
        "OTTV, RTTV, occupant load, and daylight factor are **not** implemented in `core/calculators.py`",
        "OTTV, RTTV, occupant load, and daylight factor are **not** implemented in `scripts/calculators.py`",
    ),
)
COLLECTION_NAME = re.compile(r"[a-z0-9-]+")


def fail(message: str) -> None:
    raise SystemExit(message)


def allowed_file(path: Path) -> bool:
    return path.name in ALLOWED_NAMES or path.suffix.lower() in ALLOWED_EXTENSIONS


def iter_source_files(skill_root: Path) -> list[Path]:
    """Files eligible for the Gemini zip, including ones that will be bundled."""
    chosen: list[Path] = [skill_root / "SKILL.md", skill_root / "scripts" / "calculators.py"]
    for base in (skill_root / "subskills", skill_root / "references"):
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if any(part in {"__pycache__", "evals"} for part in path.parts):
                continue
            if path.name in {".DS_Store", ".gitignore", "LICENSE"} or path.suffix == ".pyc":
                continue
            if base.name == "references" and path.suffix.lower() not in {".md", ".json"}:
                continue
            chosen.append(path)
    missing = [path for path in chosen if not path.is_file()]
    if missing:
        fail("missing source files: " + ", ".join(str(path) for path in missing))
    return chosen


def apply_calculator_wording(rel: Path, text: str) -> str:
    if rel.as_posix() == "SKILL.md":
        if SKILL_CALC_OLD not in text:
            fail("SKILL.md no longer contains the Cursor calculator command")
        text = text.replace(SKILL_CALC_OLD, SKILL_CALC_NEW, 1)
        if "python hk-architect-master/main.py" in text:
            fail("SKILL.md still tells Gemini to run main.py")
        return text
    if rel == CALC_TOPIC:
        for old, new in CALC_TOPIC_REPLACEMENTS:
            if old not in text:
                fail(f"{rel.as_posix()} missing expected text: {old}")
            text = text.replace(old, new, 1)
        if "`main.py`" in text or "core/calculators.py" in text:
            fail(f"{rel.as_posix()} still points at the Cursor calculator entry")
    return text


def _read_rest(text: str, start: int, *, in_tick: bool, in_link: bool) -> tuple[str, int]:
    if in_link:
        if start < len(text) and text[start] == ")":
            return "", start
        marker = ".md)"
        at = text.find(marker, start)
        if at < 0:
            fail("link path does not end at .md)")
        return text[start:at + 3], at + 3
    stops = {"`", "\n"} if in_tick else {" ", "\t", "\n", "`", ")", "|"}
    index = start
    while index < len(text) and text[index] not in stops:
        index += 1
    return text[start:index], index


def _emit(dest: str, section: str | None, *, in_tick: bool, closer: str, closes_tick: bool) -> str:
    if not section:
        return f"{dest}{closer}"
    if in_tick or closes_tick:
        return f"{dest}` section `{section}"
    return f"{dest}{closer} section `{section}`"


def _splice_collection(text: str, marker: str, dest_prefix: str) -> str:
    """Replace statutory path citations. Headings are not passed through here."""
    pieces: list[str] = []
    cursor = 0
    while True:
        found = text.find(marker, cursor)
        if found < 0:
            pieces.append(text[cursor:])
            break
        if found > 0 and text[found - 1] == "[":
            pieces.append(text[cursor:found + len(marker)])
            cursor = found + len(marker)
            continue
        pieces.append(text[cursor:found])
        name_at = found + len(marker)
        name_match = COLLECTION_NAME.match(text, name_at)
        if name_match is None or name_match.group(0) not in STATUTORY_COLLECTIONS:
            pieces.append(marker)
            cursor = name_at
            continue
        collection = name_match.group(0)
        slash_at = name_match.end()
        if slash_at >= len(text) or text[slash_at] != "/":
            pieces.append(text[found:slash_at])
            cursor = slash_at
            continue
        in_tick = found > 0 and text[found - 1] == "`"
        in_link = found > 0 and text[found - 1] == "("
        rest, end = _read_rest(text, slash_at + 1, in_tick=in_tick, in_link=in_link)
        dest = f"{dest_prefix}{collection}.md"
        closes_tick = end < len(text) and text[end] == "`"
        closer = ""
        if in_link and end < len(text) and text[end] == ")":
            end += 1
            closer = ")"
        section = unquote(rest) if rest else None
        pieces.append(_emit(dest, section, in_tick=in_tick, closer=closer, closes_tick=closes_tick))
        cursor = end
    return "".join(pieces)


def _splice_fixed(text: str, marker: str, dest: str, section: str | None) -> str:
    pieces: list[str] = []
    cursor = 0
    while True:
        found = text.find(marker, cursor)
        if found < 0:
            pieces.append(text[cursor:])
            break
        if found > 0 and text[found - 1] == "[":
            pieces.append(text[cursor:found + len(marker)])
            cursor = found + len(marker)
            continue
        pieces.append(text[cursor:found])
        end = found + len(marker)
        in_tick = found > 0 and text[found - 1] == "`"
        in_link = found > 0 and text[found - 1] == "("
        closes_tick = end < len(text) and text[end] == "`"
        closer = ""
        if in_link and end < len(text) and text[end] == ")":
            end += 1
            closer = ")"
        pieces.append(_emit(dest, section, in_tick=in_tick, closer=closer, closes_tick=closes_tick))
        cursor = end
    return "".join(pieces)


def rewrite_citations(text: str) -> str:
    text = _splice_collection(text, "references/statutory/", "references/statutory/")
    text = _splice_collection(text, "../statutory/", "../statutory/")
    for name in sorted(LINKED_SHEETS, key=len, reverse=True):
        text = _splice_fixed(text, f"references/{name}", "references/linked-sheets.md", name)
    text = _splice_templates(text)
    return text


def _splice_templates(text: str) -> str:
    marker = "references/templates/"
    pieces: list[str] = []
    cursor = 0
    while True:
        found = text.find(marker, cursor)
        if found < 0:
            pieces.append(text[cursor:])
            break
        if found > 0 and text[found - 1] == "[":
            pieces.append(text[cursor:found + len(marker)])
            cursor = found + len(marker)
            continue
        pieces.append(text[cursor:found])
        in_tick = found > 0 and text[found - 1] == "`"
        in_link = found > 0 and text[found - 1] == "("
        rest, end = _read_rest(text, found + len(marker), in_tick=in_tick, in_link=in_link)
        dest = "references/templates.md"
        section = unquote(rest) if rest else None
        closes_tick = end < len(text) and text[end] == "`"
        closer = ""
        if in_link and end < len(text) and text[end] == ")":
            end += 1
            closer = ")"
        pieces.append(_emit(dest, section, in_tick=in_tick, closer=closer, closes_tick=closes_tick))
        cursor = end
    return "".join(pieces)


def _self_check() -> None:
    sample = (
        "See [pnap](references/statutory/pnap/). "
        "Critical Summary: `references/statutory/hkia/HKIA Code of Professional Conduct (18-08-2017)_CS.md`. "
        "[Rules](../statutory/hkia/HKIA%20Rules%20of%20the%20Institute%20(17-06-2021)_CS.md) "
        "and [hia](references/hia-starter-checklist.md) "
        "and `../../references/hk-pow-stages-0-7.md` "
        "and [references/templates/](references/templates/) "
        "and `../../references/templates/construction-look-ahead.md`."
    )
    got = rewrite_citations(sample)
    expected = (
        "See [pnap](references/statutory/pnap.md). "
        "Critical Summary: `references/statutory/hkia.md` section `HKIA Code of Professional Conduct (18-08-2017)_CS.md`. "
        "[Rules](../statutory/hkia.md) section `HKIA Rules of the Institute (17-06-2021)_CS.md` "
        "and [hia](references/linked-sheets.md) section `hia-starter-checklist.md` "
        "and `../../references/linked-sheets.md` section `hk-pow-stages-0-7.md` "
        "and [references/templates/](references/templates.md) "
        "and `../../references/templates.md` section `construction-look-ahead.md`."
    )
    if got != expected:
        fail(f"citation rewrite self-check failed:\n{got}")


def render_bundle(sections: list[tuple[str, str]]) -> str:
    chunks = [BUNDLE_INTRO, ""]
    for heading, body in sections:
        chunks.append(f"## {heading}")
        chunks.append("")
        chunks.append(body)
        chunks.append("")
    return "\n".join(chunks).rstrip() + "\n"


def packed_markdown(rel: Path, text: str) -> str:
    return rewrite_citations(apply_calculator_wording(rel, text))


def section_body(path: Path) -> str:
    return rewrite_citations(path.read_text(encoding="utf-8")).strip()


def build_payloads(skill_root: Path) -> tuple[list[tuple[str, bytes]], dict[str, list[tuple[str, str]]]]:
    payloads: list[tuple[str, bytes]] = []
    statutory: dict[str, list[Path]] = {name: [] for name in STATUTORY_COLLECTIONS}
    sheets: list[Path] = []
    templates: list[Path] = []
    found_sheets: set[str] = set()

    for path in iter_source_files(skill_root):
        rel = path.relative_to(skill_root)
        posix = rel.as_posix()
        if posix == "SKILL.md" or posix == "scripts/calculators.py" or posix.startswith("subskills/"):
            payloads.append((f"{FOLDER}/{posix}", packed_markdown(rel, path.read_text(encoding="utf-8")).encode("utf-8")))
            continue
        if posix.startswith("references/catalogues/") or posix in {f"references/{name}" for name in KEPT_REFERENCE_FILES}:
            if path.suffix.lower() == ".md":
                data = packed_markdown(rel, path.read_text(encoding="utf-8")).encode("utf-8")
            else:
                data = path.read_bytes()
            payloads.append((f"{FOLDER}/{posix}", data))
            continue
        if posix.startswith("references/statutory/"):
            collection = posix.split("/")[2]
            if collection not in statutory:
                fail(f"unexpected statutory collection: {collection}")
            statutory[collection].append(path)
            continue
        if posix.startswith("references/templates/"):
            templates.append(path)
            continue
        if rel.parent.as_posix() == "references" and path.suffix.lower() == ".md":
            found_sheets.add(path.name)
            sheets.append(path)
            continue
        fail(f"unclassified source file: {posix}")

    if found_sheets != set(LINKED_SHEETS):
        fail(f"linked sheets changed: {sorted(found_sheets)}")
    empty = [name for name, paths in statutory.items() if not paths]
    if empty:
        fail("missing statutory collections: " + ", ".join(empty))

    bundles: dict[str, list[tuple[str, str]]] = {}
    for collection, paths in statutory.items():
        sections = []
        root = skill_root / "references" / "statutory" / collection
        for path in paths:
            heading = path.relative_to(root).as_posix()
            sections.append((heading, section_body(path)))
        sections.sort(key=lambda item: item[0].casefold())
        arc = f"{FOLDER}/references/statutory/{collection}.md"
        bundles[arc] = sections
        payloads.append((arc, render_bundle(sections).encode("utf-8")))

    sheet_sections = [(path.name, section_body(path)) for path in sheets]
    sheet_sections.sort(key=lambda item: item[0].casefold())
    sheet_arc = f"{FOLDER}/references/linked-sheets.md"
    bundles[sheet_arc] = sheet_sections
    payloads.append((sheet_arc, render_bundle(sheet_sections).encode("utf-8")))

    template_sections = [(path.name, section_body(path)) for path in templates]
    template_sections.sort(key=lambda item: item[0].casefold())
    template_arc = f"{FOLDER}/references/templates.md"
    bundles[template_arc] = template_sections
    payloads.append((template_arc, render_bundle(template_sections).encode("utf-8")))
    return payloads, bundles


def folded_description(block: list[str]) -> tuple[str, str]:
    name = ""
    desc_lines: list[str] = []
    reading_desc = False
    folded = False
    for line in block:
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
            reading_desc = False
            continue
        if line.startswith("description:"):
            rest = line.split(":", 1)[1].strip()
            folded = rest in {">", "|"}
            reading_desc = True
            if rest and not folded:
                desc_lines = [rest]
                reading_desc = False
            continue
        if reading_desc and (line.startswith(" ") or line.startswith("\t") or line.strip() == ""):
            desc_lines.append(line.strip())
            continue
        reading_desc = False
    if folded:
        description = " ".join(line for line in desc_lines if line)
    else:
        description = "\n".join(desc_lines).strip()
    return name, description


def frontmatter(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("SKILL.md is missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")
    return folded_description(lines[1:end])


def write_zip(files: list[tuple[str, bytes]], bundles: dict[str, list[tuple[str, str]]], dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".zip.tmp")
    try:
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for arcname, data in files:
                info = zipfile.ZipInfo(arcname)
                info.flag_bits |= 0x800
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data)
        check_zip(tmp, bundles)
        tmp.replace(dest)
    except BaseException:
        if tmp.exists():
            tmp.unlink()
        raise


def check_zip(path: Path, bundles: dict[str, list[tuple[str, str]]]) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        skill_files = [name for name in names if Path(name).name == "SKILL.md"]
        if skill_files != [f"{FOLDER}/SKILL.md"]:
            fail(f"expected exactly one {FOLDER}/SKILL.md, found {skill_files}")
        if any(".." in Path(name).parts for name in names):
            fail("zip contains a parent-directory path")
        uncompressed = 0
        py_names: list[str] = []
        for info in archive.infolist():
            if info.is_dir():
                continue
            uncompressed += info.file_size
            rel = Path(info.filename)
            if not allowed_file(rel):
                fail(f"unsupported file type: {info.filename}")
            parts = info.filename.split("/")
            if "statutory" in parts and len(parts) > parts.index("statutory") + 2:
                fail(f"per-file statutory path still in zip: {info.filename}")
            if rel.suffix.lower() == ".py":
                py_names.append(info.filename)
                source = archive.read(info).decode("utf-8")
                lowered = source.lower()
                hit = [marker for marker in NETWORK_MARKERS if marker in lowered]
                if hit:
                    fail(f"{info.filename} references {', '.join(hit)}")
        if uncompressed >= SIZE_LIMIT:
            fail(f"uncompressed size {uncompressed} exceeds {SIZE_LIMIT}")
        skill_text = archive.read(skill_files[0]).decode("utf-8")
        name, description = frontmatter(skill_text)
        if name != FOLDER:
            fail(f"skill name {name!r} does not match folder {FOLDER!r}")
        if not description or len(description) > DESCRIPTION_LIMIT:
            fail(f"description length {len(description)} is outside 1..{DESCRIPTION_LIMIT}")
        if "python hk-architect-master/main.py" in skill_text:
            fail("zip SKILL.md still runs main.py")
        if "references/statutory/pnap/" in skill_text:
            fail("zip SKILL.md still points at per-file statutory paths")
        topic = f"{FOLDER}/{CALC_TOPIC.as_posix()}"
        topic_text = archive.read(topic).decode("utf-8")
        if "`main.py`" in topic_text or "core/calculators.py" in topic_text:
            fail("zip calculator topic still points at the Cursor entry")
        for arc, sections in bundles.items():
            packed = archive.read(arc).decode("utf-8")
            if not packed.startswith(BUNDLE_INTRO):
                fail(f"{arc} is missing the bundle intro")
            for heading, body in sections:
                marker = f"## {heading}\n"
                if marker not in packed:
                    fail(f"{arc} is missing section {heading}")
                if body not in packed:
                    fail(f"{arc} is missing the text of {heading}")
    file_count = len([name for name in names if not name.endswith("/")])
    if file_count > ENTERPRISE_FILE_CAP:
        fail(f"{file_count} files exceeds the Gemini Enterprise cap of {ENTERPRISE_FILE_CAP}")
    if file_count != EXPECTED_FILES:
        fail(f"expected {EXPECTED_FILES} files, got {file_count}")
    print(f"files={file_count}")
    print(f"uncompressed_bytes={uncompressed}")
    print(f"description_chars={len(description)}")
    print(f"name={name}")
    print(f"py={', '.join(py_names)}")
    print(f"bundles={len(bundles)}")
    print(f"bundled_sections={sum(len(sections) for sections in bundles.values())}")


def main() -> None:
    _self_check()
    payloads, bundles = build_payloads(SKILL_ROOT)
    write_zip(payloads, bundles, ZIP_PATH)
    print(ZIP_PATH)


if __name__ == "__main__":
    main()
