# KBS Commercial Demolition Website

A professional multi-page static site designed for KBS Commercial Demolition.

## Pages
- `index.html` – home page
- `services.html` – service lines and process
- `projects.html` – filterable project gallery
- `safety.html` – safety/process page
- `about.html` – company story page
- `quote.html` – quote request form
- `contact.html` – contact and service-area page

## Replace the business details first
Open `assets/js/site.js` and update:
- `phoneDisplay`
- `phoneHref`
- `email`
- `quoteEndpoint`

These values automatically update throughout the website.

## Make the quote form receive submissions
The site works immediately as a `mailto:` fallback, but email apps are not ideal for a public website. For direct form submissions, create an endpoint with Formspree or FormSubmit, then paste it into:

```js
quoteEndpoint: 'YOUR_FORM_ENDPOINT_HERE'
```

Examples:
- Formspree: `https://formspree.io/f/your-form-id`
- FormSubmit AJAX: `https://formsubmit.co/ajax/your-email@domain.com`

The form submits using POST and will display an on-page success message after setup.

## Add your photos
The project gallery is ready for 12 images.

1. Put your photos in `assets/images/projects/`.
2. Name them `project-01.jpg`, `project-02.jpg`, up to `project-12.jpg`.
3. The site automatically uses those images instead of the included visual placeholders.

To add more than 12 photos:
1. Copy one `<article class="project">...</article>` block in `projects.html`.
2. Change the title and `data-category`.
3. Add a matching photo to the project folder.

Recommended photo export:
- JPG or WEBP
- at least 1600 px wide
- horizontal 4:3 shots work best
- keep files under 1 MB when possible for a fast site

## Replace hero/service images
Add real JPG versions named:
- `assets/images/hero.jpg`
- `assets/images/about-team.jpg`
- `assets/images/service-interior.jpg`
- `assets/images/service-structural.jpg`
- `assets/images/service-sitework.jpg`
- `assets/images/service-specialty.jpg`

The placeholder SVGs stay in the folder as fallbacks until your photos are added.

## Deployment
This is a plain static website. You can upload all files to:
- GitHub Pages
- Netlify
- Cloudflare Pages
- a hosting provider’s file manager

For GitHub Pages: upload the full contents of this folder to the repository root, then enable Pages from the main branch.

## Final publish checklist
- Replace demo phone number and email
- Connect the quote form endpoint
- Replace all image placeholders
- Add real licenses, certifications, service area, and business hours
- Add a privacy policy if you use a third-party form service
