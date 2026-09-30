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

Suggested fields, matching what the Privacy Policy says you collect: first and last name, business name, industry, phone, email, and a message box.

## SMS consent checkbox

Add this in the GHL form builder as its **own checkbox**, **unticked by default**, and **not required**. The wording below is taken from the Privacy Policy:

> I agree to receive text messages from Covered Bridge Brands, LLC at the phone number I provided regarding my inquiry and related follow-up. Consent is not a condition of purchasing any goods or services. Message frequency may vary. Message and data rates may apply. Reply STOP to opt out or HELP for help. See our Privacy Policy and Terms of Service.

Link "Privacy Policy" to `/privacy-policy` and "Terms of Service" to `/terms` if the form builder allows links in the label. This is a starting point based on your policy, not legal advice.

## Form thank-you message

`pages/contact/form-thank-you-message.html` is a styled "Thank you" message for the form's **Settings → On Submit → Message** box. It uses inline styles only, because the GHL message editor removes `<style>` tags. In the editor, switch to the code view (the `</>` icon in the lower toolbar), select everything, paste the file's contents, then **Save**.
