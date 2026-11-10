#!/usr/bin/env python3
"""Check local links and basic metadata in a built Zine site."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"', re.IGNORECASE)
IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.IGNORECASE)
SKIP_PREFIXES = ("#", "mailto:", "tel:", "data:", "javascript:")


def exists(root: Path, target: Path) -> bool:
    if target.exists():
        return True
    if (target / "index.html").exists():
        return True
    if target.suffix == "" and target.with_suffix(".html").exists():
        return True
    return False


def target_path(root: Path, page: Path, url: str) -> Path | None:
    if url.startswith(SKIP_PREFIXES):
        return None
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    if path.startswith("/"):
        target = root / path.lstrip("/")
    else:
        target = page.parent / path
    if path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    pages = sorted(root.rglob("*.html"))
    if not pages:
        print(f"No HTML files found in {root}", file=sys.stderr)
        return 1

    broken: list[tuple[Path, str]] = []
    no_alt: list[Path] = []
    no_desc: list[Path] = []

    for page in pages:
        text = page.read_text(encoding="utf-8")
        for match in ATTR_RE.finditer(text):
            url = html.unescape(match.group(1)).strip()
            target = target_path(root, page, url)
            if target is not None and not exists(root, target):
                broken.append((page.relative_to(root), url))
        if any("alt=" not in tag.lower() for tag in IMG_RE.findall(text)):
            no_alt.append(page.relative_to(root))
        description = DESC_RE.search(text)
        if not description or not description.group(1).strip():
            no_desc.append(page.relative_to(root))

    for page, url in broken:
        print(f"BROKEN LINK  {page}: {url}")
    for page in no_alt:
        print(f"NO ALT       {page}")
    for page in no_desc:
        print(f"NO DESC      {page}")

    print(
        f"Checked {len(pages)} pages: {len(broken)} broken links, "
        f"{len(no_alt)} pages with images missing alt, {len(no_desc)} pages without description."
    )
    return 1 if broken or no_alt or no_desc else 0


if __name__ == "__main__":
    raise SystemExit(main())
