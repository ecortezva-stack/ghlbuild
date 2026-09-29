# Terms of Service page (`/terms`)

> **Not ready to publish yet.** The text you sent was cut off partway through section 17 (Disclaimers). Sections 1–16 and the first two sentences of 17 are in place. Send the rest and it will be added.

Paste these blocks, in this order, each into its own GHL Custom HTML/JavaScript element:

| # | File | Block | New? |
|---|---|---|---|
| 1 | `sections/00-header.html` | Header / menu | Reused |
| 2 | `pages/terms/01-terms-hero.html` | Banner: title and effective date | **New** |
| 3 | `pages/terms/02-terms-content.html` | The terms, with an "On this page" contents list | **New** |
| 4 | `sections/06-footer.html` | Footer | Reused |

## Changing the wording

The page is generated from `pages/terms/terms-source.txt`, which holds your text exactly as written. To change it, edit that file and run:

```
python3 scripts/build-legal.py pages/terms/terms-source.txt pages/terms terms
```

In the source file, `1. Heading` starts a numbered section, `* text` is a bullet point, and every other line is a paragraph.
