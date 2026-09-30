# Covered Bridge Brands — Website (GoHighLevel)

## Pages

| Page | Path | Paste guide | Status |
|---|---|---|---|
| Home | `/` | below | Done |
| Services | `/services` | [`pages/services/README.md`](pages/services/README.md) | Done |
| Terms of Service | `/terms` | [`pages/terms/README.md`](pages/terms/README.md) | Done |
| Privacy Policy | `/privacy-policy` | [`pages/privacy/README.md`](pages/privacy/README.md) | Done |
| About | `/about` | [`pages/about/README.md`](pages/about/README.md) | Done |
| Contact | `/contact` | [`pages/contact/README.md`](pages/contact/README.md) | Done, needs its GHL form |
| Super LOA, MapScore, RoofRocket, ComfortFlow, ServiceFlow, PracticeFlow | `/super-loa`, `/mapscore`, `/roofrocket`, `/comfortflow`, `/serviceflow`, `/practiceflow` | [`pages/coming-soon/README.md`](pages/coming-soon/README.md) | Coming Soon page |

## Home page

Each file in `sections/` is one self-contained block for a GHL **Custom HTML/JavaScript** element. Paste them in order:

| File | Section | Wrapper class | Anchor |
|---|---|---|---|
| `sections/00-header.html` | Header / nav | `.cbb-header` | none |
| `sections/01-hero.html` | Hero | `.cbb-hero` | none |
| `sections/02-our-systems.html` | Our Systems (Super LOA, MapScore™, RoofRocket, ComfortFlow, ServiceFlow, PracticeFlow) | `.cbb-systems` | `#our-systems` |
| `sections/03-how-it-works.html` | How It Works | `.cbb-process` | none |
| `sections/04-why-cbb.html` | Why CBB | `.cbb-why` | none |
| `sections/05-cta.html` | CTA / Contact (optional) | `.cbb-cta` | `#contact` |
| `sections/06-footer.html` | Footer | `.cbb-footer` | none |

`preview.html` (and `pages/<page>/preview.html` for other pages) joins all the blocks into one page so you can look it over in a browser. **Don't paste it into GHL.** To rebuild it after you edit a section, run `./scripts/build-preview.sh`.

## GHL setup

- **Section/row settings:** Set each GHL section to full width with 0 padding and no background. Each block brings its own background and spacing.
- **Fonts:** Choose *Playfair Display* and *Inter* in the site's typography settings. If they aren't loaded, the blocks fall back to Georgia and the system sans-serif.
- **Header/footer:** If you already use GHL's global header or footer, you can skip `00-header` and `06-footer`.
- **Header behavior:** The header stays pinned to the top with `position: fixed` (sticky wouldn't work inside GHL's element containers), and its outer box reserves the same height so content isn't hidden underneath. Links only turn gold and underline on hover (the current page is tagged for screen readers from the URL, with no visual change), and the mobile menu uses a small inline script. In the GHL editor the pinned bar may sit over the canvas while you edit; that's expected, and the live page is unaffected.

## Photos

Your photos are already built into the blocks, so they show as soon as you paste:

| Photo | Block | Optimized file |
|---|---|---|
| Covered bridge | `01-hero.html` (`--cbb-hero-photo`) | `assets/photos/hero-bridge.webp` |
| Desk with laptops | Super LOA card in `02-our-systems.html` | `assets/photos/card-superloa.webp` |
| Desk with CBB mug | MapScore card in `02-our-systems.html` | `assets/photos/card-mapscore.webp` |
| Roof with hard hat at sunset | RoofRocket card in `02-our-systems.html` | `assets/photos/card-roofrocket.webp` |
| AC unit at dusk | ComfortFlow card in `02-our-systems.html` | `assets/photos/card-comfortflow.webp` |
| Laptop with map pins | ServiceFlow card in `02-our-systems.html` | `assets/photos/card-serviceflow.webp` |
| Desk with laptop and mug | PracticeFlow card in `02-our-systems.html` | `assets/photos/card-practiceflow.webp` |
| Misty mountains | `03-how-it-works.html` (`--cbb-process-photo`) | `assets/photos/bg-how-it-works.webp` |
| Mountain sunset | `04-why-cbb.html` (`--cbb-why-photo`) | `assets/photos/bg-why-cbb.webp` |

**Optional, for faster loading:** upload the optimized files to the GHL media library, then replace each `url('data:...')` value with `url('YOUR-MEDIA-URL')`. The hero block drops from about 195 KB to about 7 KB this way.

The four industry card logos now load from the GHL media library. The six card photos are still built in, so `02-our-systems.html` is about 254 KB; uploading `assets/photos/card-*.webp` to the media library and sending the links would bring it down to about 20 KB.

## Other things to fill in

Search the files for these markers:

- `LOGO:` The Covered Bridge Brands logo (header and footer) and the RoofRocket, ComfortFlow, ServiceFlow and PracticeFlow logos (Our Systems) are served from the GHL media library. The Super LOA and MapScore wordmarks are drawn stand-ins, and each has a commented-out `<img>` ready for the real logo file.
- **Page links:** Nav links use `/`, `/services`, `/about`, `/contact`. The Learn More buttons go to `/super-loa` and `/mapscore`. Footer legal links use `/privacy-policy` and `/terms`. These only work once your own domain is connected; on GHL's shared preview address they lead to a "Not found" page.
- `SOCIAL:` the footer shows call and email icons. LinkedIn and YouTube are left out until those accounts are ready.
- `GHL CONTACT FORM GOES HERE` is in `05-cta.html`. Paste your form's embed code inside that div, or delete the div and put a native Form element below the block.
