# Changelog

## 0.1.5 (2026-11-25)
- **Random colours:** `pick_pairing()` now shuffles the pairings for every request, so graphics no longer always start with the first pairing. Within a set, each graphic still gets a different pairing. The new `blog_colour()` helper picks a random solid colour for blog covers.
- **Solid blog backgrounds:** blog covers use one solid background colour edge to edge, with no panel over a lighter ground. `blog_cover()` now fills the 1920×1080 cover and scales the scene ×1.7.
- Blog cover examples were re-rendered on solid backgrounds.

## 0.1.4 (2026-11-25)
- **Blog covers are always 1920×1080.** The new `blog_cover()` helper wraps a scene built on the 1104×532 grid into the 1920×1080 cover. It uses a 48px panel margin, scales the scene ×1.65 and drops it 60px, so the anchor still crops at the panel bottom.
- Blog cover examples were re-rendered at 1920×1080 and renamed `*-1920x1080`.

## 0.1.3 (2026-11-25)
From review set 3 and the blog cover tests on the canvas (row 10).

### Rules
- **New connector style:** a solid 2.5px line in a quiet tone, with round caps and a small solid dot only at the target end. It replaces the dashed purple line with ring dots, which read as AI-made. Lines that cross into a white UI use lilac. Automation step connectors are unchanged.
- **Blog covers carry no text.** Each one is a real anchor on the right, cropping at the panel bottom, with linked support on the left: a tight two-card stack, an entry and result for an automation editor, or the flow directly on the panel when the cover pairs an automation with an email. One small result card fills any gap beside a flow. Emails keep real email hierarchy and are never shrunk to fit cards.
- **Profile banners (1500×500):** illustration only, with the lower-left area kept clear for the profile photo.
- **Two small cards stack tightly,** and their links bend to reach distant targets.
- **YouTube thumbnails are out of scope.**
- Tested and rejected for blog covers: components on both sides, a bigger anchor, and flat decorative illustrations.

### Kit
- `links()` now draws the new style and takes a `color` argument.

### Examples
- Added: six blog covers (`blog-cover-cart-email`, `-automation-email`, `-automation`, `-segments`, `-report`, `-sms`) and `profile-banner-1500x500`.
- Updated to the new connector style: `integrations-720x600`, `linkedin-post-1200x628`, `web-hero-product-screen-1440x960`.
- Removed: `blog-cover-courses` and `blog-cover-forms`, which had text on the cover.

## 0.1.2 (2026-11-24)
From review set 2 on the FluentCRM SaaS Identity canvas (row 09).

### Rules
- **One connector style** for card-to-UI links: purple dashed, right angles with rounded corners, a ringed dot at both ends (`links()`, `elbow()`).
- **Cards connect to what they describe:** a card beside a flow connects to its exact step; a module card sits outside the screen and connects to its nav item; a row card overlays its row as an outlined overlay (`outlined_pill()`).
- **Group support cards on one side** and the anchor on the other, never split around the anchor to force symmetry.
- **Integrations graphic:** a FluentCRM contact screen with an activity timeline in the centre, and outlined UI cards of real data (`mini_card()`) overlapping its edge at their timeline rows. Each logo appears once; no logo-tile rings.
- **Product-screen hero:** one component for each thing the headline names; the screen is sized so cards fit beside it with equal gaps; one panel wraps the whole group; the page ground is plain.
- **Stories:** about 250px clear at the top and 280px at the bottom; the panel stays inside those zones; a wide, centred anchor crops at the panel edge; no email squeezed beside a column of cards.
- **Card size matches the block scale,** and the flow and its cards are centred vertically in the panel.

### Kit
- New: `mini_card()`, `outlined_pill()`, `elbow()`, `links()`.

### Examples
- Added: `feature-card-whatsapp-290x400`, `feature-card-whatsapp-522x400`, `integrations-720x600`, `linkedin-post-1200x628`, `web-hero-product-screen-1440x960`, `social-story-1080x1920` (.dc.html and .png).

## 0.1.1 (2026-11-24)
From review comments on the FluentCRM SaaS Identity canvas.

### Rules
- **Emails are complete:** subject, header, hero, body, sections and footer; fitted to the panel width and running off the bottom edge only, never the sides.
- **Emails are quiet by default** (`quiet_email()`): white body, pale hero with a flat illustration, outline button, grey lines for copy. The bold email is only for graphics where the email is the main element.
- **Phones are zoomed in:** the phone is the anchor and crops off the bottom.
- **Spacing:** equal outer margins on all four sides; equal spacing inside panels; support cards never overlap the anchor (brand icon tile excepted; product UI crop heroes may layer cards over the crop edge).
- **Consistent outlines** on every floating card.
- **No large empty areas;** four cards as two large + two small placed diagonally (`grid4()`); neighbouring cards match in size.
- **Mix colours:** a different ground + panel pairing per graphic (`PAIRINGS`, `pick_pairing()`); purple grounds for emphasis and expanded cards.
- **Badges contrast** with their ground: solid purple on tints, pale badge only on white.
- **Social posts:** the panel starts 40 to 56px under the copy.
- **Platform icons stay on their platform** (no WooCommerce icon on a FluentCart step).
- **Big formats are scaled up** (`scaled()`) so text reads without zooming.

### Fixes
- Logo: `fluentcrm-logo-color` was the dark-background version (white text) and vanished on light grounds. Renamed to `fluentcrm-logo-dark-bg`; added `fluentcrm-logo-light-bg`.
- Phone screen rendered black on the canvas (height 100% collapsed); now an explicit height.

### Kit
- New: `quiet_email()`, `campaigns_list()`, `link_clicks()`, `revenue_card()`, `grid4()`, `scaled()`, `PAIRINGS`, `pick_pairing()`, `OUTLINE`.
- `campaign_card()` gains the outline; `eyebrow()` is solid by default (`soft=True` for white); `fernly_email()` is complete with body and footer.

### Examples
- New: email header 600×200, blog cover (forms) 1200×628, reports feature card 522×400, social portrait (SMS) 1080×1350.
- Updated to the new rules: courses blog cover, social post 1080², web hero 1440×960.
- Render check list in SKILL.md extended (overlap, spacing, unfinished emails, contrast, card sizes, readability).

## 0.1.0 (2026-11-19)
First release.
