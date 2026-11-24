---
name: fluentcrm-graphics
description: This skill should be used when the user asks to design, make or build any FluentCRM graphic, such as a website feature card, hover card pair, hero image, page header, blog cover or featured image, social post visual, email header or integration graphic. Triggers include "make a graphic for", "design a blog image", "hero image for the page", "feature card", "290x400", "social visual for FluentCRM". It builds the graphic in FluentCRM's website illustration style, checks it by rendering, and delivers PNGs plus an editable board.
---

# FluentCRM graphics

Build FluentCRM marketing graphics in the brand's website illustration language: lavender panels, tinted automation blocks with solid icon tiles, dashed connectors with ⊕ circles, designed sample emails and phone previews, product UI crops and floating stats cards. Check every graphic by rendering it, then deliver it.

Everything needed is inside this skill folder:
- `references/brand-guide.md`: rules 1 to 7, colours, type, layout, house style. Read it first on every request.
- `references/formats.md`: tested recipes per size (feature cards, hero image, blog cover, web hero, social, email header).
- `references/feature-card.md`, `references/automation-flow.md`: composition archetypes, safe zones, scale, block rules.
- `references/icons.md`, `references/logos.md`: which icon goes with which step; brand and partner marks.
- `references/tokens.json`: every token with a usage note.
- `assets/icons/` (55 FluentCRM automation icons), `assets/logos/`, `assets/brand/`.
- `scripts/kit.py` (drawing kit), `scripts/render.py` (render check), `scripts/example_generator.py` (worked example).
- `examples/`: finished boards (.dc.html) and their renders (.png) from approved work. Open the closest one before building.

## Workflow

1. **Brief.** Establish size, placement (page section, blog, social, email), background, the feature or story, and whether copy goes on the image or is added by the page. Use the default size in `formats.md` when none is given and say so in the reply. Ask only when the placement itself is unclear.

2. **Check the product facts.** Before drawing any step, feature or integration, confirm it exists with the FluentCRM product brain plugin the team has installed (ask it, or load its product-brain skill). Note which steps are free and which need FluentCRM Pro, and which belong to another product (FluentCart, LearnDash, etc.). If the product brain plugin is not available, say so and keep to features you can confirm from the brand guide. Never draw a WhatsApp step inside an automation: that action does not exist.

3. **Story.** Pick one anchor object and one story, then a composition archetype from `feature-card.md`: (1) flow with a bleeding preview, (2) flow split into two results, (3) campaign card with preview, (4) product UI crop with overlapping cards, (5) concept board. Name steps descriptively ("Send Welcome Email", "Course Purchased") and give each the fill, tile colour and icon of its real block type. Use the fictional sample brand *fernly* (plant shop) or invent another fictional brand; never a real company.

4. **Build.** Write one Python generator per request that imports the kit (`sys.path.insert(0, '<this skill>/scripts'); from kit import *`), composes absolutely positioned pieces inside `board()`, then calls `write_board()` for the editable .dc.html and `write_preview()` for the render check. Copy `scripts/example_generator.py` or the closest example as a start. For several sizes or variants, generate them all from one script. Keep copy as literal text; merge tags render through `merge_chip()`.

5. **Render check (never skip).** Run `python3 scripts/render.py preview.html out.png W H`, open the PNG and check: clipped or overflowing text; collisions or support cards overlapping the anchor; connectors that do not touch their blocks; empty patches bigger than a card; unequal margins or spacing; emails cut at the sides or looking unfinished; badges or logos that blend into their ground; cards in one layout with mismatched sizes or missing outlines; text too small to read at the final size; anything that breaks the safe zones. Measure instead of guessing: `python3 scripts/render.py --measure preview.html W H "Block label"` prints a block's box. For several boards make one contact sheet with `--sheet`. Fix and re-render until clean.

6. **Deliver.**
   - Export PNGs at 2× (3× for a single small card) and send them to the user as files.
   - If a Design canvas is available, also add the .dc.html boards to the user's own FluentCRM canvas (reuse one they already have, otherwise create one from the Design type) so they can edit text and colours. Otherwise attach the .dc.html files with the PNGs.
   - Reply briefly: what was made, decisions to confirm (default size used, copy on or off the image, Pro features shown, sample data invented), and one next step.

## Non-negotiables
- Mix colours: a different ground + panel pairing per graphic (`pick_pairing()`); purple grounds for emphasis and expanded cards.
- Emails are complete and quiet (`quiet_email()`), fitted to the width and running off the bottom only. Phones are zoomed in and crop off the bottom.
- Equal outer margins and equal internal spacing; no overlap with the anchor; the same outline on every floating card; no large empty areas; four cards as two large + two small, diagonal.
- Every support card is tied to what it describes: connected to its step or module with `links()`, or laid over its row as an outlined overlay. Support cards go on one side of the anchor, and each logo appears once. Stories keep their top and bottom safe zones. See `references/brand-guide.md` (Connections and overlays) and `references/formats.md`.
- Light grounds use `fluentcrm-logo-light-bg`; badges on tinted grounds are solid purple.
- On 1080+ formats scale kit pieces with `scaled()` so everything reads without zooming.
- One anchor and at most two support cards; previews bleed off the right or bottom only; floating cards stay 8px inside the edges.
- Nunito inside illustrations, Inter inside product UI, Manrope for headlines and copy.
- Lavender `#C9B3F5` by default; brand purple `#7742E6` for emphasis and expanded hover states, with connectors `#E4D6FB` on it.
- Top-left 48px clear for a page label pill on cards; lower-left clear for page copy on wide expanded cards.
- Sample numbers stay consistent (2,480 sent → 52.4% opened → 14.8% clicked).
- Copy follows the house style in the brand guide: no mid-sentence dashes, connected sentences, none of the banned words.
- Partner logos stay at their own colours as small tiles; FluentCRM's own marks come from `assets/brand/`.
