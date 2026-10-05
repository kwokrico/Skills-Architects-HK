"""Download Hong Kong e-Legislation English PDFs after the client-config gate."""

import re
from pathlib import Path

import requests

OUT = Path(__file__).resolve().parent / "_pdfs"
OUT.mkdir(parents=True, exist_ok=True)

URLS = {
    "cap301.pdf": "https://www.elegislation.gov.hk/hk/cap301!en.pdf",
    "cap301D.pdf": "https://www.elegislation.gov.hk/hk/cap301D!en.pdf",
    "cap499.pdf": "https://www.elegislation.gov.hk/hk/cap499!en.pdf",
    "cap53.pdf": "https://www.elegislation.gov.hk/hk/cap53!en.pdf",
    "cap59.pdf": "https://www.elegislation.gov.hk/hk/cap59!en.pdf",
    "cap59I.pdf": "https://www.elegislation.gov.hk/hk/cap59I!en.pdf",
    "cap509.pdf": "https://www.elegislation.gov.hk/hk/cap509!en.pdf",
    "cap132.pdf": "https://www.elegislation.gov.hk/hk/cap132!en.pdf",
    "cap172.pdf": "https://www.elegislation.gov.hk/hk/cap172!en.pdf",
    "cap279.pdf": "https://www.elegislation.gov.hk/hk/cap279!en.pdf",
    "cap349.pdf": "https://www.elegislation.gov.hk/hk/cap349!en.pdf",
    "cap459.pdf": "https://www.elegislation.gov.hk/hk/cap459!en.pdf",
    "cap613.pdf": "https://www.elegislation.gov.hk/hk/cap613!en.pdf",
    "cap311.pdf": "https://www.elegislation.gov.hk/hk/cap311!en.pdf",
    "cap358.pdf": "https://www.elegislation.gov.hk/hk/cap358!en.pdf",
    "cap400.pdf": "https://www.elegislation.gov.hk/hk/cap400!en.pdf",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "application/pdf,text/html,*/*",
}


def pass_gate(session: requests.Session, html: str, page_url: str) -> None:
    token = None
    match = re.search(r'name="_CSRF_TOKEN"[^>]*value="([^"]+)"', html)
    if not match:
        match = re.search(r"_CSRF_TOKEN=([^\"&\s>]+)", html)
    if match:
        token = match.group(1)
    print("gate token present", bool(token))
    data = {
        "applicationId": "RA001",
        "javascriptEnabled": "true",
        "appletLoadFailed": "true",
        "cookieEnabled": "true",
        "jvmVendor": "",
        "jvmVersion": "",
    }
    if token:
        data["_CSRF_TOKEN"] = token
    posted = session.post(
        "https://www.elegislation.gov.hk/checkconfig/submitClientConfig.do",
        data=data,
        headers={**HEADERS, "Referer": page_url},
        timeout=60,
        allow_redirects=False,
    )
    print("config-post", posted.status_code, posted.headers.get("location"))
    location = posted.headers.get("location")
    if location:
        if location.startswith("/"):
            location = "https://www.elegislation.gov.hk" + location
        followed = session.get(location, headers=HEADERS, timeout=60)
        print("followed", followed.status_code, followed.url, followed.headers.get("content-type"))
        text = followed.content.decode("utf-8", errors="replace")
        fields = dict(re.findall(r'name="([^"]+)" value="([^"]*)"', text))
        checked = session.post(
            "https://www.elegislation.gov.hk/client-check",
            data=fields,
            headers=HEADERS,
            timeout=60,
            allow_redirects=True,
        )
        print("client-check", checked.status_code, checked.url)


def fetch(session: requests.Session, name: str, url: str) -> None:
    response = session.get(url, headers=HEADERS, timeout=120, allow_redirects=True)
    body = response.content
    if body[:5] != b"%PDF-" and b"submitClientConfig" in body:
        pass_gate(session, body.decode("utf-8", errors="replace"), response.url)
        response = session.get(url, headers=HEADERS, timeout=180, allow_redirects=True)
        body = response.content
    dest = OUT / name
    dest.write_bytes(body)
    kind = "pdf" if body[:5] == b"%PDF-" else "other"
    print(f"{name} status={response.status_code} bytes={len(body)} kind={kind} ctype={response.headers.get('content-type')}")


def main() -> None:
    session = requests.Session()
    for name, url in URLS.items():
        dest = OUT / name
        if dest.exists() and dest.read_bytes()[:5] == b"%PDF-" and dest.stat().st_size > 20000:
            print(f"skip {name} bytes={dest.stat().st_size}")
            continue
        try:
            fetch(session, name, url)
        except Exception as exc:
            print(f"FAIL {name} {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    main()
