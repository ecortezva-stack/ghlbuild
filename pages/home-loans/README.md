# CBB Home Loans overview (`/home-loans`)

A short introduction to CBB Home Loans on the main CBB site (about 100 words): the business name, a headline, a short intro, three highlights and one button to its standalone website. It replaces the Coming Soon body that was on this page.

Paste these blocks in order, each into its own full-width Custom HTML/JavaScript element (0 padding, no background):

| # | File | Block |
|---|---|---|
| 1 | `sections/00-header-capital.html` | Header: Marketing Services, Business Funding, Home Loans, High Converting Leads (the current page is highlighted) |
| 2 | `pages/home-loans/cbb-home-loans-overview.html` | Introduction page body (`.cbb-hlo`) |
| 3 | `sections/06-footer.html` | Footer (same as every page) |

## Before publishing

1. Replace `REPLACE_WITH_CBB_HOME_LOANS_WEBSITE_URL` (the button, one place) with the standalone CBB Home Loans website's full `https://` address.
2. Add the approved NMLS / licensing disclosure if the page needs one. None is included.
3. Check the wording against https://valorhldirect.com/ (it couldn't be reviewed when the page was written).

## Page settings

- **Title:** CBB Home Loans | Home Purchase & Refinance Guidance
- **URL slug:** `/home-loans`
- **Meta description:** CBB Home Loans helps you understand home purchase and refinance options, including conventional, FHA, VA and USDA loans and down payment assistance.

Edit the copy in `scripts/build-overviews.py`, then run `python3 scripts/build-overviews.py`.
