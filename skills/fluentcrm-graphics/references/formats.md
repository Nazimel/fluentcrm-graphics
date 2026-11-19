# Format recipes

Proven layouts from the test runs. Each lists size, ground, safe zones, scene and the example to copy. Sizes the user names always win; when no size is given, use the default here and say so in the reply.

## Feature card, collapsed: 290×400
- **Use:** feature grids, cards that expand on hover. Copy (label pill, headline) is added by the page.
- **Ground:** Lavender `#C9B3F5`, radius 28. Options Orchid, Apricot, Coral.
- **Safe zone:** top 48px clear for the label pill.
- **Scene:** anchor + one support card. Email: `fernly_email(30, 54, 222, subject=True)` + `email_stats(154, 300, 124)`. SMS/WhatsApp: `phone(45, 52, 200, ch)` + campaign card at the bottom (`campaign_card(18, 314, 254, …)`). Automation: centred column with `contact_pill` → blocks at s≈0.62 → `split()` bleeding slightly at the bottom.
- **Examples:** `examples/feature-card-*-290x400.*`

## Feature card, expanded: 522×400
- **Use:** the hover state of the same card.
- **Ground:** brand purple `#7742E6`; connectors `#E4D6FB`.
- **Safe zones:** top 48px; lower-left ~236×110 clear for the page headline and offer line.
- **Scene:** same story as the collapsed card. Context on the left (campaign card, Inbox, contact pill, mini email joined to its send block by a dashed line), anchor on the right bleeding off the edge.
- **Examples:** `examples/feature-card-*-522x400.*`, `scripts/example_generator.py`

## Hero image beside page copy: 720×600 (default when no size is given)
- **Use:** the visual half of a two-column page hero; the headline and paragraph stay in the page HTML.
- **Ground:** Lavender, radius 40. No safe zones (copy is outside the image).
- **Scene:** archetype 4, a product UI crop (white panel, 3px purple outline, radius 32, bleeding right and bottom) with two overlapping cards that map to the page's message. Example: contact profile + signup form card (capture) + Notes & Activities card (understand).
- **Example:** `examples/hero-image-crm-features-720x600.*`

## Blog cover: 1200×628
- **Ground:** Lilac `#F7EDFC`, full bleed (radius 0).
- **Copy on the image:** eyebrow pill (e.g. "AUTOMATION GUIDE"), a short headline in Manrope 800 ~52px (shorten long titles to their promise), one supporting line in Manrope 600 ~20px slate, then integration tiles (56px logos with name labels and lavender "+" between) when the article is about integrations. Copy column left 64px, width ~480, vertically centred.
- **Scene:** a Lavender panel at the right (x 584, y 40, 576×548, radius 40, overflow hidden) with archetype 1: left-aligned flow at s≈0.8 and the designed email (or phone) bleeding off the right and bottom, joined by a dashed return line from the step that sends it. End the flow at the step that produces the preview so the line tells the truth.
- **Offer:** a version without the headline if the blog template already prints the title.
- **Example:** `examples/blog-cover-courses-1200x628.*`

## Web hero (full section): 1440×960
- Nav, copy column left (Manrope 52px headline, purple CTA, chips), scene right on a Lavender panel with flow, sample email, icon tile and an Email Stats card.
- **Example:** `examples/web-hero-1440x960.dc.html`

## Social post: 1080×1080 (also 1080×1350, 1080×1920)
- Logo and badge top, Manrope 62px headline and a supporting line, then the scene on a Lavender panel bleeding off the bottom-right. 72px edge padding. Illustration never posted without copy.
- **Example:** `examples/social-post-1080x1080.dc.html`

## Email header: 600×200 (no example yet)
- Use the brand ground or a light palette colour, logo left, short headline, and a small slice of the scene (one or two blocks or a stats card) on the right. Keep text ≥14px.
