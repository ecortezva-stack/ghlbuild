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

## If the audit shows "refused to connect"

Chrome shows that same message for several different causes, so check the console before changing anything:

1. Open the GHL **preview** of this page in Chrome (or the live page once published), not a downloaded or attached copy of the HTML file. Attachment and file previews often block outside frames themselves.
2. Press F12, open the **Console** tab, and reload.
3. Match the red message:
   - `Refused to display ... because it set 'X-Frame-Options' to 'deny'` (or `'sameorigin'`): the audit site doesn't allow embedding on coveredbridgebrands.com. Fix it in the MapScore/Paige white-label settings or with its support. Nothing on this page can override it.
   - `Refused to frame ... because an ancestor violates ... "frame-ancestors ..."`: same cause, set through the audit site's security policy. Ask for `https://coveredbridgebrands.com` to be allowed.
   - `Refused to frame ... because it violates ... "frame-src ..."`: the page *around* the iframe is blocking it. This is normal in sandboxed previews. If it happens on the GHL page itself, check for a custom Content-Security-Policy in the site's settings or tracking code.
   - `net::ERR_CONNECTION_REFUSED` or `ERR_NAME_NOT_RESOLVED` in the Console or **Network** tab: the audit address isn't reachable at all. Open it directly in a new tab and check its DNS and SSL setup.
4. If the tool loads, also check in the Network tab that `light-audit/search` doesn't redirect somewhere else.
