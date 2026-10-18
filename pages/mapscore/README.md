# MapScore main page (`/mapscore`)

Replaces the Coming Soon block on the existing `/mapscore` page. The Free Audit page (`/mapscore-free-audit`) is separate and unchanged.

## Placement in GHL

| # | Element | File |
|---|---|---|
| 1 | Shared header (already on the page) | `sections/00-header.html` |
| 2 | **Replace** the Coming Soon Custom HTML element with this file | `pages/mapscore/mapscore-main.html` |
| 3 | Shared footer (already on the page) | `sections/06-footer.html` |

Keep the section/row full width with 0 padding and no background. Don't add another header, footer, pixel, chat loader or cookie banner. The block has none.

## Settings (one place)

Open `mapscore-main.html`, find **MAPSCORE PAGE SETTINGS** near the top of the `<script>` at the bottom:

```js
var SETTINGS = {
  bookingUrl: '',        // GHL calendar link
  demoVideo: '',         // YouTube link or 11-character ID
  demoVideoTitle: 'MapScore by Covered Bridge Brands demo video',
  rankingAnimation: ''   // public https:// URL of the uploaded MP4
};
```

| Setting | While empty | Once filled in |
|---|---|---|
| `bookingUrl` | All 4 guided-call buttons go to `https://coveredbridgebrands.com/contact` and read **Request Your Free Audit Call**, with a note that we'll reach out to arrange a time | All 4 go to the calendar and read **Book Your Free Audit Call**; the contact note is hidden |
| `demoVideo` | The `#demo` section and the hero's **Watch the Demo** link stay hidden | Section and link appear; responsive YouTube player (privacy-enhanced domain), no autoplay |
| `rankingAnimation` | The animation stays hidden | Muted, looping inline MP4 with controls in the results section; it starts only when scrolled into view and never autoplays for visitors who prefer reduced motion. If the URL fails to load, it hides itself |

Only full `https://` links are accepted; anything else is ignored. For the animation, upload `Ranking Improvement GIF.mp4` to the GHL media library and paste its URL.

## Editing

Edit `mapscore-main.template.html`, then run `python3 scripts/build-mapscore.py` to rebuild `mapscore-main.html` (it embeds the images below). Run `./scripts/build-preview.sh` to refresh `preview.html`.

## Assets and sources

| Asset | Source | Used for |
|---|---|---|
| `assets/mapscore/hero-gold-pin.webp` | CBB MapScore sales deck, slide 1 background (resized from 1672×941 PNG) | Hero |
| `assets/mapscore/heatmap-before.webp`, `heatmap-after.webp` | CBB sales deck, slide 6 (provider-supplied Paige example pair, resized from 740×740) | Heatmap example, shown together with the deck's caveats. Map tiles are OpenStreetMap, credited on the page |
| Case studies (Home Crush, Rooster Roofers, The Hybrid Clinic) | CBB sales deck, slide 5 (Paige customer results, with the deck's disclaimer) | Results |
| 4.9/5, 1,000+ reviews, 13,000+ businesses; Will Higgins and Ryan Fullarton quotes | CBB sales deck, slide 8 (Paige / Merchynt review material) | Reviews, labeled as provider figures |
| Six-month guarantee wording | CBB sales deck, slide 10 | Pricing |
| Calculator | `Agency_ROI_Explainer_Guide_Iframe_Code.docx`, rebuilt and scoped | Revenue scenario calculator |
| MapScore pin mark | Stand-in mark from `sections/02-our-systems.html` (no approved MapScore logo file is in the project) | Hero eyebrow |
| Ranking animation | `Ranking Improvement GIF.mp4` (MP4, 1280×1280, 4.1 s, no audio) | Hidden until hosted |

To lighten the block (about 237 KB), upload the three `.webp` files to the GHL media library and replace each `data:image/webp;base64,...` value with its media URL.

## Provider-side items to confirm before selling

- Citations/directory sync: confirm citation credits or provisioning are enabled for each client account in Paige. The page presents citations as included in the plan.
- AI search visibility, social publishing (Facebook, Instagram, LinkedIn), YouTube and TikTok publishing, and website widgets each need the client's account connections and the matching Paige features active.
- CBB-branded newsletter: confirm it's set up before promising it to a client. The page names it only as an included extra, with no schedule.
