#!/usr/bin/env python3
"""One-shot: fetch problem statements + examples from takeuforward.org and
write them into each .py file's `# QUESTION:` block.

Strategy per page type:
1. Tutorial pages (/data-structure/, /graph/, /trie/, /dynamic-programming/):
   SSR has full content. Find "Problem Statement", extract through the first
   approach section break, then strip HTML and decode JSON escapes.
2. Paywalled /plus/dsa/ pages: only the og:description meta has the statement
   (no examples available). Use that.
3. leetcode.com URLs: og:description has a usable summary.
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
URLS_FILE = ROOT / ".sde-urls.json"

DIGIT_WORDS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
               "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
TITLE_FIXUP = {"Binary Trees[Miscellaneous]": "Binary Trees Misc"}


def _tokens(name: str) -> list[str]:
    s = name.replace("&", " and ")
    s = re.sub(r"['’‘]", "", s)
    parts = [p for p in re.split(r"[^a-zA-Z0-9]+", s) if p]
    out: list[str] = []
    for p in parts:
        if p[0].isdigit():
            head = ""
            rest = p
            while rest and rest[0].isdigit():
                head += DIGIT_WORDS[rest[0]].capitalize()
                rest = rest[1:]
            out.append(head + rest)
        else:
            out.append(p)
    return out


def make_filename(name: str) -> str:
    toks = _tokens(name)
    if not toks: return "problem.py"
    first = toks[0][0].lower() + toks[0][1:]
    rest = "".join(t[0].upper() + t[1:] if len(t) > 1 else t.upper() for t in toks[1:])
    return first + rest + ".py"


def section_to_dir(section: str) -> str:
    s = TITLE_FIXUP.get(section, section)
    s = re.sub(r"\bpart-(II|III|IV)\b", lambda m: "Part-" + m.group(1), s)
    return s


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  FAIL {url} -> {e}", file=sys.stderr)
        return ""


# ---- Decoding helpers ----

def _decode_js_string_escapes(s: str) -> str:
    """Decode \\uNNNN, \\n, \\t, \\\", \\\\, \\/ — produced when content is
    embedded as a JSON string inside <script> tags."""
    s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
    # Order matters — handle \\ last
    s = s.replace('\\"', '"').replace("\\'", "'").replace("\\/", "/")
    s = s.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "")
    s = s.replace("\\\\", "\\")
    return s


def _strip_tags(s: str) -> str:
    # Drop HTML comments first (otherwise --> leaks through)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p\s*>", "\n\n", s, flags=re.I)
    s = re.sub(r"</li\s*>", "\n", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "- ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = "\n".join(line.rstrip() for line in s.splitlines())
    return s.strip()


def _normalize(s: str) -> str:
    # collapse runs of whitespace within a line, remove empty leading/trailing lines
    out = []
    for line in s.splitlines():
        line = re.sub(r"[ \t]+", " ", line).rstrip()
        out.append(line)
    # collapse consecutive blank lines
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---- Extraction strategies ----

OG_DESC_RE = re.compile(
    r'<meta[^>]+(?:property|name)=["\']og:description["\'][^>]+content=["\']([^"\']+)["\']',
    re.I,
)
META_DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
    re.I,
)


def extract_og_description(raw_html: str) -> str | None:
    for r in (OG_DESC_RE, META_DESC_RE):
        m = r.search(raw_html)
        if m:
            return html.unescape(m.group(1)).strip()
    return None


# Break markers (anywhere in the raw HTML region) — these specifically mark
# the start of the approach blocks on tuf tutorial pages.
APPROACH_START_RE = re.compile(
    r'<summary[^>]*class="[^"]*main-summary[^"]*"'
    r'|<details[^>]*class="[^"]*main[_-]summary[^"]*"'
    r'|<!--\s*Disclaimer\s*-->'
    r'|<h2[^>]*>\s*(?:Brute|Better|Optimal|Approach\s*\d)',
    re.I,
)
# Cleanup: in-page approach nav box that appears between description and examples.
# Strip it from the region before processing.
NAV_BOX_RE = re.compile(
    r'<div class="horizontal_navbar_dsa_article">.*?</div>\s*</div>',
    re.I | re.S,
)
# Strip the "Practice:" footer link block + "Disclaimer:" paragraph
PRACTICE_FOOTER_RE = re.compile(
    r'(?:<h\d[^>]*>\s*Practice\s*:?\s*</h\d>.*?)?'
    r'<a[^>]*href="[^"]*"[^>]*>\s*<img[^>]*></a>',
    re.I | re.S,
)


def _strip_head(raw_html: str) -> str:
    """Drop everything inside <head>...</head> so meta tags don't poison scans."""
    return re.sub(r"<head[^>]*>.*?</head>", "", raw_html, count=1, flags=re.I | re.S)


def _clean_description(s: str) -> str:
    """Trim metadata prefixes/suffixes from an og:description string."""
    s = s.strip()
    # Strip "Detailed solution for ... - " prefix
    s = re.sub(r"^Detailed solution for [^-]+ - ", "", s)
    # Strip "Problem Statement:" prefix
    s = re.sub(r"^Problem\s+Statement\s*[:\-]?\s*", "", s)
    # Remove inline HTML comment artifacts that leak through ("-->" remnants)
    s = re.sub(r"--+>", "", s)
    # Truncate at "Examples" or "Example 1:" markers (og:description often crams
    # the examples into the description; we extract them separately)
    s = re.split(r"\s+(?:Examples?\s*[:.\s]|Example\s+\d+\s*:)", s, maxsplit=1)[0]
    # Drop trailing "..." (og:description gets truncated)
    s = re.sub(r"[\.\s]*\.\.\.+\s*$", "", s)
    # Strip any trailing junk: combinations of '-', '/', '>', '<', whitespace, or commas
    s = re.sub(r"[\s\-\\/<>,]+$", "", s)
    return s.strip().rstrip(".") + "."


GENERIC_DESC_RE = re.compile(
    r"^\s*Detailed tutorial and solution on takeUforward\b",
    re.I,
)


# Match the entire `<details class="article_example_details">...</details>`
# block (greedy until the matching close, which is safe since these blocks
# appear once per article and the closing tag is unique enough).
EXAMPLES_DETAILS_RE = re.compile(
    r'<details[^>]*class="[^"]*article_example_details[^"]*"[^>]*>(.*?)</details>',
    re.I | re.S,
)


def extract_examples(raw_html: str) -> str | None:
    """Extract the examples block from `<details class="article_example_details">...</details>`."""
    text = _decode_js_string_escapes(raw_html)
    m = EXAMPLES_DETAILS_RE.search(text)
    if not m:
        return None
    block = m.group(1)
    cleaned = _strip_tags(block)
    cleaned = _normalize(cleaned)
    # Drop the leading "Examples" label
    cleaned = re.sub(r"^Examples\s*", "", cleaned, count=1).strip()
    # Drop trailing "Practice:" or "Solve Problem" footer leftovers
    cleaned = re.split(r"\n\s*(?:Practice\s*:|Solve\s+Problem|Disclaimer)\s*", cleaned, maxsplit=1)[0].rstrip()
    if len(cleaned) < 20:
        return None
    if any(marker in cleaned for marker in ("self.__next_f", '"$undefined"', '"$RC(')):
        return None
    return cleaned


def extract_tutorial_content(raw_html: str) -> str | None:
    """Compose `og:description` (clean) + extracted examples block (best-effort)."""
    desc = extract_og_description(raw_html)
    if not desc:
        return None
    desc = _clean_description(desc)
    if not desc or len(desc) < 30:
        return None
    if GENERIC_DESC_RE.match(desc):
        return None
    examples = extract_examples(raw_html)
    if examples:
        return f"{desc}\n\nExamples:\n{examples}"
    return desc


def extract_problem(raw_html: str, url: str) -> str | None:
    """Decide best strategy per URL."""
    if not raw_html:
        return None
    # Tutorial pages first (richer)
    if "takeuforward.org" in url and "/plus/dsa/" not in url:
        body = extract_tutorial_content(raw_html)
        if body:
            return body
    # Fall back to og:description (works for paywalled + leetcode), cleaned
    og = extract_og_description(raw_html)
    if og:
        cleaned = _clean_description(og)
        if cleaned and len(cleaned) >= 30 and not GENERIC_DESC_RE.match(cleaned):
            return cleaned
    return None


# ---- File update ----

QUESTION_BLOCK_RE = re.compile(
    r"^(# QUESTION:[^\n]*\n)(?:#[^\n]*\n)*", re.MULTILINE
)


TODO_BLOCK = (
    "# QUESTION: {title}\n"
    "# TODO: fill in the problem description, examples, and constraints\n"
    "# (use /solve \"{title}\" \"{day}\" to fetch from the web)\n"
)


def format_block(title: str, body: str) -> str:
    lines = [f"# QUESTION: {title}"]
    for line in body.splitlines():
        line = line.rstrip()
        lines.append("# " + line if line else "#")
    return "\n".join(lines) + "\n"


def format_todo_block(title: str, day: str) -> str:
    return TODO_BLOCK.format(title=title, day=day)


def update_py_file(py_path: Path, title: str, body: str) -> bool:
    text = py_path.read_text()
    new_block = format_block(title, body)
    m = QUESTION_BLOCK_RE.search(text)
    if not m:
        py_path.write_text(new_block + "\n" + text)
        return True
    new_text = text[:m.start()] + new_block + text[m.end():]
    if new_text == text:
        return False
    py_path.write_text(new_text)
    return True


def main() -> None:
    urls = json.loads(URLS_FILE.read_text())
    print(f"Fetching {len(urls)} problem pages in parallel...")
    fetched: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        futures = {ex.submit(fetch, e["url"]): e["url"] for e in urls if e.get("url")}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                fetched[url] = fut.result()
            except Exception as exc:
                print(f"  EXC {url}: {exc}", file=sys.stderr)
                fetched[url] = ""
    print(f"Fetched {sum(1 for v in fetched.values() if v)}/{len(fetched)} unique URLs")

    counts = {"updated": 0, "og_only": 0, "no_url": 0, "no_content": 0, "no_file": 0}
    seen_files: set[Path] = set()
    for e in urls:
        section, name, url = e["section"], e["name"], e.get("url")
        day_dir = ROOT / section_to_dir(section)
        filename = make_filename(name)
        py_path = day_dir / filename
        if py_path in seen_files:
            base = filename[:-3]
            k = 2
            while (day_dir / f"{base}{k}.py") in seen_files: k += 1
            py_path = day_dir / f"{base}{k}.py"
        seen_files.add(py_path)

        if not py_path.exists():
            counts["no_file"] += 1
            print(f"  no .py: {py_path}", file=sys.stderr)
            continue
        if not url:
            # Reset to TODO so stale content doesn't linger
            text = py_path.read_text()
            mb = QUESTION_BLOCK_RE.search(text)
            if mb:
                py_path.write_text(text[:mb.start()] + format_todo_block(name, section_to_dir(section)) + text[mb.end():])
            counts["no_url"] += 1
            continue
        body = extract_problem(fetched.get(url, ""), url)
        if not body:
            counts["no_content"] += 1
            text = py_path.read_text()
            mb = QUESTION_BLOCK_RE.search(text)
            if mb:
                py_path.write_text(text[:mb.start()] + format_todo_block(name, section_to_dir(section)) + text[mb.end():])
            print(f"  no content: {name} ({url})", file=sys.stderr)
            continue
        is_og_only = ("/plus/dsa/" in url) or "leetcode.com" in url or "\n" not in body
        if update_py_file(py_path, name, body):
            counts["updated"] += 1
            if is_og_only:
                counts["og_only"] += 1
    print(
        f"Updated: {counts['updated']} (of which {counts['og_only']} desc-only) | "
        f"no-url: {counts['no_url']} | no-content: {counts['no_content']} | "
        f"no-file: {counts['no_file']}"
    )


if __name__ == "__main__":
    main()
