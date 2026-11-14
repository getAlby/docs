#!/usr/bin/env python3
"""Check Markdown/GitBook links in this repository.

Validates:
- relative links point to existing files/directories or page anchors
- HTTP(S) links return a non-error status

Designed for local use and GitHub Actions scheduled runs.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import html
import html.parser
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SKIP_SCHEMES = {
    "mailto", "tel", "bitcoin", "lightning", "lnbc", "keysend", "nostr", "web+lightning",
    "alby", "chrome", "about", "data", "javascript"
}
DEFAULT_IGNORES = [
    r"^https://twitter\.com/intent/",
    r"^https://x\.com/intent/",
]

MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
REF_LINK_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
RAW_URL_RE = re.compile(r"https?://[^\s<>)\]'\"`]+")
HTML_ATTR_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING_PUNCT_RE = re.compile(r"[^a-z0-9 _-]")

@dataclass(frozen=True)
class Link:
    source: Path
    line: int
    target: str

@dataclass(frozen=True)
class Result:
    link: Link
    ok: bool
    kind: str
    detail: str
    final_url: str = ""


def slugify_heading(text: str) -> str:
    # GitBook-like heading anchor approximation.
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).strip().lower()
    text = text.replace(">", " greater than ").replace("&", " and ")
    text = HEADING_PUNCT_RE.sub("", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text


def anchors_for_md(path: Path) -> set[str]:
    anchors: set[str] = set()
    heading_index = 0
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if m := re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line):
                heading_index += 1
                slug = slugify_heading(m.group(2))
                if slug:
                    anchors.add(slug)
                    # GitBook sometimes prefixes auto-generated duplicated/custom anchors with id-N.
                    anchors.add(f"id-{heading_index}.-{slug}")
                    anchors.add(f"id-{heading_index}-{slug}")
            for m in re.finditer(r"<a\s+[^>]*(?:id|name)=[\"']([^\"']+)[\"']", line, re.I):
                anchors.add(m.group(1))
    except OSError:
        pass
    return anchors


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def extract_links(path: Path) -> list[Link]:
    text = path.read_text(encoding="utf-8", errors="replace")
    found: list[tuple[int, str]] = []
    for regex in (MD_LINK_RE, REF_LINK_RE, HTML_ATTR_RE, RAW_URL_RE):
        for m in regex.finditer(text):
            target = m.group(1) if regex is not RAW_URL_RE else m.group(0)
            target = html.unescape(target.strip().strip("<>"))
            if not target or target.startswith("#"):
                continue
            found.append((m.start(), target))
    # De-dupe same source/line/target, keeping stable order.
    seen = set()
    links: list[Link] = []
    for offset, target in sorted(found):
        key = (line_number(text, offset), target)
        if key in seen:
            continue
        seen.add(key)
        links.append(Link(path, key[0], target))
    return links


def local_candidates(base: Path, raw_target: str) -> tuple[list[Path], str]:
    parsed = urllib.parse.urlsplit(raw_target)
    target_path = urllib.parse.unquote(parsed.path)
    anchor = urllib.parse.unquote(parsed.fragment or "")
    if not target_path:
        return [], anchor
    candidate = (base / target_path).resolve()
    candidates = [candidate]
    if candidate.suffix == "":
        candidates.extend([candidate.with_suffix(".md"), candidate / "README.md"])
    elif candidate.suffix.lower() in {".html", ".htm"}:
        candidates.append(candidate.with_suffix(".md"))
    return candidates, anchor


def check_local(root: Path, link: Link) -> Result:
    candidates, anchor = local_candidates(link.source.parent, link.target)
    in_root_candidates = [p for p in candidates if root in p.parents or p == root]
    for candidate in in_root_candidates:
        if candidate.exists():
            if anchor and candidate.suffix.lower() == ".md":
                anchors = anchors_for_md(candidate)
                if anchor and anchor not in anchors:
                    return Result(link, False, "local", f"missing anchor #{anchor} in {candidate.relative_to(root)}")
            return Result(link, True, "local", "ok")
    shown = in_root_candidates[0].relative_to(root) if in_root_candidates else link.target
    return Result(link, False, "local", f"missing file/path {shown}")


def check_http(link: Link, timeout: int, retries: int, allowed_statuses: set[int]) -> Result:
    url = link.target.replace(" ", "%20")
    headers = {
        "User-Agent": "Alby docs link checker (+https://guides.getalby.com)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    last_detail = ""
    final_url = ""
    for attempt in range(retries + 1):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=method, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    code = getattr(resp, "status", resp.getcode())
                    final_url = resp.geturl()
                    if code < 400:
                        return Result(link, True, "http", f"HTTP {code}", final_url)
                    if code in allowed_statuses:
                        return Result(link, True, "http", f"HTTP {code} (allowed; host may block bots)", final_url)
                    last_detail = f"HTTP {code}"
            except urllib.error.HTTPError as e:
                final_url = e.geturl() or url
                # Some hosts reject HEAD but allow GET; try GET before failing.
                last_detail = f"HTTP {e.code}"
                if e.code in allowed_statuses:
                    return Result(link, True, "http", f"HTTP {e.code} (allowed; host may block bots)", final_url)
                if method == "HEAD" and e.code in {403, 405, 406, 429}:
                    continue
            except Exception as e:  # noqa: BLE001 - report network/DNS/TLS failures as link-check findings
                last_detail = f"{type(e).__name__}: {e}"
        if attempt < retries:
            time.sleep(1 + attempt)
    return Result(link, False, "http", last_detail or "request failed", final_url)


def should_ignore(target: str, ignore_patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, target) for pattern in ignore_patterns)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--ignore", action="append", default=[], help="regex for targets to ignore")
    parser.add_argument(
        "--allow-status",
        default="403,429",
        help="comma-separated HTTP statuses to treat as non-fatal (default: 403,429 for bot-blocking/rate-limiting hosts)",
    )
    parser.add_argument("--markdown-glob", default="**/*.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    allowed_statuses = {int(s) for s in args.allow_status.split(",") if s.strip()}
    ignore_patterns = DEFAULT_IGNORES + args.ignore
    md_files = [p for p in root.glob(args.markdown_glob) if ".git" not in p.parts]
    links = [link for p in md_files for link in extract_links(p)]

    skipped = [l for l in links if should_ignore(l.target, ignore_patterns)]
    links = [l for l in links if not should_ignore(l.target, ignore_patterns)]

    local_links: list[Link] = []
    http_links: list[Link] = []
    for link in links:
        parsed = urllib.parse.urlsplit(link.target)
        scheme = parsed.scheme.lower()
        if scheme in {"http", "https"}:
            http_links.append(link)
        elif scheme in SKIP_SCHEMES or link.target.startswith("{"):
            skipped.append(link)
        else:
            local_links.append(link)

    results: list[Result] = []
    results.extend(check_local(root, link) for link in local_links)

    # Check each unique URL once, then fan result back to all occurrences.
    by_url: dict[str, list[Link]] = {}
    for link in http_links:
        by_url.setdefault(link.target, []).append(link)

    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(check_http, links_for_url[0], args.timeout, args.retries, allowed_statuses): links_for_url for links_for_url in by_url.values()}
        for fut in futures.as_completed(future_map):
            result = fut.result()
            for occurrence in future_map[fut]:
                results.append(Result(occurrence, result.ok, result.kind, result.detail, result.final_url))

    broken = [r for r in results if not r.ok]
    print(f"Checked {len(results)} link occurrences ({len(by_url)} unique HTTP URLs, {len(local_links)} local links); skipped {len(skipped)}.")
    print(f"Broken/problem links: {len(broken)}")
    if broken:
        print()
        for r in sorted(broken, key=lambda x: (str(x.link.source), x.link.line, x.link.target)):
            rel = r.link.source.relative_to(root)
            print(f"{rel}:{r.link.line}: {r.link.target}")
            print(f"  -> {r.kind}: {r.detail}")
            if r.final_url and r.final_url != r.link.target:
                print(f"     final: {r.final_url}")
    return 1 if broken else 0

if __name__ == "__main__":
    raise SystemExit(main())
