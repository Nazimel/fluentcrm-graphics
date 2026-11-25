# FluentCRM brand guide (draft v3, not locked)

The brand and asset system for **FluentCRM** by WPManageNinja: marketing automation that runs inside WordPress. Every graphic this plugin makes follows it.

**Positioning:** *Marketing Automation Inside WordPress, Without Limits.*

**Sources:** a full walkthrough of the FluentCRM admin; product colours read from the admin's own stylesheet variables; the illustration language read from 20 illustrations on fluentcrm.com (lavender panels, tinted automation blocks with solid icon tiles, dashed connectors, designed sample emails and phone previews, Nunito labels).

## What FluentCRM is, in four parts
1. **Audience:** contacts, lists, tags, companies, segments, forms and a 360° contact profile (emails, messages, purchases, forms, notes and activities).
2. **Campaigns:** email campaigns with a block composer, merge tags, templates and patterns, A/B subject lines, UTM tags and scheduling; recurring campaigns and sequences; SMS and WhatsApp campaigns with a shared inbox.
3. **Automation:** a visual editor with triggers from CRM, forms, commerce, LMS and WordPress, colour-coded actions, conditions and goals, plus pre-built templates.
4. **Results:** open, click and click-to-open rates, link clicks, contact growth, recovered cart revenue and a campaign calendar across channels.

Channels are equal. Say **marketing automation**, never "email marketing" alone, and show email, SMS and WhatsApp working together where the layout has room.

## Brand personality
Calm, capable, product-first, confident and spacious: a serious marketing platform that happens to live in WordPress. **Never** corporate, stock-heavy, gradient-noisy, cluttered or cartoonish.

## The rules
1. **Lead with the campaign loop.** Hero visuals show audience → automation → messages → results. Smaller layouts can show part of the loop, never a dashboard of numbers alone.
2. **Real structure, polished presentation.** Keep what makes a screen true to the product (structure, feature names, colour meaning of stat bars, status and channel colours). Refine the presentation freely: white cards with icon tiles, lavender connectors, overlays, crops, zooms, layered depth. Never invent a feature, a block type or a workflow the product cannot run.
   - **Expanded message blocks:** a message step may open inside its own card to show a short message (subject with merge tags, heading, one line, button; or the SMS as a bubble). At most two per flow; longer messages go in a separate preview card.
3. **Purple is the marketing signal.** `#7742E6` goes on the logo, the main marketing CTA, links and highlights, one main purple action per view. Inside a recreated product screen, buttons are `#222530`, as in the real admin.
4. **Names are descriptive, capabilities are real.** Name each step for what it does in the story ("Send Welcome Email", "Cart Reminder Text", "Joined As Subscriber", "Wait 15 Minutes"). Every step must map to a block type the product really has (check with the FluentCRM product brain plugin), and its tile colour and icon follow that block type. Never name a step after something the product cannot do (no WhatsApp step in an automation). Feature names in copy and literal product screenshots keep the exact product names. Label Pro features honestly when free wording is nearby. Business claims (installs, ratings, savings) are real figures or a bracketed placeholder.
5. **Sample data is clearly illustrative.** Names and numbers in a UI recreation may be sample data but must be plausible, internally consistent (rates match counts) and never presented as a customer result.
6. **One big thing per layout.** The loop, a headline, a number or a quote, never two competing anchors.
7. **Illustrations pair with copy.** Website illustrations sit beside website copy; on social graphics an illustration is never posted alone, it sits with a headline and at least one supporting line.

## Content fundamentals
- **Voice:** confident and outcome-led. Lead with what the reader gets, then the mechanism.
- **Person:** second person (*you*, *your audience*). "We" only on community, milestone and release posts.
- **Badges contrast with their ground:** solid purple `#7742E6` with white text on any tinted ground; the pale purple-wash badge only on white.
- **Casing:** sentence case for headlines and body; title case only for the positioning line. ALL CAPS only for pill badges and eyebrows.
- **Length:** headlines up to 8 words per line, 2 lines on social and 3 on web; body 2 to 4 lines.
- **Emoji:** none on web pages; on social only as a small accent inside a badge.
- **House style:** no dash in the middle of a sentence for an aside (use commas or a new sentence); prefer connected sentences over choppy fragments; never use "leverage, unlock, empower, streamline, game-changer, elevate, harness, robust, seamless, cutting-edge, landscape, paradigm shift, delve, deep dive, at the end of the day, it's worth noting".

## Colour
- **Brand:** purple `#7742E6`, purple-dark `#5F35B8` (hover, text on tints), purple-wash `#EFE8FC` (eyebrows, selected).
- **Product neutrals:** ink `#0E121B`, slate `#525866`, muted `#99A0AE` (placeholders only), line `#E1E4EA`, line-strong `#CACFD8`, surface `#F5F7FA`, surface-weak `#F9FAFB`, white, deep `#222530` (product buttons). Marketing headlines use near-black `#07090C`.
- **Product semantic:** info `#335CFF` (links), error `#FB3748`, success `#1FC16B`, warning `#F6B51E`, AI `#8762F0` on `#EFEBFF`.
- **Status badges (text/background):** Subscribed `#0B4627/#E0FAEC`, Pending `#624C18/#FFFAEB`, Unsubscribed `#222530/#F2F5F8`, Bounced `#122368/#EBF1FF`, Complained `#71330A/#FFF3EB`, Spammed `#681219/#FFEBEC`, Transactional `#351A75/#EFEBFF`.
- **Channels:** Email `#EEF2FF`, SMS `#FFFAEB`, WhatsApp `#E0FAEC`, with the matching badge text colour.
- **Campaign results bars:** sent `#7B61FF`, opened `#22D3BB`, clicked `#F6B51E`, bounced `#335CFF`, on 5 to 6px `#F5F7FA` tracks.
- **Palette, light (section backgrounds, soft cards):** Mint `#ECFFF8`, Leaf `#EAFCE8`, Periwinkle `#E4E5FF`, Peach `#FFE5CC`, Butter `#FEEBB9`, Lilac `#F7EDFC`, Blush `#FFE5E6`, Cream `#FFF9EB`. One light colour per section.
- **Palette, visible (accent cards, panels):** Lavender `#C9B3F5` (also `#C9B3F6`), Orchid mist `#F8EDFC`, Orchid `#E3B7F1`, Apricot `#FFCC99`, Coral `#FFA9A4`. Never pair near-identical colours (`#C9B3F6` with `#C9B3F5`, `#F8EDFC` with `#F7EDFC`).
- **Eight colours, picked at random:** every graphic takes one pairing, a solid colour plus its light tint, chosen at random with `pick_pairing()`, and graphics in a set never share one. Never start from the first pairing. Solid / light: Apricot `#FFCC99` / `#FFF6EC`, Orchid `#E3B7F1` / `#FBF0FD`, Coral `#FFA9A4` / `#FFF1F0`, Lavender `#C9B3F5` / `#F7EDFC`, Mint `#A8E6CF` / `#ECFFF8`, Aqua `#A3E4E0` / `#EAFBFA`, Butter `#FFE08A` / `#FFFBEA`, Periwinkle `#B8C1FA` / `#EEF0FF`. The solid colour is the panel, or the whole background on a blog cover. The light tint is the outer ground where a graphic has one. Purple `#7742E6` or purple-dark `#5F35B8` grounds are for emphasis and expanded (hover) cards. Block colours inside flows never change. See `PAIRINGS` / `pick_pairing()` in `kit.py`.
- **Illustration extras:** connector `#B98AE8` (on purple grounds `#E4D6FB`), ⊕ ring `#C77DDF`, floating-card outline `#D9B8F2`.
- **Social accents:** orange `#FF9933` for badges on purple or dark grounds; gold `#FACF5A` for stars and milestone sparkles.
- **Forbidden:** `#5468D5` as a FluentCRM colour; sibling product colours appear only as small app tiles.

## Type
- **Manrope** for marketing: display 72/800, hero 64/800, headline 44 to 52/800, subhead 20 to 24/600, body 17/400 in slate, eyebrows 12/700 caps.
- **Inter** only inside recreated product UI: numbers 24/500, titles 15/600, labels 13/400.
- **Nunito** for all text inside illustrations: block labels 800, sample email and preview headlines 800.

## Shape, space, depth
- **Radii:** illustration cards 28px (32 to 40px above 600px wide), product UI crops 32 to 40px, floating cards 14 to 18px, automation blocks 14px at full scale, pills for buttons and badges.
- **Spacing:** 64 to 80px gutters at 1440 wide; 72px edge padding on 1080 social canvases.
- **Shadows:** soft purple-tinted shadows (`rgba(60,30,120,.10–.25)`); glow halos only on milestone social posts.

## Imagery and layout
- Product UI only, rebuilt in markup. No stock photos, people photos, 3D renders or random illustrations.
- **Sample emails are complete.** Everything visible reads as a finished email: subject, brand header, hero, body, products or sections, footer with "Manage preferences". Emails are long, so they run off the **bottom** edge only, never the sides or top; size them to fit the panel width.
- **Sample emails are quiet** by default (`quiet_email()`): white body, pale tinted hero with a flat illustration, outline button, grey lines for body copy, so the flow and the headline lead. The bold version (`fernly_email()`) is only for graphics where the email itself is the anchor.
- **Phones are zoomed in:** the phone is the anchor, scaled so its header and messages fill the frame and the rest crops off the bottom.
- **Spacing and overlap:** outer margins are equal on all four sides; inside a panel the spacing is equal everywhere (panel edge → element → element → edge). Support cards never overlap the anchor; only the brand icon tile may sit over a corner. Exception: product UI crop heroes (archetype 4) may layer their cards over the crop's edge, as in the approved CRM features hero.
- **Outlines are consistent:** every floating card (campaign, inbox, stats, link clicks, revenue) carries the same 2px `#D9B8F2` outline.
- **No large empty areas:** cards fill the frame evenly except a defined copy zone. Four cards: two large + two small placed diagonally (`grid4()`), equal widths, columns ending on one line; an equal 2×2 grid is the fallback. Neighbouring cards match in size, so a single-row card becomes a list when its neighbours are lists.
- **Scale for big formats:** kit pieces are card-sized; on 1080+ frames scale them (`scaled()`) so text reads without zooming (effective text ≥16px on a 1080 frame).
- **Illustration panel:** rounded 32 to 40px panel in Lavender or a light palette colour, no dot grid. The flow sits on the left; what it sends sits on the right and bleeds off the panel: a designed sample email (a fictional store, never a real brand; the email may use any design system that suits it), a phone mockup for SMS or WhatsApp, or a white product-UI crop with a 2 to 3px lavender or purple outline. Small floating cards (Email Stats, a revenue card) and the FluentCRM icon tile may overlap corners.
- Logo top-left when the layout carries one (colour on light, white on purple or dark). Web heroes: copy left, scene right. Social: logo and badge on top, headline, then the scene bleeding off the bottom-right.

## Product UI kit (polished versions for marketing)
- **Automation block:** see `automation-flow.md`.
- **Feature card:** see `feature-card.md`.
- **Email Stats card:** title "Email Stats" (Inter), rows of label and value, bars in the stat colours, 2px `#D9B8F2` outline.
- **Message previews:** subject with merge tags as chips (`#EFEBFF` fill, `#351A75` text); SMS and WhatsApp as phone mockups with a channel badge.
- **Contact rows and profile:** warm grey `#F2EEE8` or peach initials avatars, status badges, tag and list chips, tabs with an ink underline on the active tab.

## Connections and overlays (0.1.2)
- **One connector style** for joining a card to UI (`links()`): a solid 2.5px line in a quiet tone, white on light panels and `#E4D6FB` on purple, with round caps and a small solid dot only at the target end. Lines that cross into a white UI use lilac `#B494EE`. Use right angles with rounded corners (`elbow()`) when the ends don't line up. No dashes and no ring dots: that style read as AI-made. Automation step connectors keep the product's own dashed line with ⊕.
- **Cards connect to what they describe:** a card beside a flow connects to its exact step and is centred on it; a card about a module (Campaigns, Automations) sits outside the screen and connects to that nav item.
- **Row cards overlay their row:** a card about one contact or record sits over that row as an outlined overlay, with no connector. The contact pill gets the 2px outline too (`outlined_pill()`).
- **Group support cards** on one side and the anchor on the other; never split cards around the anchor to force symmetry.
- **Match card size to the block scale** and centre the flow and its cards vertically in the panel.
- **A logo appears once per graphic.**
- **Two small cards stack tightly** with a 24 to 32px gap. A gap beside a flow is filled by one small result card next to its step, never by spreading the cards apart.

## Iconography
- Use FluentCRM's own icons from `assets/icons/` (solid glyphs, 80×80, currentColor). See `icons.md` for which icon goes with which step.
- White inside solid block tiles; purple, slate or a tile colour on light cards. Never add strokes, gradients or a second icon set to the same graphic.
- The set has no SMS or WhatsApp icon: use the `sms` and `wa` glyphs in `kit.py`.
- Brand marks are in `assets/brand/`: `fluentcrm-logo-light-bg` (purple tile, ink text) on light grounds, `fluentcrm-logo-dark-bg` or `fluentcrm-logo-white` on purple or dark grounds. Never put a white-text logo on a light ground.
- Platform icons belong to their platform: never use `new_order_woo`, `edd_*` or `woocommerce` for another platform's step (a FluentCart order uses `trigger`).
- Fluent family Fluent family and integration logos in `assets/logos/` (see `logos.md`). Never redraw a mark.

## Formats
1440 web · 1080×1080 · 1200×628 · 1080×1350 · 1080×1920 · feature cards 290×400 and 522×400 · hero image 720×600. Recipes for each are in `formats.md`.
