# Icons: FluentCRM automation icon set

The plugin's own automation icons (source folder `1-automation-icons`), cleaned for reuse: solid glyphs on an 80×80 viewBox, every shape in `currentColor`, so one file can be any palette colour.

## How to use
- **Automation block tiles:** inline the paths in a 44px tile (`ill-tile-*` background) at about 22px, coloured white. Inline SVG keeps `currentColor`; an `<img>` tag does not.
- **Recolouring:** set `color` (or `fill`) on the `<svg>`. Use palette colours only: white on a solid tile, `purple-brand` or `slate` on a light card, `ill-tile-*` colours on white.
- **Masks:** when inlining is not possible, use the file as a CSS `mask-image` on a box filled with the colour you need.
- Never redraw a glyph, add strokes, or mix these with another icon set in the same flow.

## Which icon for which block
Labels are the exact product block names; illustrations may rename steps descriptively but keep the icon of the real block type (FluentCRM 3.1.13); most actions beyond tags, lists, email and wait are Pro.

| Block (Product Brain label) | Icon |
|---|---|
| Trigger (generic) | `trigger` |
| Tag Applied | `tag_applied` |
| List Applied | `list_applied` |
| Tag Removed / List Removed (triggers) | `tag_removed` / `list_removed` |
| New User Sign Up | `user_register` |
| Order Received in WooCommerce / EDD orders | `new_order_woo` / `new_order_edd` |
| Send Custom Email | `custom_email` |
| Send Campaign Email | `send_campaign` |
| Wait X Days/Hours | `wait_time` |
| Check Condition | `conditions` |
| Apply Tag / Remove From Tag | `apply_tag` / `tag_remove` |
| Apply List / Remove From List | `apply_list` / `list_remove` |
| Set Sequence Emails / Cancel Sequence Emails | `set_sequence` / `cancel_sequence` |
| Cancel Automations / End This Funnel Here | `cancel_automation` / `end_funnel` |
| Update Contact Property | `contact_update` |
| Create WP User / Change WP User Role / Update WP User Meta | `create_wp_user` / `wp_user_role` / `wp_user_meta` |
| Link Click | `link_clicked` |
| Goal (benchmark) | `benchmarks` |
| Outgoing Webhook | `webhooks` |
| Has Selected tags / Has In Selected Lists / Check Contact's Properties / WP role checks | `has_tag` / `has_list` / `has_contact_property` / `has_wp_role` |
| Integrations (LearnDash, LifterLMS, TutorLMS, MemberPress, PMPro, RCP, WishList Member, WooCommerce, EDD, WordPress) | the matching file, e.g. `learndash`, `woo_purchased`, `ld_in_course` |

**Not in the set:** SMS and WhatsApp. Use the `sms` and `wa` glyphs in `kit.py` (`icon("sms", px)`).


## Platform icons stay on their platform
Never use a platform-specific icon (`new_order_woo`, `woo_purchased`, `edd_purchased`, `new_order_edd`, `woocommerce`, LMS icons) for another platform's step. A FluentCart order, or any order trigger without its own icon, uses `trigger`.
