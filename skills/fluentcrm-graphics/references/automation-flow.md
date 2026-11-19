# AutomationFlow

The FluentCRM automation as drawn on the website: tinted blocks with solid icon tiles and bold Nunito labels, joined by dashed lavender connectors with ⊕ circles, set on a rounded palette panel next to the email or phone preview the flow sends. **Draft v3, not locked.**

## When to use
- The centre of campaign-loop illustrations on web pages and social graphics, always next to copy.
- Pair it with what the flow sends: a designed sample email, a phone mockup for SMS or WhatsApp, or an Emails Stats card.

## Anatomy
- **Panel:** rounded 32 to 40px, solid `accent-lavender` (#C9B3F5/#C9B3F6) or a light palette colour (`bg-lilac`, `bg-periwinkle`); previews bleed off its edges.
- **Block:** inline card sized to its label, 14px radius, 2px border, padding 11px 18px 11px 11px, shadow `0 8px 24px rgba(60,30,120,.10)`; a 44px solid icon tile (10px radius) holding the matching FluentCRM automation icon from `assets/icons/`, inlined at 22px in white (see that folder's README for which icon goes with which block; SMS and WhatsApp use a solid chat bubble), then one bold label in Nunito 800 at 21px for web scale (scale the whole illustration, not the label alone). Labels may carry the value inline: "Tag Applied: Inactive_Contacts".
- **Connectors:** 2px dashed `ill-connector` (#B98AE8) aligned to the tile centre, with a 26px white ⊕ circle (2px `ill-plus-ring` #C77DDF). A dashed line or curve may lead from a send block to its preview.
- **Branches:** 44px white circles with a 2px ring: **Yes** (`ink` ring) runs sideways to its block, **No** (`accent-coral` ring) continues down.
- **Expanded message blocks:** the exception in brand-guide.md rule 2 still applies; prefer a separate designed preview card in this style.

## Block types
| Type | Fill | Border | Tile |
|---|---|---|---|
| Trigger | `bg-lilac` #F7EDFC | `accent-orchid` #E3B7F1 | `ill-tile-trigger` #B565E8 |
| Send (email, SMS, WhatsApp) | `bg-leaf` #EAFCE8 | `ill-border-send` #A9E5A1 | `ill-tile-send` #1DB83A |
| Wait | white | `line` #E1E4EA | `ill-tile-neutral` #4E5D78 |
| Condition | `bg-blush` #FFE5E6 | `accent-coral` #FFA9A4 | `ill-tile-condition` #F25C5C |
| CRM action (tag, list, property) | `bg-periwinkle` #E4E5FF or white | `accent-lavender` #C9B3F6 | `ill-tile-neutral` #4E5D78 |

## Content rules
- Labels are descriptive step names ("Send Welcome Email", "Cart Reminder Text", "Joined As Subscriber"), and each one maps to a real block type in the FluentCRM product brain, whose fill, tile colour and icon it uses. Never name a step the product cannot run.
- 3 to 6 blocks per illustration; one branch at most.
- Illustrations never stand alone: on social graphics they sit with a headline and supporting copy.
- Literal product screenshots use the editor's own colours (`block-*` tokens) instead.

## The consumer provides
See `examples/feature-card-MarketingAutomation-*` and `scripts/example_generator.py`; build blocks with `block()`, `conn()`, `conn_c()` and `split()` from `scripts/kit.py`.
