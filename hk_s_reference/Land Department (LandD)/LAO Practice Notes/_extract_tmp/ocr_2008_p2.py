from pathlib import Path
import pymupdf
import easyocr

base = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\source_reference"
)
out = Path(
    r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\_extract_tmp"
)
path = base / "2008-4.pdf"
reader = easyocr.Reader(["en"], gpu=False)
doc = pymupdf.open(path)
page = doc[1]
pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
img = out / "_gap_2008-4_p2.png"
pix.save(str(img))
lines = reader.readtext(str(img), detail=0, paragraph=True)
text = "\n".join(lines) if lines else ""
(out / "2008-4_p2_ocr.txt").write_text(text, encoding="utf-8", errors="replace")
print(text[-800:] if text else "empty")
doc.close()
