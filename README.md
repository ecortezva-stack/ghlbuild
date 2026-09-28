# Covered Bridge Brands — Home Page (GoHighLevel)

Each file in `sections/` is one self-contained block for a GHL **Custom HTML/JavaScript** element. Paste them in order:

| File | Section | Wrapper class | Anchor |
|---|---|---|---|
| `sections/00-header.html` | Header / nav | `.cbb-header` | none |
| `sections/01-hero.html` | Hero | `.cbb-hero` | none |
| `sections/02-our-systems.html` | Our Systems (Super LOA, MapScore™ by CBB, 4 industry cards) | `.cbb-systems` | `#our-systems` |
| `sections/03-how-it-works.html` | How It Works | `.cbb-process` | none |
| `sections/04-why-cbb.html` | Why CBB | `.cbb-why` | none |
| `sections/05-cta.html` | CTA / Contact (optional) | `.cbb-cta` | `#contact` |
| `sections/06-footer.html` | Footer | `.cbb-footer` | none |

`preview.html` joins all the blocks into one page so you can look it over in a browser. **Don't paste it into GHL.** To rebuild it after you edit a section, run `./scripts/build-preview.sh`.

## GHL setup

- **Section/row settings:** Set each GHL section to full width with 0 padding and no background. Each block brings its own background and spacing.
- **Fonts:** Choose *Playfair Display* and *Inter* in the site's typography settings. If they aren't loaded, the blocks fall back to Georgia and the system sans-serif.
- **Header/footer:** If you already use GHL's global header or footer, you can skip `00-header` and `06-footer`.

## Adding photos

Photos are set with one CSS variable, so you don't need to edit any other markup. Replace `none` with `url('YOUR-IMAGE-URL')`:

| Photo | Where to change it |
|---|---|
| Hero covered bridge | `--cbb-hero-photo` at the top of `01-hero.html` |
| Super LOA / MapScore card backgrounds | `style="--cbb-card-photo: none;"` on each card in `02-our-systems.html` |
| Industry card images (Roofers, HVAC, Home, Medical) | `style="--cbb-box-photo: none;"` on each card in `02-our-systems.html` |
| How It Works landscape | `--cbb-process-photo` at the top of `03-how-it-works.html` |
| Why CBB landscape | `--cbb-why-photo` at the top of `04-why-cbb.html` |

Until you add a photo, a warm gradient fills its space. The dark fade overlays stay in place over real photos, so the text stays readable.

## Other things to fill in

Search the files for these markers:

- `LOGO:` The Covered Bridge Brands logo is already embedded in the header and footer, so it shows as soon as you paste. To make those blocks lighter, upload `assets/cbb-logo.png` to the GHL media library and replace the `src="data:..."` value with its URL. The Super LOA and MapScore wordmarks are drawn stand-ins, and each has a commented-out `<img>` ready for the real logo file.
- `LINKS:` marks the nav paths, the Learn More URLs, the legal pages, and the social and email links.
- `GHL CONTACT FORM GOES HERE` is in `05-cta.html`. Paste your form's embed code inside that div, or delete the div and put a native Form element below the block.
