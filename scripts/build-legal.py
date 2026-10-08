#!/usr/bin/env python3
"""Build the two GHL blocks for a legal page from a plain-text source file.

Usage:
    python3 scripts/build-legal.py pages/terms/terms-source.txt pages/terms terms

Source format (plain text, one item per line):
    line 1                    page title, e.g. TERMS OF SERVICE (ignored; the
                              block uses the title passed on the command line)
    Effective Date: ... /
    Last updated: ...         shown under the title in the banner
    lines before 1st heading  intro paragraphs
    "N. Heading"              a numbered section heading
    "## Heading"              an unnumbered section heading
    "* text"                  a bullet point
    [label](https://...)      an inline link (email addresses link
                              automatically)
    "> text"                  a line of a mailing address (consecutive lines
                              are grouped into one address block)
    [[...]]                   a note to yourself; becomes an HTML comment
    anything else             a paragraph

Writes <outdir>/01-<slug>-hero.html and <outdir>/02-<slug>-content.html.
The wording is copied exactly; only HTML escaping is applied.
"""
import html
import re
import sys
from pathlib import Path

TITLES = {"terms": "Terms of Service", "privacy": "Privacy Policy"}
OTHER_PAGE = {  # phrase in the text -> link to the other legal page
    "terms": ("Privacy Policy", "/privacy-policy"),
    "privacy": ("Terms of Service", "/terms"),
}


def parse(path):
    lines = [l.rstrip() for l in Path(path).read_text(encoding="utf-8").splitlines()]
    lines = [l for l in lines if l.strip()]
    effective, intro, sections, current = "", [], [], None
    for line in lines[1:]:
        if re.match(r"^(Effective Date|Last updated):", line) and not effective:
            effective = line
            continue
        m = re.match(r"^(\d+)\.\s+(.+)$", line)
        if m or line.startswith("## "):
            current = {
                "id": m.group(1) if m else str(len(sections) + 1),
                "num": m.group(1) if m else "",
                "title": m.group(2) if m else line[3:].strip(),
                "items": [],
            }
            sections.append(current)
            continue
        target = current["items"] if current else intro
        if line.startswith("[[") and line.endswith("]]"):
            target.append(("note", line[2:-2].strip()))
        elif line.startswith("> "):
            if target and target[-1][0] == "address":
                target[-1][1].append(line[2:])
            else:
                target.append(("address", [line[2:]]))
        elif line.startswith("* "):
            if target and target[-1][0] == "ul":
                target[-1][1].append(line[2:])
            else:
                target.append(("ul", [line[2:]]))
        else:
            target.append(("p", line))
    return effective, intro, sections


LINK = re.compile(r"\[([^\]]+)\]\(((?:https?|mailto):[^)\s]+)\)")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def anchor(href, label):
    return f'<a class="cbb-legal__inline-link" href="{html.escape(href)}">{label}</a>'


def text(s, slug):
    # [label](https://...) writes an explicit link; on those lines the
    # automatic link to the other legal page is skipped.
    links = []

    def stash(m):
        links.append((m.group(2), html.escape(m.group(1), quote=False)))
        return f"\x00{len(links) - 1}\x00"

    out = html.escape(LINK.sub(stash, s), quote=False)
    if not links:
        phrase, href = OTHER_PAGE[slug]
        out = out.replace(phrase, anchor(href, phrase), 1)
    out = EMAIL.sub(lambda m: anchor("mailto:" + m.group(0), m.group(0)), out)
    return re.sub("\x00(\\d+)\x00", lambda m: anchor(*links[int(m.group(1))]), out)


def render_items(items, slug, indent):
    pad = " " * indent
    out = []
    for kind, val in items:
        if kind == "note":
            out.append(f"{pad}<!-- {html.escape(val, quote=False)} -->")
        elif kind == "address":
            lines = "<br>\n".join(f"{pad}  {text(v, slug)}" for v in val)
            out.append(f'{pad}<address class="cbb-legal__address">\n{lines}\n{pad}</address>')
        elif kind == "ul":
            lis = "\n".join(f'{pad}  <li class="cbb-legal__li">{text(v, slug)}</li>' for v in val)
            out.append(f'{pad}<ul class="cbb-legal__ul">\n{lis}\n{pad}</ul>')
        else:
            letters = re.sub(r"[^A-Za-z]", "", val)
            caps = len(letters) > 20 and letters.isupper()
            cls = "cbb-legal__p cbb-legal__p--caps" if caps else "cbb-legal__p"
            out.append(f'{pad}<p class="{cls}">{text(val, slug)}</p>')
    return "\n".join(out)


def main():
    src, outdir, slug = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
    title = TITLES[slug]
    effective, intro, sections = parse(src)
    incomplete = any(k == "note" for s in sections for k, _ in s["items"]) or any(k == "note" for k, _ in intro)
    here = Path(__file__).resolve().parent

    hero = (here / "legal-hero.tpl.html").read_text(encoding="utf-8")
    hero = hero.replace("__TITLE__", title).replace("__EFFECTIVE__", html.escape(effective, quote=False))
    (outdir / f"01-{slug}-hero.html").write_text(hero, encoding="utf-8")

    num = lambda s, cls: f'<span class="{cls}">{s["num"]}.</span> ' if s["num"] else ""
    toc = "\n".join(
        f'            <li class="cbb-legal__toc-item"><a class="cbb-legal__toc-link" href="#{slug}-{s["id"]}">'
        f'{num(s, "cbb-legal__toc-num")}{html.escape(s["title"], quote=False)}</a></li>'
        for s in sections
    )
    body = "\n\n".join(
        f'        <section class="cbb-legal__section" id="{slug}-{s["id"]}" aria-labelledby="{slug}-{s["id"]}-h">\n'
        f'          <h2 class="cbb-legal__h2" id="{slug}-{s["id"]}-h">{num(s, "cbb-legal__num")}'
        f'{html.escape(s["title"], quote=False)}</h2>\n'
        f'{render_items(s["items"], slug, 10)}\n'
        f"        </section>"
        for s in sections
    )
    content = (here / "legal-content.tpl.html").read_text(encoding="utf-8")
    content = (
        content.replace("__TITLE__", title)
        .replace("__INTRO__", render_items(intro, slug, 8))
        .replace("__TOC__", toc)
        .replace("__SECTIONS__", body)
        .replace("__INCOMPLETE__", "\n     WARNING: the source text is marked incomplete. Do not publish\n     until the missing sections are added." if incomplete else "")
    )
    (outdir / f"02-{slug}-content.html").write_text(content, encoding="utf-8")
    print(f"{title}: {len(sections)} sections{' (INCOMPLETE)' if incomplete else ''}")


if __name__ == "__main__":
    main()
