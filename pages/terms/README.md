# Terms of Service page (`/terms`)

Paste these blocks, in this order, each into its own GHL Custom HTML/JavaScript element:

| # | File | Block | New? |
|---|---|---|---|
| 1 | `sections/00-header.html` | Header / menu | Reused |
| 2 | `pages/terms/01-terms-hero.html` | Banner: title and "Last updated" date | **New** |
| 3 | `pages/terms/02-terms-content.html` | The terms, with an "On this page" contents list | **New** |
| 4 | `sections/06-footer.html` | Footer | Reused |

## Changing the wording

The page is generated from `pages/terms/terms-source.txt`, which holds your text exactly as written. To change it, edit that file and run:

```
python3 scripts/build-legal.py pages/terms/terms-source.txt pages/terms terms
```

In the source file, `1. Heading` starts a numbered section, `* text` is a bullet point, `> text` is a line of the mailing address, and every other line is a paragraph. Remember to change the `Last updated:` line whenever the terms change.
