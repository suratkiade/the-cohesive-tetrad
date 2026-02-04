#!/usr/bin/env python3
"""Minimal link checker for canonical markdown/text files."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
MD_LINK_RE = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
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
DEFAULT_ALLOWLIST = "scripts/link_check_allowlist.json"

def iter_urls(text: str) -> set[str]:
    return set(URL_RE.findall(text))

def iter_urls(text: str) -> set[str]:
    return set(URL_RE.findall(text))

def iter_internal_links(text: str) -> set[str]:
    candidates = set()
    for match in MD_LINK_RE.findall(text):
        target = match.strip()
        if not target or target.startswith("#"):
            continue
        if urlparse(target).scheme:
            continue
        candidates.add(target)
    return candidates


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

def load_allowlist(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    entries = payload.get("entries", [])
    return {entry["url"]: entry["reason"] for entry in entries}


def is_allowlisted(url: str, detail: str, allowlist: dict[str, str]) -> bool:
    if url not in allowlist:
        return False
    return "403" in detail or "Forbidden" in detail or "URLError" in detail


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
    parser.add_argument(
        "--allowlist",
        default=DEFAULT_ALLOWLIST,
        help="JSON allowlist for known restricted URLs",
    )
    args = parser.parse_args()

    root = Path(args.root)
    urls: set[str] = set()
    internal_links: list[tuple[str, str]] = []
    missing_files: list[str] = []

    for rel in args.files:
        path = root / rel
        if not path.exists():
            missing_files.append(rel)
            continue
        text = path.read_text(encoding="utf-8")
        urls |= iter_urls(text)
        for link in iter_internal_links(text):
            link_path = link.split("#", 1)[0]
            target = (path.parent / link_path).resolve()
            if not target.exists():
                internal_links.append((rel, link))
        urls |= iter_urls(path.read_text(encoding="utf-8"))

    if missing_files:
        print("Missing files:")
        for rel in missing_files:
            print(f"- {rel}")
        return 2

    allowlist = load_allowlist(root / args.allowlist)
    failed: list[tuple[str, str]] = []
    for url in sorted(urls):
        ok, detail = check_url(url, args.timeout)
        if ok:
            print(f"OK {url} ({detail})")
        elif is_allowlisted(url, detail, allowlist):
            print(f"SKIP {url} ({detail}; allowlisted: {allowlist[url]})")
        else:
            print(f"FAIL {url} ({detail})")
            failed.append((url, detail))
        time.sleep(args.sleep)

    if internal_links:
        print("\nBroken internal links:")
        for rel, link in internal_links:
            print(f"- {rel}: {link}")
        return 1
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
