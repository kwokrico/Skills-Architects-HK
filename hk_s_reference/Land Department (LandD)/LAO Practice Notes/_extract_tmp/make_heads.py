"""Pull issue number, title, and first 1200 chars from each extract."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\_extract_tmp")
rows = ["# extract heads", ""]
for f in sorted(OUT.glob("*.txt")):
    if f.name.startswith("_"):
        continue
    text = f.read_text(encoding="utf-8", errors="replace")
    head = re.sub(r"[ \t]+", " ", text[:1800])
    head = re.sub(r"\n{3,}", "\n\n", head)
    rows.append(f"## {f.name} ({len(text)} chars)")
    rows.append("```")
    rows.append(head.strip()[:1200])
    rows.append("```")
    rows.append("")
(OUT / "_heads.md").write_text("\n".join(rows), encoding="utf-8")
print("wrote _heads.md", len(list(OUT.glob('*.txt'))))
