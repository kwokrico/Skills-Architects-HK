"""Probe non-PNAP documents without a critical summary for extractable text."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\Rico\PycharmProjects\Skills-Architects-HK")
GAP = ROOT / "hk_s_reference" / "DOCUMENTS_WITHOUT_CS.md"
OUT = ROOT / ".tmp_gap_probe.txt"

text = GAP.read_text(encoding="utf-8")
paths = re.findall(r"^- `(.+)`$", text, re.M)
cands = [p for p in paths if "Practice Notes for Authorized Persons (PNAP)" not in p]

lines: list[str] = [f"non-pnap entries: {len(cands)}"]
for rel in cands:
    path = ROOT / "hk_s_reference" / rel
    if not path.exists():
        lines.append(f"MISSING\t{rel}")
        continue
    if path.suffix.lower() != ".pdf":
        size = path.stat().st_size
        lines.append(f"MD\t{size}\t{rel}")
        continue
    try:
        doc = fitz.open(path)
        pages = doc.page_count
        chunks = []
        for i, page in enumerate(doc):
            chunks.append(page.get_text("text") or "")
            if i >= 2 and sum(len(c) for c in chunks) > 400:
                break
        sample = " ".join(" ".join(chunks).split())[:240]
        # full char count only if sample is short; otherwise estimate from all pages for short docs
        if pages <= 40:
            full = "".join(page.get_text("text") or "" for page in doc)
            n = len(full.strip())
        else:
            n = sum(len((page.get_text("text") or "").strip()) for page in doc)
        lines.append(f"PDF\tpages={pages}\tchars={n}\t{rel}\t|| {sample}")
        doc.close()
    except Exception as exc:  # noqa: BLE001
        lines.append(f"ERR\t{type(exc).__name__}: {exc}\t{rel}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {OUT} lines={len(lines)}")
