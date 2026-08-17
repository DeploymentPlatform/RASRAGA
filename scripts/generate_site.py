#!/usr/bin/env python3
"""Generate all Ras Raaga static HTML pages (50–55). Run once; no build step at deploy."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
TICKET = "https://avenueticket.com/event/bhajan-clubbing-with-ras"
IG = "https://www.instagram.com/rasraaga/"
EVENT_DATE = "30th August 2026"
VENUE = "585 Mowry Ave, Fremont, CA 94536"
VENUE_NAME = "Event Venue"
CITY = "Fremont, CA"
SITE_NAME = "Ras Raaga"
SITE_TAGLINE = "Cultural & Community Events"
SITE_BASE = "https://deploymentplatform.github.io/RASRAGA"
ADMIN_EMAIL = "hello@rasraaga.com"

# Upcoming / current events — event-specific details live on individual event pages only.
EVENTS = [
    {
        "slug": "bhajan-clubbing",
        "title": "Bhajan Clubbing with Ras Raaga",
        "short_desc": "An evening of live bhajans, community celebration, youth and family participation, and meaningful connection in Fremont.",
        "date": EVENT_DATE,
        "time": "Doors 4:00 PM · Program 5:00–8:00 PM",
        "doors": "4:00 PM",
        "program": "5:00 PM – 8:00 PM",
        "venue_name": VENUE_NAME,
        "venue": VENUE,
        "city": CITY,
        "ticket_url": TICKET,
        "ticket_price_label": None,  # Pricing shown only via official ticketing — do not invent prices
        "artists": "BayRaagis (Live)",
        "image_label": "♪",
        "published": True,
        "timezone": "America/Los_Angeles",
        # Program start/end in event timezone (ISO 8601 with offset)
        "start_at": "2026-08-30T17:00:00-07:00",
        "end_at": "2026-08-30T20:00:00-07:00",
        "highlights": [
            "Live bhajan performances with BayRaagis",
            "Family-friendly and youth-welcoming atmosphere",
            "Community celebration with sacred joy",
            "Food and beverages available from participating vendors",
            "Opportunities for sponsors and restaurant partners",
        ],
        "performances": "Live bhajan sessions featuring BayRaagis — call-and-response energy, classic repertoire, and moments of collective bliss from welcome through closing blessings.",
        "youth_family": "Children and youth are welcome with parental supervision. The evening is designed for families, first-timers, and longtime devotees alike — a warm space to clap, sing, sway, or simply receive.",
        "food_info": "Where applicable, the ticketing system may offer an optional ticket package with a food credit or food add-on — see the official ticket page for current options.",
        "ticket_categories_note": "Ticket categories and exact pricing are listed on the official ticketing platform. Example category types may include Youth Admission (Below 18 Years), General Admission, and Admission with Food Credit when offered. Do not rely on this site for prices — always confirm at checkout.",
        "instructions": [
            "Purchase tickets only through the official link on this page.",
            "Arrive by doors at 4:00 PM for a settled start.",
            "Phones on silent; capture memories respectfully.",
            "Follow volunteer and venue instructions for safety.",
            "Food is purchased separately unless you select a food-credit package at ticketing.",
        ],
        "contact_note": f"Questions about this event? Email {ADMIN_EMAIL} or use our Contact page. For ticket issues, check Ticket FAQs and your confirmation email first.",
    },
]

SPONSORS = [
    ("hashtag-india", "Hashtag India", "Indian Authentic Food", "Celebrating authentic Indian flavors that nourish body and soul."),
    ("kumar-jewelers", "Kumar Jewelers", "Fine Jewelry", "Craftsmanship and tradition — jewels that honor life's sacred moments."),
    ("instaservice", "InstaService.com", "Technology Services", "Reliable digital solutions empowering communities and businesses."),
    ("bharat-puja", "Bharat Puja & Gifts", "Puja Essentials & Gifts", "Everything you need for devotion, festivals, and sacred home rituals."),
    ("chaat-bhavan", "Chaat Bhavan", "Indian Street Food", "Beloved Bay Area chaat and comfort food with heartfelt hospitality."),
    ("mantra-india", "Mantra India", "Lifestyle & Culture", "Bringing Indian lifestyle, culture, and mindful living to the community."),
    ("forsys", "Forsys", "Enterprise Solutions", "Innovation and excellence — proudly supporting spiritual community events."),
]

# Placeholder sponsorship matrix — client will provide final packages, prices, and benefits.
SPONSOR_LEVELS = ("Silver Sponsor", "Gold Sponsor", "Platinum Sponsor", "Presenting Sponsor")
SPONSOR_BENEFITS = [
    ("Logo placement on the website", "✓", "✓", "✓", "✓"),
    ("Social media promotion", "✓", "✓", "✓", "✓"),
    ("Event flyer visibility", "—", "✓", "✓", "✓"),
    ("Stage acknowledgement", "—", "✓", "✓", "✓"),
    ("Vendor or promotional booth", "—", "—", "✓", "✓"),
    ("Event banner placement", "—", "—", "✓", "✓"),
    ("Promotional video mentions", "—", "—", "✓", "✓"),
    ("Email or community promotions", "—", "—", "—", "✓"),
    ("Complimentary passes", "Placeholder", "Placeholder", "Placeholder", "Placeholder"),
    ("On-stage brand recognition", "—", "—", "✓", "✓"),
    ("Investment / package price", "TBD*", "TBD*", "TBD*", "TBD*"),
]

BLOGS = [
    ("power-of-bhajans", "The Power of Bhajans in Modern Life", "Devotion", "2026-05-12",
     "In a world of endless notifications, bhajans offer a gentle return to the heart."),
    ("bay-area-spiritual-gatherings", "Why Bay Area Needs More Spiritual Gatherings", "Community", "2026-05-18",
     "Silicon Valley thrives on innovation — it also needs spaces of stillness and song."),
    ("meet-bayraagis", "Meet BayRaagis – The Soul Behind the Music", "Artists", "2026-05-25",
     "An intimate look at the collective bringing live bhajan energy to Fremont."),
    ("prepare-heart-bhajan-evening", "How to Prepare Your Heart for a Bhajan Evening", "Practice", "2026-06-01",
     "Simple rituals to arrive open, grounded, and ready for bliss."),
    ("top-10-bhajans", "Top 10 Bhajans That Touch the Soul", "Music", "2026-06-08",
     "Timeless names of the Divine that have moved generations to tears of joy."),
    ("raising-children-devotion", "Raising Children with Devotion in America", "Family", "2026-06-14",
     "How diaspora families keep bhakti alive for the next generation."),
    ("science-behind-chanting", "The Science Behind Chanting", "Wellness", "2026-06-20",
     "What research suggests about mantra, breath, and the nervous system."),
    ("stress-to-bliss-stories", "From Stress to Bliss – Real Stories", "Stories", "2026-06-26",
     "Community voices on how kirtan softened burnout and loneliness."),
    ("what-is-bhajan-clubbing", "What is Bhajan Clubbing?", "Event", "2026-07-01",
     "A joyful new way to gather — devotion with the energy of celebration."),
    ("creating-sacred-space-home", "Creating Sacred Space at Home", "Practice", "2026-07-05",
     "Turn a corner of your home into an altar of calm and remembrance."),
    ("interview-bayraagis", "Interview: Voices of BayRaagis", "Interview", "2026-07-08",
     "Artists share why they sing, what bhajan means, and what to expect on August 30."),
    ("countdown-august-30", "Countdown to August 30 – An Evening Awaits", "Event", "2026-07-10",
     "Mark your calendar. Soften your heart. Bliss is coming to Fremont."),
    ("sponsor-spotlight-hashtag", "Sponsor Spotlight: Hashtag India", "Sponsors", "2026-07-12",
     "How authentic food partners help make Bhajan Clubbing a full-sensory celebration."),
    ("fremont-spiritual-scene", "Fremont’s Spiritual Scene – A Quiet Renaissance", "Local", "2026-07-14",
     "Temples, sanghas, and new gatherings weaving devotion into Bay Area life."),
    ("finding-community-kirtan", "Finding Community Through Kirtan", "Community", "2026-07-15",
     "Why singing together may be the antidote to modern isolation."),
    ("evening-of-bliss", "An Evening of Bliss – What Awaits You", "Event", "2026-07-16",
     "Walk through the night: doors, music, silence, and the afterglow of Om."),
    ("namaste-next-gen", "Namaste to the Next Generation", "Family", "2026-07-17",
     "Teens, toddlers, and the timeless pull of divine names."),
    ("why-we-gather", "Why We Gather – The Heart of Ras Raaga", "Vision", "2026-07-18",
     "Beyond an event — a movement of joy, bhakti, and belonging."),
]


def depth_prefix(rel_path: str) -> str:
    parts = Path(rel_path).parts
    # file in root → ""
    if len(parts) == 1:
        return ""
    return "../" * (len(parts) - 1)


def nav_html(p: str) -> str:
    return f"""
<nav class="nav-desktop" aria-label="Primary">
  <div class="nav-item"><a class="nav-link" href="{p}index.html">Home</a></div>
  <div class="nav-item">
    <a class="nav-link" href="{p}about/index.html">About <svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg></a>
    <div class="dropdown" role="menu">
      <a href="{p}about/index.html">About Ras Raaga</a>
      <a href="{p}about/vision-mission.html">Our Vision &amp; Mission</a>
      <a href="{p}about/story.html">Our Story</a>
    </div>
  </div>
  <div class="nav-item">
    <a class="nav-link" href="{p}events/index.html">Upcoming Events <svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg></a>
    <div class="dropdown" role="menu">
      <a href="{p}events/index.html">All Upcoming Events</a>
      <a href="{p}events/bhajan-clubbing.html">Bhajan Clubbing</a>
      <a href="{p}event/schedule.html">Program Schedule</a>
      <a href="{p}event/venue.html">Venue &amp; Directions</a>
      <a href="{p}tickets/book.html">Book Tickets</a>
    </div>
  </div>
  <div class="nav-item">
    <a class="nav-link" href="{p}sponsorship.html">Sponsorship <svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg></a>
    <div class="dropdown" role="menu">
      <a href="{p}sponsorship.html">Become a Sponsor</a>
      <a href="{p}sponsors/index.html">Current Partners</a>
    </div>
  </div>
  <div class="nav-item"><a class="nav-link" href="{p}feedback.html">Feedback</a></div>
  <div class="nav-item nav-item--end">
    <a class="nav-link" href="{p}gallery/photos.html">Gallery <svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg></a>
    <div class="dropdown" role="menu">
      <a href="{p}gallery/photos.html">Photo Gallery</a>
      <a href="{p}gallery/videos.html">Video Highlights</a>
      <a href="{p}gallery/previous-events.html">Previous Events</a>
    </div>
  </div>
  <div class="nav-item"><a class="nav-link" href="{p}blog/index.html">Blog</a></div>
  <div class="nav-item nav-item--end">
    <a class="nav-link" href="{p}community/join.html">Community <svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg></a>
    <div class="dropdown" role="menu">
      <a href="{p}community/join.html">Join the Family</a>
      <a href="{p}community/volunteer.html">Volunteer</a>
      <a href="{p}community/testimonials.html">Testimonials</a>
      <a href="{p}artists/index.html">Artists</a>
    </div>
  </div>
  <div class="nav-item"><a class="nav-link" href="{p}contact.html">Contact</a></div>
</nav>"""


def mobile_nav(p: str) -> str:
    return f"""
<div class="mobile-nav" id="mobile-nav" hidden aria-label="Mobile navigation">
  <a href="{p}index.html">Home</a>
  <a href="{p}about/index.html">About</a>
  <a class="sub" href="{p}about/vision-mission.html">Vision &amp; Mission</a>
  <a class="sub" href="{p}about/story.html">Our Story</a>
  <a href="{p}events/index.html">Upcoming Events</a>
  <a class="sub" href="{p}events/bhajan-clubbing.html">Bhajan Clubbing</a>
  <a class="sub" href="{p}tickets/book.html">Book Tickets</a>
  <a href="{p}sponsorship.html">Sponsorship</a>
  <a class="sub" href="{p}sponsors/index.html">Current Partners</a>
  <a href="{p}feedback.html">Feedback</a>
  <a href="{p}gallery/photos.html">Gallery</a>
  <a href="{p}blog/index.html">Blog</a>
  <a href="{p}community/join.html">Community</a>
  <a href="{p}faq.html">FAQ</a>
  <a href="{p}contact.html">Contact</a>
  <a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
</div>"""


def header(p: str) -> str:
    return f"""
<a class="skip-link sr-only" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="logo-link" href="{p}index.html" aria-label="Ras Raaga Home">
      <img class="logo-img" src="{p}assets/images/logo.png" alt="Ras Raaga logo" width="56" height="70" decoding="async" />
      <div class="logo-text">Ras Raaga<span>{SITE_TAGLINE}</span></div>
    </a>
    {nav_html(p)}
    <div class="header-actions">
      <a class="btn btn-gold header-cta" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
      <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
{mobile_nav(p)}
"""


def footer(p: str) -> str:
    sponsor_links = "\n".join(
        f'<li><a href="{p}sponsors/{slug}.html">{name}</a></li>' for slug, name, _, _ in SPONSORS
    )
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img class="logo-img" src="{p}assets/images/logo-gold.png" alt="Ras Raaga" width="72" height="90" loading="lazy" decoding="async" />
      <p>Ras Raaga conducts and promotes cultural, community, youth, and family events — performances, activities, food experiences, and meaningful connection.</p>
      <div class="social-links mt-2" aria-label="Social media">
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram @rasraaga">IG</a>
      </div>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul class="footer-links">
        <li><a href="{p}events/index.html">Upcoming Events</a></li>
        <li><a href="{p}sponsorship.html">Sponsorship</a></li>
        <li><a href="{p}feedback.html">Feedback</a></li>
        <li><a href="{p}tickets/book.html">Tickets</a></li>
        <li><a href="{p}blog/index.html">Blog</a></li>
        <li><a href="{p}faq.html">FAQ</a></li>
      </ul>
    </div>
    <div>
      <h4>Sponsors</h4>
      <ul class="footer-links">{sponsor_links}</ul>
    </div>
    <div>
      <h4>Stay Connected</h4>
      <p style="font-size:0.9rem;margin:0">Newsletter — event updates and community news.</p>
      <form class="newsletter-form" data-newsletter data-base="{p}" action="{p}newsletter-thank-you.html" method="get">
        <label class="sr-only" for="nl-email">Email</label>
        <input id="nl-email" name="email" type="email" required placeholder="Your email" autocomplete="email" />
        <button class="btn btn-gold" type="submit">Join</button>
      </form>
      <p class="mt-2" style="font-size:0.85rem"><a href="{p}contact.html" style="color:var(--gold-light)">Contact the team</a> · <a href="{IG}" style="color:var(--gold-light)" target="_blank" rel="noopener">@rasraaga</a></p>
    </div>
  </div>
  <div class="container footer-bottom">
    <p class="mb-0">© 2026 Ras Raaga. All rights reserved.</p>
    <p class="mb-0">
      <a href="{p}legal/privacy.html">Privacy</a> ·
      <a href="{p}legal/terms.html">Terms</a> ·
      <a href="{p}legal/refund.html">Refunds</a> ·
      <a href="{p}media-kit.html">Media Kit</a> ·
      <a href="{p}sponsorship.html">Partner With Us</a>
    </p>
  </div>
</footer>
<a class="btn btn-gold float-ticket" href="{TICKET}" target="_blank" rel="noopener" aria-label="Book tickets now">Book Tickets</a>
"""


def shell(rel_path: str, title: str, description: str, body: str, og_type: str = "website", extra_json_ld: str = "") -> str:
    p = depth_prefix(rel_path)
    full_title = f"{title} | {SITE_NAME}" if title != SITE_NAME else f"{SITE_NAME} – {SITE_TAGLINE}"
    canonical = f"{SITE_BASE}/" if rel_path == "index.html" else f"{SITE_BASE}/{rel_path}"
    og_image = f"{SITE_BASE}/assets/images/logo-on-black.png"
    json_ld = extra_json_ld or f"""{{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Ras Raaga",
    "url": "{SITE_BASE}/",
    "logo": "{og_image}",
    "sameAs": ["{IG}"],
    "description": "Ras Raaga conducts and promotes cultural, community, youth, and family events across the Bay Area."
  }}"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{full_title}</title>
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#4A0E0E" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:title" content="{full_title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:url" content="{canonical}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{full_title}" />
  <meta name="twitter:description" content="{description}" />
  <link rel="icon" href="{p}assets/images/logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            maroon: {{ DEFAULT: '#4A0E0E', deep: '#2D0808', soft: '#6B1A1A' }},
            gold: {{ DEFAULT: '#D4AF37', light: '#E8C96A', dark: '#B8942D' }},
            cream: {{ DEFAULT: '#FDF6E3', dark: '#F5EBD0' }},
            saffron: '#E8A838',
            purpleaccent: '#5C3A6E'
          }},
          fontFamily: {{
            display: ['Playfair Display', 'Georgia', 'serif'],
            body: ['Poppins', 'system-ui', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  <link rel="stylesheet" href="{p}assets/css/main.css" />
  <script type="application/ld+json">
  {json_ld}
  </script>
</head>
<body class="bg-mandala page-enter" x-data="{{ mobileOpen: false }}">
  <div class="page-loader" aria-hidden="true"><div class="loader-lotus" role="status" aria-label="Loading"></div></div>
  {header(p)}
  <main id="main">{body}</main>
  {footer(p)}
  <script src="{p}assets/js/events-data.js"></script>
  <script src="{p}assets/js/main.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      var nav = document.getElementById('mobile-nav');
      if (nav) nav.removeAttribute('hidden');
    }});
  </script>
</body>
</html>
"""


def write_events_data():
    """Export published events for countdown and other client features (single source: EVENTS)."""
    payload = []
    for ev in EVENTS:
        if not ev.get("published", True):
            continue
        payload.append(
            {
                "slug": ev["slug"],
                "title": ev["title"],
                "startAt": ev["start_at"],
                "endAt": ev["end_at"],
                "timezone": ev.get("timezone", "America/Los_Angeles"),
                "published": True,
            }
        )
    js_path = ROOT / "assets" / "js" / "events-data.js"
    js_path.parent.mkdir(parents=True, exist_ok=True)
    js_path.write_text(
        "window.RASRAGA_EVENTS = " + json.dumps(payload, indent=2) + ";\n",
        encoding="utf-8",
    )
    print("✓ assets/js/events-data.js")


def page_hero(title: str, subtitle: str, crumbs: str, eyebrow: str = "Ras Raaga") -> str:
    return f"""
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">{crumbs}</nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <div class="gold-line center"></div>
    <p>{subtitle}</p>
  </div>
</section>
"""


def cta_block(p: str = "") -> str:
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-banner reveal">
      <p class="eyebrow">Join the experience</p>
      <h2>Ready for your next cultural evening?</h2>
      <p>Explore upcoming events, secure tickets through our official partner, or partner with us as a sponsor or food vendor.</p>
      <div class="flex-center mt-3">
        <a class="btn btn-gold" href="{p}events/index.html">Upcoming Events</a>
        <a class="btn btn-outline-light" href="{p}sponsorship.html">Become a Sponsor</a>
      </div>
    </div>
  </div>
</section>
"""


def event_card_html(ev: dict, p: str) -> str:
    price = (
        f'<p class="event-card-price"><strong>Tickets</strong> from {ev["ticket_price_label"]}</p>'
        if ev.get("ticket_price_label")
        else '<p class="event-card-price"><strong>Tickets</strong> Available via official booking</p>'
    )
    return f"""
<article class="event-card reveal">
  <div class="event-card-media" aria-hidden="true"><span>{ev.get("image_label", "♪")}</span></div>
  <div class="event-card-body">
    <h3>{ev["title"]}</h3>
    <p>{ev["short_desc"]}</p>
    <ul class="event-card-meta">
      <li><strong>Date</strong> {ev["date"]}</li>
      <li><strong>Time</strong> {ev["time"]}</li>
      <li><strong>Venue</strong> {ev["venue"]}</li>
      <li><strong>Location</strong> {ev["city"]}</li>
    </ul>
    {price}
    <div class="event-card-actions">
      <a class="btn btn-outline" href="{p}events/{ev["slug"]}.html">View Event Details</a>
      <a class="btn btn-gold" href="{ev["ticket_url"]}" target="_blank" rel="noopener">Get Tickets</a>
    </div>
  </div>
</article>
"""


def write(rel: str, title: str, desc: str, body: str, **kw):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(shell(rel, title, desc, body, **kw), encoding="utf-8")
    print("✓", rel)


def blog_body(title: str, category: str, date: str, lead: str, paragraphs: list, p: str) -> str:
    content = "\n".join(f"<p>{para}</p>" for para in paragraphs)
    related = "".join(
        f'<a class="blog-card reveal" href="{p}blog/{slug}.html"><div class="blog-card-img">ॐ</div><div class="blog-card-body"><div class="blog-meta">{cat}</div><h3>{t}</h3></div></a>'
        for slug, t, cat, _, _ in BLOGS[:3]
    )
    return f"""
{page_hero(title, lead, f'<a href="{p}index.html">Home</a> / <a href="{p}blog/index.html">Blog</a> / {title}')}
<section class="section">
  <article class="container-narrow prose reveal">
    <p class="blog-meta">{category} · {date}</p>
    {content}
    <div class="ticket-panel mt-4">
      <h3>Experience it live</h3>
      <p>Join Bhajan Clubbing with Ras Raaga on {EVENT_DATE} in Fremont.</p>
      <a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
    </div>
  </article>
</section>
<section class="section-sm">
  <div class="container">
    <h2 class="section-title text-center">Continue reading</h2>
    <div class="gold-line center"></div>
    <div class="grid-3 mt-3">{related}</div>
  </div>
</section>
"""


def make_blog_paragraphs(slug: str, title: str) -> list:
    """Rich unique-ish content per blog."""
    common_close = (
        f"On {EVENT_DATE}, Ras Raaga invites you to Bhajan Clubbing in Fremont — "
        "doors at 4:00 PM, program 5:00–8:00 PM, with BayRaagis live. Come as you are. Leave a little lighter."
    )
    library = {
        "power-of-bhajans": [
            "Modern life asks us to move fast. Bhajans ask us to feel deeply. When we sing the names of the Divine — Ram, Krishna, Shiva, Devi — something ancient wakes up in the nervous system. Breath slows. Shoulders drop. The heart remembers it was never alone.",
            "You do not need perfect pitch. You need presence. In community kirtan, voices weave into one offering. That is the quiet magic of bhakti: individual worry dissolves into collective joy.",
            "Whether you grew up with temple bells or discovered mantra last year, bhajans meet you where you are. They are medicine disguised as melody.",
            "Bring your stress, your longing, your gratitude. Let the rhythm hold you. Om Namah Shivaya. Jai Shri Ram. Let the evening do the rest.",
            common_close,
        ],
        "bay-area-spiritual-gatherings": [
            "The Bay Area builds the future — apps, chips, breakthroughs. Yet many of us still ache for something older: shared silence, shared song, a place where achievement is not the price of belonging.",
            "Spiritual gatherings are not escapes from modernity. They are anchors within it. Temples, yoga sanghas, and evenings like Bhajan Clubbing create pockets of sacred time in a calendar crowded with deadlines.",
            "Fremont, in particular, holds a vibrant South Asian heartbeat. Families, students, and seekers live side by side. What we need now is intentional celebration of devotion — joyful, inclusive, and beautiful.",
            "Ras Raaga exists for that reason: to make bhakti feel accessible, elegant, and alive for today’s Bay Area.",
            common_close,
        ],
        "meet-bayraagis": [
            "BayRaagis are more than performers. They are a living current of raag, rhythm, and reverence — artists who treat the stage as an altar and the audience as family.",
            "Expect live instrumentation, call-and-response energy, and moments where the room softens into hush. Their gift is not spectacle for its own sake; it is invitation.",
            "Behind every bhajan is practice, lineage, and love for the Divine Name. When BayRaagis begin, you may find your own voice rising before you notice.",
            "On August 30, they bring that soul-fire to Ras Raaga’s Bhajan Clubbing. Come ready to listen — and to sing.",
            common_close,
        ],
        "prepare-heart-bhajan-evening": [
            "Preparation is simple. Drink water. Eat lightly. Wear something that feels respectful and free. Leave the phone on silent — or better, in another room of your mind.",
            "Before you arrive, sit for three breaths. Offer a quiet intention: peace for yourself, healing for someone you love, gratitude for another day of life.",
            "If you know a few lines of a favorite bhajan, hum them on the drive. If you don’t, smile anyway. Openness is the only prerequisite.",
            "During the program, if tears come, let them. If laughter comes, share it. Bhakti is not a performance review.",
            common_close,
        ],
        "top-10-bhajans": [
            "Every heart has its own top ten. Still, some melodies travel across oceans and generations. Here are names and songs that often open the floodgates of feeling:",
            "1) Hanuman Chalisa — courage wrapped in devotion. 2) Om Jai Jagdish Hare — aarti that feels like home. 3) Raghupati Raghava — unity in the name of Ram. 4) Vaishnav Jan To — compassion as spiritual practice. 5) Shree Ram Jai Ram — the simplest path of remembrance.",
            "6) Achyutam Keshavam — lyrical love for Krishna. 7) Mahamrityunjaya — healing and protection. 8) Gayatri Mantra — clarity of mind. 9) Devi aartis — the Mother’s embrace. 10) Local favorites BayRaagis may surprise you with on the night.",
            "Come hear which ones choose you. Sometimes the bhajan finds the devotee.",
            common_close,
        ],
        "raising-children-devotion": [
            "Raising children in America with a living sense of devotion is less about rigid rules and more about warm rhythm: festival nights, gentle mantras at bedtime, stories of Rama and Sita told with joy.",
            "Kids remember how we felt more than what we preached. When they see us sing with sincerity — not pressure — they absorb belonging.",
            "Bhajan Clubbing is designed to be family-welcoming. Let children sway, clap, and watch elders wipe happy tears. That image becomes their inheritance.",
            "Between soccer practice and school apps, carve out sacred fun. Devotion can be delightful.",
            common_close,
        ],
        "science-behind-chanting": [
            "Science does not replace faith — it sometimes bows to it. Studies on mantra and group singing point toward calmer heart-rate variability, reduced perceived stress, and a rise in social bonding hormones.",
            "Repetition focuses attention. Rhythm entrains breath. Community singing may quiet the brain’s threat chatter and invite parasympathetic rest.",
            "You do not need a lab coat to feel this. One evening of kirtan often teaches what papers describe: the body softens when the Name is alive on the tongue.",
            "Come curious. Leave with data written in your own nervous system.",
            common_close,
        ],
        "stress-to-bliss-stories": [
            "“I came exhausted from back-to-back meetings. I left humming.” — a volunteer from last season’s gatherings.",
            "“As a new parent, I felt disconnected from my culture. One bhajan evening reminded me I still belong.” — a Fremont mother.",
            "“I don’t speak much Hindi, but the feeling needed no translation.” — a college student discovering kirtan.",
            "These are not miracles reserved for saints. They are ordinary grace. Stress may still return on Monday — but bliss leaves a trail you can follow home.",
            common_close,
        ],
        "what-is-bhajan-clubbing": [
            "Bhajan Clubbing is Ras Raaga’s signature experience: the depth of traditional bhajan meeting the warmth and energy of a community night out — without the emptiness of ordinary nightlife.",
            "Think soft lights, elegant aesthetics, live music, and hearts open. You come to celebrate devotion socially, joyfully, and beautifully.",
            "It is not a concert where you only watch. It is a circle where you participate — clapping, singing, smiling at strangers who feel like family by the end.",
            "August 30 is your invitation to try something sacred and new.",
            common_close,
        ],
        "creating-sacred-space-home": [
            "You do not need a large home temple. A clean shelf, a diya, a photo or murti you love, and five minutes of quiet can become a portal.",
            "Keep the space uncluttered. Add a flower when you can. Play a soft bhajan playlist in the morning. Let fragrance and sound mark the threshold between rush and reverence.",
            "After Bhajan Clubbing, bring a little of that atmosphere home. Light a lamp. Hum what stayed with you. Sacred space grows where attention rests.",
            "Your home can be a small Vrindavan of the heart.",
            common_close,
        ],
        "interview-bayraagis": [
            "Q: What does a perfect bhajan evening feel like? A: When ego leaves the stage and only offering remains — when the audience sings louder than the mic.",
            "Q: What should first-timers know? A: There is no wrong seat and no wrong voice. Sit where you can see, breathe, and smile. The music will meet you.",
            "Q: Why Fremont, why now? A: Because the Bay Area is hungry for authentic joy. Technology connects devices; bhajan connects beings.",
            "BayRaagis will bring that intention live on August 30. We can’t wait for you to feel it.",
            common_close,
        ],
        "countdown-august-30": [
            "The calendar is not just a date — it is a doorway. {EVENT_DATE} will arrive whether we prepare or not. Preparing turns arrival into pilgrimage.",
            "Tell a friend. Book tickets early. Clear your evening. Wear your favorite festive colors. Arrive by doors at 4:00 PM so you settle before the first note.",
            "Between now and then, practice small devotion: one mantra while commuting, one candle at dusk, one act of kindness without announcement.",
            "Bliss favors the ready heart.",
            common_close,
        ],
        "sponsor-spotlight-hashtag": [
            "Hashtag India brings authentic Indian food into the story of celebration. Nourishment is part of hospitality — and hospitality is part of bhakti culture.",
            "When sponsors believe in community gatherings, artists can focus on music and families can focus on presence. We are grateful for partners who understand that culture needs champions.",
            "Explore all our sponsors and consider supporting the businesses that support sacred joy.",
            common_close,
        ],
        "fremont-spiritual-scene": [
            "Fremont’s spiritual life is quietly rich: temples ringing with aarti, yoga studios humming with breath, living rooms hosting satsang, and now evenings like Bhajan Clubbing expanding what celebration can mean.",
            "The city’s diversity is its strength. When traditions share space with respect, everyone rises.",
            "Ras Raaga is proud to plant another flag of beauty and devotion on Mowry Ave — not to compete, but to contribute.",
            common_close,
        ],
        "finding-community-kirtan": [
            "Loneliness is epidemic even in crowded cities. Kirtan offers a radical alternative: synchronized hearts. You may not know the person beside you — yet you share the same Om.",
            "Community is not built by networking cards. It is built by shared vulnerability and shared joy. Singing is both.",
            "Join the Ras Raaga family. Volunteer. Return for future gatherings. Let friendship grow from the soil of devotion.",
            common_close,
        ],
        "evening-of-bliss": [
            "4:00 PM — doors open. Soft greetings. Find your place. 5:00 PM — BayRaagis begin. The room warms. By dusk, something unnamed has shifted.",
            "Expect peaks of energy and valleys of stillness. Expect familiar melodies and unexpected tears. Expect to leave with a quieter mind.",
            "Beyond the last note is the beyond: the soft afterglow where you drive home humming, already inviting someone to the next one.",
            common_close,
        ],
        "namaste-next-gen": [
            "The next generation will inherit whatever we normalize. If we normalize only hustle, they inherit hurry. If we normalize devotion with joy, they inherit belonging.",
            "Teens may roll their eyes — until a chorus hits and something true slips past irony. Toddlers may dance off-beat — and teach us presence.",
            "Bhajan Clubbing welcomes families. Bring them into the circle. Let namaste mean more than a greeting — let it mean we see the Divine in each other.",
            common_close,
        ],
        "why-we-gather": [
            "Ras Raaga gathers people because bliss multiplies in company. Because culture survives through celebration. Because the Name deserves beautiful evenings, not only private playlists.",
            "Our vision is a Bay Area where spiritual joy is public, elegant, and welcoming — where “clubbing” can mean community in the highest sense.",
            "Thank you for reading, for caring, for considering a ticket. We will see you under the soft glow of August 30.",
            "Jai Shri Ram. Om Shanti. With love, Team Ras Raaga.",
            common_close,
        ],
    }
    paras = library.get(slug)
    if not paras:
        return [
            lead_fallback(title),
            "Bhakti is both personal and communal. When we gather to sing, we remember that spirituality can be joyful, elegant, and deeply human.",
            common_close,
        ]
    return [para.format(EVENT_DATE=EVENT_DATE) if "{EVENT_DATE}" in para else para for para in paras]


def lead_fallback(title: str) -> str:
    return f"{title} — a reflection from the Ras Raaga community on devotion, belonging, and the beauty of shared song."


def generate():
    write_events_data()
    # ——— HOME ———
    p = ""
    home_event_cards = "".join(event_card_html(ev, "") for ev in EVENTS)
    write(
        "index.html",
        SITE_NAME,
        "Ras Raaga conducts and promotes cultural, community, youth, and family events — performances, food experiences, sponsorship opportunities, and community connection.",
        f"""
<section class="hero">
  <div class="container hero-content hero-content--clean">
    <div class="hero-brand">
      <img class="hero-logo" src="assets/images/logo-gold.png" alt="Ras Raaga" width="120" height="150" decoding="async" />
    </div>
    <h1>Celebrating Culture. Connecting Communities.</h1>
    <p class="hero-support">Discover vibrant cultural events, live performances, youth activities, family entertainment, food experiences, and meaningful community connections.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="events/index.html">Explore Upcoming Events</a>
      <a class="btn btn-outline-light" href="sponsorship.html">Become a Sponsor</a>
    </div>
    <div class="hero-countdown" data-next-event-countdown hidden>
      <p class="hero-countdown-heading">Countdown to Our Next Event</p>
      <p class="hero-countdown-event" data-countdown-event-title></p>
      <div class="countdown" data-countdown-units aria-live="polite">
        <div class="countdown-unit"><span class="num" data-unit="days">00</span><span class="label">Days</span></div>
        <div class="countdown-unit"><span class="num" data-unit="hours">00</span><span class="label">Hours</span></div>
        <div class="countdown-unit"><span class="num" data-unit="mins">00</span><span class="label">Minutes</span></div>
        <div class="countdown-unit"><span class="num" data-unit="secs">00</span><span class="label">Seconds</span></div>
      </div>
      <p class="hero-countdown-live" data-countdown-live hidden>The Event Is Live</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:center">
      <div class="reveal">
        <p class="eyebrow">About Ras Raaga</p>
        <h2 class="section-title">A platform for cultural &amp; community celebration</h2>
        <div class="gold-line"></div>
        <p class="section-lead">Ras Raaga organizes and promotes cultural, community, entertainment, youth, and family events. We bring people together through performances, activities, food vendors, sponsors, and shared experiences that strengthen belonging across the Bay Area.</p>
        <a class="btn btn-outline mt-2" href="about/index.html">Learn About Us</a>
      </div>
      <div class="grid-2 reveal reveal-delay-1" style="gap:1rem">
        <div class="feature-block"><div class="feature-icon">♪</div><h3>Performances</h3><p>Live music and cultural showcases that celebrate heritage with joy.</p></div>
        <div class="feature-block"><div class="feature-icon">❀</div><h3>Community</h3><p>Spaces where families, youth, and neighbors connect meaningfully.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="text-center">
      <p class="eyebrow reveal">What’s next</p>
      <h2 class="section-title reveal">Upcoming events</h2>
      <div class="gold-line center"></div>
      <p class="section-lead reveal" style="margin-inline:auto">Browse current and upcoming gatherings. Dates, venues, and tickets live on each event’s detail page.</p>
    </div>
    <div class="event-grid mt-4">{home_event_cards}</div>
    <p class="text-center mt-3"><a class="btn btn-outline" href="events/index.html">View All Upcoming Events</a></p>
  </div>
</section>

<section class="section bg-maroon">
  <div class="container text-center">
    <p class="eyebrow reveal">The experience</p>
    <h2 class="reveal">What our events offer</h2>
    <div class="gold-line center"></div>
    <p class="reveal" style="max-width:40rem;margin-inline:auto">From live performances to youth activities and family entertainment, each gathering is crafted for warmth, hospitality, and cultural pride.</p>
    <div class="grid-3 mt-4">
      <div class="feature-block reveal" style="background:rgba(255,255,255,0.06);border-color:rgba(212,175,55,0.35)"><h3 style="color:var(--cream)">Live performances</h3><p>Artists and cultural programs that bring energy and heart to every evening.</p></div>
      <div class="feature-block reveal reveal-delay-1" style="background:rgba(255,255,255,0.06);border-color:rgba(212,175,55,0.35)"><h3 style="color:var(--cream)">Youth &amp; family</h3><p>Welcoming experiences designed for all ages — participation, joy, and belonging.</p></div>
      <div class="feature-block reveal reveal-delay-2" style="background:rgba(255,255,255,0.06);border-color:rgba(212,175,55,0.35)"><h3 style="color:var(--cream)">Food &amp; vendors</h3><p>Restaurant and food vendor booths where guests can purchase meals and refreshments.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:center">
      <div class="reveal">
        <p class="eyebrow">Youth &amp; families</p>
        <h2 class="section-title">Built for the next generation — and everyone who loves them</h2>
        <div class="gold-line"></div>
        <p>Our events welcome youth participation and family-friendly experiences. Whether you are attending your first cultural evening or continuing a family tradition, there is a place for you in the circle.</p>
        <a class="btn btn-outline mt-2" href="community/join.html">Join the Community</a>
      </div>
      <div class="reveal feature-block">
        <h3>Community impact</h3>
        <p>Every gathering strengthens local culture, supports artists and vendors, and creates shared memories. Volunteers, sponsors, and attendees together make these evenings possible.</p>
        <a href="community/volunteer.html">Volunteer with us →</a>
      </div>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="grid-2">
      <div class="feature-block reveal">
        <p class="eyebrow">Sponsorship</p>
        <h2>Partner with culturally engaged audiences</h2>
        <div class="gold-line"></div>
        <p>Local businesses, restaurants, community organizations, and brands can partner with our events for meaningful visibility before, during, and after each gathering.</p>
        <a class="btn btn-gold mt-2" href="sponsorship.html">Become a Sponsor</a>
      </div>
      <div class="feature-block reveal reveal-delay-1">
        <p class="eyebrow">Restaurants &amp; food vendors</p>
        <h2>Serve the community</h2>
        <div class="gold-line"></div>
        <p>Food will be available for purchase at events. Restaurants may operate food booths, and vendor or sponsorship opportunities are available. Interested restaurants can contact the event team for participation details.</p>
        <p style="font-size:0.9rem"><em>Standard admission does not include food unless a food-credit package is selected at ticketing.</em></p>
        <a class="btn btn-outline mt-2" href="contact.html">Contact for Vendor Details</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center">
      <h2 class="section-title reveal">Proud partners</h2>
      <div class="gold-line center"></div>
    </div>
    <div class="grid-4 mt-3">
      {"".join(f'<a class="sponsor-tile reveal" href="sponsors/{s[0]}.html"><div class="name">{s[1]}</div><div class="tag">{s[2]}</div></a>' for s in SPONSORS)}
    </div>
    <p class="text-center mt-3"><a class="btn btn-outline" href="sponsors/index.html">View All Sponsors</a>
    <a class="btn btn-gold" href="sponsorship.html">Sponsorship Opportunities</a></p>
  </div>
</section>

<section class="section-sm bg-maroon">
  <div class="container text-center reveal">
    <p class="eyebrow">Your voice matters</p>
    <h2>Share your feedback</h2>
    <div class="gold-line center"></div>
    <p style="max-width:36rem;margin-inline:auto">Attendees, sponsors, vendors, and volunteers — tell us about your experience. Your feedback helps us improve future events.</p>
    <a class="btn btn-gold mt-3" href="feedback.html">Give Feedback</a>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="text-center mb-0">
      <h2 class="section-title reveal">From the blog</h2>
      <div class="gold-line center"></div>
    </div>
    <div class="grid-3 mt-3">
      {"".join(f'<a class="blog-card reveal" href="blog/{s}.html"><div class="blog-card-img">ॐ</div><div class="blog-card-body"><div class="blog-meta">{c}</div><h3>{t}</h3><p>{lead}</p></div></a>' for s,t,c,_,lead in BLOGS[:3])}
    </div>
    <p class="text-center mt-3"><a href="blog/index.html">All articles →</a></p>
  </div>
</section>
{cta_block("")}
""",
    )

    # ——— ABOUT ———
    write(
        "about/index.html",
        "About Ras Raaga",
        "Learn about Ras Raaga — a Bay Area organization conducting cultural, community, youth, and family events.",
        page_hero("About Ras Raaga", "Celebrating culture and connecting communities through joyful gatherings.", '<a href="../index.html">Home</a> / About')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Ras Raaga is an organization and platform that conducts and promotes cultural, community, entertainment, youth, and family events across the Bay Area.</p>
<p>We believe celebration can be warm, beautiful, and communal — bringing together performances, activities, food vendors, sponsors, and people of all ages who want to belong.</p>
<p>From signature evenings like Bhajan Clubbing to future cultural gatherings, our mission is to create welcoming experiences that strengthen community connection.</p>
<p>Follow our journey on Instagram <a href="{IG}" target="_blank" rel="noopener">@rasraaga</a>, explore <a href="../events/index.html">upcoming events</a>, or <a href="../sponsorship.html">partner with us</a>.</p>
<p><a class="btn btn-gold" href="../about/vision-mission.html">Vision &amp; Mission</a>
<a class="btn btn-outline" href="../events/index.html">Upcoming Events</a></p>
</div></section>{cta_block("../")}
""",
    )

    write(
        "about/vision-mission.html",
        "Vision & Mission",
        "Ras Raaga’s vision and mission — building joyful cultural community through events and belonging in the Bay Area.",
        page_hero("Our Vision & Mission", "To make cultural joy public, elegant, and welcoming.", '<a href="../index.html">Home</a> / <a href="index.html">About</a> / Vision')
        + f"""
<section class="section"><div class="container grid-2">
<div class="feature-block reveal"><h3>Vision</h3><div class="gold-line"></div>
<p>A Bay Area where culture and community are celebrated with beauty — where people of all ages gather to experience performances, connect, and belong.</p></div>
<div class="feature-block reveal reveal-delay-1"><h3>Mission</h3><div class="gold-line"></div>
<p>To curate cultural and community events, support artists and youth participation, partner with sponsors and food vendors, and grow a family rooted in kindness and shared celebration.</p></div>
</div>
<div class="container-narrow prose mt-4 reveal">
<h2>Values we hold</h2>
<ul>
<li><strong>Culture first</strong> — heritage and joy at the center.</li>
<li><strong>Inclusion</strong> — every sincere heart has a seat.</li>
<li><strong>Excellence</strong> — beauty honors community.</li>
<li><strong>Partnership</strong> — we rise by lifting sponsors, vendors, and volunteers.</li>
</ul>
</div></section>{cta_block("../")}
""",
    )

    write(
        "about/story.html",
        "Our Story",
        "How Ras Raaga began — building joyful cultural gatherings for the Bay Area community.",
        page_hero("Our Story", "When cultural heart met community celebration.", '<a href="../index.html">Home</a> / <a href="index.html">About</a> / Story')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Ras Raaga began with a simple longing: to create gatherings that feel alive for today’s Bay Area — warm, beautiful, and communal.</p>
<p>Too often, cultural life is boxed into quiet corners while celebration is outsourced to spaces that leave us empty. We imagined a bridge — meaningful programs, welcoming hospitality, and the thrill of gathering together.</p>
<p>That spark grew into events like <a href="../events/bhajan-clubbing.html">Bhajan Clubbing</a> and a broader platform for cultural, youth, and family experiences. This is only the beginning — every ticket, volunteer hour, and partnership writes the next chapter.</p>
<blockquote>We gather to celebrate culture and connect communities.</blockquote>
</div></section>{cta_block("../")}
""",
    )

    # ——— UPCOMING EVENTS ———
    events_list = "".join(event_card_html(ev, "../") for ev in EVENTS)
    write(
        "events/index.html",
        "Upcoming Events",
        "Browse current and upcoming Ras Raaga cultural and community events. View details and get tickets.",
        page_hero("Upcoming Events", "Current and future gatherings — culture, community, youth, and family.", '<a href="../index.html">Home</a> / Upcoming Events')
        + f"""
<section class="section"><div class="container">
<p class="section-lead reveal" style="max-width:40rem">Explore our upcoming events. Select an event for full details including schedule, venue, tickets, food information, and participation opportunities.</p>
<div class="event-grid mt-4">{events_list}</div>
</div></section>
""",
    )

    for ev in EVENTS:
        highlights = "".join(f"<li>{h}</li>" for h in ev["highlights"])
        instructions = "".join(f"<li>{i}</li>" for i in ev["instructions"])
        sponsor_logos = "".join(
            f'<a class="sponsor-tile" href="../sponsors/{slug}.html"><div class="name">{name}</div><div class="tag">{tag}</div></a>'
            for slug, name, tag, _ in SPONSORS
        )
        event_json_ld = f"""{{
    "@context": "https://schema.org",
    "@type": "MusicEvent",
    "name": "{ev["title"]}",
    "startDate": "2026-08-30T17:00:00-07:00",
    "endDate": "2026-08-30T20:00:00-07:00",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "eventStatus": "https://schema.org/EventScheduled",
    "location": {{
      "@type": "Place",
      "name": "{ev["venue_name"]}",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "585 Mowry Ave",
        "addressLocality": "Fremont",
        "addressRegion": "CA",
        "postalCode": "94536",
        "addressCountry": "US"
      }}
    }},
    "image": ["{SITE_BASE}/assets/images/logo-on-black.png"],
    "description": "{ev["short_desc"]}",
    "organizer": {{
      "@type": "Organization",
      "name": "Ras Raaga",
      "url": "{SITE_BASE}/"
    }},
    "offers": {{
      "@type": "Offer",
      "url": "{ev["ticket_url"]}",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-01-01"
    }},
    "performer": {{
      "@type": "MusicGroup",
      "name": "BayRaagis"
    }}
  }}"""
        write(
            f"events/{ev['slug']}.html",
            ev["title"],
            ev["short_desc"],
            page_hero(ev["title"], "Event details, tickets, and what to expect.", f'<a href="../index.html">Home</a> / <a href="index.html">Upcoming Events</a> / {ev["title"]}', eyebrow="Event details")
            + f"""
<section class="section"><div class="container">
<div class="event-banner reveal" aria-hidden="true"><span>{ev.get("image_label", "♪")}</span><strong>{ev["title"]}</strong></div>
<div class="grid-2 mt-4">
<div class="prose reveal">
<h2>About this event</h2>
<p>{ev["short_desc"]}</p>
<p>An Evening of Bhajans, Bliss &amp; Beyond — a live cultural music evening featuring <strong>{ev["artists"]}</strong>. Come for the performances; stay for community connection and family-friendly celebration.</p>
<h3>Event highlights</h3>
<ul>{highlights}</ul>
<h3>Performances &amp; activities</h3>
<p>{ev["performances"]}</p>
<h3>Youth &amp; family participation</h3>
<p>{ev["youth_family"]}</p>
<h3>Food availability</h3>
<p><strong>Food is not included with the standard admission ticket. Food and beverages will be available for purchase from participating restaurant and food vendor booths.</strong></p>
<p>{ev["food_info"]}</p>
</div>
<div class="reveal">
<div class="meta-box">
<dl>
<dt>Date</dt><dd>{ev["date"]}</dd>
<dt>Timings</dt><dd>Doors {ev["doors"]} · Program {ev["program"]}</dd>
<dt>Venue</dt><dd>{ev["venue_name"]}</dd>
<dt>Address</dt><dd>{ev["venue"]}</dd>
<dt>City</dt><dd>{ev["city"]}</dd>
<dt>Artists</dt><dd>{ev["artists"]}</dd>
</dl>
</div>
<div class="ticket-panel mt-3">
<p class="eyebrow">Official ticketing</p>
<h3>Get tickets</h3>
<p>Exact ticket categories and prices are shown on the official ticketing platform. We do not list invented prices on this site.</p>
<a class="btn btn-gold" style="width:100%;margin-bottom:0.75rem" href="{ev["ticket_url"]}" target="_blank" rel="noopener">Get Tickets</a>
<p style="font-size:0.85rem">You will be redirected to our secure ticketing partner at avenueticket.com</p>
<p class="mt-2"><a href="../tickets/faqs.html">Ticket FAQs</a> · <a href="../event/schedule.html">Schedule</a> · <a href="../event/venue.html">Venue</a></p>
</div>
</div>
</div>

<div class="grid-2 mt-4">
<div class="feature-block reveal">
<h3>Ticket categories</h3>
<p>{ev["ticket_categories_note"]}</p>
<ul>
<li>Youth Admission – Below 18 Years <em>(when offered)</em></li>
<li>General Admission</li>
<li>Admission with Food Credit <em>(optional add-on, when offered)</em></li>
</ul>
<p style="font-size:0.9rem">Confirm current categories and pricing at checkout via the Get Tickets button above.</p>
</div>
<div class="feature-block reveal">
<h3>Important instructions</h3>
<ul>{instructions}</ul>
</div>
</div>

<div class="feature-block reveal mt-4">
<h3>Contact for this event</h3>
<p>{ev["contact_note"]}</p>
<p><a class="btn btn-outline" href="../contact.html">Contact Us</a>
<a class="btn btn-outline" href="mailto:{ADMIN_EMAIL}">Email {ADMIN_EMAIL}</a></p>
</div>

<div class="mt-4 reveal">
<h2 class="section-title text-center">Sponsors &amp; partners</h2>
<div class="gold-line center"></div>
<div class="grid-4 mt-3">{sponsor_logos}</div>
<p class="text-center mt-3"><a href="../sponsors/index.html">View all sponsors</a> · <a href="../sponsorship.html">Become a sponsor</a></p>
</div>

<div class="flex-center mt-4">
<a class="btn btn-gold" href="{ev["ticket_url"]}" target="_blank" rel="noopener">Get Tickets</a>
<a class="btn btn-outline" href="../event/what-to-expect.html">What to Expect</a>
<a class="btn btn-outline" href="../event/dress-code.html">Dress Code</a>
</div>
</div></section>
""",
            extra_json_ld=event_json_ld,
        )

    # ——— EVENT (legacy detail pages — kept for existing links) ———
    write(
        "event/overview.html",
        "Event Overview",
        "Bhajan Clubbing with Ras Raaga — event overview for 30 August 2026 in Fremont with BayRaagis.",
        page_hero("Event Overview", "Everything you need to know about the evening.", '<a href="../index.html">Home</a> / <a href="../events/index.html">Upcoming Events</a> / Overview', eyebrow="Bhajan Clubbing")
        + f"""
<section class="section"><div class="container">
<div class="grid-2">
<div class="prose reveal">
<p><strong>Bhajan Clubbing with Ras Raaga</strong> is a live cultural music evening featuring <strong>BayRaagis</strong>. Come for the bhajans; stay for community connection and family-friendly celebration.</p>
<ul>
<li>Date: <strong>{EVENT_DATE}</strong></li>
<li>Venue: <strong>{VENUE}</strong></li>
<li>Doors: <strong>4:00 PM</strong></li>
<li>Program: <strong>5:00 PM – 8:00 PM</strong></li>
</ul>
<p><strong>Food is not included with the standard admission ticket.</strong> Food and beverages will be available for purchase from participating restaurant and food vendor booths.</p>
<p><a class="btn btn-gold" href="../events/bhajan-clubbing.html">Full Event Details</a>
<a class="btn btn-outline" href="{TICKET}" target="_blank" rel="noopener">Get Tickets</a>
<a class="btn btn-outline" href="schedule.html">Full Schedule</a></p>
</div>
<div class="meta-box reveal">
<dl>
<dt>Tagline</dt><dd>An Evening of Bhajans, Bliss &amp; Beyond</dd>
<dt>Artists</dt><dd>BayRaagis (Live Performances)</dd>
<dt>Best for</dt><dd>Families, youth, music lovers, first-timers</dd>
<dt>Social</dt><dd><a href="{IG}" target="_blank" rel="noopener">@rasraaga</a></dd>
</dl>
</div>
</div></div></section>{cta_block("../")}
""",
    )

    write(
        "event/schedule.html",
        "Full Program Schedule",
        "Program schedule for Ras Raaga Bhajan Clubbing — doors 4 PM, program 5–8 PM on 30 August 2026.",
        page_hero("Full Program Schedule", "A flowing evening from welcome to final Om.", '<a href="../index.html">Home</a> / <a href="overview.html">Event</a> / Schedule')
        + f"""
<section class="section"><div class="container-narrow">
<div class="timeline reveal">
<div class="timeline-item"><div class="timeline-time">4:00 PM</div><h3>Doors Open</h3><p>Arrive, settle, greet the Ras Raaga family. Light refreshments vibe and sacred ambiance as you find your place.</p></div>
<div class="timeline-item"><div class="timeline-time">4:45 PM</div><h3>Welcome &amp; Opening</h3><p>A warm introduction to the evening’s spirit — intention, gratitude, and the invitation to sing along.</p></div>
<div class="timeline-item"><div class="timeline-time">5:00 PM</div><h3>BayRaagis Live — Session I</h3><p>Opening bhajans to soften the heart and lift the room. Call-and-response begins.</p></div>
<div class="timeline-item"><div class="timeline-time">6:15 PM</div><h3>Pause &amp; Presence</h3><p>A gentle interlude — stretch, sip water, share a smile. Optional sponsor acknowledgments.</p></div>
<div class="timeline-item"><div class="timeline-time">6:30 PM</div><h3>BayRaagis Live — Session II</h3><p>Deeper repertoire, beloved classics, and moments of collective bliss.</p></div>
<div class="timeline-item"><div class="timeline-time">7:45 PM</div><h3>Closing Blessings</h3><p>Final offerings, gratitude, and a shared Om to carry home.</p></div>
<div class="timeline-item"><div class="timeline-time">8:00 PM</div><h3>Program Concludes</h3><p>Depart with peace. Continue the night’s glow with friends and family.</p></div>
</div>
<p class="text-center mt-3"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Your Seat</a></p>
<p class="text-center" style="font-size:0.9rem">Schedule may flex slightly to honor the flow of live devotion.</p>
</div></section>
""",
    )

    write(
        "event/venue.html",
        "Venue & Directions",
        "Venue and directions for Ras Raaga Bhajan Clubbing at 585 Mowry Ave, Fremont, CA 94536.",
        page_hero("Venue & Directions", VENUE, '<a href="../index.html">Home</a> / <a href="overview.html">Event</a> / Venue')
        + f"""
<section class="section"><div class="container">
<div class="grid-2">
<div class="reveal prose">
<h2>Find us in Fremont</h2>
<p>We gather at <strong>{VENUE}</strong>. Plan extra time for parking and a calm arrival before doors open at 4:00 PM.</p>
<h3>Getting here</h3>
<ul>
<li><strong>By car:</strong> Use GPS for 585 Mowry Ave, Fremont. Arrive early for parking ease.</li>
<li><strong>Rideshare:</strong> Drop off at the main entrance; pin the address in your app.</li>
<li><strong>Public transit:</strong> Check local AC Transit / BART + rideshare combinations for your starting point.</li>
</ul>
<h3>Accessibility</h3>
<p>If you need seating assistance or accessibility support, email us via the <a href="../contact.html">contact page</a> before the event.</p>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
</div>
<div class="reveal">
<div class="map-embed">
<iframe title="Map of 585 Mowry Ave Fremont" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
src="https://maps.google.com/maps?q=585%20Mowry%20Ave%2C%20Fremont%2C%20CA%2094536&t=&z=15&ie=UTF8&iwloc=&output=embed"></iframe>
</div>
<p class="mt-2" style="font-size:0.9rem"><a href="https://www.google.com/maps/search/?api=1&query=585+Mowry+Ave+Fremont+CA+94536" target="_blank" rel="noopener">Open in Google Maps →</a></p>
</div>
</div></div></section>
""",
    )

    write(
        "event/what-to-expect.html",
        "What to Expect",
        "What to expect at Ras Raaga Bhajan Clubbing — music, atmosphere, community, and how to prepare.",
        page_hero("What to Expect", "Joyful devotion, live music, and a premium spiritual atmosphere.", '<a href="../index.html">Home</a> / Event / What to Expect')
        + f"""
<section class="section"><div class="container">
<div class="grid-3">
<div class="feature-block reveal"><h3>Sound</h3><p>Live bhajans with BayRaagis — immersive, heartfelt, sing-along friendly.</p></div>
<div class="feature-block reveal"><h3>Space</h3><p>Elegant décor with maroon-and-gold warmth, soft lighting, and sacred accents.</p></div>
<div class="feature-block reveal"><h3>People</h3><p>Families, friends, and seekers — a welcoming Ras Raaga family vibe.</p></div>
<div class="feature-block reveal"><h3>Flow</h3><p>Doors at 4, program 5–8, with natural pauses for presence and comfort.</p></div>
<div class="feature-block reveal"><h3>Participation</h3><p>Clap, sing, sway — or simply receive. All levels of familiarity are welcome.</p></div>
<div class="feature-block reveal"><h3>Afterglow</h3><p>Leave lighter. Many guests describe a calm that lasts into the week.</p></div>
</div>
<div class="text-center mt-4"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
<a class="btn btn-outline" href="dress-code.html">Dress Code</a></div>
</div></section>
""",
    )

    write(
        "event/dress-code.html",
        "Dress Code & Guidelines",
        "Dress code and guest guidelines for Ras Raaga Bhajan Clubbing in Fremont.",
        page_hero("Dress Code & Guidelines", "Festive, respectful, and comfortable.", '<a href="../index.html">Home</a> / Event / Dress Code')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<h2>Suggested attire</h2>
<p>Indian festive wear is encouraged — kurta, saree, salwar, elegant western modest attire. Colors of maroon, cream, gold, and saffron echo the evening beautifully. Wear what helps you feel both respectful and free to clap and sway.</p>
<h2>Guidelines</h2>
<ul>
<li>Arrive by <strong>4:00 PM</strong> doors for a settled start.</li>
<li>Phones on silent; capture memories respectfully without blocking views.</li>
<li>Fragrance: keep light out of consideration for others.</li>
<li>Children welcome with parental supervision.</li>
<li>No outside disruption; this is a sacred celebration.</li>
<li>Follow volunteer and venue instructions for safety.</li>
</ul>
<p>Questions? Visit our <a href="../faq.html">FAQ</a> or <a href="../contact.html">Contact</a> page.</p>
<p><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a></p>
</div></section>
""",
    )

    # ——— ARTISTS ———
    write(
        "artists/index.html",
        "BayRaagis – Artists",
        "Meet BayRaagis — live performers at Ras Raaga Bhajan Clubbing on 30 August 2026.",
        page_hero("BayRaagis", "The soul behind the music — live at Bhajan Clubbing.", '<a href="../index.html">Home</a> / Artists')
        + f"""
<section class="section"><div class="container">
<div class="grid-2" style="align-items:center">
<div class="reveal" style="min-height:280px;border-radius:16px;background:linear-gradient(145deg,var(--maroon),var(--purple));display:flex;align-items:center;justify-content:center;color:var(--gold);font-family:var(--font-display);font-size:3rem;">♪ BayRaagis</div>
<div class="prose reveal">
<p>BayRaagis bring living raag and heartfelt bhakti to the stage. Their performances balance musical excellence with humble offering — inviting every guest into the circle of song.</p>
<p>At Ras Raaga’s Bhajan Clubbing, expect an evening crafted for both listening and participating. From classic bhajans to soul-stirring crescendos, BayRaagis carry the room from welcome to final blessing.</p>
<p><a href="../blog/meet-bayraagis.html">Read: Meet BayRaagis</a> · <a href="../blog/interview-bayraagis.html">Artist Interview</a></p>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Hear Them Live — Book Tickets</a>
</div>
</div></div></section>{cta_block("../")}
""",
    )

    # ——— TICKETS ———
    write(
        "tickets/book.html",
        "Book Tickets",
        "Book tickets for Ras Raaga events via our official ticketing partner. Current event: Bhajan Clubbing, 30 August 2026, Fremont.",
        page_hero("Book Tickets", "Secure your place through our official ticketing partner.", '<a href="../index.html">Home</a> / Tickets', eyebrow="Official ticketing")
        + f"""
<section class="section"><div class="container" style="max-width:640px">
<div class="ticket-panel reveal">
<p class="eyebrow">Current event</p>
<h2>Bhajan Clubbing with Ras Raaga</h2>
<p>{EVENT_DATE} · {VENUE}<br/>Doors 4:00 PM · Program 5:00–8:00 PM · BayRaagis Live</p>
<div class="gold-line center"></div>
<a class="btn btn-gold" style="width:100%;margin-bottom:0.75rem" href="{TICKET}" target="_blank" rel="noopener">Buy Tickets Now</a>
<p style="font-size:0.85rem">You will be redirected to our secure ticketing partner at avenueticket.com</p>
<p class="mt-2" style="font-size:0.9rem"><strong>Food is not included with the standard admission ticket.</strong> Food and beverages will be available for purchase from participating vendors. Optional food-credit packages may appear on the ticketing page when offered.</p>
<p class="mt-2"><a href="../events/bhajan-clubbing.html">Event Details</a> · <a href="faqs.html">Ticket FAQs</a> · <a href="group-booking.html">Group Booking</a> · <a href="../legal/refund.html">Refund Policy</a></p>
</div>
</div></section>
""",
    )

    write(
        "tickets/faqs.html",
        "Ticket FAQs",
        "Frequently asked questions about tickets for Ras Raaga Bhajan Clubbing.",
        page_hero("Ticket FAQs", "Clear answers before you book.", '<a href="../index.html">Home</a> / Tickets / FAQs')
        + f"""
<section class="section"><div class="container-narrow">
<details class="faq-item reveal"><summary>Where do I buy tickets?</summary><p>Only through our official link: <a href="{TICKET}" target="_blank" rel="noopener">avenueticket.com/event/bhajan-clubbing-with-ras</a>.</p></details>
<details class="faq-item reveal"><summary>Are tickets refundable?</summary><p>Please review our <a href="../legal/refund.html">Refund Policy</a>. Policies of the ticketing platform also apply.</p></details>
<details class="faq-item reveal"><summary>Can I buy tickets at the door?</summary><p>Door availability is not guaranteed. We strongly recommend booking online in advance.</p></details>
<details class="faq-item reveal"><summary>Do children need tickets?</summary><p>Please follow the age and ticket rules listed on the ticketing page at purchase time.</p></details>
<details class="faq-item reveal"><summary>Group of 8+?</summary><p>See <a href="group-booking.html">Group Booking</a> for guidance.</p></details>
<p class="mt-4 text-center"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a></p>
</div></section>
""",
    )

    write(
        "tickets/group-booking.html",
        "Group Booking",
        "Group booking information for families, sanghas, and friends attending Ras Raaga Bhajan Clubbing.",
        page_hero("Group Booking", "Bring your circle — bliss multiplies together.", '<a href="../index.html">Home</a> / Tickets / Group')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Planning to attend with family, friends, or your local satsang? Groups create the warmest energy in the room.</p>
<h2>How to book as a group</h2>
<ol>
<li>Purchase the required quantity via the <a href="{TICKET}" target="_blank" rel="noopener">official ticket link</a>.</li>
<li>For large groups (10+) or special seating questions, <a href="../contact.html">contact us</a> with your group size and names.</li>
<li>Arrive together by doors at 4:00 PM when possible.</li>
</ol>
<p>Corporate or sponsor group packages may be available — see <a href="../sponsorship.html">Sponsorship</a>.</p>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Group Tickets</a>
</div></section>
""",
    )

    # ——— SPONSORS & SPONSORSHIP ———
    benefit_rows = "".join(
        f"<tr><th scope=\"row\">{row[0]}</th>"
        + "".join(f"<td>{cell}</td>" for cell in row[1:])
        + "</tr>"
        for row in SPONSOR_BENEFITS
    )
    level_headers = "".join(f"<th scope=\"col\">{lvl}</th>" for lvl in SPONSOR_LEVELS)
    write(
        "sponsorship.html",
        "Become a Sponsor",
        "Partner with Ras Raaga — sponsorship opportunities for businesses, restaurants, and community organizations.",
        page_hero("Become a Sponsor", "Meaningful visibility with families, youth, and culturally engaged audiences.", '<a href="index.html">Home</a> / Sponsorship')
        + f"""
<section class="section"><div class="container">
<div class="container-narrow prose reveal" style="max-width:48rem;margin-inline:auto">
<p>Partner with us to connect your business with families, youth, community leaders, and culturally engaged audiences. Our sponsorship opportunities are designed to provide meaningful visibility before, during, and after each event.</p>
<p>Local businesses, restaurants, community organizations, and brands are welcome to partner with Ras Raaga events. Restaurants and food businesses may also participate as sponsors or food vendors — food will be available for purchase at events, and restaurants may operate food booths.</p>
</div>

<div class="reveal mt-4">
<h2 class="section-title text-center">Sponsorship levels</h2>
<div class="gold-line center"></div>
<p class="text-center section-lead" style="margin-inline:auto">The comparison below is a placeholder structure. Final packages, prices, and benefits will be provided by the client and can be updated easily.</p>
<div class="table-wrap mt-3">
<table class="sponsor-table">
<thead><tr><th scope="col">Benefit</th>{level_headers}</tr></thead>
<tbody>{benefit_rows}</tbody>
</table>
</div>
<p class="text-center mt-2" style="font-size:0.85rem">*TBD and Placeholder values are editable until final sponsorship packages are confirmed. Benefits shown are illustrative, not guarantees.</p>
</div>

<div class="grid-2 mt-4">
<div class="feature-block reveal">
<h3>Restaurant &amp; food vendor participation</h3>
<ul>
<li>Food will be available for purchase at the event.</li>
<li>Restaurants may operate food booths.</li>
<li>Vendor and sponsorship opportunities are available.</li>
<li>Interested restaurants can contact the event team for participation details.</li>
</ul>
<p>Food is not included with every ticket. Guests purchase food separately unless they select an optional food-credit package at ticketing (when offered).</p>
</div>
<div class="feature-block reveal" id="sponsorship-enquiry">
<h3>Request sponsorship details</h3>
<p>Tell us about your business and we will share the latest packages when available.</p>
<div class="form-status" data-form-status hidden role="status"></div>
<form class="site-form" data-mail-form data-mail-to="{ADMIN_EMAIL}" data-mail-subject="Sponsorship Enquiry">
<label for="sp-name">Full Name <span class="req">*</span></label>
<input id="sp-name" name="name" required autocomplete="name" />
<label for="sp-email">Email Address <span class="req">*</span></label>
<input id="sp-email" name="email" type="email" required autocomplete="email" />
<label for="sp-org">Business / Organization</label>
<input id="sp-org" name="organization" autocomplete="organization" />
<label for="sp-phone">Phone Number</label>
<input id="sp-phone" name="phone" type="tel" autocomplete="tel" />
<label for="sp-interest">Interest</label>
<select id="sp-interest" name="interest">
<option value="Sponsorship package details">Sponsorship package details</option>
<option value="Food vendor booth">Food vendor booth</option>
<option value="Both sponsorship and vendor">Both sponsorship and vendor</option>
<option value="Other partnership">Other partnership</option>
</select>
<label for="sp-msg">Message <span class="req">*</span></label>
<textarea id="sp-msg" name="message" rows="4" required placeholder="Tell us about your goals and preferred event(s)."></textarea>
<button class="btn btn-gold" type="submit">Request Sponsorship Details</button>
</form>
</div>
</div>

<p class="text-center mt-4"><a class="btn btn-outline" href="sponsors/index.html">View Current Partners</a>
<a class="btn btn-outline" href="contact.html">General Contact</a></p>
</div></section>
""",
    )

    write(
        "sponsors/index.html",
        "Our Sponsors",
        "Meet the sponsors supporting Ras Raaga events — partners in culture, food, and community.",
        page_hero("Our Sponsors", "Grateful to the partners who make community celebration possible.", '<a href="../index.html">Home</a> / Sponsors')
        + f"""
<section class="section"><div class="container">
<div class="grid-3">
{"".join(f'''<a class="sponsor-tile reveal" href="{slug}.html">
<div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,rgba(212,175,55,0.3),rgba(74,14,14,0.15));display:flex;align-items:center;justify-content:center;font-family:var(--font-display);color:var(--maroon);font-size:1.4rem">{name[0]}</div>
<div class="name">{name}</div><div class="tag">{tag}</div></a>''' for slug, name, tag, _ in SPONSORS)}
</div>
<p class="text-center mt-4"><a class="btn btn-gold" href="../sponsorship.html">Become a Sponsor</a>
<a class="btn btn-outline" href="../sponsorship.html#sponsorship-enquiry">Request Sponsorship Details</a></p>
<div class="container-narrow prose mt-4 reveal text-center">
<h2>Partnership opportunities</h2>
<p>Silver, Gold, Platinum, and Presenting sponsorship levels are available as placeholder structures until final packages are confirmed. Restaurants may also participate as food vendors. See our <a href="../sponsorship.html">Sponsorship</a> page for the comparison table and enquiry form.</p>
</div>
</div></section>
""",
    )

    for slug, name, tag, blurb in SPONSORS:
        write(
            f"sponsors/{slug}.html",
            f"{name} – Sponsor",
            f"{name} proudly sponsors Ras Raaga Bhajan Clubbing. {blurb}",
            page_hero(name, tag, f'<a href="../index.html">Home</a> / <a href="index.html">Sponsors</a> / {name}')
            + f"""
<section class="section"><div class="container-narrow prose reveal">
<div class="sponsor-tile" style="margin-bottom:2rem">
<div style="width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,var(--gold-light),var(--maroon));display:flex;align-items:center;justify-content:center;color:white;font-family:var(--font-display);font-size:2rem">{name[0]}</div>
<div class="name">{name}</div><div class="tag">{tag}</div>
</div>
<p>{blurb}</p>
<p>Ras Raaga is honored to partner with <strong>{name}</strong> for Bhajan Clubbing on {EVENT_DATE}. Their support helps us create a premium, welcoming evening of live bhajans with BayRaagis for the Bay Area community.</p>
<p>When you support businesses that support culture, everyone rises. Please keep {name} in mind — and join us in thanking all sponsors who believe in joyful devotion.</p>
<p><a class="btn btn-outline" href="index.html">All Sponsors</a>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
<a class="btn btn-outline" href="../contact.html">Partner With Us</a></p>
</div></section>
""",
        )

    # ——— GALLERY ———
    gallery_items = "".join(
        f'<div class="gallery-item reveal"><div class="gallery-pattern">{"❀♪ॐ"[i%3]}</div><div class="caption">{cap}</div></div>'
        for i, cap in enumerate([
            "Evening glow · devotion in light",
            "Hands in rhythm · hearts in sync",
            "BayRaagis energy · live raag",
            "Community smiles · Fremont family",
            "Maroon & gold · sacred ambiance",
            "Children swaying · next generation",
            "Collective Om · closing peace",
            "Volunteer warmth · seva in action",
            "Anticipation · doors at dusk",
        ])
    )
    write(
        "gallery/photos.html",
        "Photo Gallery",
        "Photo gallery from Ras Raaga gatherings — glimpses of bhajan, community, and bliss.",
        page_hero("Photo Gallery", "Moments of devotion, joy, and togetherness.", '<a href="../index.html">Home</a> / Gallery')
        + f"""
<section class="section"><div class="container">
<div class="grid-3">{gallery_items}</div>
<p class="text-center mt-4" style="font-size:0.9rem">Gallery grows after each gathering. Tag us <a href="{IG}" target="_blank" rel="noopener">@rasraaga</a> with your photos.</p>
<p class="text-center"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Be in the Next Frame — Book Tickets</a></p>
</div></section>
""",
    )

    write(
        "gallery/videos.html",
        "Video Highlights",
        "Video highlights from Ras Raaga and Bhajan Clubbing previews.",
        page_hero("Video Highlights", "Feel the energy before you arrive.", '<a href="../index.html">Home</a> / Gallery / Videos')
        + f"""
<section class="section"><div class="container">
<div class="grid-2">
<div class="feature-block reveal" style="min-height:220px;display:flex;flex-direction:column;justify-content:center;text-align:center;background:linear-gradient(145deg,var(--maroon),var(--purple));color:var(--cream);border:none">
<div style="font-size:2.5rem;color:var(--gold)">▶</div>
<h3 style="color:var(--cream)">Bhajan Clubbing Teaser</h3>
<p style="color:rgba(253,246,227,0.85)">Coming soon on Instagram @rasraaga</p>
</div>
<div class="feature-block reveal" style="min-height:220px;display:flex;flex-direction:column;justify-content:center;text-align:center;background:linear-gradient(145deg,var(--maroon-soft),var(--maroon-deep));color:var(--cream);border:none">
<div style="font-size:2.5rem;color:var(--gold)">▶</div>
<h3 style="color:var(--cream)">BayRaagis Moments</h3>
<p style="color:rgba(253,246,227,0.85)">Live clips shared closer to {EVENT_DATE}</p>
</div>
</div>
<p class="text-center mt-4"><a class="btn btn-outline" href="{IG}" target="_blank" rel="noopener">Watch on Instagram</a>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a></p>
</div></section>
""",
    )

    write(
        "gallery/previous-events.html",
        "Previous Events",
        "Recaps of previous Ras Raaga gatherings and the path to Bhajan Clubbing 2026.",
        page_hero("Previous Events", "Every gathering plants seeds for the next bloom.", '<a href="../index.html">Home</a> / Gallery / Previous')
        + f"""
<section class="section"><div class="container">
<div class="grid-2">
<div class="feature-block reveal">
<p class="eyebrow">Community Recap</p>
<h3>Early Ras Raaga Gatherings</h3>
<p>Intimate evenings of song and connection that proved a simple truth: the Bay Area hungers for beautiful bhakti spaces. Those nights inspired the scale and elegance of Bhajan Clubbing.</p>
</div>
<div class="feature-block reveal">
<p class="eyebrow">Looking Ahead</p>
<h3>August 30, 2026 — The Milestone</h3>
<p>Bhajan Clubbing is our most ambitious offering yet — live with BayRaagis, premium hospitality, and a full community celebration at {VENUE}.</p>
<a class="btn btn-gold mt-2" href="{TICKET}" target="_blank" rel="noopener">Join This Chapter</a>
</div>
</div>
<div class="prose container-narrow mt-4 reveal">
<h2>What we learned</h2>
<ul>
<li>People want devotion that feels joyful, not intimidating.</li>
<li>Live artists transform atmosphere instantly.</li>
<li>Volunteers and sponsors are the invisible scaffolding of bliss.</li>
<li>Families come when the space feels safe, warm, and beautiful.</li>
</ul>
</div>
</div></section>
""",
    )

    # ——— BLOG ———
    blog_cards = "".join(
        f'<a class="blog-card reveal" href="{slug}.html"><div class="blog-card-img">ॐ</div><div class="blog-card-body"><div class="blog-meta">{cat} · {date}</div><h3>{title}</h3><p>{lead}</p></div></a>'
        for slug, title, cat, date, lead in BLOGS
    )
    write(
        "blog/index.html",
        "Blog",
        "Ras Raaga blog — reflections on bhajan, community, devotion, and Bhajan Clubbing in the Bay Area.",
        page_hero("Blog & Reflections", "Stories, guides, and inspiration for the journey of bhakti.", '<a href="../index.html">Home</a> / Blog')
        + f"""
<section class="section"><div class="container">
<div class="grid-3">{blog_cards}</div>
</div></section>
""",
    )

    for slug, title, cat, date, lead in BLOGS:
        paras = make_blog_paragraphs(slug, title)
        write(
            f"blog/{slug}.html",
            title,
            lead,
            blog_body(title, cat, date, lead, paras, "../"),
            og_type="article",
        )

    # ——— COMMUNITY ———
    write(
        "community/join.html",
        "Join the Ras Raaga Family",
        "Join the Ras Raaga family — stay connected for events, seva, and spiritual community in the Bay Area.",
        page_hero("Join the Ras Raaga Family", "Belonging begins with a single Om.", '<a href="../index.html">Home</a> / Community')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<div id="subscribed-msg" class="ticket-panel" style="display:none;margin-bottom:2rem">
<h3>You are on the list ✦</h3>
<p>Thank you for subscribing. We will share gentle event updates and devotion notes — never spam, always with heart.</p>
</div>
<p>The Ras Raaga family is everyone who longs for joyful devotion — artists, parents, students, elders, and curious first-timers.</p>
<h2>Ways to join</h2>
<ul>
<li>Book tickets for <strong>{EVENT_DATE}</strong> and experience Bhajan Clubbing.</li>
<li>Follow <a href="{IG}" target="_blank" rel="noopener">@rasraaga</a> on Instagram.</li>
<li>Subscribe to our newsletter (footer form).</li>
<li><a href="volunteer.html">Volunteer</a> with seva spirit.</li>
<li>Share the event with three friends who need more bliss.</li>
</ul>
<a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
<a class="btn btn-outline" href="volunteer.html">Volunteer</a>
</div></section>
<script>
if (new URLSearchParams(location.search).get('subscribed')) {{
  var m = document.getElementById('subscribed-msg');
  if (m) m.style.display = 'block';
}}
</script>
""",
    )

    write(
        "community/volunteer.html",
        "Volunteer",
        "Volunteer with Ras Raaga — seva opportunities for Bhajan Clubbing on 30 August 2026.",
        page_hero("Volunteer With Us", "Seva is love in motion.", '<a href="../index.html">Home</a> / Community / Volunteer')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Volunteers are the quiet heroes of every sacred gathering — welcoming guests, guiding flow, and holding the space with kindness.</p>
<h2>Roles may include</h2>
<ul>
<li>Guest welcome &amp; check-in support</li>
<li>Seating guidance</li>
<li>Stage/backstage coordination support</li>
<li>Hospitality &amp; water stations</li>
<li>Photo/social documentation (as assigned)</li>
</ul>
<p>To express interest, visit our <a href="../contact.html">Contact</a> page with subject line <strong>Volunteer – August 30</strong> and share your skills and availability.</p>
<a class="btn btn-gold" href="../contact.html">Contact to Volunteer</a>
</div></section>
""",
    )

    write(
        "community/testimonials.html",
        "Testimonials",
        "Testimonials from the Ras Raaga community — voices of bliss, belonging, and bhajan.",
        page_hero("Testimonials", "Voices from the heart of our community.", '<a href="../index.html">Home</a> / Community / Testimonials')
        + f"""
<section class="section"><div class="container grid-2">
<blockquote class="testimonial reveal">“I came tired. I left humming. Ras Raaga reminded me that devotion can feel like celebration.”<cite>— Ananya, San Jose</cite></blockquote>
<blockquote class="testimonial reveal">“My kids actually asked when the next bhajan night is. That has never happened before.”<cite>— Rohit, Fremont</cite></blockquote>
<blockquote class="testimonial reveal">“BayRaagis made the room feel like one family. Tears, claps, smiles — all welcome.”<cite>— Meera, Sunnyvale</cite></blockquote>
<blockquote class="testimonial reveal">“Premium without pretension. Spiritual without stiffness. Exactly what the Bay Area needed.”<cite>— Kabir, Oakland</cite></blockquote>
</div>
<p class="text-center mt-4"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Create Your Own Story — Book Tickets</a></p>
</section>
""",
    )

    # ——— CONTACT ———
    write(
        "contact.html",
        "Contact",
        "Contact Ras Raaga for event questions, volunteering, press, sponsorship, and vendor participation.",
        page_hero("Contact Us", "We would love to hear from you.", '<a href="index.html">Home</a> / Contact')
        + f"""
<section class="section"><div class="container grid-2">
<div class="prose reveal">
<h2>Get in touch</h2>
<p>For ticket issues, please first check <a href="tickets/faqs.html">Ticket FAQs</a> and your ticketing confirmation email.</p>
<p><strong>Email:</strong> <a href="mailto:{ADMIN_EMAIL}">{ADMIN_EMAIL}</a><br/>
<strong>Instagram:</strong> <a href="{IG}" target="_blank" rel="noopener">@rasraaga</a></p>
<p>For partnerships and food vendor participation, see <a href="sponsorship.html">Sponsorship</a>. For press, see <a href="media-kit.html">Media Kit</a>. To share your experience, visit <a href="feedback.html">Feedback</a>.</p>
<p><a href="events/index.html">View upcoming events →</a></p>
</div>
<div>
<div class="form-status" data-form-status hidden role="status"></div>
<form class="feature-block reveal site-form" data-mail-form data-mail-to="{ADMIN_EMAIL}" data-mail-subject="Website Contact">
<label for="name">Name <span class="req">*</span></label>
<input id="name" name="name" required autocomplete="name" placeholder="Your name" />
<label for="email">Email <span class="req">*</span></label>
<input id="email" name="email" type="email" required autocomplete="email" placeholder="you@email.com" />
<label for="msg">Message <span class="req">*</span></label>
<textarea id="msg" name="message" rows="5" required placeholder="How can we help?"></textarea>
<button class="btn btn-gold" type="submit">Send Message</button>
</form>
</div>
</div></section>
""",
    )

    # ——— FEEDBACK ———
    event_options = "".join(
        f'<option value="{ev["title"]}">{ev["title"]}</option>' for ev in EVENTS
    )
    write(
        "feedback.html",
        "Feedback",
        "Share feedback with Ras Raaga — attendees, sponsors, vendors, and volunteers help us improve future events.",
        page_hero("Feedback", "Your feedback helps us improve future events and create better experiences for our community.", '<a href="index.html">Home</a> / Feedback')
        + f"""
<section class="section"><div class="container" style="max-width:720px">
<p class="section-lead reveal">Attendees, sponsors, vendors, volunteers, and visitors are invited to report their experience. Submitted feedback is sent to our administrative team and is not displayed publicly.</p>
<div class="form-status reveal" data-form-status hidden role="status"></div>
<form class="feature-block reveal site-form mt-3" data-mail-form data-mail-to="{ADMIN_EMAIL}" data-mail-subject="Event Feedback" data-allow-file="true">
<label for="fb-name">Full Name <span class="req">*</span></label>
<input id="fb-name" name="name" required autocomplete="name" />

<label for="fb-email">Email Address <span class="req">*</span></label>
<input id="fb-email" name="email" type="email" required autocomplete="email" />

<label for="fb-phone">Phone Number</label>
<input id="fb-phone" name="phone" type="tel" autocomplete="tel" />

<label for="fb-event">Event Attended <span class="req">*</span></label>
<select id="fb-event" name="event_attended" required>
<option value="">Select an event</option>
{event_options}
<option value="Other / General">Other / General</option>
</select>

<label for="fb-category">Feedback Category <span class="req">*</span></label>
<select id="fb-category" name="category" required>
<option value="">Select a category</option>
<option>General Experience</option>
<option>Ticketing</option>
<option>Venue</option>
<option>Food and Vendors</option>
<option>Performances</option>
<option>Youth Activities</option>
<option>Sponsorship</option>
<option>Accessibility</option>
<option>Complaint</option>
<option>Suggestion</option>
<option>Other</option>
</select>

<label for="fb-rating">Rating <span class="req">*</span></label>
<select id="fb-rating" name="rating" required>
<option value="">Select a rating</option>
<option value="5">5 — Excellent</option>
<option value="4">4 — Good</option>
<option value="3">3 — Average</option>
<option value="2">2 — Poor</option>
<option value="1">1 — Very Poor</option>
</select>

<label for="fb-message">Message or Feedback <span class="req">*</span></label>
<textarea id="fb-message" name="message" rows="5" required placeholder="Share your experience, suggestions, or concerns."></textarea>

<label for="fb-file">Photo or File Upload</label>
<input id="fb-file" name="attachment" type="file" accept="image/*,.pdf,.doc,.docx" />
<p class="form-hint">After you submit, your email app will open. Please attach the selected file to that email before sending.</p>

<label class="form-check" for="fb-permission">
<input id="fb-permission" name="permission_to_contact" type="checkbox" value="Yes" />
<span>Permission to Contact — Ras Raaga may follow up about this feedback</span>
</label>

<button class="btn btn-gold" type="submit">Submit Feedback</button>
</form>
</div></section>
""",
    )

    # ——— LEGAL ———
    write(
        "legal/privacy.html",
        "Privacy Policy",
        "Privacy Policy for the Ras Raaga website and Bhajan Clubbing communications.",
        page_hero("Privacy Policy", "Your trust matters to us.", '<a href="../index.html">Home</a> / Legal / Privacy')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Last updated: July 2026. Ras Raaga (“we”) respects your privacy.</p>
<h2>Information we collect</h2>
<p>If you subscribe to our newsletter or contact us, we may collect your name, email, and message content. Ticket purchases are processed by our ticketing partner; their privacy policy applies to payment data.</p>
<h2>How we use information</h2>
<p>We use contact details to respond to inquiries, share event updates, and improve our community offerings. We do not sell your personal information.</p>
<h2>Cookies &amp; analytics</h2>
<p>Our static site may use basic hosting analytics. Third-party embeds (maps, fonts, CDNs) may set their own cookies per their policies.</p>
<h2>Contact</h2>
<p>Questions? Visit our <a href="../contact.html">Contact</a> page.</p>
</div></section>
""",
    )

    write(
        "legal/terms.html",
        "Terms & Conditions",
        "Terms and conditions for attending Ras Raaga Bhajan Clubbing and using this website.",
        page_hero("Terms & Conditions", "Please read before attending.", '<a href="../index.html">Home</a> / Legal / Terms')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>By using this website and attending Bhajan Clubbing with Ras Raaga, you agree to these terms.</p>
<h2>Event admission</h2>
<p>Valid tickets are required. Ras Raaga and venue staff may refuse entry for safety or disruptive conduct. Schedule and artists are subject to reasonable adjustments.</p>
<h2>Code of conduct</h2>
<p>Guests agree to treat volunteers, artists, and fellow attendees with respect. Harassment or disruption may result in removal without refund where permitted by policy.</p>
<h2>Media</h2>
<p>By attending, you acknowledge that photography and videography may occur for community and promotional use. Contact us if you have special concerns.</p>
<h2>Website</h2>
<p>Content is provided for information. Ticket sales are governed by the ticketing platform’s terms.</p>
</div></section>
""",
    )

    write(
        "legal/refund.html",
        "Refund Policy",
        "Refund policy for Ras Raaga Bhajan Clubbing tickets.",
        page_hero("Refund Policy", "Clarity with compassion.", '<a href="../index.html">Home</a> / Legal / Refunds')
        + f"""
<section class="section"><div class="container-narrow prose reveal">
<p>Ticket refunds and exchanges are subject to the policies displayed at checkout on our ticketing partner (<a href="{TICKET}" target="_blank" rel="noopener">avenueticket.com</a>) and applicable law.</p>
<h2>General guidance</h2>
<ul>
<li>Review refund windows carefully before purchasing.</li>
<li>Event cancellation by organizers typically triggers remedy per ticketing partner rules.</li>
<li>Duplicate purchases or technical errors: contact the ticketing platform first, then reach us via <a href="../contact.html">Contact</a> with your order ID.</li>
</ul>
<p>We appreciate your understanding — every ticket helps create a beautiful evening of devotion for the whole community.</p>
</div></section>
""",
    )

    # ——— ADDITIONAL (to reach 55) ———
    write(
        "faq.html",
        "Frequently Asked Questions",
        "Detailed FAQ for Ras Raaga Bhajan Clubbing — timing, venue, tickets, families, and more.",
        page_hero("FAQ", "Answers for a peaceful arrival.", '<a href="index.html">Home</a> / FAQ')
        + f"""
<section class="section"><div class="container-narrow">
<details class="faq-item reveal" open><summary>What is Bhajan Clubbing?</summary><p>A Ras Raaga evening of live bhajans with celebratory community energy — devotion that feels joyful and premium.</p></details>
<details class="faq-item reveal"><summary>When and where?</summary><p>{EVENT_DATE} at {VENUE}. Doors 4:00 PM; program 5:00–8:00 PM.</p></details>
<details class="faq-item reveal"><summary>Who performs?</summary><p>BayRaagis — live performances.</p></details>
<details class="faq-item reveal"><summary>Is it family-friendly?</summary><p>Yes. Children are welcome with supervision. See Dress Code &amp; Guidelines for tips.</p></details>
<details class="faq-item reveal"><summary>Do I need to know the lyrics?</summary><p>No. Listen, clap, and join when you feel ready. Participation is invitational.</p></details>
<details class="faq-item reveal"><summary>What should I wear?</summary><p>Festive and respectful attire. Indian wear encouraged but not required.</p></details>
<details class="faq-item reveal"><summary>Where do I park?</summary><p>Use venue-area parking; arrive early. See Venue &amp; Directions.</p></details>
<details class="faq-item reveal"><summary>How do I volunteer or sponsor?</summary><p>See <a href="community/volunteer.html">Volunteer</a> and <a href="sponsors/index.html">Sponsors &amp; Partnership</a>.</p></details>
<p class="text-center mt-4"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a></p>
</div></section>
""",
    )

    write(
        "media-kit.html",
        "Media Kit",
        "Ras Raaga media kit — logos, event facts, press release, and resources for Bhajan Clubbing.",
        page_hero("Media Kit", "Assets and facts for press & partners.", '<a href="index.html">Home</a> / Media Kit')
        + f"""
<section class="section"><div class="container">
<div class="grid-2">
<div class="prose reveal">
<h2>Brand assets</h2>
<ul>
<li><a href="assets/images/logo.png">Logo (transparent)</a></li>
<li><a href="assets/images/logo-on-black.png">Logo (on black)</a></li>
<li><a href="assets/images/logo-white.png">Logo (white)</a></li>
<li><a href="assets/images/logo-gold.png">Logo (gold)</a></li>
</ul>
<h2>Quick facts</h2>
<ul>
<li>Event: Bhajan Clubbing with Ras Raaga</li>
<li>Tagline: An Evening of Bhajans, Bliss &amp; Beyond</li>
<li>Date: {EVENT_DATE}</li>
<li>Venue: {VENUE}</li>
<li>Doors: 4:00 PM · Program: 5:00–8:00 PM</li>
<li>Artists: BayRaagis</li>
<li>Tickets: <a href="{TICKET}" target="_blank" rel="noopener">avenueticket.com/event/bhajan-clubbing-with-ras</a></li>
<li>Instagram: @rasraaga</li>
</ul>
</div>
<div class="feature-block reveal" style="text-align:center">
<img src="assets/images/logo.png" alt="Ras Raaga logo" style="height:160px;margin:0 auto 1rem" loading="lazy" />
<p>Please maintain clear space around the logo and do not recolor outside provided variants.</p>
</div>
</div>
<article class="container-narrow prose mt-4 reveal">
<h2>Press release</h2>
<p><strong>FREMONT, CA</strong> — Ras Raaga announces <em>Bhajan Clubbing</em>, an evening of live bhajans featuring BayRaagis on <strong>{EVENT_DATE}</strong> at <strong>{VENUE}</strong>. Doors open at 4:00 PM with program from 5:00 PM to 8:00 PM.</p>
<p>“We created Bhajan Clubbing so devotion can feel joyful, communal, and beautiful,” said the Ras Raaga organizing team.</p>
<p>Tickets: <a href="{TICKET}" target="_blank" rel="noopener">{TICKET}</a> · Media inquiries via <a href="contact.html">Contact</a>.</p>
<p class="mt-3"><a class="btn btn-gold" href="contact.html">Media Inquiries</a>
<a class="btn btn-outline" href="sponsors/index.html">Sponsorship</a></p>
</article>
</div></section>
""",
    )

    write(
        "spiritual-resources.html",
        "Spiritual Resources",
        "Spiritual resources from Ras Raaga — bhajan lyrics, home practice, and reading for devotees.",
        page_hero("Spiritual Resources", "Gentle tools for daily devotion.", '<a href="index.html">Home</a> / Resources')
        + f"""
<section class="section"><div class="container">
<div class="grid-3">
<a class="feature-block reveal" href="blog/creating-sacred-space-home.html"><h3>Sacred Space at Home</h3><p>Create a small altar of calm.</p></a>
<a class="feature-block reveal" href="blog/prepare-heart-bhajan-evening.html"><h3>Prepare Your Heart</h3><p>Arrive open for kirtan.</p></a>
<a class="feature-block reveal" href="blog/science-behind-chanting.html"><h3>Science of Chanting</h3><p>Mind, breath, and mantra.</p></a>
<a class="feature-block reveal" href="blog/top-10-bhajans.html"><h3>Beloved Bhajans</h3><p>Ten songs that touch the soul.</p></a>
<a class="feature-block reveal" href="blog/what-is-bhajan-clubbing.html"><h3>What is Bhajan Clubbing?</h3><p>Understand the experience.</p></a>
<a class="feature-block reveal" href="blog/index.html"><h3>Full Blog</h3><p>18 reflections to explore.</p></a>
</div>
<div class="container-narrow prose mt-4 reveal">
<h2>Bhajan lyrics to warm your voice</h2>
<h3>Raghupati Raghava</h3>
<p>Raghupati Raghava Raja Ram<br/>Patita Pavana Sita Ram<br/>Ishwara Allah Tero Nam<br/>Sabko Sanmati De Bhagwan</p>
<h3>Shree Ram Jai Ram</h3>
<p>Shree Ram Jai Ram Jai Jai Ram — repeat with love; the simplest path of remembrance.</p>
<h3>Om Jai Jagdish Hare (excerpt)</h3>
<p>Om Jai Jagdish Hare, Swami Jai Jagdish Hare… Bhakt janon ke sankat, kshan mein door kare.</p>
<p>BayRaagis may offer additional repertoire on {EVENT_DATE}. These lines are invitations, not a fixed setlist.</p>
</div>
<p class="text-center mt-4"><a class="btn btn-gold" href="{TICKET}" target="_blank" rel="noopener">Experience Live — Book Tickets</a></p>
</div></section>
""",
    )

    write(
        "newsletter-thank-you.html",
        "Newsletter Thank You",
        "Thank you for joining the Ras Raaga newsletter.",
        page_hero("You are on the list", "Welcome to gentle reminders of devotion.", '<a href="index.html">Home</a> / Thank You')
        + f"""
<section class="section"><div class="container-narrow text-center reveal">
<p>Thank you for subscribing. We will share event updates, bhajan reflections, and community news — never spam, always with heart.</p>
<p class="mt-3"><a class="btn btn-gold" href="events/index.html">Explore Upcoming Events</a>
<a class="btn btn-outline" href="blog/index.html">Read the Blog</a>
<a class="btn btn-outline" href="feedback.html">Share Feedback</a></p>
</div></section>
""",
    )

    write(
        "404.html",
        "Page Not Found",
        "404 — page not found on Ras Raaga website.",
        f"""
<section class="page-hero" style="min-height:50vh;display:flex;align-items:center">
<div class="container">
<p class="eyebrow">404</p>
<h1>This path is quiet…</h1>
<div class="gold-line center"></div>
<p>The page you seek is not here. Let us guide you back to bliss.</p>
<div class="flex-center mt-3">
<a class="btn btn-gold" href="index.html">Go Home</a>
<a class="btn btn-outline-light" href="events/index.html">Upcoming Events</a>
<a class="btn btn-outline-light" href="{TICKET}" target="_blank" rel="noopener">Book Tickets</a>
</div>
</div>
</section>
""",
    )

    # Count pages
    html_files = list(ROOT.rglob("*.html"))
    # exclude nothing in venv
    html_files = [h for h in html_files if ".venv" not in str(h)]
    print(f"\nGenerated {len(html_files)} HTML pages.")


if __name__ == "__main__":
    generate()
