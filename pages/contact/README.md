# Contact page (`/contact`)

Paste these blocks, in this order, each into its own GHL Custom HTML/JavaScript element:

| # | File | Block | New? |
|---|---|---|---|
| 1 | `sections/00-header.html` | Header / menu | Reused |
| 2 | `pages/contact/01-contact-hero.html` | Banner with "Call 814-893-1075" and "Send a Message" buttons | **New** |
| 3 | `pages/contact/02-contact-main.html` | Call/text, email, address with directions, hours, and the form panel | **New** |
| 4 | `sections/06-footer.html` | Footer (now shows call and email icons; no social links yet) | Updated |

## Adding the contact form

This page uses its **own** GHL form, separate from the home page forms.

1. In GHL, create the contact form (Sites > Forms).
2. Open it and choose **Integrate**, then copy the **Embed** code.
3. In block 3, paste it between the `<div class="cbb-contact__form">` tags, replacing the comment. The "Contact form goes here" box disappears once the form is in.

The live form is **CBB | Website Inquiry** (`2nrDrpbvRx335NyofhIm`). Keep its current fields and settings.

## Text-message consent

The two inquiry forms (CBB | Website Inquiry and CBB | Service Inquiry) have **no phone field and no SMS consent checkbox**. Don't add them. SMS consent is collected only by the GHL-generated A2P chat widget, and its compliance wording and fields are controlled by GHL.

Each form should show visible links to the Privacy Policy (`/privacy-policy`) and Terms of Service (`/terms`) at its bottom, added in the GHL form builder.

## Form thank-you message

`pages/contact/form-thank-you-message.html` is a styled "Thank you" message for the form's **Settings → On Submit → Message** box. It uses inline styles only, because the GHL message editor removes `<style>` tags. In the editor, switch to the code view (the `</>` icon in the lower toolbar), select everything, paste the file's contents, then **Save**.
