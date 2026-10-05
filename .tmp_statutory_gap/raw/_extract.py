"""Extract text and contents headings from downloaded e-Legislation PDFs."""

from pathlib import Path

from pypdf import PdfReader

PDF_DIR = Path(__file__).resolve().parent / "_pdfs"
OUT = Path(__file__).resolve().parent / "_txt"
OUT.mkdir(exist_ok=True)


def main() -> None:
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        reader = PdfReader(str(pdf))
        pages = []
        for index, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            pages.append(text)
        (OUT / f"{pdf.stem}.txt").write_text("\n\n".join(pages), encoding="utf-8")
        print(f"{pdf.name} pages={len(reader.pages)} chars={sum(len(p) for p in pages)}")


if __name__ == "__main__":
    main()
