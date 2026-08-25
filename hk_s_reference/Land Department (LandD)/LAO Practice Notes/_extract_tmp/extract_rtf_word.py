"""Re-extract RTF files via Word COM (plain-text body, not RTF markup)."""
from __future__ import annotations

from pathlib import Path

SRC = Path(r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes")
OUT = SRC / "_extract_tmp"

import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = False
word.DisplayAlerts = 0
try:
    for f in sorted(SRC.glob("*.rtf")):
        dest = OUT / (f.stem.replace(" ", "_") + ".txt")
        print(f"Word RTF {f.name}", flush=True)
        doc = word.Documents.Open(str(f), ReadOnly=True)
        try:
            text = doc.Content.Text or ""
        finally:
            doc.Close(False)
        dest.write_text(text, encoding="utf-8", errors="replace")
        print(f"  {len(text)} chars", flush=True)
finally:
    word.Quit()
print("done rtf")
