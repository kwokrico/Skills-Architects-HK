"""OCR specific blank PDF pages that native text missed."""
from pathlib import Path
import pymupdf
import easyocr

base = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\source_reference"
)
out = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\_extract_tmp"
)

jobs = [
    ("PN 1_2022.pdf", [5]),  # 1-based
    ("PN 10_2025.pdf", [4]),
    ("2014_4.pdf", [8]),
    ("2008-4.pdf", [5]),
]

reader = easyocr.Reader(["en"], gpu=False)
for name, pages in jobs:
    path = base / name
    doc = pymupdf.open(path)
    parts = []
    for n in pages:
        page = doc[n - 1]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
        img = out / f"_gap_{path.stem.replace(' ', '_')}_p{n}.png"
        pix.save(str(img))
        lines = reader.readtext(str(img), detail=0, paragraph=True)
        text = "\n".join(lines) if lines else ""
        parts.append(f"----- page {n} -----\n{text}\n")
        print(name, "p", n, "chars", len(text))
    dest = out / (path.stem.replace(" ", "_") + "_gap_ocr.txt")
    dest.write_text("".join(parts), encoding="utf-8", errors="replace")
    doc.close()
print("done")
