# Privacy Policy page (`/privacy-policy`)

Paste these blocks, in this order, each into its own GHL Custom HTML/JavaScript element:

| # | File | Block | New? |
|---|---|---|---|
| 1 | `sections/00-header.html` | Header / menu | Reused |
| 2 | `pages/privacy/01-privacy-hero.html` | Banner: title and "Last updated" date | **New** |
| 3 | `pages/privacy/02-privacy-content.html` | The policy, with an "On this page" contents list | **New** |
| 4 | `sections/06-footer.html` | Footer | Reused |

## Changing the wording

The page is generated from `pages/privacy/privacy-source.txt`, which holds your text exactly as written. To change it, edit that file and run:

```
python3 scripts/build-legal.py pages/privacy/privacy-source.txt pages/privacy privacy
```

In the source file, `## Heading` starts a section, `* text` is a bullet point, `> text` is a line of the mailing address, and every other line is a paragraph. Remember to change the `Last updated:` line whenever the policy changes.
