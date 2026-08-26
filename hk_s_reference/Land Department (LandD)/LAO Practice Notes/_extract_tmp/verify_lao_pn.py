"""Verify LAO_PN_Technical_Summaries.md against source_md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source_md"
OUT = ROOT / "LAO_PN_Technical_Summaries.md"


def main() -> None:
    src = list(SRC.glob("*_CS.md"))
    text = OUT.read_text(encoding="utf-8")
    h2 = re.findall(r"^## LAO Practice Note No\.", text, re.M)
    h1 = re.findall(r"^# LAO Practice Note No\.", text, re.M)
    anchors = re.findall(r'<a id="([^"]+)"></a>', text)
    index_links = re.findall(r"^\- \[.+?\]\(#([^\)]+)\)", text, re.M)
    pointers = re.findall(
        r"\*Source Critical Summary:\* `source_md/([^`]+)`", text
    )
    src_names = {p.name for p in src}
    print(f"src {len(src)}")
    print(f"h2 sections {len(h2)} leftover h1 {len(h1)}")
    print(f"anchors {len(anchors)} unique {len(set(anchors))}")
    print(f"index {len(index_links)} unique {len(set(index_links))}")
    print(f"pointers {len(pointers)} unique {len(set(pointers))}")
    print("missing pointers", sorted(src_names - set(pointers)))
    print("extra pointers", sorted(set(pointers) - src_names))
    print("index not in anchors", sorted(set(index_links) - set(anchors)))
    print("anchors not in index", sorted(set(anchors) - set(index_links)))
    print("dup anchors", [a for a in set(anchors) if anchors.count(a) > 1])
    print("dup pointers", [p for p in set(pointers) if pointers.count(p) > 1])
    headings = re.findall(r"^## LAO Practice Note No\..+$", text, re.M)
    print("first h2", headings[0])
    print("last h2", headings[-1])
    missing = ["1/2025A", "3/2025", "5/2020A", "12/2023A"]
    coverage = text.split("**Coverage:**", 1)[1].split("\n", 1)[0]
    print("coverage line", coverage)
    for item in missing:
        print(item, "in coverage", item in coverage)


if __name__ == "__main__":
    main()
