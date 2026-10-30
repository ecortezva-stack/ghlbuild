#!/usr/bin/env python3
"""Build the two business overview pages.

Writes:
  pages/home-loans/cbb-home-loans-overview.html  CBB Home Loans (.cbb-hlo)
  pages/funding/cbb-capital-overview.html        Covered Bridge Capital (.cbb-cap)

Both share one layout and stylesheet (below), scoped to each page's own
root class. Each page's main button goes to that business's standalone
website, written as a REPLACE_WITH_... value until the address exists.

Run:  python3 scripts/build-overviews.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent


def bridge_svg():
    """Decorative truss-arch line drawing for the hero (aria-hidden)."""
    lines = ['<path d="M10 230 Q260 20 510 230" />', '<path d="M0 230 H520" />']
    for x in range(60, 461, 50):
        t = (x - 10) / 500
        y = 230 * (1 - t) ** 2 + 40 * (1 - t) * t + 230 * t ** 2
        lines.append(f'<path d="M{x} 230 V{y:.1f}" />')
    body = "\n      ".join(lines)
    return (f'<svg class="__R____art" viewBox="0 0 520 240" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" aria-hidden="true" focusable="false">\n      {body}\n    </svg>')


CSS = """<style>
  .__R__ {
    --__R__-bg: #0D0D0D;
    --__R__-surface: #121619;
    --__R__-gold: #D2A34C;
    --__R__-gold-hover: #EAC266;
    --__R__-text: #F2F0EB;
    --__R__-muted: #BFBAAB;
    --__R__-line: rgba(210, 163, 76, 0.22);
    --__R__-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
    --__R__-sans: 'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif;
    --__R__-gutter: clamp(20px, 4vw, 48px);

    display: block;
    width: 100%;
    margin: 0;
    padding: 0;
    background: var(--__R__-bg);
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

  /* ---------- Layout ---------- */
  .__R__ .__R____section {
    position: relative;
    margin: 0;
    padding: clamp(64px, 8vw, 112px) var(--__R__-gutter);
    scroll-margin-top: 100px; /* clears the fixed site header */
  }
  .__R__ .__R____section--surface {
    background: var(--__R__-surface);
  }
  .__R__ .__R____inner {
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
  }
  .__R__ .__R____header {
    max-width: 760px;
    margin: 0 0 clamp(36px, 5vw, 60px);
  }

  /* ---------- Type ---------- */
  .__R__ .__R____eyebrow {
    margin: 0 0 18px;
    padding: 0;
    font-family: var(--__R__-sans);
    font-size: 0.8125rem;
    font-weight: 500;
    line-height: 1.5;
    letter-spacing: 0.26em;
    text-transform: uppercase;
    color: var(--__R__-gold);
  }
  .__R__ .__R____h1 {
    margin: 0 0 24px;
    padding: 0;
    font-family: var(--__R__-serif);
    font-size: clamp(2.75rem, 4.6vw + 1rem, 5rem);
    font-weight: 600;
    line-height: 1.05;
    letter-spacing: -0.01em;
    text-transform: none;
    color: var(--__R__-text);
  }
  .__R__ .__R____h2 {
    margin: 0 0 18px;
    padding: 0;
    font-family: var(--__R__-serif);
    font-size: clamp(2rem, 2.2vw + 1.2rem, 3rem);
    font-weight: 600;
    line-height: 1.15;
    letter-spacing: -0.005em;
    text-transform: none;
    color: var(--__R__-text);
  }
  .__R__ .__R____h3 {
    margin: 0 0 8px;
    padding: 0;
    font-family: var(--__R__-sans);
    font-size: 1.125rem;
    font-weight: 600;
    line-height: 1.35;
    letter-spacing: 0;
    text-transform: none;
    color: var(--__R__-text);
  }
  .__R__ .__R____lede {
    max-width: 40em;
    margin: 0 0 36px;
    padding: 0;
    font-size: clamp(1.0625rem, 0.4vw + 0.98rem, 1.25rem);
    line-height: 1.7;
    color: rgba(242, 240, 235, 0.9);
  }
  .__R__ .__R____p {
    margin: 0 0 16px;
    padding: 0;
    font-size: 1.0625rem;
    line-height: 1.75;
    color: var(--__R__-muted);
  }
  .__R__ .__R____p:last-child {
    margin-bottom: 0;
  }
  .__R__ .__R____item .__R____p {
    font-size: 1rem;
    line-height: 1.7;
  }
  .__R__ .__R____fine {
    max-width: 72ch;
    margin: clamp(32px, 4vw, 44px) 0 0;
    padding: 0;
    font-size: 0.875rem;
    line-height: 1.65;
    color: var(--__R__-muted);
  }

  /* ---------- Buttons ---------- */
  .__R__ .__R____actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 14px 18px;
    margin: 0;
  }
  .__R__ .__R____btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    min-height: 54px;
    margin: 0;
    padding: 0 30px;
    border: 1px solid transparent;
    border-radius: 3px;
    font-family: var(--__R__-sans);
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: 0.01em;
    text-align: center;
    text-decoration: none;
    text-transform: none;
    cursor: pointer;
    transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
  }
  .__R__ .__R____btn svg {
    width: 18px;
    height: 18px;
    flex: 0 0 18px;
  }
  .__R__ .__R____btn--gold {
    background: var(--__R__-gold);
    color: #0D0D0D;
  }
  .__R__ .__R____btn--gold:hover {
    background: var(--__R__-gold-hover);
    color: #0D0D0D;
    transform: translateY(-1px);
    box-shadow: 0 10px 28px rgba(210, 163, 76, 0.25);
  }
  .__R__ .__R____btn--ghost {
    background: transparent;
    border-color: rgba(210, 163, 76, 0.6);
    color: var(--__R__-text);
  }
  .__R__ .__R____btn--ghost:hover {
    border-color: var(--__R__-gold-hover);
    color: var(--__R__-gold-hover);
  }
  .__R__ .__R____btn:focus-visible {
    outline: 2px solid var(--__R__-gold-hover);
    outline-offset: 3px;
  }
  .__R__ .__R____note {
    margin: 20px 0 0;
    padding: 0;
    font-size: 0.875rem;
    line-height: 1.6;
    color: var(--__R__-muted);
  }

  /* ---------- 1. Hero ---------- */
  .__R__ .__R____hero {
    position: relative;
    margin: 0;
    padding: clamp(88px, 11vw, 150px) var(--__R__-gutter) clamp(72px, 9vw, 120px);
    background:
      radial-gradient(55% 75% at 88% 10%, rgba(210, 163, 76, 0.14), rgba(210, 163, 76, 0) 65%),
      linear-gradient(180deg, #0D0D0D 0%, #101316 100%);
    border-bottom: 1px solid var(--__R__-line);
    overflow: hidden;
  }
  .__R__ .__R____hero .__R____inner {
    position: relative;
    z-index: 1;
  }
  .__R__ .__R____hero-copy {
    max-width: 760px;
  }
  .__R__ .__R____rule {
    display: block;
    width: 64px;
    height: 1px;
    margin: 0 0 28px;
    background: linear-gradient(90deg, var(--__R__-gold), rgba(210, 163, 76, 0));
  }
  .__R__ .__R____art {
    position: absolute;
    right: clamp(-40px, -2vw, 0px);
    bottom: -2px;
    z-index: 0;
    width: clamp(320px, 40vw, 600px);
    height: auto;
    color: var(--__R__-gold);
    opacity: 0.28;
    pointer-events: none;
  }

  /* ---------- 2. Introduction ---------- */
  .__R__ .__R____intro {
    display: grid;
    grid-template-columns: minmax(0, 5fr) minmax(0, 6fr);
    gap: clamp(32px, 6vw, 96px);
    align-items: start;
  }
  .__R__ .__R____points {
    margin: 0;
    padding: 0;
    list-style: none;
    border-bottom: 1px solid var(--__R__-line);
  }
  .__R__ .__R____points > li {
    margin: 0;
    padding: 24px 0;
    border-top: 1px solid var(--__R__-line);
  }
  .__R__ .__R____points > li::marker {
    content: none;
  }

  /* ---------- 3. Options / categories ---------- */
  .__R__ .__R____grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0 clamp(32px, 5vw, 72px);
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .__R__ .__R____item {
    display: grid;
    grid-template-columns: 2.5rem minmax(0, 1fr);
    gap: 16px;
    margin: 0;
    padding: 28px 0;
    border-top: 1px solid var(--__R__-line);
  }
  .__R__ .__R____item::marker {
    content: none;
  }
  .__R__ .__R____num {
    font-family: var(--__R__-serif);
    font-size: 1.25rem;
    font-weight: 600;
    line-height: 1.35;
    color: var(--__R__-gold);
  }

  /* ---------- 4. Steps ---------- */
  .__R__ .__R____steps {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(28px, 4vw, 56px);
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .__R__ .__R____step {
    margin: 0;
    padding: 28px 0 0;
    border-top: 1px solid rgba(210, 163, 76, 0.55);
  }
  .__R__ .__R____step::marker {
    content: none;
  }
  .__R__ .__R____step-num {
    display: block;
    margin: 0 0 14px;
    font-family: var(--__R__-serif);
    font-size: 2.25rem;
    font-weight: 600;
    line-height: 1;
    color: var(--__R__-gold);
  }

  /* ---------- 5. Closing CTA ---------- */
  .__R__ .__R____cta {
    text-align: center;
    background:
      radial-gradient(50% 80% at 50% 0%, rgba(210, 163, 76, 0.12), rgba(210, 163, 76, 0) 70%),
      var(--__R__-surface);
    border-top: 1px solid var(--__R__-line);
  }
  .__R__ .__R____cta .__R____inner {
    max-width: 760px;
  }
  .__R__ .__R____cta .__R____lede {
    margin-left: auto;
    margin-right: auto;
  }
  .__R__ .__R____cta .__R____actions {
    justify-content: center;
  }

  /* ---------- Responsive ---------- */
  @media (max-width: 1150px) {
    .__R__ .__R____section {
      scroll-margin-top: 84px;
    }
  }
  @media (max-width: 900px) {
    .__R__ .__R____intro {
      grid-template-columns: minmax(0, 1fr);
    }
    .__R__ .__R____steps {
      grid-template-columns: minmax(0, 1fr);
    }
    .__R__ .__R____art {
      opacity: 0.14;
    }
  }
  @media (max-width: 760px) {
    .__R__ .__R____grid {
      grid-template-columns: minmax(0, 1fr);
    }
  }
  @media (max-width: 480px) {
    .__R__ .__R____actions {
      flex-direction: column;
      align-items: stretch;
    }
    .__R__ .__R____btn {
      width: 100%;
      padding: 0 20px;
    }
    .__R__ .__R____item {
      grid-template-columns: 2rem minmax(0, 1fr);
      gap: 12px;
    }
  }
  @media (prefers-reduced-motion: reduce) {
    .__R__ .__R____btn {
      transition: none;
    }
    .__R__ .__R____btn--gold:hover {
      transform: none;
    }
  }
</style>
"""

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')


def page(r, header_comment, body):
    html = header_comment + CSS + "\n" + body
    html = html.replace("__ART__", bridge_svg()).replace("__ARROW__", ARROW)
    return html.replace("__R__", r)


def items(rows):
    out = []
    for i, (title, text) in enumerate(rows, 1):
        out.append(f"""          <li class="__R____item">
            <span class="__R____num" aria-hidden="true">{i:02d}</span>
            <div>
              <h3 class="__R____h3">{title}</h3>
              <p class="__R____p">{text}</p>
            </div>
          </li>""")
    return "\n".join(out)


def steps(rows):
    out = []
    for i, (title, text) in enumerate(rows, 1):
        out.append(f"""          <li class="__R____step">
            <span class="__R____step-num" aria-hidden="true">{i}</span>
            <h3 class="__R____h3">{title}</h3>
            <p class="__R____p">{text}</p>
          </li>""")
    return "\n".join(out)


def points(rows):
    return "\n".join(f"""          <li>
            <h3 class="__R____h3">{t}</h3>
            <p class="__R____p">{p}</p>
          </li>""" for t, p in rows)


# =====================================================================
# CBB Home Loans
# =====================================================================
HL_URL = "REPLACE_WITH_CBB_HOME_LOANS_WEBSITE_URL"
HL_BTN = f"""<a class="__R____btn __R____btn--gold" href="{HL_URL}">
            Visit the CBB Home Loans Website
            __ARROW__
          </a>"""

hl_comment = f"""<!-- ============================================================
     CBB HOME LOANS — OVERVIEW PAGE BODY  (page: /home-loans)
     Paste into one GoHighLevel Custom HTML/JavaScript element,
     between sections/00-header-capital.html and
     sections/06-footer.html. Section: full width, 0 padding, no
     background. All styles are scoped to .cbb-hlo. No script.

     >>> DESTINATION TO REPLACE BEFORE PUBLISHING
         {HL_URL}
         is the standalone CBB Home Loans website. It appears in
         the 2 "Visit the CBB Home Loans Website" buttons (top and
         bottom). Replace both with the full https:// address.
         Don't use #, a Coming Soon page, the Capital website or an
         application portal instead.

     >>> LICENSING: before publishing, add the approved NMLS /
         licensing disclosure where marked near the end of the
         loan options section. None is included here.
     ============================================================ -->
"""

hl_body = f"""<div class="__R__">

  <!-- 1. Hero -->
  <section class="__R____hero" aria-labelledby="__R__-title">
    __ART__
    <div class="__R____inner">
      <div class="__R____hero-copy">
        <p class="__R____eyebrow">Home Financing</p>
        <h1 class="__R____h1" id="__R__-title">CBB Home Loans</h1>
        <span class="__R____rule" aria-hidden="true"></span>
        <p class="__R____lede">
          Clear, personal guidance for buying a home or refinancing the one you have. We help you
          understand your loan options, get your documents in order and know what to expect at
          each step of the mortgage process.
        </p>
        <div class="__R____actions">
          {HL_BTN}
          <a class="__R____btn __R____btn--ghost" href="#__R__-options">Explore Loan Options</a>
        </div>
        <p class="__R____note">Applications and contact options are on the CBB Home Loans website.</p>
      </div>
    </div>
  </section>

  <!-- 2. How CBB Home Loans helps -->
  <section class="__R____section" aria-labelledby="__R__-about-title">
    <div class="__R____inner">
      <div class="__R____intro">
        <div>
          <p class="__R____eyebrow">How We Help</p>
          <h2 class="__R____h2" id="__R__-about-title">Guidance from first questions to closing</h2>
          <p class="__R____p">
            A mortgage is one of the biggest financial decisions most people make, and the process can
            feel unfamiliar. CBB Home Loans helps borrowers understand their choices before they commit,
            whether they're buying their first home, moving to their next one or refinancing.
          </p>
          <p class="__R____p">
            The goal is simple: you should know what you're signing up for, why a loan option may or may
            not suit you, and what comes next.
          </p>
        </div>
        <ul class="__R____points">
{points([
    ("Clear explanations of your options",
     "How each type of loan works, and the questions worth asking as you compare them."),
    ("Buyer education",
     "What to expect from the mortgage process, explained in plain language, so there are fewer surprises along the way."),
    ("Help preparing your documents",
     "Guidance on what to gather and how to organize it, so your information is ready when it's needed."),
    ("Support through each step",
     "A team to answer questions as your loan moves forward, from the first conversation to closing."),
])}
        </ul>
      </div>
    </div>
  </section>

  <!-- 3. Loan options -->
  <section class="__R____section __R____section--surface" id="__R__-options" aria-labelledby="__R__-options-title">
    <div class="__R____inner">
      <header class="__R____header">
        <p class="__R____eyebrow">Loan Options</p>
        <h2 class="__R____h2" id="__R__-options-title">Ways to finance your home</h2>
        <p class="__R____p">
          Every program has its own guidelines. The team can explain which options may fit your goals,
          your finances and the property you have in mind.
        </p>
      </header>
      <ul class="__R____grid">
{items([
    ("Home purchase",
     "Financing to buy a home, whether it's your first purchase or your next move."),
    ("Refinancing",
     "Replacing your current mortgage with a new loan that better fits where you are today."),
    ("Conventional loans",
     "Mortgages that aren't insured or guaranteed by a government agency."),
    ("FHA loans",
     "Loans insured by the Federal Housing Administration, often considered by buyers looking for a lower down payment or more flexible credit guidelines."),
    ("VA loans",
     "Loans guaranteed by the U.S. Department of Veterans Affairs for eligible veterans, service members and certain surviving spouses."),
    ("USDA loans",
     "Loans backed by the U.S. Department of Agriculture for eligible properties in qualifying rural and suburban areas, with income limits."),
    ("Down payment assistance",
     "Programs that may help eligible buyers with down payment or closing costs. What's available depends on the program and where you're buying."),
])}
      </ul>
      <p class="__R____fine">
        This is an overview, not an offer to lend or a commitment. Eligibility, terms and program
        availability depend on the loan program, your financial situation, the property and underwriting.
      </p>
      <!-- LICENSING: add the approved NMLS / licensing disclosure here before publishing, e.g.
      <p class="__R____fine">[approved disclosure text]</p> -->
    </div>
  </section>

  <!-- 4. Next steps -->
  <section class="__R____section" aria-labelledby="__R__-steps-title">
    <div class="__R____inner">
      <header class="__R____header">
        <p class="__R____eyebrow">Getting Started</p>
        <h2 class="__R____h2" id="__R__-steps-title">Your next steps</h2>
      </header>
      <ol class="__R____steps">
{steps([
    ("Explore your options",
     "Read about the loan programs and down payment assistance on the CBB Home Loans website."),
    ("Speak with the team",
     "Talk through your goals and questions. The team will explain the options that may fit and the documents you'll need."),
    ("Continue on the CBB Home Loans website",
     "When you're ready, apply and find every way to reach the team on the dedicated website."),
])}
      </ol>
    </div>
  </section>

  <!-- 5. Closing CTA -->
  <section class="__R____section __R____cta" aria-labelledby="__R__-cta-title">
    <div class="__R____inner">
      <p class="__R____eyebrow">CBB Home Loans</p>
      <h2 class="__R____h2" id="__R__-cta-title">Ready to explore your home financing options?</h2>
      <p class="__R____lede">
        Visit the CBB Home Loans website to learn more about each program, contact the team and apply
        when you're ready.
      </p>
      <div class="__R____actions">
        {HL_BTN}
      </div>
    </div>
  </section>

</div>
"""

# =====================================================================
# Covered Bridge Capital
# =====================================================================
CAP_URL = "REPLACE_WITH_COVERED_BRIDGE_CAPITAL_WEBSITE_URL"
CAP_BTN = f"""<a class="__R____btn __R____btn--gold" href="{CAP_URL}">
            Visit the Covered Bridge Capital Website
            __ARROW__
          </a>"""

cap_comment = f"""<!-- ============================================================
     COVERED BRIDGE CAPITAL — OVERVIEW PAGE BODY  (page: /funding)
     Paste into one GoHighLevel Custom HTML/JavaScript element,
     between sections/00-header-capital.html and
     sections/06-footer.html. Section: full width, 0 padding, no
     background. All styles are scoped to .cbb-cap. No script.

     >>> DESTINATION TO REPLACE BEFORE PUBLISHING
         {CAP_URL}
         is the standalone Covered Bridge Capital website. It
         appears in the 2 "Visit the Covered Bridge Capital Website"
         buttons (top and bottom). Replace both with the full
         https:// address. Don't use #, a Coming Soon page, the
         Home Loans website or an application portal instead.
     ============================================================ -->
"""

cap_body = f"""<div class="__R__">

  <!-- 1. Hero -->
  <section class="__R____hero" aria-labelledby="__R__-title">
    __ART__
    <div class="__R____inner">
      <div class="__R____hero-copy">
        <p class="__R____eyebrow">Business &amp; Real Estate Financing</p>
        <h1 class="__R____h1" id="__R__-title">Covered Bridge Capital</h1>
        <span class="__R____rule" aria-hidden="true"></span>
        <p class="__R____lede">
          Financing options for business owners and real estate investors. Covered Bridge Capital helps
          you explore the funding that fits what you're working toward, from day-to-day working capital
          and equipment to investment property.
        </p>
        <div class="__R____actions">
          {CAP_BTN}
          <a class="__R____btn __R____btn--ghost" href="#__R__-options">See Funding Options</a>
        </div>
        <p class="__R____note">Program details and next steps are on the Covered Bridge Capital website.</p>
      </div>
    </div>
  </section>

  <!-- 2. Who it serves -->
  <section class="__R____section" aria-labelledby="__R__-who-title">
    <div class="__R____inner">
      <div class="__R____intro">
        <div>
          <p class="__R____eyebrow">Who We Serve</p>
          <h2 class="__R____h2" id="__R__-who-title">Funding for businesses and investors</h2>
          <p class="__R____p">
            Whether you need flexible capital to keep operations running or financing for your next
            property, the right option depends on what the money is for, how quickly you need it and
            how you plan to repay it.
          </p>
          <p class="__R____p">
            Covered Bridge Capital helps you make sense of the choices, so you can focus on the programs
            that suit your situation.
          </p>
        </div>
        <ul class="__R____points">
{points([
    ("Business owners",
     "Companies looking for working capital, a line of credit, equipment, expansion funding or longer-term growth financing. Some programs are designed for newer businesses and startups."),
    ("Real estate investors",
     "Investors financing commercial property, rental property, renovation or construction projects, short-term bridge needs or a portfolio of properties."),
])}
        </ul>
      </div>
    </div>
  </section>

  <!-- 3. Funding categories -->
  <section class="__R____section __R____section--surface" id="__R__-options" aria-labelledby="__R__-options-title">
    <div class="__R____inner">
      <header class="__R____header">
        <p class="__R____eyebrow">Funding Options</p>
        <h2 class="__R____h2" id="__R__-options-title">Types of financing to explore</h2>
        <p class="__R____p">
          Each program has its own requirements, such as time in business, revenue and credit history,
          and they vary from one program to the next.
        </p>
      </header>
      <ul class="__R____grid">
{items([
    ("Business lines of credit",
     "A revolving credit line you can draw from as needs come up and repay over time. Useful for managing cash flow, seasonal swings and unexpected expenses."),
    ("SBA financing",
     "Loans made under U.S. Small Business Administration programs, often used for larger, longer-term needs such as expansion, acquisitions or owner-occupied real estate."),
    ("Working capital &amp; business term loans",
     "Lump-sum funding repaid over a set term, for inventory, payroll, hiring, marketing or a specific project. Some short-term products are priced with a factor rate, a fixed multiple of the amount funded, which isn't the same as an interest rate or APR."),
    ("Equipment &amp; asset-backed financing",
     "Financing for vehicles, machinery and other equipment, or funding secured by other business assets."),
    ("Business credit &amp; credit stacking",
     "Strategies to establish business credit and access several business credit lines or cards. Any introductory rate period depends on the card issuer and your approval."),
    ("Commercial &amp; investment real estate",
     "Financing for commercial and investment property, including short-term bridge loans, rental-property loans, construction financing and loans for portfolios of properties."),
])}
      </ul>
      <p class="__R____fine">
        This is an overview, not an offer or commitment to lend. Availability, eligibility, rates, terms,
        amounts and funding times depend on the specific program and on underwriting, and not every
        product is available in every state or to every applicant.
      </p>
    </div>
  </section>

  <!-- 4. Process -->
  <section class="__R____section" aria-labelledby="__R__-steps-title">
    <div class="__R____inner">
      <header class="__R____header">
        <p class="__R____eyebrow">How It Works</p>
        <h2 class="__R____h2" id="__R__-steps-title">From funding need to next step</h2>
      </header>
      <ol class="__R____steps">
{steps([
    ("Discuss your funding needs",
     "Share what the funding is for, roughly how much you need and your timeline."),
    ("Review potential program fit",
     "Look at which programs may suit your business or property, and what each one requires."),
    ("Continue on the Covered Bridge Capital website",
     "Find full program details, next steps and ways to reach the team on the dedicated website."),
])}
      </ol>
    </div>
  </section>

  <!-- 5. Closing CTA -->
  <section class="__R____section __R____cta" aria-labelledby="__R__-cta-title">
    <div class="__R____inner">
      <p class="__R____eyebrow">Covered Bridge Capital</p>
      <h2 class="__R____h2" id="__R__-cta-title">Find the funding for what's next</h2>
      <p class="__R____lede">
        Visit the Covered Bridge Capital website to explore programs in more detail and take the next step.
      </p>
      <div class="__R____actions">
        {CAP_BTN}
      </div>
    </div>
  </section>

</div>
"""

for path, r, comment, body, url in [
    ("pages/home-loans/cbb-home-loans-overview.html", "cbb-hlo", hl_comment, hl_body, HL_URL),
    ("pages/funding/cbb-capital-overview.html", "cbb-cap", cap_comment, cap_body, CAP_URL),
]:
    out = page(r, comment, body)
    assert "__R__" not in out and "__ART__" not in out and "__ARROW__" not in out
    assert out.count(f'href="{url}"') == 2 and "Trulli" not in out
    (root / path).write_text(out, encoding="utf-8")
    print("Wrote", path)
