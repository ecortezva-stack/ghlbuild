#!/usr/bin/env python3
"""Build the two short business introduction pages.

Writes:
  pages/home-loans/cbb-home-loans-overview.html  CBB Home Loans (.cbb-hlo)
  pages/funding/cbb-capital-overview.html        Covered Bridge Capital (.cbb-cap)

Each is one concise section: business name, headline, short intro, three
highlights and one button to that business's standalone website, written
as a REPLACE_WITH_... value until the address exists. Both share the
layout and stylesheet below, scoped to each page's own root class.

Run:  python3 scripts/build-overviews.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent


def bridge_svg():
    """Decorative truss-arch line drawing (aria-hidden)."""
    lines = ['<path d="M10 230 Q260 20 510 230" />', '<path d="M0 230 H520" />']
    for x in range(60, 461, 50):
        t = (x - 10) / 500
        y = 230 * (1 - t) ** 2 + 40 * (1 - t) * t + 230 * t ** 2
        lines.append(f'<path d="M{x} 230 V{y:.1f}" />')
    body = "\n    ".join(lines)
    return (f'<svg class="__R____art" viewBox="0 0 520 240" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" aria-hidden="true" focusable="false">\n    {body}\n  </svg>')


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

    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    min-height: clamp(560px, 78vh, 820px);
    margin: 0;
    padding: clamp(80px, 10vw, 136px) clamp(20px, 4vw, 48px);
    background:
      radial-gradient(55% 70% at 85% 15%, rgba(210, 163, 76, 0.14), rgba(210, 163, 76, 0) 65%),
      linear-gradient(180deg, #0D0D0D 0%, #111417 100%);
    color: var(--__R__-text);
    font-family: var(--__R__-sans);
    font-size: 16px;
    line-height: 1.6;
    text-align: left;
    overflow: hidden;
  }
  .__R__,
  .__R__ *,
  .__R__ *::before,
  .__R__ *::after {
    box-sizing: border-box;
  }
  .__R__ .__R____inner {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: minmax(0, 7fr) minmax(0, 5fr);
    gap: clamp(40px, 7vw, 112px);
    align-items: center;
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
  }

  /* ---------- Name, headline, intro ---------- */
  .__R__ .__R____h1 {
    margin: 0;
    padding: 0;
    font-weight: 400;
    text-transform: none;
  }
  .__R__ .__R____name {
    display: block;
    margin: 0 0 20px;
    font-family: var(--__R__-sans);
    font-size: clamp(0.8125rem, 0.25vw + 0.75rem, 0.9375rem);
    font-weight: 600;
    line-height: 1.5;
    letter-spacing: 0.26em;
    text-transform: uppercase;
    color: var(--__R__-gold);
  }
  .__R__ .__R____headline {
    display: block;
    font-family: var(--__R__-serif);
    font-size: clamp(2.5rem, 3.8vw + 1rem, 4.5rem);
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
    margin: 0 0 clamp(32px, 4vw, 40px);
    padding: 0;
    font-size: clamp(1.0625rem, 0.4vw + 0.98rem, 1.25rem);
    line-height: 1.7;
    color: rgba(242, 240, 235, 0.9);
  }

  /* ---------- Button ---------- */
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
  .__R__ .__R____fine {
    max-width: 36em;
    margin: 18px 0 0;
    padding: 0;
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

  /* ---------- Decoration ---------- */
  .__R__ .__R____art {
    position: absolute;
    right: 0;
    bottom: -2px;
    z-index: 0;
    width: clamp(320px, 42vw, 620px);
    height: auto;
    color: var(--__R__-gold);
    opacity: 0.16;
    pointer-events: none;
  }

  /* ---------- Responsive ---------- */
  @media (max-width: 900px) {
    .__R__ {
      min-height: 0;
    }
    .__R__ .__R____inner {
      grid-template-columns: minmax(0, 1fr);
    }
    .__R__ .__R____art {
      opacity: 0.1;
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


def build(r, name, path, url, label, headline, intro, highlights, fine):
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

     >>> URL TO REPLACE BEFORE PUBLISHING (1 place: the button)
         {url}
         Replace it with the full https:// address of the standalone
         {name} website.
     ============================================================ -->
{CSS}
<section class="__R__" aria-labelledby="__R__-title">
  {bridge_svg()}
  <div class="__R____inner">
    <div>
      <h1 class="__R____h1" id="__R__-title">
        <span class="__R____name">{name}</span>
        <span class="__R____headline">{headline}</span>
      </h1>
      <span class="__R____rule" aria-hidden="true"></span>
      <p class="__R____intro">{intro}</p>
      <!-- Button destination: {url} -->
      <a class="__R____btn" href="{url}">
        {label}
        {ARROW}
      </a>{fine_html}
    </div>
    <ul class="__R____list" aria-label="What {name} offers">
{items}
    </ul>
  </div>
</section>
"""
    html = html.replace("__R__", r)
    assert html.count(f'href="{url}"') == 1 and "Trulli" not in html and "__" + "R" not in html
    return html


PAGES = [
    dict(
        out="pages/home-loans/cbb-home-loans-overview.html",
        r="cbb-hlo", name="CBB Home Loans", path="/home-loans",
        url="REPLACE_WITH_CBB_HOME_LOANS_WEBSITE_URL",
        label="Visit CBB Home Loans",
        headline="Your path home, guided every step of the way.",
        intro=("Whether you're buying a home or refinancing the one you have, CBB Home Loans "
               "explains your options in plain language and helps you move forward with confidence."),
        highlights=[
            ("Home purchase &amp; refinancing",
             "Financing for your first home, your next move or a mortgage that better fits your life today."),
            ("Conventional, FHA, VA &amp; USDA loans",
             "A range of loan programs, explained so you can compare them clearly."),
            ("Guidance from start to finish",
             "Help preparing your documents and answers to your questions throughout the process."),
        ],
        fine="",
    ),
    dict(
        out="pages/funding/cbb-capital-overview.html",
        r="cbb-cap", name="Covered Bridge Capital", path="/funding",
        url="REPLACE_WITH_COVERED_BRIDGE_CAPITAL_WEBSITE_URL",
        label="Visit Covered Bridge Capital",
        headline="Capital to build, grow and invest.",
        intro=("Covered Bridge Capital helps business owners and real estate investors explore "
               "financing for what comes next, from steadier cash flow to new equipment or your next investment property."),
        highlights=[
            ("Working capital &amp; lines of credit",
             "Flexible funding for payroll, inventory, growth and the gaps in between."),
            ("Equipment financing",
             "Financing for the vehicles, machinery and tools your business runs on."),
            ("Investment-property financing",
             "Options for rental, renovation and construction projects, short-term bridge needs and growing a portfolio."),
        ],
        fine="All financing is subject to program requirements and underwriting approval.",
    ),
]

for pg in PAGES:
    out = pg.pop("out")
    (root / out).write_text(build(**pg), encoding="utf-8")
    print("Wrote", out)
