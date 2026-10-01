# Coming Soon page (use on every product page that isn't live yet)

One block serves all six product pages. It reads the page address and shows the right product name:

| Page path | Heading shown |
|---|---|
| `/super-loa` | Super LOA Is Coming Soon |
| `/mapscore` | MapScore™ by CBB Is Coming Soon |
| `/roof-rocket` | RoofRocket by CBB Is Coming Soon |
| `/comfort-flow` | ComfortFlow by CBB Is Coming Soon |
| `/service-flow` | ServiceFlow by CBB Is Coming Soon |
| `/practice-flow` | PracticeFlow by CBB Is Coming Soon |
| anything else | Something New Is Coming Soon |

Paste these blocks, in this order, on **each** product page:

| # | File | Block |
|---|---|---|
| 1 | `sections/00-header.html` | Header / menu |
| 2 | `pages/coming-soon/01-coming-soon.html` | Coming Soon (same file on every product page) |
| 3 | `sections/06-footer.html` | Footer |

The buttons go to `/contact` ("Notify Me") and `/services` ("Explore Our Services"), and the phone number calls 814-893-1075. The product name appears once the page is on its real path; in the GHL editor preview it may show the general "Something New" wording.

When a product launches, replace this block on that page with its full product page.
