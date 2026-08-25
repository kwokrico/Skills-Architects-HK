"""Extract text from LAO Practice Notes (PDF / RTF / DOC) for Critical Summaries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

SRC = Path(r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes")
OUT = SRC / "_extract_tmp"
OUT.mkdir(exist_ok=True)

SKIP_DIRS = {"_extract_tmp", "source_reference", "source_md"}


def extract_pdf(path: Path) -> str:
    import pymupdf

    parts: list[str] = []
    with pymupdf.open(path) as doc:
        for i, page in enumerate(doc):
            parts.append(f"\n----- page {i + 1}/{doc.page_count} -----\n")
            parts.append(page.get_text("text") or "")
    return "".join(parts)


def extract_rtf(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            text = ""
    else:
        text = raw.decode("latin-1", errors="replace")
    # Strip RTF control words; keep readable runs.
    text = re.sub(r"\\'[0-9a-fA-F]{2}", lambda m: bytes.fromhex(m.group(0)[2:]).decode("latin-1", errors="replace"), text)
    text = re.sub(r"\\par[d]?", "\n", text)
    text = re.sub(r"\\tab", "\t", text)
    text = re.sub(r"\\line", "\n", text)
    text = re.sub(r"\\[a-zA-Z]+-?\d* ?", "", text)
    text = re.sub(r"[{}]", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_doc(path: Path) -> str:
    try:
        import win32com.client

        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(path), ReadOnly=True)
        try:
            text = doc.Content.Text
        finally:
            doc.Close(False)
            word.Quit()
        return text or ""
    except Exception as exc:  # ponytail: Word COM may be unavailable; ole dump is the ceiling
        print(f"  Word COM failed for {path.name}: {exc}", file=sys.stderr)
        import olefile

        if not olefile.isOleFile(path):
            return f"[OLE extract failed: not OLE] {exc}"
        ole = olefile.OleFileIO(path)
        chunks: list[str] = []
        for stream in ole.listdir():
            name = "/".join(stream)
            if "WordDocument" in name or "1Table" in name or stream[-1].startswith("\x01"):
                data = ole.openstream(stream).read()
                ascii_run = re.findall(rb"[\x20-\x7e\r\n\t]{8,}", data)
                for run in ascii_run:
                    chunks.append(run.decode("ascii", errors="ignore"))
        ole.close()
        return "\n".join(chunks)


def main() -> None:
    files = sorted(
        f
        for f in SRC.iterdir()
        if f.is_file() and f.suffix.lower() in {".pdf", ".rtf", ".doc", ".docx"}
    )
    index_lines = ["# extract index", ""]
    for f in files:
        dest = OUT / (f.stem.replace(" ", "_") + ".txt")
        print(f"extract {f.name} -> {dest.name}", flush=True)
        try:
            if f.suffix.lower() == ".pdf":
                text = extract_pdf(f)
            elif f.suffix.lower() == ".rtf":
                text = extract_rtf(f)
            else:
                text = extract_doc(f)
        except Exception as exc:
            text = f"[EXTRACT ERROR] {type(exc).__name__}: {exc}"
            print(f"  ERROR {f.name}: {exc}", file=sys.stderr)
        dest.write_text(text, encoding="utf-8", errors="replace")
        chars = len(text)
        preview = re.sub(r"\s+", " ", text[:400]).strip()
        index_lines.append(f"- `{f.name}` | {chars} chars | {preview}")
    (OUT / "_index.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"done {len(files)} files", flush=True)


if __name__ == "__main__":
    main()
