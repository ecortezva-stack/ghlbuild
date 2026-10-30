#!/usr/bin/env python3
"""Build the header variants and the /data-list Coming Soon page.

Writes:
  sections/00-header-home.html     Home page header: Home, Marketing Services,
                                   Business Funding, Home Loans, High
                                   Converting Leads, About, Contact.
                                   Root class .cbb-hh.
  sections/00-header-capital.html  Header for /funding, /home-loans and
                                   /data-list: Marketing Services, Business
                                   Funding, Home Loans, High Converting Leads,
                                   with the current page highlighted.
                                   Root class .cbb-hc.
  pages/data-list/01-data-list-soon.html    Coming Soon body (.cbb-dsoon)

The /funding and /home-loans page bodies are built by
scripts/build-overviews.py.

Both headers are made from sections/00-header.html (the header every other
page uses), so styling and behavior stay the same. Edit that file or this
script, then run:  python3 scripts/build-variants.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
base = (root / "sections/00-header.html").read_text(encoding="utf-8")

BASE_NAV = """          <li class="cbb-header__item"><a class="cbb-header__link" href="/">Home</a></li>
          <li class="cbb-header__item"><a class="cbb-header__link" href="/services">Marketing Services</a></li>
          <li class="cbb-header__item"><a class="cbb-header__link" href="/about">About</a></li>
          <li class="cbb-header__item"><a class="cbb-header__link" href="/contact">Contact</a></li>
"""
BASE_NAV_NOTE = """        <!-- Links only turn gold and underline on hover. The current page is
             tagged for screen readers (aria-current) from the URL, with no
             visual change. -->
"""
BASE_INTRO = """     CBB — HEADER / NAVIGATION
     Paste into a GoHighLevel Custom HTML/JavaScript element.
     All styles are scoped to .cbb-header; the script only touches
     elements inside .cbb-header.
"""
BASE_MOBILE_CSS = "  /* ---- Mobile: slide-down menu ---- */\n"
for s in (BASE_NAV, BASE_NAV_NOTE, BASE_INTRO, BASE_MOBILE_CSS,
          "@media (max-width: 860px)", "'(min-width: 861px)'", 'href="/" aria-label="Covered Bridge Brands home"'):
    assert base.count(s) == 1, s


def item(prefix, href, label):
    return f'          <li class="{prefix}__item"><a class="{prefix}__link" href="{href}">{label}</a></li>\n'


def variant(prefix, intro, note, links, extra_css="", breakpoint=860, logo_href="/"):
    out = base.replace(BASE_INTRO, intro).replace(BASE_NAV_NOTE, note)
    out = out.replace(BASE_NAV, "".join(item("cbb-header", h, l) for h, l in links))
    out = out.replace(BASE_MOBILE_CSS, extra_css + BASE_MOBILE_CSS)
    out = out.replace("@media (max-width: 860px)", f"@media (max-width: {breakpoint}px)")
    out = out.replace("'(min-width: 861px)'", f"'(min-width: {breakpoint + 1}px)'")
    out = out.replace('href="/" aria-label="Covered Bridge Brands home"',
                      f'href="{logo_href}" aria-label="Covered Bridge Brands home"')
    # Unique root class and id so this block can't clash with the shared header.
    out = out.replace("cbb-header-nav", f"{prefix}-nav")
    out = out.replace("cbb-header__", f"{prefix}__")
    out = out.replace("--cbb-header-h", f"--{prefix}-h")
    out = out.replace("cbb-header", prefix)
    return out


# Menu label -> page heading for each page these headers add.
SERVICES = "Marketing Services"
FUNDING, CAPITAL = "Business Funding", "COVERED BRIDGE CAPITAL"          # /funding
LOANS, HOME_LOANS = "Home Loans", "COVERED BRIDGE HOME LOANS"            # /home-loans
LEADS = "High Converting Leads"                                          # /data-list (menu and heading)

# Long labels: tighter spacing, labels on one line, and between the
# breakpoint and 1280px a slightly smaller logo and link text.
TIGHT = """  /* ---- Long labels: tighter spacing so everything fits on one line ---- */
  .cbb-header .cbb-header__list {
    gap: clamp(18px, 1.9vw, 36px);
  }
  .cbb-header .cbb-header__link {
    white-space: nowrap;
  }
  @media (max-width: 1280px) {
    .cbb-header .cbb-header__logo {
      height: clamp(46px, 4.2vw, 54px);
    }
    .cbb-header .cbb-header__link {
      font-size: 0.875rem;
    }
  }

"""

HOME_BP, CAP_BP = 1150, 920  # mobile menu at this width and below

# ---------- Home header ----------
home = variant(
    "cbb-hh",
    intro=f"""     CBB — HEADER / NAVIGATION (HOME PAGE ONLY)
     Use this on the Home page in place of sections/00-header.html.
     Every other page keeps sections/00-header.html.
     Paste into a GoHighLevel Custom HTML/JavaScript element.
     All styles are scoped to .cbb-hh; the script only touches
     elements inside .cbb-hh.

     Links: Home, Marketing Services (/services), Business Funding
     (/funding), Home Loans (/home-loans), High Converting Leads
     (/data-list), About, Contact. With seven links the menu switches
     to the mobile (hamburger) menu at __HOME_BP__px and below.
""",
    note=BASE_NAV_NOTE,
    links=[("/", "Home"), ("/services", SERVICES), ("/funding", FUNDING), ("/home-loans", LOANS),
           ("/data-list", LEADS), ("/about", "About"), ("/contact", "Contact")],
    extra_css=TIGHT,
    breakpoint=HOME_BP,
).replace("__HOME_BP__", str(HOME_BP))
(root / "sections/00-header-home.html").write_text(home, encoding="utf-8")

# ---------- /funding, /home-loans and /data-list header ----------
cap = variant(
    "cbb-hc",
    intro=f"""     CBB — HEADER / NAVIGATION (FUNDING, HOME LOANS AND LEADS PAGES)
     Use this on /funding, /home-loans and /data-list in place of
     sections/00-header.html. The same block works on all three.
     Paste into a GoHighLevel Custom HTML/JavaScript element.
     All styles are scoped to .cbb-hc; the script only touches
     elements inside .cbb-hc.

     Links: Marketing Services (the main site's /services), Business
     Funding (/funding), Home Loans (/home-loans), High Converting
     Leads (/data-list). The menu switches to the mobile (hamburger)
     menu at __CAP_BP__px and below. The link for the page you're
     on is highlighted in gold with an underline, picked from the page
     address. GHL's editor preview uses a different address, so the
     highlight only shows on the published pages.
""",
    note="""        <!-- The current page's link stays gold with an underline and is
             tagged for screen readers (aria-current), picked from the URL. -->
""",
    links=[("https://coveredbridgebrands.com/services", SERVICES), ("/funding", FUNDING),
           ("/home-loans", LOANS), ("/data-list", LEADS)],
    breakpoint=CAP_BP,
    extra_css=TIGHT + """  /* ---- Current page: gold text with the underline showing ---- */
  .cbb-header .cbb-header__link[aria-current="page"] {
    color: var(--cbb-gold);
    font-weight: 500;
  }
  .cbb-header .cbb-header__link[aria-current="page"]::after {
    transform: scaleX(1);
  }

""",
    logo_href="https://coveredbridgebrands.com/",
).replace("__CAP_BP__", str(CAP_BP))
# The Marketing Services link is a full URL, so match on each link's path
# rather than its href.
old_match = "        var path = clean(a.getAttribute('href'));\n"
assert cap.count(old_match) == 1
cap = cap.replace(old_match, "        var path = clean(a.pathname);\n")
(root / "sections/00-header-capital.html").write_text(cap, encoding="utf-8")

# ---------- Coming Soon bodies ----------
SOON = """<!-- ============================================================
     CBB — __TITLE__: COMING SOON  (page: __PATH__)
     Paste into a GoHighLevel Custom HTML/JavaScript element, between
     sections/00-header-capital.html and sections/06-footer.html.
     All styles are scoped to .__ROOT__. No script.
     ============================================================ -->
<style>
  .__ROOT__ {
    --cbb-gold: #D5A756;
    --cbb-gold-light: #F3CF7C;
    --cbb-gold-deep: #C9994A;
    --cbb-black: #0A0B0C;
    --cbb-surface: #121415;
    --cbb-cream: #F6EFE3;
    --cbb-muted: #B9BEC4;
    --cbb-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
    --cbb-sans: 'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif;

    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: clamp(480px, 72vh, 760px);
    margin: 0;
    padding: clamp(72px, 9vw, 120px) clamp(20px, 4vw, 48px);
    background:
      radial-gradient(55% 60% at 50% 42%, rgba(213, 167, 86, 0.16), rgba(213, 167, 86, 0) 70%),
      linear-gradient(180deg, #0D0E0E 0%, #15130F 55%, #0A0B0C 100%);
    color: var(--cbb-cream);
    font-family: var(--cbb-sans);
    text-align: center;
    overflow: hidden;
  }
  .__ROOT__,
  .__ROOT__ *,
  .__ROOT__ *::before,
  .__ROOT__ *::after {
    box-sizing: border-box;
  }
  .__ROOT__ .__P____inner {
    width: 100%;
    max-width: 860px;
    margin: 0 auto;
  }
  .__ROOT__ .__P____eyebrow {
    margin: 0 0 18px;
    padding: 0;
    font-family: var(--cbb-sans);
    font-size: clamp(0.75rem, 0.3vw + 0.66rem, 0.875rem);
    font-weight: 500;
    line-height: 1.6;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    color: var(--cbb-gold);
  }
  .__ROOT__ .__P____title {
    margin: 0;
    padding: 0;
    font-family: var(--cbb-serif);
    font-size: __SIZE__;
    font-weight: 600;
    line-height: 1.12;
    letter-spacing: __TRACK__;
    text-transform: none;
    overflow-wrap: break-word;
    color: var(--cbb-gold);
    background: linear-gradient(180deg, var(--cbb-gold-light) 0%, var(--cbb-gold) 55%, var(--cbb-gold-deep) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .__ROOT__ .__P____rule {
    display: block;
    width: 64px;
    height: 1px;
    margin: clamp(24px, 2.6vw, 32px) auto;
    background: linear-gradient(90deg, rgba(213, 167, 86, 0), var(--cbb-gold), rgba(213, 167, 86, 0));
  }
  .__ROOT__ .__P____status {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin: 0;
    padding: 11px 20px;
    border-radius: 2px;
    background: linear-gradient(135deg, var(--cbb-gold-deep), var(--cbb-gold-light));
    color: var(--cbb-black);
    font-family: var(--cbb-sans);
    font-size: 0.8125rem;
    font-weight: 700;
    line-height: 1;
    letter-spacing: 0.22em;
    text-transform: uppercase;
  }
  .__ROOT__ .__P____dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--cbb-black);
    animation: __P__-pulse 1.8s ease-in-out infinite;
  }
  @keyframes __P__-pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.25; }
  }
  .__ROOT__ .__P____note {
    margin: clamp(28px, 3vw, 36px) 0 0;
    padding: 0;
    font-family: var(--cbb-sans);
    font-size: 0.9375rem;
    line-height: 1.6;
    color: rgba(246, 239, 227, 0.78);
  }
  .__ROOT__ .__P____link {
    color: var(--cbb-gold);
    text-decoration: none;
    white-space: nowrap;
  }
  .__ROOT__ .__P____link:hover {
    color: var(--cbb-gold-light);
  }
  .__ROOT__ .__P____link:focus-visible {
    outline: 2px solid var(--cbb-gold-light);
    outline-offset: 3px;
  }
  @media (prefers-reduced-motion: reduce) {
    .__ROOT__ .__P____dot {
      animation: none;
    }
  }
</style>

<section class="__ROOT__" aria-labelledby="__P__-title">
  <div class="__P____inner">
    <p class="__P____eyebrow">Covered Bridge Brands</p>
    <h1 class="__P____title" id="__P__-title">__TITLE__</h1>
    <span class="__P____rule" aria-hidden="true"></span>
    <p class="__P____status"><span class="__P____dot" aria-hidden="true"></span>Coming Soon</p>
    <p class="__P____note">
      Questions in the meantime? Call or text
      <a class="__P____link" href="tel:+18148931075">814-893-1075</a>.
    </p>
  </div>
</section>
"""


def soon(rootcls, title, path, size, track):
    out = SOON.replace("__ROOT__", rootcls).replace("__P__", rootcls)
    return (out.replace("__TITLE__", title).replace("__PATH__", path)
               .replace("__SIZE__", size).replace("__TRACK__", track))


# The two brand headings are set in capitals, so they use a smaller size and
# slight tracking; they wrap onto two lines on phones.
# /funding and /home-loans now use full overview pages (scripts/build-overviews.py).
(root / "pages/data-list").mkdir(exist_ok=True)
(root / "pages/data-list/01-data-list-soon.html").write_text(
    soon("cbb-dsoon", LEADS, "/data-list", "clamp(2.25rem, 3.8vw + 1rem, 4.5rem)", "-0.01em"), encoding="utf-8")

print("Wrote sections/00-header-home.html, sections/00-header-capital.html,")
print("      pages/data-list/01-data-list-soon.html")
