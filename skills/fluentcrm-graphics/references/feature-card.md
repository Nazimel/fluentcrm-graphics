# FeatureCard

One self-contained illustration card in the website's language, built from the 20 website reference illustrations and first shipped as the Black Friday feature cards (Email Campaign, SMS Marketing, WhatsApp Marketing, Marketing Automation). The same system scales to any size and either ground, so one scene can become a 290×400 grid card, its 522×400 hover state, a 1080² social visual or a 1200×628 blog cover. **Draft v3, not locked.**

## When to use
- Feature grids, hover-expand pairs, feature-page heroes, and the visual half of social posts and blog covers.
- The card is the illustration only. Copy comes from the page or from the layout around it (rule 7): web pages put the label pill and copy in HTML on top, and social layouts put a headline beside or above the card.

## Anatomy
- **Ground:** the card itself, 28px radius at 290 to 600px wide (32 to 40px above that), overflow hidden.
- **Scene:** one anchor object (a flow, a designed email, a phone, a product UI crop), with one or two support cards at most.
- **Layer order:** ground → bleeding preview → flow or campaign cards → floating cards (stats, inbox, revenue, brand icon tile). Never more than three layers deep.
- **Bleed:** emails run off the bottom edge only (complete, fitted to the width); phones are zoomed in and crop off the bottom; product UI crops may run off the right and bottom. Floating cards stay fully inside, at least 8px from every edge. Nothing bleeds off the top-left corner.
- **Spacing:** equal outer margins; equal spacing between panel edge, cards and anchor. Support cards do not overlap the anchor (only the brand icon tile may sit on a corner). Every floating card has the same 2px `#D9B8F2` outline.
- **Fill:** no empty patch bigger than a card outside the copy zone. Four cards → two large + two small, diagonal (`grid4()`).

## Grounds
| Ground | Use | Adjustments |
|---|---|---|
| `accent-lavender` #C9B3F5 (default) | Standard and collapsed cards; also Orchid #E3B7F1, Apricot #FFCC99 or Coral #FFA9A4 when a set needs variety | Connectors `ill-connector` #B98AE8 |
| `purple-brand` #7742E6 | Emphasis and expanded (hover) state | Connectors switch to `ill-connector-on-dark` #E4D6FB; white cards keep their shadows; no purple-brand fills on elements sitting directly on the ground |
| Light palette (`bg-lilac`, `bg-periwinkle`) | Soft sections on white pages | As lavender |

A collapsed/expanded pair switches ground (lavender → brand purple) so the hover change reads at a glance.

## Safe zones
- **Label pill:** top-left, full width × 48px on every size. Keep content clear; the page places a pill such as "Email Campaign" there.
- **Copy zone:** on wide or expanded cards (aspect wider than 1:1), keep the lower-left area of about 45% of the width × 30% of the height free for the page's headline and offer line.
- When the layout carries its own copy (social, blog cover), the copy may occupy those zones instead.

## Composition archetypes (from the website references)
1. **Flow + bleeding preview:** a left-aligned flow column overlapping the left edge of the email, phone or form it sends, with a dashed return line that runs down from the last block and curves into the preview.
2. **Flow split to two outputs:** a centred flow that splits with dashed lines into two results (Yes/No branches, or phone on one side and email on the other).
3. **Campaign object + preview:** a campaign card (icon tile, name, recipients, Sent badge, subject or message with a merge-tag chip) beside the designed email or phone, plus Email Stats or Inbox.
4. **Product UI crop:** a white admin panel with a 2 to 3px purple outline, cropped by the card edges, optionally with an overlapping second card (AI Summary, Emails Stats) or a dashed purple callout around one element (a shortcode dropdown, a filter menu).
5. **Concept board:** a white board with generic steps ("Automation starts", "Choose the next action") branching into coloured integration tiles.

## Sizes and scale
Scale the whole scene, never one label. Block scale by card width: 290 to 320 → 0.62 to 0.72; 420 to 600 → 0.62 to 0.8; 1000+ → 1.0 to 1.25. Minimum text is 9px at 290 wide (scale up proportionally). The two shipped sizes:
- **290×400 collapsed:** the anchor object plus one support card (email + Email Stats; phone + campaign card; split flow with a contact pill on top).
- **522×400 expanded:** the same scene with its context added on the left (campaign card, Inbox, contact pill, a small email preview joined to its send block), the anchor moved right, and the copy zone kept clear.

## Floating card kit
Email Stats (Opened, Clicked with stat-colour bars), Inbox (two reply rows with unread dots and a channel badge), contact pill (initials avatar, name, one status line), Sales Revenue (one big number and mini bars), and the FluentCRM icon tile overlapping a preview corner.

## Content rules
- One story per card, told the same way in both sizes.
- Step names are descriptive ("Send Welcome Email", "Cart Reminder Text"), and each maps to a real block type in the FluentCRM product brain (rule 4). Sample brands are fictional and may use their own design system; numbers stay internally consistent (rates match counts).
- **Channels:** SMS may appear in a flow (`Send a SMS`, Pro). WhatsApp has no automation action, so WhatsApp scenes show a WhatsApp campaign and the shared inbox, never a WhatsApp block. SMS and WhatsApp cards share one layout and differ only in icon, channel badge and chat colours.
- Icons come from `assets/icons/`; use the `sms` and `wa` glyphs in `kit.py` for those channels.

## Examples
`examples/feature-card-*-290x400` and `examples/feature-card-*-522x400` (.dc.html boards and .png renders). `scripts/example_generator.py` rebuilds a pair with the kit.

**Expanded cards (0.1.2):** stack the support cards (campaign card, Inbox) on one side and the anchor (phone) on the other. Never place cards on both sides of the anchor to force symmetry, because it leaves blank gaps. Example: `examples/feature-card-whatsapp-522x400`.
