"""Build architect critical summaries from BD building-works HTML pages.

ponytail: one-shot crawler for this scrape. Re-run the whole script to refresh;
it does not incrementally merge edits made by hand in the output folder.
"""

from __future__ import annotations

import html
import os
import re
import time
import urllib.error
import urllib.request
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

ROOT = Path(
    r"c:\Users\Rico\PycharmProjects\Skills-Architects-HK\hk_s_reference"
    r"\Building Department (BD)\BD Website"
)
MWCS = Path(
    r"c:\Users\Rico\PycharmProjects\Skills-Architects-HK\hk_s_reference"
    r"\Building Department (BD)\Minor Works (MWCS)\Minor Works Control System_CS.md"
)
SEED = "https://www.bd.gov.hk/en/building-works/index.html"
FORM_URLS = [
    "https://www.bd.gov.hk/en/resources/forms/form_mw.html",
    "https://www.bd.gov.hk/en/resources/forms/form_sc.html",
    "https://www.bd.gov.hk/en/resources/forms/form_nbw.html",
]
HOST = "www.bd.gov.hk"
SKIP_EXT = (
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".doc", ".docx",
    ".xls", ".xlsx", ".zip", ".mp4", ".css", ".js", ".svg", ".webp",
)
UA = {"User-Agent": "Mozilla/5.0 (compatible; HK-architect-reference/1.0)"}
SCRAPE = "2 Oct 2026"

JUNK_LINE = re.compile(
    r"^(skip to content|text size|contact us|search|home|important notices|"
    r"privacy policy|sitemap|top|share on facebook|share on whatsapp|"
    r"share by email|quick links|english|eng|繁體|简体|"
    r"back to top|print this page|last update:?)$",
    re.I,
)


def norm(url: str) -> str:
    p = urlparse(url)
    path = p.path or "/"
    if path.endswith("/"):
        path += "index.html"
    return urlunparse(("https", HOST, path, "", "", ""))


def tc_url(en: str) -> str:
    return en.replace("https://www.bd.gov.hk/en/", "https://www.bd.gov.hk/tc/", 1)


def in_building_works(url: str) -> bool:
    path = urlparse(url).path.lower()
    if any(path.endswith(ext) for ext in SKIP_EXT):
        return False
    return path.startswith("/en/building-works/")


def clean_text(raw: str) -> str:
    t = html.unescape(raw)
    t = re.sub(r"<[^>]+>", " ", t)
    t = t.replace("\xa0", " ")
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"m\s*2\b", "m²", t)
    t = t.replace("m2", "m²")
    return t


_BOLD_PATTERNS = (
    re.compile(
        r"(?i)\b(?:not more than|not less than|no more than|at least|not exceeding|"
        r"more than|less than|within)\s+\d[\d,]*(?:\.\d+)?"
        r"(?:\s*(?:mm|cm|m²|m|days|day|working days))?"
    ),
    re.compile(
        r"(?i)(?:(?:≤|≥|>=|<=|>|<)\s*)?\d[\d,]*(?:\.\d+)?\s*(?:mm|cm|m²|m)\b"
    ),
    re.compile(r"(?i)\b(?:7 days|14 days|30 days|four working days)\b"),
)


def _apply_pat(text: str, pat: re.Pattern[str]) -> str:
    bits = re.split(r"(\*\*[^*]*\*\*)", text)
    out: list[str] = []
    for bit in bits:
        if bit.startswith("**"):
            out.append(bit)
        else:
            out.append(pat.sub(lambda m: f"**{m.group(0)}**", bit))
    return "".join(out)


def bold_limits(text: str) -> str:
    if not text or text.startswith("http"):
        return text
    for pat in _BOLD_PATTERNS:
        text = _apply_pat(text, pat)
    return text.replace("****", "**")


def safe_stem(title: str) -> str:
    t = re.sub(r'[<>:"/\\|?*]', " ", title)
    t = re.sub(r"\s+", " ", t).strip(" .")
    if len(t) > 110:
        t = t[:110].rstrip()
    return t or "Untitled"


def clean_title(title: str) -> str:
    t = re.sub(r"\s*[-|]\s*Buildings Department\s*$", "", title).strip()
    t = re.sub(r"^Forms,\s*", "", t)
    return t or title


def fetch(url: str) -> str:
    last: Exception | None = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
            if "html" not in ctype.lower() and not url.endswith(".html"):
                return ""
            return data.decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 — retry network faults
            last = exc
            time.sleep(0.4 * (attempt + 1))
    raise RuntimeError(f"{url} :: {last}")


def links_from(page_url: str, html_text: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for href in re.findall(r'href="([^"]+)"', html_text):
        if href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        u = norm(urljoin(page_url, href))
        if u in seen or not in_building_works(u):
            continue
        seen.add(u)
        found.append(u)
    return found


def crawl() -> dict[str, str]:
    pages: dict[str, str] = {}
    seen: set[str] = set()
    q: deque[str] = deque([norm(SEED)])
    while q:
        batch: list[str] = []
        while q and len(batch) < 10:
            u = q.popleft()
            if u in seen:
                continue
            seen.add(u)
            batch.append(u)
        if not batch:
            break
        with ThreadPoolExecutor(max_workers=6) as pool:
            futs = {pool.submit(fetch, u): u for u in batch}
            for fut in as_completed(futs):
                u = futs[fut]
                try:
                    html_text = fut.result()
                except Exception as exc:  # noqa: BLE001
                    print("FAIL", exc)
                    continue
                if not html_text or "page not found" in html_text.lower()[:500]:
                    print("EMPTY", u)
                    continue
                pages[u] = html_text
                for link in links_from(u, html_text):
                    if link not in seen:
                        q.append(link)
        print(f"crawled {len(pages)} queued {len(q)}")
    for u in FORM_URLS:
        u = norm(u)
        if u not in pages:
            pages[u] = fetch(u)
            print("form", u)
    return pages


SKIP_CLASS_BITS = (
    "footer", "topmenu", "main-menu", "language", "breadcrumb",
    "social-share", "share-list", "quicklink", "site-header",
)


class StreamParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_content = False
        self.stopped = False
        self.skip_depth = 0
        self.stack: list[dict] = []
        self.stream: list[tuple] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.stopped:
            return
        ad = {k: (v or "") for k, v in attrs}
        if ad.get("id") == "content":
            self.in_content = True
        if not self.in_content:
            return
        cls = ad.get("class", "")
        low = cls.lower()
        if tag in ("script", "style", "noscript", "header", "footer") or any(
            b in low for b in SKIP_CLASS_BITS
        ):
            self.skip_depth += 1
            self.stack.append({"tag": tag, "skip": True, "cls": cls, "bits": [], "child_emit": False})
            return
        if self.skip_depth:
            self.stack.append({"tag": tag, "skip": True, "cls": cls, "bits": [], "child_emit": False})
            return
        self.stack.append({"tag": tag, "skip": False, "cls": cls, "bits": [], "child_emit": False})

    def handle_endtag(self, tag: str) -> None:
        if not self.in_content or self.stopped or not self.stack:
            return
        el = self.stack.pop()
        if el["skip"]:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        text = clean_text("".join(el["bits"]))
        cls = el["cls"]
        kind = None
        if "card-header" in cls:
            kind = "h3"
        elif tag in ("h1", "h2", "h3", "h4"):
            kind = tag
        elif tag in ("p", "li"):
            kind = tag
        if tag == "table":
            rows = el.get("rows") or []
            if rows:
                self.stream.append(("table", rows))
                self._mark_parent()
            return
        if kind and text and not self._is_junk(text):
            if text.lower().startswith("quick links"):
                self.stopped = True
                return
            self.stream.append((kind, text))
            self._mark_parent()
            return
        if tag == "div" and text and not el["child_emit"] and len(text) >= 12 and not self._is_junk(text):
            if text.lower().startswith("quick links"):
                self.stopped = True
                return
            self.stream.append(("p", text))
            self._mark_parent()
            return
        if text and self.stack and not el["child_emit"]:
            self.stack[-1]["bits"].append(text + " ")

    def handle_data(self, data: str) -> None:
        if not self.in_content or self.stopped or self.skip_depth or not self.stack:
            return
        el = self.stack[-1]
        if el["skip"]:
            return
        if el["tag"] in ("td", "th") and el is self._cell_parent():
            el["bits"].append(data)
            return
        el["bits"].append(data)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def _cell_parent(self) -> dict | None:
        for el in reversed(self.stack):
            if el["tag"] in ("td", "th"):
                return el
        return None

    def _mark_parent(self) -> None:
        if self.stack:
            self.stack[-1]["child_emit"] = True

    def _is_junk(self, text: str) -> bool:
        return bool(JUNK_LINE.match(text.strip()))

    # Capture table rows without leaking cells into the prose stream.
    def handle_starttag_rows(self) -> None:
        return


# The parser above does not yet collect table rows. Patch via subclass logic
# by intercepting tr/td in an extended parser.


class PageParser(StreamParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        super().handle_starttag(tag, attrs)
        if self.stopped or not self.in_content or self.skip_depth:
            return
        if tag == "tr" and self.stack:
            self.stack[-1]["row"] = []
        if tag in ("td", "th") and self.stack:
            self.stack[-1]["bits"] = []

    def handle_endtag(self, tag: str) -> None:
        if not self.in_content or self.stopped or not self.stack:
            super().handle_endtag(tag)
            return
        el = self.stack[-1]
        if tag in ("td", "th") and not el["skip"]:
            cell = clean_text("".join(el["bits"]))
            el["bits"] = []
            for parent in reversed(self.stack[:-1]):
                if "row" in parent:
                    parent["row"].append(cell)
                    break
            # Do not also treat the cell as a paragraph.
            el["child_emit"] = True
            self.stack.pop()
            if self.stack:
                self.stack[-1]["child_emit"] = True
            return
        if tag == "tr" and not el["skip"]:
            row = [c for c in el.get("row", []) if c]
            if row:
                for parent in reversed(self.stack[:-1]):
                    if parent["tag"] == "table":
                        parent.setdefault("rows", []).append(row)
                        break
            el["child_emit"] = True
            self.stack.pop()
            if self.stack:
                self.stack[-1]["child_emit"] = True
            return
        super().handle_endtag(tag)


@dataclass
class Page:
    url: str
    title: str
    kind: str
    stream: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    procedure: list = field(default_factory=list)
    item_no: str = ""
    item_class: str = ""
    types: list = field(default_factory=list)
    categories: list = field(default_factory=list)
    forms: list = field(default_factory=list)
    schedule_note: str = ""
    path: Path | None = None


def page_title(html_text: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html_text, re.I | re.S)
    raw = clean_text(m.group(1)) if m else "Untitled"
    return clean_title(raw)


def kind_of(url: str, html_text: str) -> str:
    path = urlparse(url).path
    if "/resources/forms/form_" in path:
        return "form"
    if "designated-exempted-works" in path and "index_mwcs_works_" in path:
        return "dew"
    if re.search(r"index_mwcs_item\d+_\d+\.html", path):
        return "item"
    if "index_mwcs_items_c" in path:
        return "category"
    return "narrative"


def _outer_lis(fragment: str) -> list[str]:
    items: list[str] = []
    depth = 0
    start: int | None = None
    for m in re.finditer(r"<li[^>]*>|</li>", fragment):
        if m.group(0).startswith("<li"):
            if depth == 0:
                start = m.end()
            depth += 1
        else:
            depth = max(0, depth - 1)
            if depth == 0 and start is not None:
                items.append(fragment[start:m.start()])
                start = None
    return items


def extract_category(html_text: str) -> list:
    content = html_text.split('id="content"', 1)[-1]
    content = re.split(r">\s*Quick links\s*<", content, maxsplit=1)[0]
    stream: list = []
    head = re.split(r"<h2\b", content, maxsplit=1)[0]
    for p in re.findall(r"<p[^>]*>([\s\S]*?)</p>", head):
        t = clean_text(p)
        if t and not JUNK_LINE.match(t) and "adobe" not in t.lower():
            stream.append(("p", t))
    blocks = re.split(r"(<h2[^>]*>[\s\S]*?</h2>)", content)
    for block in blocks:
        if block.startswith("<h2"):
            title = clean_text(block)
            if title and not title.lower().startswith("quick links"):
                stream.append(("h2", title))
            continue
        pieces = re.split(r"(<h3[^>]*>[\s\S]*?</h3>)", block)
        for piece in pieces:
            if piece.startswith("<h3"):
                title = clean_text(piece)
                if title:
                    stream.append(("h3", title))
                continue
            cards = re.findall(
                r'<div class="card rounded-0">([\s\S]*?)<div class="card-footer',
                piece,
            )
            for card in cards:
                header_m = re.search(r'class="card-header[^"]*"[^>]*>([\s\S]*?)</div>', card)
                klass = clean_text(header_m.group(1)) if header_m else ""
                num_m = re.search(r"<strong>\s*([\d.]+)\s*</strong>", card)
                num = num_m.group(1) if num_m else ""
                h4_m = re.search(r"<h4[^>]*>([\s\S]*?)</h4>", card)
                nature = clean_text(h4_m.group(1)) if h4_m else ""
                rows = [["Gate", "Requirement"]]
                ol_m = re.search(r"<ol[^>]*>([\s\S]*?)</ol>", card)
                if ol_m:
                    for item_html in _outer_lis(ol_m.group(1)):
                        gate = clean_text(re.split(r"<ul\b", item_html, maxsplit=1)[0])
                        ul_m = re.search(r"<ul[^>]*>([\s\S]*)</ul>", item_html)
                        reqs = (
                            [clean_text(x) for x in _outer_lis(ul_m.group(1))]
                            if ul_m
                            else []
                        )
                        rows.append([gate or nature, "; ".join(r for r in reqs if r)])
                else:
                    for li in _outer_lis(card):
                        t = clean_text(li)
                        if t:
                            rows.append([t, ""])
                label = " ".join(x for x in (klass, f"item {num}" if num else "", nature) if x)
                stream.append(("h3", label))
                if len(rows) > 1:
                    stream.append(("table", rows))
                stream.append((
                    "p",
                    f"If any gate fails, item {num or label} on this card does not apply.",
                ))
    return stream


def extract_forms(html_text: str) -> list:
    content = html_text.split('id="content"', 1)[-1]
    content = re.split(r">\s*Quick links\s*<", content, maxsplit=1)[0]
    stream: list = []
    chunks = re.split(r"(<h[23][^>]*>[\s\S]*?</h[23]>)", content)
    current_title = ""
    pending: list[list[str]] = []

    def flush() -> None:
        nonlocal pending
        if pending:
            stream.append(("table", [["Form", "What the page says", "Edition / channel"], *pending]))
            pending = []

    for chunk in chunks:
        if chunk.startswith("<h"):
            flush()
            title = clean_text(chunk)
            if title and not title.lower().startswith("quick links"):
                current_title = title
                stream.append(("h2", title))
            continue
        intro = re.search(r"<p[^>]*>([\s\S]*?)</p>", chunk)
        if intro:
            t = clean_text(intro.group(1))
            if t and "adobe" not in t.lower() and len(t) > 30:
                stream.append(("p", t))
        for table in re.findall(r"<table[\s\S]*?</table>", chunk):
            for tr in re.findall(r"<tr[\s\S]*?</tr>", table):
                cells = [clean_text(c) for c in re.findall(r"<t[hd][^>]*>([\s\S]*?)</t[hd]>", tr)]
                cells = [c for c in cells if c and c.lower() not in {"yes", "no"}]
                if not cells or not re.match(r"^[A-Z]{2,4}\d", cells[0]):
                    continue
                desc = cells[1] if len(cells) > 1 else ""
                desc = re.split(r"See Detail|Sample|Demonstration", desc)[0].strip(" |")
                date_m = re.search(r"(\d{2}/\d{4})", " ".join(cells))
                channel = "via RMWMS" if "RMWMS" in " ".join(cells) else ""
                extra = " ".join(x for x in ((date_m.group(1) if date_m else ""), channel) if x)
                pending.append([cells[0], desc, extra])
        _ = current_title
    flush()
    return stream


def sd_line(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text)
    keys = (
        "must", "required", "shall", "prior approval", "consent",
        "not more than", "not less than", "more than", "less than",
        "unauthorised", "unauthorized", "occupation permit",
        "class i", "class ii", "class iii", "does not apply", "appoint",
    )
    chosen = ""
    for p in parts:
        low = p.lower()
        if "acrobat" in low or low.startswith("download "):
            continue
        if any(k in low for k in keys) and len(p) > 40:
            chosen = p.strip()
            break
    if not chosen:
        return ""
    chosen = bold_limits(chosen)
    if len(chosen) > 320:
        chosen = chosen[:320].rsplit(" ", 1)[0].rstrip(",;:") + "."
    return chosen


def extract_item_bits(html_text: str, page: Page) -> None:
    tables = []
    for t in re.findall(r'<table class="mw-item-detail"[\s\S]*?</table>', html_text):
        rows = []
        for r in re.findall(r"<tr[\s\S]*?</tr>", t):
            cells = [
                clean_text(c)
                for c in re.findall(r"<t[hd][^>]*>([\s\S]*?)</t[hd]>", r)
            ]
            cells = [c for c in cells if c]
            if cells:
                rows.append(cells)
        if rows:
            tables.append(rows)
    page.tables = tables
    for row in tables[0] if tables else []:
        if row and row[0].lower().startswith("item no"):
            page.item_no = row[-1]
        if row and "designated exempted works item no" in row[0].lower():
            page.item_no = row[-1]
    m = re.search(r'class="badge c-(\d)', html_text)
    if m:
        page.item_class = {"1": "Class I", "2": "Class II", "3": "Class III"}.get(m.group(1), "")
    page.types = sorted(set(re.findall(r"mw-type-([a-z])", html_text)))
    page.types = [t.upper() for t in page.types]
    cat = re.search(r"<strong>Category</strong>([\s\S]*?)<strong>Forms</strong>", html_text)
    if cat:
        page.categories = [
            clean_text(x)
            for x in re.findall(r"<a [^>]*>([\s\S]*?)</a>", cat.group(1))
        ]
    form_zone = re.search(r"<strong>Forms</strong>([\s\S]*?)</div>", html_text)
    zone = form_zone.group(1) if form_zone else ""
    page.forms = list(dict.fromkeys(re.findall(r"MW\d{2}", zone)))
    note = re.search(r"More details:\s*([^<]+)", html_text)
    if note:
        page.schedule_note = clean_text(note.group(1))
    mproc = re.search(
        r'id="procedure"([\s\S]*?)(?:More about minor works|Quick links|<footer)',
        html_text,
    )
    if not mproc:
        return
    chunk = re.sub(r"<br\s*/?>", "\n", mproc.group(1), flags=re.I)
    chunk = re.sub(r"</(p|li|div|h\d|span)>", "\n", chunk)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    lines = []
    for ln in chunk.split("\n"):
        ln = clean_text(ln)
        if not ln or JUNK_LINE.match(ln) or ln.lower().startswith("quick links"):
            continue
        if ln in {"Step 1", "Step 2", "Step 3", "Step 4"} and lines and lines[-1] == ln:
            continue
        lines.append(ln)
    # Drop the jump-nav duplicate "Step 1 Step 2 Step 3" run at the start.
    while lines and re.fullmatch(r"Step \d", lines[0]):
        # keep the first Step only once we hit a non-step after a step cluster
        if len(lines) > 1 and re.fullmatch(r"Step \d", lines[1]):
            lines.pop(0)
            continue
        break
    page.procedure = lines


def parse_stream(html_text: str) -> list:
    parser = PageParser()
    try:
        parser.feed(html_text)
    except Exception:  # noqa: BLE001
        return []
    # Drop duplicate adjacent lines and nav leftovers.
    out = []
    prev = None
    for item in parser.stream:
        if item == prev:
            continue
        kind, data = item[0], item[1]
        if kind != "table" and (len(data) < 2 or JUNK_LINE.match(data)):
            continue
        if kind != "table" and data.lower() in {"see also", "more about minor works", "more about minor works items"}:
            continue
        out.append(item)
        prev = item
    return out


def rel_mwcs(dest: Path) -> str:
    rel = os.path.relpath(MWCS, start=dest.parent)
    return Path(rel).as_posix()


def header(title: str, url: str, dest: Path, extra: str = "") -> str:
    tc = tc_url(url)
    mw = ""
    if "/minor-works/" in url or "/signboards/" in url:
        mw = f" Sister summary: [Minor Works Control System_CS.md]({rel_mwcs(dest)})."
    lines = [
        f"# {title}",
        "**Architect critical summary for schematic design**",
        f"{SCRAPE} | Buildings Department | [English]({url}) · [繁體]({tc})",
        "",
        f"> Scope note: {extra}{mw}".rstrip(),
        "",
        "## Regulatory Overview",
        "",
    ]
    return "\n".join(lines)


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    normed = []
    for r in rows:
        cells = [bold_limits(c.replace("|", "/")) for c in r] + [""] * (width - len(r))
        normed.append(cells[:width])
    head = normed[0]
    # If the first row is a single long cell, no header.
    if width == 1:
        return "\n".join(f"- {c[0]}" for c in normed)
    body = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * width) + "|"]
    for r in normed[1:]:
        body.append("| " + " | ".join(r) + " |")
    if len(normed) == 1:
        body = [
            "| Parameter | Requirement |",
            "|---|---|",
            "| " + " | ".join(normed[0]) + " |",
        ]
    return "\n".join(body)


def first_sentences(text: str, n: int = 2) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text)
    parts = [p.strip() for p in parts if len(p.strip()) > 20]
    if not parts:
        return text.strip()
    return " ".join(parts[:n])


def render_item(page: Page) -> str:
    no = page.item_no or "?"
    if page.kind == "dew":
        title = page.title if " and " in page.title or "&" in page.title else (
            f"Designated Exempted Works Item {no}" if no != "?" else page.title
        )
        if len(page.tables) > 1:
            title = page.title
    else:
        title = f"MW Item {no}"
    label = "Designated exempted works" if page.kind == "dew" else (page.item_class or "Minor works")
    nums: list[str] = []
    for table in page.tables:
        for row in table:
            if row and "item no" in row[0].lower():
                nums.append(row[-1])
    shown = ", ".join(dict.fromkeys(nums)) or no
    scope = (
        f"BD webpage for {label} item {shown}, scraped {SCRAPE}. "
        "Every limit below is printed on that page. "
        "If a criterion is not in the table, this page does not state it."
    )
    if page.schedule_note:
        scope += f" The page points to: {page.schedule_note}."
    dest = page.path or ROOT / "x.md"
    out = [header(title, page.url, dest, scope)]
    bits = [f"This page covers **{label}** item **{shown}**."]
    if page.types:
        bits.append("Registered contractor types on the page: **" + ", ".join(page.types) + "**.")
    if page.categories:
        bits.append("BD files it under: " + "; ".join(page.categories) + ".")
    overview = " ".join(bits)
    # Pull nature row into the second sentence when present.
    nature = ""
    for table in page.tables:
        for row in table:
            if row and "nature of works" in row[0].lower() and len(row) > 1:
                nature = row[-1]
                break
    if nature:
        overview += f" Nature of works stated on the page: **{nature}**."
    out.append(overview)
    out.append("")
    out.append("## Critical main topics and subtopics")
    out.append("")
    for i, table in enumerate(page.tables, 1):
        heading = "Item gate" if len(page.tables) == 1 else f"Item gate {i}"
        out.append(f"### {i}. {heading}")
        out.append("")
        # Rebuild as Parameter | Requirement using first cell as parameter.
        rows = [["Parameter", "Requirement"]]
        for row in table:
            if len(row) == 1:
                rows.append([row[0], ""])
            else:
                rows.append([row[0], " ".join(row[1:])])
        out.append(md_table(rows))
        out.append("")
    n = len(page.tables) + 1
    if page.forms or page.procedure:
        out.append(f"### {n}. Submission path printed on this page")
        out.append("")
        if page.forms:
            out.append("Forms named on the page: **" + ", ".join(page.forms) + "**.")
            out.append("")
        if page.procedure:
            out.append("| Step | What the page says |")
            out.append("|---|---|")
            step = ""
            buf: list[str] = []

            def flush_step() -> None:
                if step and buf:
                    out.append(f"| {step} | {bold_limits(' '.join(buf)).replace('|', '/')} |")

            for ln in page.procedure:
                if re.fullmatch(r"Step \d", ln):
                    flush_step()
                    step = ln
                    buf = []
                else:
                    buf.append(ln)
            flush_step()
            out.append("")
        gate_fail = (
            "If any row of the gate is not met, this item does not apply. "
            "Re-match another item or use full Cap 123 approval and consent."
            if page.kind == "item"
            else "If any row of the gate is not met, this designated exempted works item does not apply."
        )
        out.append(f"**SD takeaway:** {gate_fail}")
        out.append("")
    else:
        out.append(
            "**SD takeaway:** If any row of the gate is not met, this item does not apply."
        )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_narrative(page: Page) -> str:
    title = page.title
    scope = (
        f"BD webpage “{title}”, scraped {SCRAPE}. "
        "This summary keeps the constraints the page itself states. "
        "It does not add dimensions, clause numbers, or exemptions the page does not print."
    )
    dest = page.path or ROOT / "x.md"
    prose_bits: list[str] = []
    for kind, data in page.stream:
        if kind in ("h1", "h2", "h3", "h4"):
            break
        if kind in ("p", "li") and isinstance(data, str):
            prose_bits.append(data)
    overview_src = " ".join(prose_bits[:4])
    overview = first_sentences(overview_src, 2) if overview_src else (
        "This page is a Buildings Department navigation or index page and states no separate design limit."
    )
    out = [header(title, page.url, dest, scope)]
    out.append(bold_limits(overview))
    out.append("")
    out.append("## Critical main topics and subtopics")
    out.append("")
    sections: list[dict] = []
    cur: dict = {"title": "What this page decides", "body": []}
    for item in page.stream:
        kind, data = item
        if kind in ("h1", "h2", "h3", "h4"):
            if cur["body"] or (cur["title"] and sections):
                sections.append(cur)
            cur = {"title": data, "body": []}
        else:
            cur["body"].append(item)
    if cur["body"]:
        sections.append(cur)
    # Drop leading empty title section duplicates of the page title.
    numbered = []
    for sec in sections:
        title_l = (sec["title"] or "").lower()
        if title_l in {page.title.lower(), "see also"} and not sec["body"]:
            continue
        if title_l.startswith("quick links"):
            continue
        if not sec["body"]:
            continue
        numbered.append(sec)
    if not numbered:
        numbered = [{"title": "What this page decides", "body": page.stream}]
    for i, sec in enumerate(numbered, 1):
        name = sec["title"] or "What this page decides"
        if name.lower() == title.lower():
            name = "What this page decides"
        out.append(f"### {i}. {name}")
        out.append("")
        bullets: list[str] = []

        def flush_bullets() -> None:
            if not bullets:
                return
            # Parameter-like bullets become a two-column table.
            pairs = []
            for b in bullets:
                m = re.match(r"^(.{3,80}?)[:：]\s+(.+)$", b)
                if m:
                    pairs.append([m.group(1), m.group(2)])
            if pairs and len(pairs) == len(bullets):
                out.append(md_table([["Parameter", "Requirement"], *pairs]))
            else:
                for b in bullets:
                    out.append(f"- {bold_limits(b)}")
            out.append("")
            bullets.clear()

        for kind, data in sec["body"]:
            if kind == "li":
                bullets.append(data)
            elif kind == "table":
                flush_bullets()
                header_cells = {c.lower() for c in data[0]} if data else set()
                if header_cells & {"gate", "form", "parameter"}:
                    out.append(md_table(data))
                elif data and len(data[0]) <= 2:
                    paired = [
                        [r[0], " ".join(r[1:])] if len(r) > 1 else [r[0], ""]
                        for r in data
                    ]
                    out.append(md_table([["Parameter", "Requirement"], *paired]))
                else:
                    out.append(md_table(data))
                out.append("")
            else:
                flush_bullets()
                if data.lower() == name.lower():
                    continue
                out.append(bold_limits(data))
                out.append("")
        flush_bullets()
        blob = " ".join(
            data for kind, data in sec["body"] if isinstance(data, str)
        )
        takeaway = sd_line(blob)
        if takeaway and len(takeaway) > 40:
            out.append(f"**SD takeaway:** {takeaway}")
            out.append("")
    text = "\n".join(out).rstrip() + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def folder_for(url: str, title: str) -> Path:
    path = urlparse(url).path
    if path.endswith(("form_mw.html", "form_sc.html", "form_nbw.html")):
        return ROOT / "Specified forms"
    if path.rstrip("/").endswith("/en/building-works/index.html"):
        return ROOT
    if "/new-building-works/" in path:
        return ROOT / "New building works"
    if "/alterations-and-additions/" in path:
        return ROOT / "Alterations and additions"
    if "/site-monitoring/" in path:
        return ROOT / "Site monitoring"
    if "/signboards/" in path:
        return ROOT / "Signboards"
    if "/designated-exempted-works/" in path:
        return ROOT / "Minor works" / "Designated exempted works"
    if "/procedures/" in path:
        return ROOT / "Minor works" / "Procedures"
    if "/prescribed-professionals-contractors/" in path:
        return ROOT / "Minor works" / "Prescribed professionals and contractors"
    if "/minor-works-items/" in path:
        if "index_mwcs_items_c" in path:
            return ROOT / "Minor works" / "Minor works items" / "Categories"
        return ROOT / "Minor works" / "Minor works items"
    if "/minor-works/" in path:
        return ROOT / "Minor works"
    return ROOT


def file_title(page: Page) -> str:
    if page.kind == "item" and page.item_no:
        return f"MW Item {page.item_no}"
    if page.kind == "dew" and page.item_no and len(page.tables) <= 1:
        return f"Designated Exempted Works Item {page.item_no}"
    return page.title


def assign_paths(pages: list[Page]) -> None:
    used: dict[Path, str] = {}
    for page in pages:
        title = file_title(page)
        folder = folder_for(page.url, title)
        dest = folder / f"{safe_stem(title)}_CS.md"
        n = 2
        while dest in used and used[dest] != page.url:
            dest = folder / f"{safe_stem(title)} ({n})_CS.md"
            n += 1
        used[dest] = page.url
        page.path = dest


def build_pages(raw: dict[str, str]) -> list[Page]:
    pages: list[Page] = []
    for url, html_text in sorted(raw.items()):
        page = Page(url=url, title=page_title(html_text), kind=kind_of(url, html_text))
        if page.kind in ("item", "dew"):
            extract_item_bits(html_text, page)
            if not page.tables:
                page.kind = "narrative"
                page.stream = parse_stream(html_text)
        elif page.kind == "category":
            page.stream = extract_category(html_text) or parse_stream(html_text)
            if not any(kind == "table" for kind, _ in page.stream):
                page.stream = parse_stream(html_text)
        elif page.kind == "form":
            page.stream = extract_forms(html_text) or parse_stream(html_text)
        else:
            page.stream = parse_stream(html_text)
        pages.append(page)
    assign_paths(pages)
    return pages


def render(page: Page) -> str:
    if page.kind in ("item", "dew") and page.tables:
        return render_item(page)
    return render_narrative(page)


def write_all(pages: list[Page]) -> None:
    if ROOT.exists():
        for p in ROOT.rglob("*.md"):
            p.unlink()
    for page in pages:
        assert page.path is not None
        text = render(page)
        page.path.parent.mkdir(parents=True, exist_ok=True)
        page.path.write_text(text, encoding="utf-8")


def catalogue(pages: list[Page]) -> str:
    groups: dict[str, list[Page]] = {}
    for page in pages:
        assert page.path is not None
        rel_parent = page.path.parent.relative_to(ROOT).as_posix()
        if rel_parent == ".":
            rel_parent = "(section hub)"
        groups.setdefault(rel_parent, []).append(page)
    lines = [
        "### Catalogue of scraped pages",
        "",
        f"Every HTML page reached from the building-works menu on {SCRAPE}, plus the three specified-form indexes linked from that menu. Traditional Chinese URL is the same path under `/tc/`.",
        "",
    ]
    for key in sorted(groups):
        lines.append(f"#### {key}")
        lines.append("")
        lines.append("| Summary | English | 繁體 |")
        lines.append("|---|---|---|")
        for page in sorted(groups[key], key=lambda p: str(p.path)):
            assert page.path is not None
            rel = page.path.relative_to(ROOT).as_posix()
            title = file_title(page).replace("|", "/")
            lines.append(
                f"| [{title}]({rel}) | [en]({page.url}) | [tc]({tc_url(page.url)}) |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    raw = crawl()
    pages = build_pages(raw)
    write_all(pages)
    # Catalogue is appended to the section hub after render, so the hub
    # file written above is replaced with hub text + catalogue.
    hub = next(p for p in pages if p.url.rstrip("/").endswith("/en/building-works/index.html") or p.url.endswith("/building-works/index.html"))
    assert hub.path is not None
    hub_text = render(hub).rstrip() + "\n\n" + catalogue(pages)
    hub.path.write_text(hub_text, encoding="utf-8")
    kinds: dict[str, int] = {}
    for p in pages:
        kinds[p.kind] = kinds.get(p.kind, 0) + 1
    print("WROTE", len(pages), kinds)


if __name__ == "__main__":
    main()
