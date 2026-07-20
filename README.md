# Ras Raaga – Bhajan Clubbing

Premium static website for **Bhajan Clubbing with Ras Raaga** — an evening of bhajans, bliss & beyond.

- **Date:** 30th August 2026  
- **Venue:** 585 Mowry Ave, Fremont, CA 94536  
- **Doors:** 4:00 PM · **Program:** 5:00 PM – 8:00 PM  
- **Artists:** BayRaagis (Live)  
- **Tickets:** [buytickets.at/rasraaga/2311367](https://buytickets.at/rasraaga/2311367)  
- **Instagram:** [@rasraaga](https://www.instagram.com/rasraaga/)

## Tech stack

- Static HTML (55 pages)
- Tailwind CSS (CDN) + custom `assets/css/main.css`
- Alpine.js (CDN) + `assets/js/main.js`
- Google Fonts: Playfair Display + Poppins
- Zero build step — deploy as-is to GitHub Pages

## Local preview

```bash
# From the project root (Python 3)
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

Or use any static server (VS Code Live Server, `npx serve`, etc.).

## GitHub Pages deployment

### Option A — Deploy from `main` (root)

1. This project targets: **https://github.com/DeploymentPlatform/RASRAGA**
2. Push to `main` (already configured as `origin`).
3. On GitHub: **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **main** / **/** (root)
4. Live site: **https://deploymentplatform.github.io/RASRAGA/**

## Regenerating pages

Shared layout and content live in the generator:

```bash
python3 scripts/generate_site.py
```

This overwrites HTML files. Edit `scripts/generate_site.py` for site-wide changes, or edit individual HTML files for one-off tweaks.

## Folder structure

```
├── index.html                 # Home
├── about/                     # About, vision, story
├── event/                     # Overview, schedule, venue, expectations, dress code
├── artists/                   # BayRaagis
├── tickets/                   # Book, FAQs, group booking
├── sponsors/                  # All sponsors + 7 partner pages
├── gallery/                   # Photos, videos, previous events
├── blog/                      # Index + 18 articles
├── community/                 # Join, volunteer, testimonials
├── legal/                     # Privacy, terms, refunds
├── faq.html
├── media-kit.html
├── spiritual-resources.html
├── newsletter-thank-you.html
├── 404.html
├── contact.html
├── assets/
│   ├── css/main.css
│   ├── js/main.js
│   └── images/logo.png, logo-white.png, logo-gold.png
└── scripts/generate_site.py
```

## Page count

**55 HTML pages** (within the 50–55 target), including 18 blog posts.

## License

Event content © 2026 Ras Raaga. All rights reserved.
