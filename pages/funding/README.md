# Covered Bridge Capital overview (`/funding`)

A short introduction to Covered Bridge Capital on the main CBB site (about 100 words): the business name, a headline, a short intro, three highlights and one button to its standalone website. It replaces the Coming Soon body that was on this page.

Paste these blocks in order, each into its own full-width Custom HTML/JavaScript element (0 padding, no background):

| # | File | Block |
|---|---|---|
| 1 | `sections/00-header-capital.html` | Header: Marketing Services, Business Funding, Home Loans, High Converting Leads (the current page is highlighted) |
| 2 | `pages/funding/cbb-capital-overview.html` | Introduction page body (`.cbb-cap`) |
| 3 | `sections/06-footer.html` | Footer (same as every page) |

## Before publishing

1. Replace `REPLACE_WITH_COVERED_BRIDGE_CAPITAL_WEBSITE_URL` (the button, one place) with the standalone Covered Bridge Capital website's full `https://` address.
2. Check the wording against the Covered Bridge Capital financing PDFs (they weren't available when the page was written).

## Page settings

- **Title:** Covered Bridge Capital | Business & Real Estate Financing
- **URL slug:** `/funding`
- **Meta description:** Covered Bridge Capital helps business owners and real estate investors explore financing: lines of credit, SBA, working capital, equipment, business credit and real estate loans.

Edit the copy in `scripts/build-overviews.py`, then run `python3 scripts/build-overviews.py`.
