"""Assemble verbatim raw dumps with a source header."""

from pathlib import Path

import requests

RAW = Path(__file__).resolve().parent
TXT = RAW / "_txt"
HEADER_DATE = "Fetched: 2026-10-05"


def write_md(name: str, url: str, body: str) -> None:
    text = f"Source-URL: {url}\n{HEADER_DATE}\n\n{body.rstrip()}\n"
    (RAW / name).write_text(text, encoding="utf-8")
    print(name, len(text))


def from_txt(name: str, url: str, stem: str, end_line: int | None = None) -> None:
    lines = (TXT / f"{stem}.txt").read_text(encoding="utf-8").splitlines()
    if end_line is not None:
        lines = lines[:end_line]
    write_md(name, url, "\n".join(lines))


def fetch_html(name: str, url: str) -> None:
    response = requests.get(
        url,
        timeout=60,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    write_md(name, url, response.text)


def main() -> None:
    from_txt(
        "env-heritage-01.md",
        "https://www.elegislation.gov.hk/hk/cap301!en.pdf",
        "cap301",
    )
    from_txt(
        "env-heritage-02.md",
        "https://www.elegislation.gov.hk/hk/cap301D!en.pdf",
        "cap301D",
    )
    fetch_html(
        "env-heritage-03.md",
        "https://www.cad.gov.hk/english/obstructions.html",
    )
    from_txt(
        "env-heritage-04.md",
        "https://www.elegislation.gov.hk/hk/cap499!en.pdf",
        "cap499",
    )
    fetch_html(
        "env-heritage-05.md",
        "https://www.epd.gov.hk/eia/en/legis/memorandum/text1.html",
    )
    gazette_url = "https://www.epd.gov.hk/eia/common/files/legis/memorandum/es5202327182.pdf"
    gazette_pdf = RAW / "_gazette_eia_tm.pdf"
    gazette_response = requests.get(gazette_url, timeout=120, headers={"User-Agent": "Mozilla/5.0"})
    gazette_response.raise_for_status()
    gazette_pdf.write_bytes(gazette_response.content)
    from pypdf import PdfReader

    gazette_text = "\n\n".join(
        (page.extract_text() or "") for page in PdfReader(str(gazette_pdf)).pages
    )
    write_md("env-heritage-05b.md", gazette_url, gazette_text)
    from_txt(
        "env-heritage-06.md",
        "https://www.elegislation.gov.hk/hk/cap53!en.pdf",
        "cap53",
    )
    from_txt(
        "env-heritage-07.md",
        "https://www.elegislation.gov.hk/hk/cap59!en.pdf",
        "cap59",
    )
    from_txt(
        "env-heritage-08.md",
        "https://www.elegislation.gov.hk/hk/cap59I!en.pdf",
        "cap59I",
    )
    from_txt(
        "env-heritage-09.md",
        "https://www.elegislation.gov.hk/hk/cap509!en.pdf",
        "cap509",
    )
    fetch_html(
        "env-heritage-10.md",
        "https://www.labour.gov.hk/eng/legislat/content3.htm",
    )
    fetch_html(
        "env-heritage-11.md",
        "https://www.epd.gov.hk/epd/english/envir_standards/statutory/esg_stat.html",
    )
    fetch_html(
        "env-heritage-12.md",
        "https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_apco.html",
    )
    fetch_html(
        "env-heritage-13.md",
        "https://www.epd.gov.hk/epd/english/environmentinhk/noise/guide_ref/noise_guidelines.html",
    )
    from_txt(
        "env-heritage-14.md",
        "https://www.elegislation.gov.hk/hk/cap311!en.pdf",
        "cap311",
        360,
    )
    from_txt(
        "env-heritage-15.md",
        "https://www.elegislation.gov.hk/hk/cap358!en.pdf",
        "cap358",
        150,
    )
    from_txt(
        "env-heritage-16.md",
        "https://www.elegislation.gov.hk/hk/cap400!en.pdf",
        "cap400",
        140,
    )
    fetch_html(
        "env-heritage-17.md",
        "https://www.cedd.gov.hk/eng/publications/geo/geoguides/geo-g5/index.html",
    )
    fetch_html(
        "env-heritage-18.md",
        "https://www.cedd.gov.hk/eng/publications/geo/geoguides/index.html",
    )
    fetch_html(
        "env-heritage-19.md",
        "https://www.epd.gov.hk/epd/english/application_for_licences/guidance/ia_322.html",
    )
    titles = []
    pairs = [
        ("cap132", "https://www.elegislation.gov.hk/hk/cap132!en.pdf"),
        ("cap349", "https://www.elegislation.gov.hk/hk/cap349!en.pdf"),
        ("cap279", "https://www.elegislation.gov.hk/hk/cap279!en.pdf"),
        ("cap459", "https://www.elegislation.gov.hk/hk/cap459!en.pdf"),
        ("cap613", "https://www.elegislation.gov.hk/hk/cap613!en.pdf"),
        ("cap172", "https://www.elegislation.gov.hk/hk/cap172!en.pdf"),
    ]
    for stem, url in pairs:
        head = "\n".join((TXT / f"{stem}.txt").read_text(encoding="utf-8").splitlines()[:12])
        titles.append(f"Source-URL: {url}\n{head}")
    write_md(
        "env-heritage-20.md",
        "https://www.elegislation.gov.hk/hk/cap132!en.pdf",
        "\n\n".join(titles),
    )


if __name__ == "__main__":
    main()
