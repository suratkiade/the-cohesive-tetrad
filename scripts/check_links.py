#!/usr/bin/env python3
"""Minimal link checker for canonical markdown/text files."""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")

DEFAULT_FILES = [
    "README.md",
    "CANONICAL_INDEX.md",
    "CHANGELOG.md",
    "META_LINKS.md",
    "llms.txt",
    "llms-full.txt",
    "manuscript/README.md",
    "journal/README.md",
    "semantic-defs/README.md",
]


def iter_urls(text: str) -> set[str]:
    return set(URL_RE.findall(text))


def check_url(url: str, timeout: float) -> tuple[bool, str]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return True, "skipped"

    headers = {
        "User-Agent": "the-cohesive-tetrad-link-checker/1.0",
    }

    for method in ("HEAD", "GET"):
        try:
            req = Request(url, method=method, headers=headers)
            with urlopen(req, timeout=timeout) as response:
                status = response.status
                if 200 <= status < 400:
                    return True, f"{status} {method}"
                return False, f"{status} {method}"
        except HTTPError as exc:
            if exc.code == 405 and method == "HEAD":
                continue
            return False, f"{exc.code} {method}"
        except URLError as exc:
            return False, f"URLError {exc.reason}"
    return False, "unreachable"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check external links.")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Timeout per request in seconds",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.2,
        help="Sleep between requests in seconds",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default=DEFAULT_FILES,
        help="Files to scan for URLs",
    )
    args = parser.parse_args()

    root = Path(args.root)
    urls: set[str] = set()
    missing_files: list[str] = []

    for rel in args.files:
        path = root / rel
        if not path.exists():
            missing_files.append(rel)
            continue
        urls |= iter_urls(path.read_text(encoding="utf-8"))

    if missing_files:
        print("Missing files:")
        for rel in missing_files:
            print(f"- {rel}")
        return 2

    failed: list[tuple[str, str]] = []
    for url in sorted(urls):
        ok, detail = check_url(url, args.timeout)
        status = "OK" if ok else "FAIL"
        print(f"{status} {url} ({detail})")
        if not ok:
            failed.append((url, detail))
        time.sleep(args.sleep)

    if failed:
        print("\nFailed URLs:")
        for url, detail in failed:
            print(f"- {url} ({detail})")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
