# FluentCRM Graphics

Makes FluentCRM marketing graphics in the website illustration style: feature cards and their hover versions, hero images, blog covers, social visuals and email headers.

## Install

In Claude (claude.ai, the desktop app or Cowork): **Customize > Plugins > Add > Add marketplace**, enter `Nazimel/fluentcrm-graphics`, then install **fluentcrm-graphics**. Updates arrive when this repository changes.

In Claude Code:

```
/plugin marketplace add Nazimel/fluentcrm-graphics
/plugin install fluentcrm-graphics@fluentcrm-graphics
```


## How to use
Ask in plain language, for example:
- "Make a 290×400 feature card for email campaigns."
- "Design a blog image for: How to Sell Online Courses on Autopilot with FluentCart, LearnDash and FluentCRM."
- "Hero image for the Free CRM Features page. Copy: Organize Smarter, Understand Better, Grow Faster."

Say the size and where it goes if you know them; otherwise a sensible default is used and named in the reply.

You get PNG files at 2× resolution, plus an editable board (on your Design canvas when available) so you can change text and colours.

## What it relies on
- **FluentCRM product brain plugin** (already installed for the team): every automation step, feature and integration in a graphic is checked against it, and Pro-only features are flagged.
- Everything else is bundled: the brand guide, 55 FluentCRM icons, brand marks and partner logos, the drawing kit, a render check, and finished examples to copy from.

## Rules it follows
- Real features only, with descriptive step names (for example "Send Welcome Email" for a Send Custom Email step). No WhatsApp step in automations.
- Fictional sample brands only (the house sample is "fernly", a plant shop).
- Purple #7742E6 is the marketing signal; Lavender #C9B3F5 is the default illustration panel.

## Version
0.1.0 · Brand guide draft v3 (not locked). Raise `version` in `.claude-plugin/plugin.json` and `marketplace.json` on every release so installs pick up the update. Send changes to Nazir.
