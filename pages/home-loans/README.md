# CBB Home Loans overview (`/home-loans`)

The CBB Home Loans page on the main CBB site: what the business does, its main loan options, how to get started, and a button to its standalone website. It replaces the Coming Soon body that was on this page.

Paste these blocks in order, each into its own full-width Custom HTML/JavaScript element (0 padding, no background):

| # | File | Block |
|---|---|---|
| 1 | `sections/00-header-capital.html` | Header: Marketing Services, Business Funding, Home Loans, High Converting Leads (the current page is highlighted) |
| 2 | `pages/home-loans/cbb-home-loans-overview.html` | Overview page body (`.cbb-hlo`) |
| 3 | `sections/06-footer.html` | Footer (same as every page) |

## Before publishing

1. Replace both `REPLACE_WITH_CBB_HOME_LOANS_WEBSITE_URL` values (top and bottom buttons) with the standalone CBB Home Loans website's full `https://` address.
2. Add the approved NMLS / licensing disclosure where the HTML comment `LICENSING:` marks it. None is included.
3. Check the copy against https://valorhldirect.com/ (it couldn't be reviewed when the page was written).

## Page settings

- **Title:** CBB Home Loans | Home Purchase & Refinance Guidance
- **URL slug:** `/home-loans`
- **Meta description:** CBB Home Loans helps you understand home purchase and refinance options, including conventional, FHA, VA and USDA loans and down payment assistance.

Edit the copy in `scripts/build-overviews.py`, then run `python3 scripts/build-overviews.py`.
