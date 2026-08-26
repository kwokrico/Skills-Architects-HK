"""One-shot combiner: source_md/*_CS.md -> LAO_PN_Technical_Summaries.md."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source_md"
OUT = ROOT / "LAO_PN_Technical_Summaries.md"

FN_RE = re.compile(
    r"LAO Practice Note No\. (APSRSE )?(\d+)[_-](\d{2,4})([A-Za-z]*)",
    re.IGNORECASE,
)

HEADER = """# LAO Practice Notes — Technical Design Summaries

**Scope:** LAO Practice Notes (including APSRSE 2/94 and 2/96) from this library’s `source_md/*_CS.md`.
**Focus:** Lease GFA/SC/DDH, GBP under lease, waivers, NDA/standard-rate premium, trees/landscape, Certificate of Compliance.
**Coverage:** 96 practice notes (one section each). Missing variants named in CS but with no source in this library: **1/2025A**, **3/2025**, **5/2020A**, **12/2023A**.
**Caveat:** Advisory desk reference only. Verify the live LandsD LAO PN list and the project land grant before reliance. Individual `source_md/*_CS.md` files remain the per-instrument source; this file is the scan layer.

---

## How to use

1. Check the **supersession map** before relying on an older PN.
2. Jump via the **issue index**.
3. Open the matching `source_md/*_CS.md` / `source_reference/` PDF for citation text.

---

## Issue index

"""

SUPERSESSION = """
---

## Supersession and succession (quick map)

Chains below are taken only from CS Source / header / SD takeaway wording in this library. If a CS is silent, no successor is invented.

| Theme | Chain (oldest → current in this library) |
|---|---|
| GBP / MLP under lease | **1/1991** (MLP purpose) + **APSRSE 2/94** (12-week MLP clock; **5/2002** later shortens the clock) + **APSRSE 2/96** (amendment MLPs). **7/2006** amendment-plan handling. Current GBP pack: **2/2018** (supersedes 1/1994), **3/2018** (supersedes 8/2006), **4/2018** (streamlined process from 1 Feb 2019). BIM area calcs: **6/2024** (in addition to 3/2018 CAD). Phased GBP / DDH / landscaping for uncompleted residential: **8/2025**. |
| Lease GFA / SC | **4/2014** (supersedes APSRSE 1/98(A), 5/2000, 7/2002, APSS 3/99) as varied by **4/2014A**. Recreational facilities: **4/2000B** (supersedes 4/2000(A)). Aboveground parking GFA exemption: **9/2025** (supersedes 3/2025, not in this library). |
| DDH / DD | **3/2020** (supersedes 3/2014) as varied by **3/2020A** (underground SC / JPN 7). |
| Landscape / trees | Landscape clause: **1/2020** (supersedes 6/2003); forms/figures superseded by **1/2020A**. Trees: **6/2023** (supersedes 2/2020 and 2/2020A). |
| IB waivers / conversion | Testing labs **1/2016**. Data centre **3/2012** as varied by **3/2012A** / **3/2012B**. Other IB waivers **4/2019** together with **5/2019** (supersede 5/2001, 5/2001A, 2/2003, 9/2002, 3/2013, 1/2015). Entire-IB special waiver **6/2019** as varied by **6/2019A**; sample form superseded by **8/2024**. Buffer/lower floors **3/2019**. Transitional housing **7/2019**. RBS fees vary App III of **5/2019** via **2/2024**. |
| JPN 1/2 premium rates | **3/2001** (as supplemented by **6/2001**), **6/2002**, **3/2003**, **2/2011** (supersedes 2/2010 rates) → **4/2023** (supersedes 3/2001A and 1/2018) as varied by **3/2024** → **6/2025**. |
| MiC (JPN 8) | **6/2022** as varied by **4/2024** (new rate table) → **7/2025** (replaces 4/2024 App I rates). |
| IB redevelopment standard rates | **12/2023** (supersedes 1/2021 and 1/2021A) as varied by **5/2025** (supersedes 12/2023A). Time-limited intensity: **2/2019** as varied by **2/2019A**; sample form superseded by **7/2024**. |
| NT agri / NDA exchanges | Agri pilot **11/2023** + rates **11/2023A** as varied by **4/2025**. KTN/FLN **1/2022** as varied by **1/2022A**; rates **3/2022** as varied by **3/2022A**. HSK/HT **1/2024** as varied by **1/2024A**; rates **5/2024**. YLS **2/2025**. ECNTA **13/2023**. |
| Lease-mod processing | **2/2023** (supersedes 3/1999, 9/2000, 4/2001, 1/2006, 5/2006, 9/2006, 4/2007, 5/2007, 3/2008, 3/2009, 4/2009). Ownership/land-grant records: **8/2023** (supersedes 1/2023). Pay-for-what-you-build pilot: **2/2026** (read with 2/2023). |
| CC / NTEH SCC | CC applications: **1/2026** (supersedes 1/1987 and 8/2000; varies 4/2008). NTEH SCC: **1/2025** as varied by **1/2025B** (supersedes 1/2025A). |
| BC extensions | **2/2021** (supersedes 4/2020, 5/2008, 5/1996, 5/1994). COVID nil-premium: **2/2022**. |
| Other | Offensive trades: **3/2023** (supersedes 3/2021 as varied by 1/2023, and 6/2007). Compensation professional fees: **5/2020** (supersedes 1/96) as supplemented by **5/2020B** (supersedes 5/2020A). A rent rolls: **7/2023** (supersedes 6/2006 and 6/2006A). |

---

## Practice note summaries
"""


@dataclass(frozen=True)
class Note:
    path: Path
    year: int
    issue: int
    letter: str
    is_apsrse: bool
    label: str
    anchor: str
    blurb: str
    body: str


def parse_note(path: Path) -> Note:
    match = FN_RE.search(path.name)
    if match is None:
        raise ValueError(f"unparseable filename: {path.name}")
    apsrse, num_s, year_s, letter_raw = match.groups()
    issue = int(num_s)
    year = int(year_s)
    if year < 100:
        year += 1900
    letter = (letter_raw or "").upper()
    is_apsrse = bool(apsrse)
    if is_apsrse:
        label = f"PN APSRSE {issue}/{year_s}"
        anchor = f"pn-apsrse-{issue}-{year_s}".lower()
    else:
        label = f"PN {issue}/{year}{letter}"
        anchor = f"pn-{issue}-{year}{letter.lower()}"

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"missing H1: {path.name}")
    h1 = lines[0][2:].strip()
    if " — " in h1:
        blurb = h1.split(" — ", 1)[1].strip()
    else:
        blurb = h1
    lines[0] = "#" + lines[0]  # demote # to ##
    body = "\n".join(lines).rstrip()
    pointer = f"*Source Critical Summary:* `source_md/{path.name}`"
    if pointer not in body:
        body = f"{body}\n{pointer}"
    return Note(
        path=path,
        year=year,
        issue=issue,
        letter=letter,
        is_apsrse=is_apsrse,
        label=label,
        anchor=anchor,
        blurb=blurb,
        body=body,
    )


def main() -> None:
    notes = [parse_note(p) for p in SRC.glob("*_CS.md")]
    notes.sort(key=lambda n: (n.year, n.issue, n.letter, n.is_apsrse, n.path.name))
    if len(notes) != 96:
        raise SystemExit(f"expected 96 CS files, got {len(notes)}")

    index_lines = [f"- [{n.label}](#{n.anchor}) — {n.blurb}" for n in notes]
    sections: list[str] = []
    for note in notes:
        sections.append(f"<a id=\"{note.anchor}\"></a>\n\n{note.body}")

    out = (
        HEADER
        + "\n".join(index_lines)
        + "\n"
        + SUPERSESSION
        + "\n"
        + "\n\n---\n\n".join(sections)
        + "\n"
    )
    OUT.write_text(out, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(notes)} notes, {len(out.splitlines())} lines)")


if __name__ == "__main__":
    main()
