#!/usr/bin/env python3
"""Build the two short business introduction pages.

Writes:
  pages/home-loans/cbb-home-loans-overview.html  CBB Home Loans (.cbb-hlo)
  pages/funding/cbb-capital-overview.html        Covered Bridge Capital (.cbb-cap)

Both use one layout: a COVERED BRIDGE BRANDS eyebrow, the business name,
a headline, a short intro, three highlights and one button to that
business's standalone website, with a supporting line (and, for Capital,
a disclaimer) under it. The button's destination is a REPLACE_WITH_...
value until the real address exists. The stylesheet is shared and scoped
to each page's own root class. The visible copy is the approved wording;
change it only in PAGES below.

Run:  python3 scripts/build-overviews.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent

CSS = """<style>
  .__R__ {
    --__R__-bg: #0D0D0D;
    --__R__-surface: #121619;
    --__R__-gold: #D2A34C;
    --__R__-gold-hover: #EAC266;
    --__R__-text: #F2F0EB;
    --__R__-muted: #BFBAAB;
    --__R__-line: rgba(210, 163, 76, 0.25);
    --__R__-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
    --__R__-sans: 'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif;

    display: block;
    width: 100%;
    margin: 0;
    padding: clamp(72px, 9vw, 128px) clamp(20px, 4vw, 48px);
    background:
      radial-gradient(55% 70% at 85% 10%, rgba(210, 163, 76, 0.12), rgba(210, 163, 76, 0) 65%),
      linear-gradient(180deg, var(--__R__-bg) 0%, var(--__R__-surface) 100%);
    color: var(--__R__-text);
    font-family: var(--__R__-sans);
    font-size: 16px;
    line-height: 1.6;
    text-align: left;
    overflow-x: hidden;
  }
  .__R__,
  .__R__ *,
  .__R__ *::before,
  .__R__ *::after {
    box-sizing: border-box;
  }
  .__R__ .__R____inner {
    display: grid;
    grid-template-columns: minmax(0, 7fr) minmax(0, 5fr);
    gap: clamp(40px, 7vw, 112px);
    align-items: center;
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
  }

  /* ---------- Eyebrow, name, headline, intro ---------- */
  .__R__ .__R____eyebrow {
    margin: 0 0 18px;
    padding: 0;
    font-family: var(--__R__-sans);
    font-size: 0.8125rem;
    font-weight: 500;
    line-height: 1.5;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--__R__-gold);
  }
  .__R__ .__R____name {
    margin: 0 0 14px;
    padding: 0;
    font-family: var(--__R__-serif);
    font-size: clamp(1.5rem, 1vw + 1.15rem, 2rem);
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: 0.005em;
    text-transform: none;
    color: var(--__R__-gold);
  }
  .__R__ .__R____headline {
    margin: 0;
    padding: 0;
    font-family: var(--__R__-serif);
    font-size: clamp(2.5rem, 3.6vw + 1rem, 4.25rem);
    font-weight: 600;
    line-height: 1.08;
    letter-spacing: -0.01em;
    color: var(--__R__-text);
  }
  .__R__ .__R____rule {
    display: block;
    width: 64px;
    height: 1px;
    margin: clamp(24px, 3vw, 32px) 0;
    background: linear-gradient(90deg, var(--__R__-gold), rgba(210, 163, 76, 0));
  }
  .__R__ .__R____intro {
    max-width: 36em;
    margin: 0 0 clamp(30px, 3.6vw, 38px);
    padding: 0;
    font-size: clamp(1.0625rem, 0.35vw + 0.98rem, 1.1875rem);
    line-height: 1.7;
    color: rgba(242, 240, 235, 0.9);
  }

  /* ---------- Button and the lines beneath it ---------- */
  .__R__ .__R____btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    min-height: 56px;
    margin: 0;
    padding: 0 32px;
    border: 0;
    border-radius: 3px;
    background: var(--__R__-gold);
    color: #0D0D0D;
    font-family: var(--__R__-sans);
    font-size: 1.0625rem;
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: 0.01em;
    text-align: center;
    text-decoration: none;
    text-transform: none;
    transition: background-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
  }
  .__R__ .__R____btn svg {
    width: 18px;
    height: 18px;
    flex: 0 0 18px;
  }
  .__R__ .__R____btn:hover {
    background: var(--__R__-gold-hover);
    color: #0D0D0D;
    transform: translateY(-1px);
    box-shadow: 0 10px 28px rgba(210, 163, 76, 0.25);
  }
  .__R__ .__R____btn:focus-visible {
    outline: 2px solid var(--__R__-gold-hover);
    outline-offset: 4px;
  }
  .__R__ .__R____support {
    max-width: 36em;
    margin: 16px 0 0;
    padding: 0;
    font-size: 0.9375rem;
    line-height: 1.6;
    color: var(--__R__-muted);
  }
  .__R__ .__R____fine {
    max-width: 36em;
    margin: 20px 0 0;
    padding: 16px 0 0;
    border-top: 1px solid rgba(191, 186, 171, 0.18);
    font-size: 0.875rem;
    line-height: 1.6;
    color: var(--__R__-muted);
  }

  /* ---------- Highlights ---------- */
  .__R__ .__R____list {
    margin: 0;
    padding: 0;
    list-style: none;
    border-bottom: 1px solid var(--__R__-line);
  }
  .__R__ .__R____item {
    display: grid;
    grid-template-columns: 2.25rem minmax(0, 1fr);
    gap: 14px;
    margin: 0;
    padding: clamp(22px, 2.6vw, 28px) 0;
    border-top: 1px solid var(--__R__-line);
  }
  .__R__ .__R____item::marker {
    content: none;
  }
  .__R__ .__R____num {
    font-family: var(--__R__-serif);
    font-size: 1.25rem;
    font-weight: 600;
    line-height: 1.3;
    color: var(--__R__-gold);
  }
  .__R__ .__R____h2 {
    margin: 0 0 6px;
    padding: 0;
    font-family: var(--__R__-sans);
    font-size: 1.125rem;
    font-weight: 600;
    line-height: 1.35;
    letter-spacing: 0;
    text-transform: none;
    color: var(--__R__-text);
  }
  .__R__ .__R____p {
    margin: 0;
    padding: 0;
    font-size: 1rem;
    line-height: 1.65;
    color: var(--__R__-muted);
  }

  /* ---------- Responsive ---------- */
  @media (max-width: 900px) {
    .__R__ .__R____inner {
      grid-template-columns: minmax(0, 1fr);
    }
  }
  @media (max-width: 480px) {
    .__R__ .__R____btn {
      display: flex;
      width: 100%;
      padding: 0 20px;
    }
  }
  @media (prefers-reduced-motion: reduce) {
    .__R__ .__R____btn {
      transition: none;
    }
    .__R__ .__R____btn:hover {
      transform: none;
    }
  }
</style>
"""

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')


def build(r, name, path, url, label, headline, intro, highlights, support, fine):
    items = "\n".join(f"""        <li class="__R____item">
          <span class="__R____num" aria-hidden="true">{i:02d}</span>
          <div>
            <h2 class="__R____h2">{t}</h2>
            <p class="__R____p">{p}</p>
          </div>
        </li>""" for i, (t, p) in enumerate(highlights, 1))
    fine_html = f'\n      <p class="__R____fine">{fine}</p>' if fine else ""
    html = f"""<!-- ============================================================
     {name.upper()} — INTRODUCTION PAGE BODY  (page: {path})
     Paste into one GoHighLevel Custom HTML/JavaScript element,
     between sections/00-header-capital.html and
     sections/06-footer.html. Section: full width, 0 padding, no
     background. All styles are scoped to .{r}. No script.

     >>> URL TO REPLACE BEFORE PUBLISHING (1 place: the button below)
         {url}
         Placeholder for the standalone {name} website, which
         doesn't have its address yet. Replace it with the full
         https:// address.
     ============================================================ -->
{CSS}
<section class="__R__" aria-labelledby="__R__-title">
  <div class="__R____inner">
    <div>
      <p class="__R____eyebrow">Covered Bridge Brands</p>
      <h1 class="__R____name" id="__R__-title">{name}</h1>
      <p class="__R____headline">{headline}</p>
      <span class="__R____rule" aria-hidden="true"></span>
      <p class="__R____intro">{intro}</p>
      <!-- WEBSITE BUTTON: replace {url} -->
      <a class="__R____btn" href="{url}">
        {label}
        {ARROW}
      </a>
      <p class="__R____support">{support}</p>{fine_html}
    </div>
    <ul class="__R____list" aria-label="What {name} offers">
{items}
    </ul>
  </div>
</section>
"""
    html = html.replace("__R__", r)
    assert html.count(f'href="{url}"') == 1 and "__" + "R" not in html
    for banned in ("Trulli", "Valor", "Coming Soon", "Scout", "Floify"):
        assert banned.lower() not in html.lower(), banned
    return html


PAGES = [
    dict(
        out="pages/home-loans/cbb-home-loans-overview.html",
        r="cbb-hlo", name="CBB Home Loans", path="/home-loans",
        url="REPLACE_WITH_CBB_HOME_LOANS_WEBSITE_URL",
        label="Visit CBB Home Loans",
        headline="Your next chapter starts at home.",
        intro=("Whether you&rsquo;re buying your first home, making your next move or exploring "
               "refinancing, CBB Home Loans helps you understand your options and take the next "
               "step with confidence."),
        highlights=[
            ("Purchase &amp; Refinance",
             "Explore financing for a home purchase or refinancing your current mortgage."),
            ("A Range of Loan Options",
             "Conventional, FHA, VA and USDA loan options."),
            ("Guidance Along the Way",
             "Get help understanding loan options, preparing documents and navigating the process."),
        ],
        support="Explore loan options and connect with the team on our dedicated website.",
        fine="",
    ),
    dict(
        out="pages/funding/cbb-capital-overview.html",
        r="cbb-cap", name="Covered Bridge Capital", path="/funding",
        url="REPLACE_WITH_COVERED_BRIDGE_CAPITAL_WEBSITE_URL",
        label="Visit Covered Bridge Capital",
        headline="Capital for your next move.",
        intro=("From managing cash flow to investing in equipment or real estate, Covered Bridge "
               "Capital helps business owners and investors explore financing options that fit "
               "their goals."),
        highlights=[
            ("Working Capital &amp; Credit",
             "Explore working capital, business lines of credit and term financing."),
            ("Equipment &amp; Business Growth",
             "Discover equipment, asset-backed and SBA financing options."),
            ("Real Estate Investment",
             "Explore financing for investment properties, commercial real estate and construction."),
        ],
        support="Explore financing options and connect with the team on our dedicated website.",
        fine=("Financing is subject to applicable program requirements and underwriting approval. "
              "Availability and terms vary."),
    ),
]

for pg in PAGES:
    out = pg.pop("out")
    (root / out).write_text(build(**pg), encoding="utf-8")
    print("Wrote", out)
