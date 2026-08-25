"""OCR image-only / low-text PDFs with EasyOCR."""
from __future__ import annotations

from pathlib import Path

import pymupdf

SRC = Path(r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes")
OUT = SRC / "_extract_tmp"

# Files whose native text extract is too thin to write a CS from.
SCANNED = [
    "2000_4B.pdf",
    "2000A_3.pdf",
    "2006-4e.pdf",
    "2009-2.pdf",
    "2011_2.pdf",
    "2012A_3.pdf",
    "9101apsr.pdf",
    "PN 1_2017.pdf",
    "PN 2_2021.pdf",
    "PN 3_2020.pdf",
    "PN 5_2020.pdf",
]


def main() -> None:
    import easyocr

    reader = easyocr.Reader(["en"], gpu=False)
    for name in SCANNED:
        path = SRC / name
        dest = OUT / (path.stem.replace(" ", "_") + ".txt")
        print(f"OCR {name}", flush=True)
        parts: list[str] = []
        with pymupdf.open(path) as doc:
            for i, page in enumerate(doc):
                pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
                img_path = OUT / f"_ocr_{path.stem.replace(' ', '_')}_p{i + 1}.png"
                pix.save(str(img_path))
                lines = reader.readtext(str(img_path), detail=0, paragraph=True)
                parts.append(f"\n----- page {i + 1}/{doc.page_count} -----\n")
                parts.append("\n".join(lines) if lines else "")
                print(f"  page {i + 1}/{doc.page_count} {sum(len(x) for x in lines)} chars", flush=True)
        dest.write_text("".join(parts), encoding="utf-8", errors="replace")
        print(f"  wrote {dest.name} {dest.stat().st_size} bytes", flush=True)
    print("done ocr")


if __name__ == "__main__":
    main()
