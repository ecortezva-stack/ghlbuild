# Covered Bridge Brands — Home Page (GoHighLevel)

Each file in `sections/` is one self-contained block for a GHL **Custom HTML/JavaScript** element. Paste them in order:

| File | Section | Wrapper class | Anchor |
|---|---|---|---|
| `sections/01-hero.html` | Hero | `.cbb-hero` | none |
| `sections/02-our-systems.html` | Our Systems | `.cbb-systems` | `#our-systems` |
| `sections/03-how-it-works.html` | How It Works | `.cbb-process` | none |
| `sections/04-why-cbb.html` | Why CBB | `.cbb-why` | none |
| `sections/05-cta.html` | CTA / Contact | `.cbb-cta` | `#contact` |

`preview.html` joins all five into one page so you can look it over in a browser. **Don't paste it into GHL.** To rebuild it after you edit a section, run `./scripts/build-preview.sh`.

## GHL setup

- **Section/row settings:** Set each GHL section to full width with 0 padding and no background. Each block brings its own background and spacing.
- **Fonts:** Choose *Playfair Display* and *Inter* in the site's typography settings. If they aren't loaded, the blocks fall back to Georgia and the system sans-serif.
- **Anchors:** "Explore Services" scrolls to `#our-systems`, and "Contact Us" and every "Notify Me" scroll to `#contact`.

## Things to fill in

Search the files for these markers:

- `IMAGE:` marks where a photo belongs: the hero covered bridge and one image per system card. Uncomment the `<img>` right below the marker and set its `src` to a GHL media-library URL. Until you do, the gradient fill shows.
- `LINK:` marks the outbound URLs for the Super LO and System Two cards. They are `href="#"` for now.
- `NAME TBC` is on the System Two card title.
- `GHL CONTACT FORM GOES HERE` is in the CTA block. You have two options:
  - **A.** Paste the form's embed code (Sites → Forms → Integrate) inside that div. The form then sits inside the gold panel, and the dashed placeholder hides itself.
  - **B.** Delete the div and put a native Form element directly below the CTA block. The heading text re-centers on its own.
