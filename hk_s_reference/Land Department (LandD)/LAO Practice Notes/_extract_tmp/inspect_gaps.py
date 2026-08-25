from pathlib import Path
import pymupdf

base = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\source_reference"
)
out = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\_extract_tmp"
)

def dump(name: str) -> None:
    p = base / name
    doc = pymupdf.open(p)
    parts = [f"# {name} pages={doc.page_count} size={p.stat().st_size}\n"]
    for i, page in enumerate(doc):
        t = page.get_text("text") or ""
        parts.append(f"\n----- page {i+1}/{doc.page_count} chars={len(t)} -----\n")
        parts.append(t)
    dest = out / (p.stem.replace(" ", "_") + "_pages.txt")
    dest.write_text("".join(parts), encoding="utf-8", errors="replace")
    doc.close()

for name in [
    "PN 1_2022.pdf",
    "PN 10_2025.pdf",
    "2008-4.pdf",
    "2014_4.pdf",
    "PN 3_2022.pdf",
    "PN 3_2024.pdf",
    "PN 4_2024.pdf",
]:
    dump(name)
print("ok")
