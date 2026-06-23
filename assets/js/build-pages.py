from pathlib import Path
root=Path('/mnt/data/kbs-demolition-website')

def nav(active):
    links=[('Home','index.html','home'),('Services','services.html','services'),('Projects','projects.html','projects'),('Safety','safety.html','safety'),('About','about.html','about'),('Contact','contact.html','contact')]
    linkhtml=''.join(f'<a href="{href}" class="{"active" if key==active else ""}">{label}</a>' for label,href,key in links)
    return f'''<div class="topbar"><div class="container topbar-inner"><span>Commercial demolition • interior selective demolition • site clearing</span><a data-phone href="tel:+12075550124">(207) 555-0124</a></div></div>
<header class="site-header"><div class="container nav"><a class="brand" href="index.html" aria-label="KBS Commercial Demolition home"><img class="brand-mark" src="assets/images/logo-mark.jpg" alt="KBS Commercial Demolition logo"><span>KBS <small>COMMERCIAL DEMOLITION</small></span></a><button class="menu-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button><nav class="nav-links">{linkhtml}<a href="quote.html" class="button button-primary">Request a Quote →</a></nav></div></header>'''

def footer():
    return '''<footer class="footer"><div class="container footer-grid"><div><a class="brand" href="index.html"><img class="brand-mark" src="assets/images/logo-mark.jpg" alt="KBS Commercial Demolition logo"><span>KBS <small>COMMERCIAL DEMOLITION</small></span></a><p>Reliable commercial demolition planning and execution for contractors, property owners, and facility managers.</p></div><div><h4>Explore</h4><a href="services.html">Services</a><a href="projects.html">Projects</a><a href="safety.html">Safety</a><a href="about.html">About KBS</a></div><div><h4>Get Started</h4><a href="quote.html">Request a Quote</a><a href="contact.html">Contact Us</a><a href="mailto:estimating@yourkbsdomain.com" data-email>estimating@yourkbsdomain.com</a><a href="tel:+12075550124" data-phone>(207) 555-0124</a></div><div><h4>Built for complex work</h4><p>Clear communication, controlled execution, and site-ready turnover.</p><a href="quote.html" class="button button-primary">Start a Project</a></div></div><div class="container footer-bottom"><span>© <span id="year"></span> KBS Commercial Demolition. All rights reserved.</span><span>Licensed • Insured • Safety-driven</span></div></footer><script>document.getElementById('year').textContent=new Date().getFullYear()</script><script src="assets/js/site.js"></script>'''

def page(title, active, content, desc='KBS Commercial Demolition — professional demolition services for commercial projects.'):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{desc}"><title>{title} | KBS Commercial Demolition</title><link rel="icon" href="assets/images/logo-mark.jpg"><link rel="stylesheet" href="assets/css/site.css"></head><body>{nav(active)}{content}{footer()}</body></html>'''

def img(path, alt): return f'<img src="assets/images/{path}.jpg" data-fallback="assets/images/{path}.svg" alt="{alt}" loading="lazy">'

home=f'''<main>
<section class="hero"><div class="container hero-content"><p class="eyebrow">Commercial demolition specialists</p><h1 class="display">Clear the way for what’s next.</h1><p>KBS delivers controlled commercial demolition, selective interior work, and site preparation with the planning, communication, and jobsite discipline your project demands.</p><div class="hero-actions"><a href="quote.html" class="button button-primary">Request a Quote →</a><a href="projects.html" class="button button-outline">View Our Work</a></div></div></section>
<section class="trust-strip"><div class="container trust-grid"><div class="trust-item"><span>Focused on</span>Commercial projects</div><div class="trust-item"><span>Work approach</span>Planned & controlled</div><div class="trust-item"><span>Priority</span>Safety & communication</div><div class="trust-item"><span>From start to finish</span>Site-ready turnover</div></div></section>
<section class="section"><div class="container grid-2"><div><p class="eyebrow">Demolition with discipline</p><h2 class="display section-title">The partner contractors call when the work has to stay on schedule.</h2><p class="lead">From a single tenant buildout to a multi-phase commercial property redevelopment, KBS approaches every scope with organized planning, experienced crews, and an unwavering focus on keeping the site controlled.</p><a class="button button-dark" href="about.html">Why KBS →</a></div><div class="media-card tall">{img('about-team','KBS commercial demolition team on site')}</div></div></section>
<section class="section split-band"><div class="container"><p class="eyebrow">Capabilities</p><h2 class="display section-title">Built around the real needs of commercial projects.</h2><div class="grid-3" style="margin-top:2rem"><a class="service-card" href="services.html#interior">{img('service-interior','Interior demolition work')}<h3>Interior Demolition</h3><p>Selective removal for renovations, reconfigurations, and tenant improvements.</p></a><a class="service-card" href="services.html#structural">{img('service-structural','Structural demolition machinery')}<h3>Structural Demolition</h3><p>Controlled demolition planning for commercial structures and site redevelopment.</p></a><a class="service-card" href="services.html#site">{img('service-sitework','Commercial site clearing')}<h3>Site Clearing & Prep</h3><p>Remove, clear, and prepare the site for the next phase of construction.</p></a></div></div></section>
<section class="section"><div class="container grid-2"><div class="media-card">{img('projects/project-01','Commercial demolition project')}</div><div><p class="eyebrow">Proof in the work</p><h2 class="display section-title">A project gallery built to show real results.</h2><p class="lead">Your photos should do the talking. The KBS site includes a full portfolio page with filters, large project cards, and room to add as many before-and-after, equipment, and completed-site photos as you want.</p><a class="button button-dark" href="projects.html">Explore Projects →</a><div class="photo-note">This starter site is already set up for 12 project images. Add more by copying a project card — instructions are included in the README.</div></div></div></section>
<section class="cta"><div class="container"><div><p class="eyebrow">Let’s price your next scope</p><h2 class="display">Get a clear, straightforward quote from KBS.</h2></div><a href="quote.html" class="button button-primary">Request a Quote →</a></div></section>
</main>'''
(root/'index.html').write_text(page('KBS Commercial Demolition','home',home))

services=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Services</div><p class="eyebrow">Capabilities</p><h1 class="display">Demolition scopes, planned right.</h1><p>Commercial demolition support designed for the realities of active sites, tight schedules, and the next phase of construction.</p></div></section><section class="section"><div class="container"><div class="grid-2"><div><p class="eyebrow">What we do</p><h2 class="display section-title">A focused demolition partner from planning to clean turnover.</h2></div><p class="lead">We work alongside owners, general contractors, facility teams, and trades to complete the demolition scope cleanly and efficiently — while keeping communication direct and the worksite organized.</p></div><div class="grid-3" style="margin-top:2.5rem"><article class="card" id="interior"><h3>Interior & Selective Demolition</h3><p>Removal of partitions, ceilings, finishes, fixtures, flooring, and non-structural components for renovations and tenant improvements.</p></article><article class="card" id="structural"><h3>Structural Demolition</h3><p>Planned removal of commercial structures and structural elements with an emphasis on coordinated sequencing and site control.</p></article><article class="card" id="site"><h3>Site Clearing & Preparation</h3><p>Clearing unwanted structures, debris, and materials so the construction site is ready for the next stage of work.</p></article><article class="card"><h3>Concrete & Hardscape Removal</h3><p>Removal of slabs, curbs, walkways, foundations, and other exterior elements within a defined demolition scope.</p></article><article class="card"><h3>Tenant Improvement Support</h3><p>Responsive demolition for buildouts, retail remodels, office transitions, and occupied-property project schedules.</p></article><article class="card"><h3>Debris Management</h3><p>Organized material handling, load-out, and jobsite cleanup to help keep your project moving forward.</p></article></div></div></section><section class="section split-band"><div class="container grid-2"><div class="media-card">{img('service-specialty','Commercial demolition services')}</div><div><p class="eyebrow">How we work</p><h2 class="display section-title">Clear scope. Controlled execution.</h2><div class="process grid-3" style="margin-top:1.6rem"><article class="card"><h3>Review</h3><p>We understand the site, schedule, access, and demolition needs.</p></article><article class="card"><h3>Plan</h3><p>We coordinate the work sequence, safety approach, and logistics.</p></article><article class="card"><h3>Execute</h3><p>We complete the scope with consistent communication and clean turnover.</p></article></div></div></div></section><section class="cta"><div class="container"><div><p class="eyebrow">Need pricing?</p><h2 class="display">Tell us about the scope.</h2></div><a href="quote.html" class="button button-primary">Request a Quote →</a></div></section></main>'''
(root/'services.html').write_text(page('Services','services',services))

projects_cards=[]
project_data=[('Commercial','Retail Interior Demo','Commercial retail space prepared for a full renovation.'),('Commercial','Office Suite Selective Demo','Targeted interior removal for an office reconfiguration.'),('Sitework','Site Clearing & Turnover','Exterior clearing ready for the next construction phase.'),('Commercial','Multi-Unit Commercial Renovation','Coordinated demolition across a multi-space commercial property.'),('Structural','Commercial Structure Removal','Controlled removal supporting site redevelopment.'),('Sitework','Concrete & Hardscape Removal','Removal and cleanup for a redesigned exterior footprint.'),('Commercial','Restaurant Buildout Preparation','Interior demolition supporting a new restaurant concept.'),('Commercial','Warehouse Reconfiguration','Selective demo to open up a new operational layout.'),('Structural','Redevelopment Demolition','A clean start for a new commercial build.'),('Sitework','Property Clearing','Material removal and site cleanup for project readiness.'),('Commercial','Tenant Transition Scope','Fast-turn interior demo between commercial occupants.'),('Commercial','Renovation Preparation','Interior space cleared for construction crews.')]
for i,(cat,name,desc) in enumerate(project_data,1):
    num=f'{i:02d}'; projects_cards.append(f'''<article class="project" data-category="{cat.lower()}"><img src="assets/images/projects/project-{num}.jpg" data-fallback="assets/images/projects/project-{num}.svg" alt="{name}" loading="lazy"><div class="overlay"><div class="tag">{cat}</div><h3>{name}</h3></div></article>''')
projects=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Projects</div><p class="eyebrow">Our work</p><h1 class="display">Projects that make room for progress.</h1><p>Use this portfolio to showcase the work KBS is proud of — demolition in action, completed turnarounds, before-and-after photos, equipment, and jobsite progress.</p></div></section><section class="section"><div class="container"><p class="eyebrow">Portfolio</p><h2 class="display section-title">Real project photos belong here.</h2><p class="lead">Every image below is an easy-to-replace placeholder. Add your own photos to the project image folder using the matching project number, and they will automatically display on the site.</p><div class="filter-bar"><button class="filter-button active" data-filter="all">All Projects</button><button class="filter-button" data-filter="commercial">Commercial</button><button class="filter-button" data-filter="structural">Structural</button><button class="filter-button" data-filter="sitework">Sitework</button></div><div class="project-grid">{''.join(projects_cards)}</div><div class="photo-note">Want a bigger portfolio? Duplicate any project card in <strong>projects.html</strong>, add a new image to <strong>assets/images/projects</strong>, and change its title/category. Detailed steps are in README.md.</div></div></section><section class="cta"><div class="container"><div><p class="eyebrow">Your project next</p><h2 class="display">Ready to discuss a demolition scope?</h2></div><a href="quote.html" class="button button-primary">Request a Quote →</a></div></section></main>'''
(root/'projects.html').write_text(page('Projects','projects',projects))

safety=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Safety</div><p class="eyebrow">Safety & process</p><h1 class="display">Controlled work starts before equipment arrives.</h1><p>Safety is built into planning, communication, site awareness, and disciplined execution — not handled as an afterthought.</p></div></section><section class="section"><div class="container grid-2"><div><p class="eyebrow">Our approach</p><h2 class="display section-title">A safer, better-organized demolition site.</h2><p class="lead">KBS approaches each project with a focus on clear work boundaries, crew coordination, site conditions, and communication with the people working around the demolition scope.</p><ul class="safety-list"><li>Project-specific work planning</li><li>Site access and hazard awareness</li><li>Clear crew communication</li><li>Orderly work zones and cleanup</li><li>Coordination with trades and project teams</li><li>Controlled material handling</li></ul></div><div><div class="media-card tall">{img('service-structural','Demolition equipment at a commercial project')}</div></div></div></section><section class="section split-band"><div class="container"><p class="eyebrow">What clients can expect</p><div class="grid-3"><article class="card"><h3>Preparation</h3><p>We start by understanding the scope, site constraints, access requirements, schedule, and the work happening around us.</p></article><article class="card"><h3>Coordination</h3><p>We stay connected with the project team so the demolition work supports the construction plan instead of creating surprises.</p></article><article class="card"><h3>Turnover</h3><p>Our goal is a clear, workable site that helps the next trade or phase start with confidence.</p></article></div></div></section><section class="cta"><div class="container"><div><p class="eyebrow">Plan the work with KBS</p><h2 class="display">Talk through your project requirements.</h2></div><a href="quote.html" class="button button-primary">Request a Quote →</a></div></section></main>'''
(root/'safety.html').write_text(page('Safety','safety',safety))

about=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / About</div><p class="eyebrow">About KBS</p><h1 class="display">Commercial demolition done with accountability.</h1><p>KBS is built for the contractors and property owners who want a reliable demolition partner — one that communicates well, respects the jobsite, and follows through.</p></div></section><section class="section"><div class="container grid-2"><div class="media-card tall">{img('about-team','KBS team at a commercial demolition site')}</div><div><p class="eyebrow">Who we are</p><h2 class="display section-title">Direct. Capable. Ready for the work.</h2><p class="lead">We understand that demolition is rarely a stand-alone task. It is the beginning of a renovation, redevelopment, or construction schedule. That means the details matter: access, coordination, the condition of the site, material handling, and leaving the next team ready to begin.</p><p class="muted">Replace this copy with KBS’s story, founding year, service area, key team members, licenses, and the type of projects you want more of. It is written to be easy to customize without redesigning the page.</p><a href="contact.html" class="button button-dark">Talk With Our Team →</a></div></div></section><section class="section split-band"><div class="container grid-4"><div class="stat"><strong>01</strong><span>Commercial focus</span></div><div class="stat"><strong>02</strong><span>Clear communication</span></div><div class="stat"><strong>03</strong><span>Controlled execution</span></div><div class="stat"><strong>04</strong><span>Clean turnover</span></div></div></section><section class="cta"><div class="container"><div><p class="eyebrow">Work with KBS</p><h2 class="display">Bring us into your next project early.</h2></div><a href="quote.html" class="button button-primary">Request a Quote →</a></div></section></main>'''
(root/'about.html').write_text(page('About KBS','about',about))

quote=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Request a Quote</div><p class="eyebrow">Start a conversation</p><h1 class="display">Request a project quote.</h1><p>Tell us what you are planning. The more detail you include, the better prepared we can be for the first conversation.</p></div></section><section class="section"><div class="container"><div class="form-shell"><aside class="form-aside"><p class="eyebrow">KBS estimating</p><h2 class="display">Let’s scope it out.</h2><p>Send project details, timing, and site information. We will follow up to discuss the work and next steps.</p><ul class="contact-points"><li><strong>Phone</strong><br><a data-phone href="tel:+12075550124">(207) 555-0124</a></li><li><strong>Email</strong><br><a data-email href="mailto:estimating@yourkbsdomain.com">estimating@yourkbsdomain.com</a></li><li><strong>Helpful details</strong><br>Address, project type, scope, schedule, and available photos or plans.</li></ul></aside><div class="form-card"><h2 style="margin-top:0">Project Details</h2><form data-quote-form><div class="form-grid"><div class="field"><label for="name">Your name *</label><input id="name" name="Name" required></div><div class="field"><label for="company">Company</label><input id="company" name="Company"></div><div class="field"><label for="email">Email *</label><input id="email" name="Email" type="email" required></div><div class="field"><label for="phone">Phone *</label><input id="phone" name="Phone" type="tel" required></div><div class="field"><label for="project-type">Project type *</label><select id="project-type" name="Project Type" required><option value="">Select one</option><option>Interior / selective demolition</option><option>Structural demolition</option><option>Site clearing / preparation</option><option>Concrete / hardscape removal</option><option>Tenant improvement support</option><option>Other commercial scope</option></select></div><div class="field"><label for="timing">Desired timing</label><select id="timing" name="Desired Timing"><option value="">Select one</option><option>As soon as possible</option><option>Within 30 days</option><option>1–3 months</option><option>Planning / budgeting</option></select></div><div class="field full"><label for="location">Project location *</label><input id="location" name="Project Location" placeholder="City, state, or full project address" required></div><div class="field full"><label for="details">Describe the scope *</label><textarea id="details" name="Scope Details" placeholder="What needs to be removed? Is the building occupied? Are there plans, photos, access limitations, deadlines, or special requirements?" required></textarea></div></div><button type="submit" class="button button-primary">Request My Quote →</button><p class="form-note">This form is set up with a mail-app fallback until you connect your preferred form service. Full setup instructions are included in README.md.</p><div class="status" role="status"></div></form></div></div></div></section></main>'''
(root/'quote.html').write_text(page('Request a Quote','quote',quote,'Request a commercial demolition quote from KBS.'))

contact=f'''<main><section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Contact</div><p class="eyebrow">Contact KBS</p><h1 class="display">Let’s talk about the work.</h1><p>Reach out for project conversations, pricing requests, or questions about whether KBS is a fit for your commercial demolition scope.</p></div></section><section class="section"><div class="container grid-2"><div><p class="eyebrow">Direct contact</p><h2 class="display section-title">A straightforward way to get in touch.</h2><div class="card" style="margin-top:1.5rem"><h3>Estimating & project inquiries</h3><p><strong>Phone:</strong> <a data-phone href="tel:+12075550124">(207) 555-0124</a></p><p><strong>Email:</strong> <a data-email href="mailto:estimating@yourkbsdomain.com">estimating@yourkbsdomain.com</a></p><p><strong>Hours:</strong> Monday–Friday, 7:00 AM–5:00 PM</p></div><p class="photo-note">Replace the contact details, hours, and service-area information with KBS’s live business information before publishing.</p><a href="quote.html" class="button button-dark">Request a Quote →</a></div><div class="map-placeholder"><div><p class="eyebrow">Service area</p><h2 class="display" style="font-size:3rem">Add your primary service area here.</h2><p>This space is ready for a Google Map embed or a custom service-area graphic. The README explains both options.</p></div></div></div></section></main>'''
(root/'contact.html').write_text(page('Contact','contact',contact))

readme='''# KBS Commercial Demolition Website

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
'''
(root/'README.md').write_text(readme)
