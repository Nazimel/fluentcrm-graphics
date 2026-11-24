# Changelog

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
