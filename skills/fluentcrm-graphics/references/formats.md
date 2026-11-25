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

**Integrations graphic (720×600):** the centre is a FluentCRM contact screen with an activity timeline ("Activity from your plugins"). Each integration is an outlined `mini_card()` of real data (order, signup, enrolment, renewal, booking, ticket) overlapping the screen edge at its own timeline row, with a purple tab dot. Cards alternate sides. Logos appear only in the cards, and timeline nodes are plain dots. No logo-tile rings and no bare icon hub.

## Blog cover: 1920×1080 (always)
- **No text on the cover.** The page prints the title, so no headline, eyebrow, logo or summary appears on the image.
- **Size:** always 1920×1080, never 1200×628.
- **Ground and panel:** a pairing ground, full bleed. One pairing panel with equal 48px margins (1824×984, radius 56, overflow hidden). Build the scene on a 1104×532 grid (anchor top at y 48 and running past y 532, left column centred on y 266), then wrap it with `blog_cover(scene, panel_colour)`. That scales it ×1.65 and drops it 60px, so the anchor crops at the panel bottom.
- **Structure:** one real anchor on the right, cropping at the panel's bottom edge. The anchor can be a screen, report, automation editor, phone or a realistic email. Each element on the left is linked with `links()` to the part of the anchor it explains. The left margin equals the right margin.
  - **Anchor plus cards:** the left column is two related cards at the same scale, about k 1.27, stacked tightly with a 24 to 32px gap and centred vertically as a pair. When their targets are far apart, the links bend at rounded corners outside the screen; the cards never spread apart. Example: segments uses Segment rules and Joined this week; a campaign report uses the campaign card and Sent to.
  - **Automation as the anchor:** the automation editor screen, with a header, Active toggle, dotted canvas and the flow. The left cards are the entry (who triggered it) and the result (who reached the end), linked to the first and last steps.
  - **Automation plus email:** the flow sits directly on the panel at block scale about 1.0, with no frame or background. The realistic email, about 440px wide, sits on the right. One line runs from the send step to the email. One small result card fills the gap beside the step it belongs to, such as "Cart recovered" beside the goal, without touching the email.
- **Realistic email:** the email follows normal email hierarchy: inbox bar, brand header, headline, body, product rows with thumbnails and prices, subtotal, a full-width CTA and a footer note. Never shrink the email to make room for cards.
- **Avoid:** components on both sides, flat decorative illustrations, and enlarging the anchor to fill space. All of these were tested and rejected.
- **Examples:** `examples/blog-cover-cart-email-1920x1080`, `blog-cover-automation-email-1920x1080`, `blog-cover-automation-1920x1080`, `blog-cover-segments-1920x1080`, `blog-cover-report-1920x1080`, `blog-cover-sms-1920x1080`.

## Web hero (full section): 1440×960
**Product-screen hero:** show one component for each thing the headline names (contacts screen, automation card, campaigns). Size the screen so module cards fit beside it with equal 24px gaps, and put row cards over their rows as outlined overlays. A single panel wraps the whole group (cards, screen, overlays) with 32px of padding and bleeds off the bottom. The page ground is one plain colour. Never put a strip behind the screen alone. Centre the group horizontally.

- Nav, copy column left (Manrope 52px headline, purple CTA, chips), scene right on a Lavender panel with flow, sample email, icon tile and an Email Stats card.
- **Example:** `examples/web-hero-1440x960.dc.html`

## Social post: 1080×1080 (also 1080×1350, 1080×1920)
- `fluentcrm-logo-light-bg` and a solid purple badge on top, Manrope 62 to 64px headline and a supporting line, 72px edge padding. Illustration never posted without copy.
- **The panel starts right under the copy:** 40 to 56px below the last line, not at a fixed top. It runs off the bottom and right.
- **Scale everything up** with `scaled()`: phone k≈2.2, zoomed so its header and messages fill the panel and the rest crops off the bottom; support cards k≈1.67, same width, left-aligned, stacked with an equal gap. Equal 48px spacing panel edge → cards → phone → frame edge; no overlap.
- An email scene follows the email rules: complete, fitted, runs off the bottom (e.g. top ~454, height to frame bottom + 30).
- **Example:** `examples/social-post-1080x1080.dc.html`

**Story (1080×1920):** keep about 250px clear at the top and 280px at the bottom for the platform UI. The panel sits inside those zones and does not bleed. The anchor (email, phone) is wide and centred and crops at the panel's bottom edge, with at most two support cards in one row above it. Never squeeze an email into a column beside cards.

**Profile banner (1500×500):** illustration only, with no logo or copy. Keep the lower-left area, about 440×200, clear for the profile photo. The panel runs from x 460 to 1452 and from y 48 to 452. It holds one realistic email anchor with the matching flow linked to its send step. Example: `examples/profile-banner-1500x500`.

**Not supported:** YouTube thumbnails. If one is requested, say this skill doesn't make them.

**LinkedIn post (1200×628):** copy on the left, panel on the right. If a flow is shown, its cards connect to their steps.

## Email header: 600×200
- Pairing ground (e.g. Cream), `fluentcrm-logo-light-bg` top-left, Manrope ~26px headline on two lines, and a pairing panel on the right (x 340, 240 wide, radius 24) running off the bottom with one or two blocks at s≈0.6. Keep text ≥14px.
- **Example:** `examples/email-header-600x200.*`

## Reports / stats card: 522×400 (expanded)
- Purple or purple-dark ground. Four cards as two large + two small, diagonal (`grid4(24, 48, 474, 328, cards=(campaigns_list, revenue_card, link_clicks, email_stats-style))`): large 192 tall, small 120, 16px gaps. Fill each card; no empty bottoms.
- **Example:** `examples/feature-card-reports-522x400.*`
