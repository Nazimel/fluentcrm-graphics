# Format recipes

Proven layouts from the test runs. Each lists size, ground, safe zones, scene and the example to copy. Sizes the user names always win; when no size is given, use the default here and say so in the reply. Pick a different ground + panel pairing for each graphic (`pick_pairing(i)`); the colours below are defaults, not fixed.

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
- **Ground:** a pairing ground (e.g. Periwinkle `#E4E5FF`), full bleed (radius 0). **Equal 48px outer margins on all four sides.**
- **Copy on the image:** solid purple eyebrow pill (e.g. "AUTOMATION GUIDE"), a short headline in Manrope 800 ~52px (shorten long titles to their promise), one supporting line in Manrope 600 ~20px slate, then integration tiles (56px logos with name labels and lavender "+" between) when the article is about integrations. Copy column left 48px, width ~480, vertically centred between 48px top and bottom.
- **Scene:** a pairing panel at the right (x 576, y 48, 576×532, radius 40, overflow hidden) with archetype 1: left-aligned flow at s≈0.7 (x 32) and a `quiet_email()` (x 289, w 255) that fits the panel width and runs off the bottom only. Spacing panel edge → flow → email → panel edge is an equal 32px. A short dashed line joins the send step to the email. Shorten step labels to keep the spacing.
- **Offer:** a version without the headline if the blog template already prints the title.
- **Example:** `examples/blog-cover-courses-1200x628.*`

## Web hero (full section): 1440×960
- Nav, copy column left (Manrope 52px headline, purple CTA, chips), scene right on a Lavender panel with flow, sample email, icon tile and an Email Stats card.
- **Example:** `examples/web-hero-1440x960.dc.html`

## Social post: 1080×1080 (also 1080×1350, 1080×1920)
- `fluentcrm-logo-light-bg` and a solid purple badge on top, Manrope 62 to 64px headline and a supporting line, 72px edge padding. Illustration never posted without copy.
- **The panel starts right under the copy:** 40 to 56px below the last line, not at a fixed top. It runs off the bottom and right.
- **Scale everything up** with `scaled()`: phone k≈2.2, zoomed so its header and messages fill the panel and the rest crops off the bottom; support cards k≈1.67, same width, left-aligned, stacked with an equal gap. Equal 48px spacing panel edge → cards → phone → frame edge; no overlap.
- An email scene follows the email rules: complete, fitted, runs off the bottom (e.g. top ~454, height to frame bottom + 30).
- **Example:** `examples/social-post-1080x1080.dc.html`

## Email header: 600×200
- Pairing ground (e.g. Cream), `fluentcrm-logo-light-bg` top-left, Manrope ~26px headline on two lines, and a pairing panel on the right (x 340, 240 wide, radius 24) running off the bottom with one or two blocks at s≈0.6. Keep text ≥14px.
- **Example:** `examples/email-header-600x200.*`

## Reports / stats card: 522×400 (expanded)
- Purple or purple-dark ground. Four cards as two large + two small, diagonal (`grid4(24, 48, 474, 328, cards=(campaigns_list, revenue_card, link_clicks, email_stats-style))`): large 192 tall, small 120, 16px gaps. Fill each card; no empty bottoms.
- **Example:** `examples/feature-card-reports-522x400.*`
