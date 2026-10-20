# MapScore main page (`/mapscore`)

Replaces the Coming Soon block on the existing `/mapscore` page. The audit-tool page (`/mapscore-free-audit`) stays published and unchanged for marketing analysts to share during booked calls, but this page doesn't link to it.

## Placement in GHL

| # | Element | File |
|---|---|---|
| 1 | Shared header (already on the page) | `sections/00-header.html` |
| 2 | **Replace** the Coming Soon Custom HTML element with this file | `pages/mapscore/mapscore-main.html` |
| 3 | Shared footer (already on the page) | `sections/06-footer.html` |

Keep the section full width with 0 padding and no background. Don't add another header, footer, pixel, chat loader or cookie banner. The block has none.

## Upload and configure

1. Upload each file below to **GHL Media** and copy its public URL.
2. In `mapscore-main.html`, find **MAPSCORE PAGE SETTINGS** in the `<script>` at the bottom. Each setting is labeled with the file it expects (`/* upload: … */`).
3. Paste each URL between the matching quotes, then paste the whole block into GHL.

Anything left `''` is hidden on the page; it never shows a broken image.

| Setting | Upload this file (`assets/mapscore/…`) | Used for |
|---|---|---|
| `bookingUrl` | — (GHL calendar link) | Every **Book a Free Guided Audit** button. While empty, the buttons scroll to the guided-audit section on the page. |
| `marketingVideo` | `White Label Promo Video.mp4` (already set to its GHL Media link) | **Discover MapScore** player: built-in 16:9 player with controls and fullscreen, no autoplay. Also accepts a YouTube link or ID. |
| `marketingVideoPoster` | optional still image (16:9 JPG/WebP) | Picture shown in the Discover player before the video plays. Empty: the browser shows the video's first frame. |
| `demoVideo` | — (GHL Media .mp4, or YouTube link or ID) | **See MapScore in Action** player. Shows "Coming soon" until set. |
| `demoVideoPoster` | optional still image | Same as above, for the demo player. |
| `assets.mapscoreLogo` | approved MapScore logo (not supplied yet) | Replaces the drawn MapScore wordmark in the hero. |
| `assets.graphicProfile` | `graphics/google-business-profile.webp` | Google Business Profile illustration |
| `assets.graphicPosts` | `graphics/automated-google-posts.webp` | Posts illustration |
| `assets.graphicReviews` | `graphics/review-collection.webp` | Review collection illustration |
| `assets.graphicApproval` | `graphics/review-approval.webp` | Review approval illustration |
| `assets.graphicDirectory` | `graphics/directory-and-search-network.webp` | Directory network illustration |
| `assets.rroofLogo` / `rroofBefore` / `rroofAfter` | `customers/rooster-roofers-logo.webp`, `-before.webp`, `-after.webp` | Rooster Roofers story |
| `assets.hybridLogo` / `hybridBefore` / `hybridAfter` | `customers/hybrid-clinic-logo.webp`, `-before.webp`, `-after.webp` | The Hybrid Clinic story |
| `assets.homecrushLogo` / `homecrushBefore` / `homecrushAfter` | `customers/home-crush-logo.webp`, `-before.webp`, `-after.webp` | Home Crush story |
| `assets.rankingAnimation` | `ranking-improvement.mp4` | Ranking animation (muted, inline, with controls; stays paused for visitors who prefer reduced motion) |
| `assets.rankingAnimationPoster` | `ranking-improvement-poster.webp` | Still frame shown before the animation plays |
| `assets.presentationDownload` | `CBB_MapScore_Presentation.pptx` | "Download the presentation" link |
| `assets.slides` (11 entries, in order) | `slides/slide-01.webp` … `slide-11.webp` | Presentation viewer |

The hero photo (`hero-gold-pin.webp`) is already embedded in the block.

The promo video link and any poster come from `pages/mapscore/asset-urls.json` (`marketingVideo`, `marketingVideoPoster`) when you run the build. If a video file can't load, the player is replaced by a short note with a link to open the video in a new tab.

## The presentation

The page uses the slide images and .pptx you uploaded to GHL Media (links in `asset-urls.json`). `assets/mapscore/CBB_MapScore_Presentation.pptx` is the repo copy of the corrected deck: the guarantee and website-builder wording are removed, supplier names are out, there are no speaker notes, slide 11 has a single **Book a Free Guided Audit** action and says "Your CBB marketing analyst guides the audit with you", and slide 6 identifies its heatmaps as Home Crush (before and after 30 days). `slides/` holds its 11 slides exported for the viewer, and `CBB_MapScore_Presentation.pdf` is a PDF copy. Slide 11's link points to `https://coveredbridgebrands.com/mapscore#ms-book`.

## Editing

Edit `mapscore-main.template.html`, then run `python3 scripts/build-mapscore.py`. It rebuilds `mapscore-main.html` (empty URLs, ready for GHL) and `preview.html` (uses the local files so everything shows).

## Asset sources

| Files | Source |
|---|---|
| `graphics/*` | Merchynt agency marketing assets, https://www.merchynt.com/marketingassets (originals listed in the supplied `asset-sources.csv`), resized to 960 px |
| `customers/*` | Merchynt customer heatmaps and logos, https://www.merchynt.com/paige (supplied pack), resized to 560 px |
| `ranking-improvement.mp4` | Supplied `Ranking Improvement GIF.mp4` (H.264, 1280×1280, 4.1 s, no audio); poster is its frame at 0.3 s |
| `hero-gold-pin.webp`, `slides/*`, `.pptx`, `.pdf` | CBB MapScore sales presentation |
| Case-study figures, review excerpts, provider ratings | CBB sales presentation, slides 5 and 8 (provider material) |
