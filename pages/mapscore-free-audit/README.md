# MapScore Free Audit page (`/mapscore-free-audit`)

Separate from the main MapScore page. Paste these blocks, in this order, each into its own GHL Custom HTML/JavaScript element:

| # | File | Block |
|---|---|---|
| 1 | `sections/00-header.html` | Header / menu (shared) |
| 2 | `pages/mapscore-free-audit/mapscore-free-audit.html` | The whole page body, including the embedded audit tool |
| 3 | `sections/06-footer.html` | Footer (shared) |

Set the GHL page path to `mapscore-free-audit`, and set the section/row to full width with 0 padding and no background, like the other pages.

- **Start Free Audit** scrolls to the audit section (`id="mapscore-audit"`), which stops just below the fixed header. You can link straight to it with `https://coveredbridgebrands.com/mapscore-free-audit#mapscore-audit`.
- **Iframe height:** `height:1100px` in the iframe's `style` is a starting value. The tool doesn't resize itself, so if its controls, results or consent text are cut off, raise that number.
- The block has no JavaScript, tracking, form fields or CRM connections. Everything the visitor enters goes into the audit tool itself.
