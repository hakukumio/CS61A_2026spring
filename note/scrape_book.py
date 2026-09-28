#!/usr/bin/env python3
"""Scrape composingprograms.com (Version 2) into a local Markdown book.

Produces:
    book/Chapter1/1.1.md ... 1.7.md
    book/Chapter2/2.1.md ... 2.9.md
    book/Chapter3/3.1.md ... 3.5.md
    book/Chapter4/4.1.md ... 4.8.md
    book/img/*.png

Source: https://composingprograms.com/pages/

Downloaded HTML is cached in .cache/ so re-runs work offline; pass --refresh
to re-fetch.
"""

import argparse
import os
import re
import sys
import urllib.request
from pathlib import Path

import markdownify
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / ".cache" / "cp"
BOOK = ROOT / "book"
BASE = "https://composingprograms.com"
UA = {"User-Agent": "Mozilla/5.0 (book archiver)"}


def fetch(url: str, dest: Path, refresh: bool = False) -> bytes:
    """Download url to dest, reusing the cached copy unless refresh is set."""
    if dest.exists() and not refresh:
        return dest.read_bytes()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return data


def fetch_text(url: str, dest: Path, refresh: bool = False) -> str:
    return fetch(url, dest, refresh).decode("utf-8")


# --------------------------------------------------------------------------
# Table of contents
# --------------------------------------------------------------------------

def parse_toc(html: str):
    """Return [(chapter_no, section_no, slug, title), ...] from the index page."""
    soup = BeautifulSoup(html, "lxml")
    entries = []
    chapter = 0
    for node in soup.select("h3, li > a"):
        if node.name == "h3":
            m = re.match(r"Chapter\s+(\d+)", node.get_text())
            if m:
                chapter = int(m.group(1))
        else:
            m = re.match(r"/(pages/)?(\d\d)-(.+)\.html$", node.get("href", ""))
            if not m:
                continue
            sec = m.group(2)  # e.g. "12"
            entries.append((chapter, f"{sec[0]}.{sec[1]}", f"{sec[0]}{sec[1]}-{m.group(3)}",
                            node.get_text(strip=True)))
    return entries


SECTION_FILE = {}  # section number -> (chapter_no, filename)


def build_index(entries):
    for chapter, secnum, _slug, _title in entries:
        SECTION_FILE[secnum] = (chapter, f"{secnum}.md")


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------

YOUTUBE_RE = re.compile(r"youtube\.com/embed/([A-Za-z0-9_-]{11})")


class Converter(markdownify.MarkdownConverter):
    """markdownify with the few custom mappings this site needs."""

    def convert_tt(self, el, text, parent_tags):
        # <tt class="docutils literal">name</tt> is inline code
        text = text.strip()
        return f"`{text}`" if text else ""

    def convert_pre(self, el, text, parent_tags):
        text = el.get_text()
        if not text.endswith("\n"):
            text += "\n"
        # Pygments blocks, and the Python Tutor embeds, are all Python.
        parent = el.parent
        python = (parent is not None and parent.name == "div"
                  and ("highlight" in (parent.get("class") or [])
                       or "example" in (parent.get("class") or [])))
        lang = "python" if python else ""
        return f"\n\n```{lang}\n{text}```\n\n"

    def convert_div(self, el, text, parent_tags):
        classes = el.get("class") or []

        # Embedded YouTube lecture video: keep a real link, drop the JS player.
        if "youtube" in classes:
            m = YOUTUBE_RE.search(str(el))
            if m:
                vid = m.group(1)
                return (f"\n\n> **Video:** [Watch on YouTube]"
                        f"(https://www.youtube.com/watch?v={vid})\n\n")
            return ""

        # Python Tutor frame: the div *is* the source code.
        if "example" in classes:
            if el.find("pre") is not None or el.find("div", class_="highlight"):
                return text
            code = el.get_text()
            if not code.endswith("\n"):
                code += "\n"
            return f"\n\n```python\n{code}```\n\n"

        # Pygments wrapper; convert_pre reads the language off this class.
        if "highlight" in classes:
            return text

        # Poetry-style line blocks: preserve the line breaks.
        if "line-block" in classes:
            lines = "  \n".join(  # trailing two spaces = hard break in Markdown
                d.get_text(strip=True) for d in el.find_all("div", class_="line")
            )
            return f"\n\n{lines}\n\n"

        return text

    def convert_img(self, el, text, parent_tags):
        src = el.get("src", "")
        alt = (el.get("alt") or "").strip()
        # src is "../img/foo.png"; our layout keeps the same relative depth,
        # so the path works unchanged from book/ChapterN/.
        return f"![{alt}]({src})"

    def convert_a(self, el, text, parent_tags):
        href = el.get("href", "")
        text = text.strip()

        # Cross-page links -> local Markdown files.
        m = re.match(r"\.\./pages/(\d\d)-.*\.html$", href)
        if m:
            secid = m.group(1)
            target = SECTION_FILE.get(f"{secid[0]}.{secid[1]}")
            if target:
                chapter, name = target
                here = getattr(self, "_chapter")
                rel = name if chapter == here else f"../Chapter{chapter}/{name}"
                return f"[{text}]({rel})"
        if not href:
            return text
        return f"[{text}]({href})"


def normalize(md: str) -> str:
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+$", "", md, flags=re.M)      # trailing whitespace
    md = re.sub(r"\n{3,}", "\n\n", md)               # collapse blank runs
    md = re.sub(r"^(#{1,6}) +(\d[\d.]*) +", r"\1 \2 ", md, flags=re.M)
    return md.strip() + "\n"


def convert_page(html: str, chapter: int) -> str:
    soup = BeautifulSoup(html, "lxml")
    inner = soup.select_one("div.inner-content")
    if inner is None:
        raise SystemExit("could not find div.inner-content")

    for junk in inner.select("script, style"):
        junk.decompose()

    # Headings: files that open with a chapter <h1> keep it as the title and
    # nest the section under it; everything else promotes the section to <h1>.
    has_h1 = inner.find("h1") is not None
    shift = 0 if has_h1 else 1
    for h in inner.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        level = max(1, int(h.name[1]) - shift)
        h.name = f"h{level}"

    conv = Converter(heading_style="ATX", bullets="-", strong_em_symbol="*",
                     escape_asterisks=False, escape_underscores=False)
    conv._chapter = chapter
    return normalize(conv.convert_soup(inner))


# --------------------------------------------------------------------------
# Images
# --------------------------------------------------------------------------

def grab_images(entries, refresh=False):
    """Download every image referenced by the pages into book/img/."""
    srcs = set()
    for _c, _s, slug, _t in entries:
        html = (CACHE / f"{slug}.html").read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "lxml")
        inner = soup.select_one("div.inner-content")
        if inner:
            srcs.update(img["src"] for img in inner.find_all("img") if img.get("src"))
    for src in sorted(srcs):
        name = os.path.basename(src)
        fetch(f"{BASE}/img/{name}", BOOK / "img" / name, refresh)
    return len(srcs)


def grab_examples(refresh=False):
    """Download the ../examples/... files the pages link to, keeping the same
    relative path so those links resolve offline from book/ChapterN/."""
    wanted = set()
    for md in BOOK.glob("Chapter*/*.md"):
        wanted.update(re.findall(r"\((\.\./examples/[^)\s]+)\)", md.read_text(encoding="utf-8")))
    for link in sorted(wanted):
        rel = link[len("../"):]  # "examples/scalc/scalc.py.html"
        if ".." in rel.split("/"):
            continue
        fetch(f"{BASE}/{rel}", BOOK / rel, refresh)
    return len(wanted)


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="re-download all HTML")
    args = ap.parse_args()

    index_html = fetch_text(f"{BASE}/pages/", CACHE / "index.html", args.refresh)
    entries = parse_toc(index_html)
    if not entries:
        raise SystemExit("no sections found in the index page")
    build_index(entries)

    for chapter, secnum, slug, title in entries:
        dest = CACHE / f"{slug}.html"
        html = fetch_text(f"{BASE}/pages/{slug}.html", dest, args.refresh)
        md = convert_page(html, chapter)
        out = BOOK / f"Chapter{chapter}" / f"{secnum}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        print(f"{out.relative_to(ROOT)}  {len(md):>7,} bytes  {title}")

    n = grab_images(entries, args.refresh)
    e = grab_examples(args.refresh)
    print(f"\n{len(entries)} pages -> {BOOK.relative_to(ROOT)}/, "
          f"{n} images -> book/img/, {e} example files -> book/examples/")


if __name__ == "__main__":
    main()
