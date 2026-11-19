"""Worked example: the Black Friday feature-card pair (Email Campaign collapsed + Marketing Automation expanded).

Run:  python3 example_generator.py OUTDIR
Writes .dc.html boards and preview HTML into OUTDIR, then render each preview with render.py.
Copy this file as the starting point for a new request.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

out = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(out, exist_ok=True)

# 1) Email Campaign, collapsed 290x400 on lavender: anchor email + one support card (Email Stats).
#    Top 48px stays clear for the page's label pill.
scene = fernly_email(30, 54, 222, subject=True) + email_stats(154, 300, 124)
root = board(290, 400, scene)
write_board(f'{out}/EmailCampaign.dc.html', 290, 400, root, 'FluentCRM email campaign card, 290×400')
write_preview(f'{out}/EmailCampaign.preview.html', root, page_bg='#2A1650')

# 2) Marketing Automation, expanded 522x400 on brand purple: contact + email preview on the left,
#    centred flow with a Yes/No split on the right, lower-left kept clear for page copy.
s, c = 0.64, CONNECTOR_ON_DARK
flow = (f'<div style="position: absolute; left: 224px; width: 290px; top: 56px; display: flex; flex-direction: column; align-items: center">'
        + block('trigger', 'tag_applied', 'Joined Spring List', s) + conn_c(s, c)
        + block('send', 'custom_email', 'Send Welcome Email', s) + conn_c(s, c)
        + block('condition', 'conditions', 'Opened Email?', s)
        + split(280, block('crm', 'apply_tag', 'Tag Engaged', 0.6), block('send', 'sms', 'Send Text', 0.6), c)
        + '</div>')
link1 = f'<div style="position: absolute; left: 150px; top: 78px; width: 133px; border-top: 2px dashed {c}"></div>'
link2 = f'<div style="position: absolute; left: 200px; top: 157px; width: 72px; border-top: 2px dashed {c}"></div>'
left = (f'<div style="position: absolute; left: 24px; top: 60px">{contact_pill(line="Joined the spring list")}</div>'
        f'<div style="position: absolute; left: 24px; top: 112px">{mini_email()}</div>')
root = board(522, 400, link1 + link2 + flow + left)
write_board(f'{out}/MarketingAutomationWide.dc.html', 522, 400, root, 'FluentCRM marketing automation card, 522×400 expanded',
            ground=PURPLE, options=(PURPLE, PURPLE_DARK, LAVENDER, ORCHID))
write_preview(f'{out}/MarketingAutomationWide.preview.html', root, ground=PURPLE, page_bg='#2A1650')
print('ok')
