"""FluentCRM graphics kit: HTML building blocks for website-illustration-style boards.

Import from a generator script:
    import sys; sys.path.insert(0, '<skill dir>/scripts')
    from kit import *

Every function returns an HTML string with inline styles. Compose a scene with
absolutely positioned pieces inside board(), then write_board() for the .dc.html
canvas file and write_preview() for the local render check (see render.py).
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')

NUN = "font-family: 'Nunito', 'Manrope', system-ui, sans-serif"   # text inside illustrations
INT = "font-family: 'Inter', system-ui, sans-serif"               # product UI (stats, inbox, badges)
MAN = "font-family: 'Manrope', 'Inter', system-ui, sans-serif"    # marketing headlines and copy

# ---------------------------------------------------------------- colours
LAVENDER, ORCHID, APRICOT, CORAL = '#C9B3F5', '#E3B7F1', '#FFCC99', '#FFA9A4'
LILAC, PERIWINKLE, CREAM = '#F7EDFC', '#E4E5FF', '#FFF9EB'
PURPLE, PURPLE_DARK, PURPLE_WASH = '#7742E6', '#5F35B8', '#EFE8FC'
INK, SLATE, MUTED, LINE, SURFACE = '#0E121B', '#525866', '#99A0AE', '#E1E4EA', '#F5F7FA'
NEAR_BLACK = '#07090C'
CONNECTOR, CONNECTOR_ON_DARK = '#B98AE8', '#E4D6FB'
CARD_OUTLINE = '#D9B8F2'
OUTLINE = f'border: 2px solid {CARD_OUTLINE}'   # every floating card uses this outline

# Ground + panel pairings. Use a different pairing for each graphic in a set.
PAIRINGS = [
    ('Cream + Apricot', '#FFF9EB', '#FFCC99'),
    ('Periwinkle + Orchid', '#E4E5FF', '#E3B7F1'),
    ('Cream + Coral', '#FFF9EB', '#FFA9A4'),
    ('Lilac + Lavender', '#F7EDFC', '#C9B3F5'),
    ('Mint + Lavender', '#ECFFF8', '#C9B3F5'),
    ('White + Periwinkle', '#FFFFFF', '#C9B3F6'),
]
EMPHASIS_GROUNDS = ('#7742E6', '#5F35B8')   # expanded/hover and emphasis cards

import random as _random
_PAIR_ORDER = []
def pick_pairing(i=None):
    """(name, ground, panel). Random by default: every request gets a shuffled order, so the first graphic
    is not always the same pairing. Within one run, successive calls (or i = 0, 1, 2...) walk that shuffled
    order, so graphics in a set never share a pairing. Never hard-code PAIRINGS[0]."""
    global _PAIR_ORDER
    if not _PAIR_ORDER:
        _PAIR_ORDER = _random.sample(PAIRINGS, len(PAIRINGS))
    if i is None:
        p = _PAIR_ORDER.pop(0); _PAIR_ORDER.append(p); return p
    return _PAIR_ORDER[i % len(_PAIR_ORDER)]
def blog_colour():
    """A random solid background colour for a blog cover (a pairing's panel colour)."""
    return pick_pairing()[2]
SHADOW = 'box-shadow: 0 12px 28px rgba(60,30,120,0.16)'

# ---------------------------------------------------------------- icons
def icon_inner(name):
    """Inner markup of a FluentCRM automation icon (80x80, currentColor)."""
    s = open(os.path.join(ASSETS, 'icons', name + '.svg')).read()
    s = re.sub(r'<metadata>.*?</metadata>', '', s, flags=re.S)
    s = re.sub(r'^.*?<svg[^>]*>', '', s, flags=re.S)
    s = re.sub(r'</svg>\s*$', '', s, flags=re.S)
    return re.sub(r'\s+', ' ', s).strip()

GLYPHS = {  # 24x24 glyphs for channels missing from the official set
    'sms': '<path fill-rule="evenodd" d="M5 3h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8.2L3 21.2V5a2 2 0 0 1 2-2Zm3 6.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm4 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm4 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>',
    'wa': '<path fill-rule="evenodd" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm-3.3 5.3c.3 0 .6 0 .8.5l1 2.2c.1.3 0 .5-.1.7l-.7.8c-.2.2-.2.4 0 .7.6 1 1.4 1.8 2.4 2.4.3.2.5.2.7 0l.8-.9c.2-.2.4-.3.7-.2l2.2 1c.4.2.5.4.4.8-.2 1.2-1.2 2-2.4 2-3.9-.3-7.2-3.6-7.5-7.5 0-1.2.8-2.3 1.7-2.5Z"/>',
}

def icon(name, px, color='currentColor'):
    """Inline icon: a file stem from assets/icons, or 'sms' / 'wa'."""
    if name in GLYPHS:
        return f'<svg width="{px}" height="{px}" viewBox="0 0 24 24" fill="{color}" aria-hidden="true">{GLYPHS[name]}</svg>'
    return f'<svg width="{px}" height="{px}" viewBox="0 0 80 80" fill="{color}" aria-hidden="true">{icon_inner(name)}</svg>'

def svg_file(path, px):
    """Inline a full-colour SVG file (brand marks, logos) at a square size."""
    s = open(path).read()
    s = re.sub(r'<metadata>.*?</metadata>', '', s, flags=re.S).replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r'\1', s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r'\1', s, count=1)
    return s.replace('<svg', f'<svg width="{px}" height="{px}"', 1)

def brand(name, px):
    return svg_file(os.path.join(ASSETS, 'brand', name + '.svg'), px)

def logo(name, px):
    return svg_file(os.path.join(ASSETS, 'logos', name + '.svg'), px)

# ---------------------------------------------------------------- automation blocks
K = {  # kind: fill, border, tile
    'trigger': ('#F7EDFC', '#E3B7F1', '#B565E8'),
    'send': ('#EAFCE8', '#A9E5A1', '#1DB83A'),
    'wait': ('#FFFFFF', '#E1E4EA', '#4E5D78'),
    'condition': ('#FFE5E6', '#FFA9A4', '#F25C5C'),
    'crm': ('#E4E5FF', '#C9B3F6', '#4E5D78'),
    'goal': ('#ECFFF8', '#9FE3C6', '#12A57A'),
}

def block(kind, icon_name, label, s=1.0):
    f, b, t = K[kind]
    return (f'<div style="display: inline-flex; align-items: center; gap: {14*s:.0f}px; box-sizing: border-box; background: {f}; '
            f'border: 2px solid {b}; border-radius: {14*s:.0f}px; padding: {11*s:.0f}px {18*s:.0f}px {11*s:.0f}px {11*s:.0f}px; '
            f'box-shadow: 0 {8*s:.0f}px {24*s:.0f}px rgba(60,30,120,0.10); white-space: nowrap; {NUN}">'
            f'<span style="width: {44*s:.0f}px; height: {44*s:.0f}px; flex-shrink: 0; border-radius: {10*s:.0f}px; background: {t}; color: #FFFFFF; '
            f'display: flex; align-items: center; justify-content: center">{icon(icon_name, round(22*s))}</span>'
            f'<span style="font-size: {21*s:.1f}px; font-weight: 800; color: {INK}">{label}</span></div>')

def dash_v(h, color=CONNECTOR, ml=None):
    m = f' margin-left: {ml:.0f}px;' if ml is not None else ''
    return f'<div style="width: 0; height: {h}px;{m} border-left: 2px dashed {color}"></div>'

def dash_h(w, color=CONNECTOR):
    return f'<div style="width: {w}px; height: 0; border-top: 2px dashed {color}"></div>'

def plus(s=1.0, ml=None):
    d = round(26*s); m = f' margin-left: {ml:.0f}px;' if ml is not None else ''
    return (f'<span style="width: {d}px; height: {d}px;{m} box-sizing: border-box; border-radius: 999px; background: #FFFFFF; border: 2px solid #C77DDF; '
            f'color: #A855F7; display: flex; align-items: center; justify-content: center; font-size: {round(16*s)}px; font-weight: 700; line-height: 1; {NUN}">+</span>')

def conn(s=1.0, color=CONNECTOR):
    """Connector for a LEFT-aligned column (align-items: flex-start): centred on the icon tile."""
    return (f'<div style="display: flex; flex-direction: column; align-items: flex-start">'
            + dash_v(round(11*s), color, 34*s) + plus(s, 35*s - 13*s) + dash_v(round(11*s), color, 34*s) + '</div>')

def conn_c(s=1.0, color=CONNECTOR):
    """Connector for a CENTRED column (align-items: center)."""
    return dash_v(round(9*s + 2), color) + plus(s) + dash_v(round(9*s + 2), color)

def yesno(txt, yes, s=1.0):
    d = round(44*s); bd = INK if yes else CORAL
    return (f'<span style="width: {d}px; height: {d}px; box-sizing: border-box; flex-shrink: 0; border-radius: 999px; background: #FFFFFF; '
            f'border: 2px solid {bd}; color: {INK}; display: flex; align-items: center; justify-content: center; font-size: {round(15*s)}px; font-weight: 800; {NUN}">{txt}</span>')

def split(w, left_block, right_block, color=CONNECTOR, circle_s=0.6):
    """Yes/No split under a centred flow: two equal branches, each ending in a block."""
    col = lambda lab, yes, blk: (f'<div style="display: flex; flex-direction: column; align-items: center">'
                                 f'{dash_v(8, color)}{yesno(lab, yes, circle_s)}{dash_v(8, color)}{blk}</div>')
    return (f'<div style="width: {w}px; display: flex; flex-direction: column; align-items: center">{dash_v(8, color)}'
            f'<div style="width: 50%; height: 0; border-top: 2px dashed {color}"></div>'
            f'<div style="width: 100%; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr))">'
            f'{col("Yes", True, left_block)}{col("No", False, right_block)}</div></div>')

# ---------------------------------------------------------------- small UI parts
def tile(svg, color, size=30, r=9):
    return (f'<span style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: {r}px; background: {color}; color: #FFFFFF; '
            f'display: flex; align-items: center; justify-content: center">{svg}</span>')

def badge(text, fg, bg, size=9.5):
    return f'<span style="{INT}; font-size: {size}px; font-weight: 600; color: {fg}; background: {bg}; padding: 3px 8px; border-radius: 999px; white-space: nowrap">{text}</span>'

STATUS = {'Subscribed': ('#0B4627', '#E0FAEC'), 'Pending': ('#624C18', '#FFFAEB'), 'Unsubscribed': ('#222530', '#F2F5F8'),
          'Bounced': ('#122368', '#EBF1FF'), 'Complained': ('#71330A', '#FFF3EB'), 'Spammed': ('#681219', '#FFEBEC'),
          'Transactional': ('#351A75', '#EFEBFF'), 'Sent': ('#0B4627', '#E0FAEC'), 'Lead': ('#351A75', '#EFEBFF')}

def status(name, size=9.5):
    fg, bg = STATUS[name]; return badge(name, fg, bg, size)

def merge_chip():
    """Merge tag chip. Renders {{mergeTag}}, so the board's renderVals() must return mergeTag (write_board does)."""
    return f'<span style="{INT}; font-size: 9.5px; font-weight: 500; color: #351A75; background: #EFEBFF; padding: 2px 6px; border-radius: 6px">{{{{mergeTag}}}}</span>'

def eyebrow(text, soft=False, size=12):
    """Pill badge. Solid purple with white text on any tinted ground; soft=True (purple wash) only on white."""
    fg, bg = (PURPLE_DARK, PURPLE_WASH) if soft else ('#FFFFFF', PURPLE)
    return f'<span style="align-self: flex-start; {INT}; font-size: {size}px; font-weight: 700; letter-spacing: 0.1em; color: {fg}; background: {bg}; padding: 7px 14px; border-radius: 999px">{text}</span>'

# ---------------------------------------------------------------- cards
def campaign_card(x, y, w, icon_svg, tile_color, title, sub, label=None, line_html=None):
    """Campaign object: icon tile, name, recipients, Sent badge, optional SUBJECT/MESSAGE line."""
    line = ''
    if line_html:
        line = (f'<div style="margin-top: 9px; padding-top: 7px; border-top: 1px solid {LINE}; display: flex; flex-direction: column; gap: 3px">'
                f'<span style="font-size: 9px; font-weight: 700; letter-spacing: 0.06em; color: {MUTED}">{label}</span>'
                f'<span style="display: flex; align-items: center; font-size: 11px; font-weight: 700; white-space: nowrap">{line_html}</span></div>')
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; background: #FFFFFF; {OUTLINE}; border-radius: 14px; padding: 10px 12px; {SHADOW}; {NUN}; color: {INK}">'
            f'<div style="display: flex; align-items: center; gap: 9px">{tile(icon_svg, tile_color)}'
            f'<div style="flex: 1; display: flex; flex-direction: column; gap: 1px; min-width: 0">'
            f'<span style="font-size: 13px; font-weight: 800; line-height: 1.15">{title}</span>'
            f'<span style="font-size: 10px; font-weight: 600; color: {SLATE}">{sub}</span></div>{status("Sent")}</div>{line}</div>')

def _stat(label, val, color, width):
    return (f'<div style="display: flex; flex-direction: column; gap: 4px">'
            f'<div style="display: flex; justify-content: space-between; font-size: 10px; color: {SLATE}"><span>{label}</span><span style="color: {INK}; font-weight: 600">{val}</span></div>'
            f'<div style="height: 5px; border-radius: 999px; background: {SURFACE}"><div style="width: {width}%; height: 5px; border-radius: 999px; background: {color}"></div></div></div>')

def email_stats(x, y, w, rows=(('Opened', '52.4%', '#22D3BB', 52.4), ('Clicked', '14.8%', '#F6B51E', 14.8))):
    """Floating Email Stats card. Stat colours: sent #7B61FF, opened #22D3BB, clicked #F6B51E, bounced #335CFF."""
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; background: #FFFFFF; border: 2px solid {CARD_OUTLINE}; border-radius: 14px; '
            f'padding: 7px 10px 9px; box-shadow: 0 14px 30px rgba(60,30,120,0.20); {INT}; display: flex; flex-direction: column; gap: 5px">'
            f'<span style="font-size: 10.5px; font-weight: 600; color: {INK}">Email Stats</span>' + ''.join(_stat(*r) for r in rows) + '</div>')

def contact_pill(name='Grace Lee', initials='GL', line='Tagged Interested'):
    return (f'<div style="display: inline-flex; align-items: center; gap: 8px; background: #FFFFFF; border-radius: 999px; padding: 5px 12px 5px 5px; box-shadow: 0 10px 24px rgba(40,20,90,0.18); {NUN}">'
            f'<span style="width: 26px; height: 26px; border-radius: 999px; background: #F2EEE8; color: #3A2E22; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800">{initials}</span>'
            f'<span style="display: flex; flex-direction: column; line-height: 1.15"><span style="font-size: 11.5px; font-weight: 800; color: {INK}">{name}</span>'
            f'<span style="font-size: 9.5px; font-weight: 600; color: {SLATE}">{line}</span></span></div>')

# ---------------------------------------------------------------- sample brand: fernly (plant shop)
FERN_GREEN, FERN_CREAM = '#1F4D3A', '#FFF9EB'

def _plant(leaf, pot):
    return (f'<svg width="54" height="54" viewBox="0 0 54 54" aria-hidden="true">'
            f'<ellipse cx="20" cy="20" rx="8" ry="14" transform="rotate(-28 20 20)" fill="{leaf}"/>'
            f'<ellipse cx="34" cy="20" rx="8" ry="14" transform="rotate(28 34 20)" fill="{leaf}"/>'
            f'<ellipse cx="27" cy="16" rx="7" ry="15" fill="{leaf}" opacity="0.85"/>'
            f'<path d="M15 32h24l-3 18H18z" fill="{pot}"/></svg>')

def _product(bg, leaf, pot, name, price):
    return (f'<div style="flex: 1; background: {bg}; border-radius: 10px; padding: 6px 6px 8px; display: flex; flex-direction: column; align-items: center; gap: 2px">'
            f'{_plant(leaf, pot)}<span style="font-size: 10px; font-weight: 800; color: #1F3B2D">{name}</span>'
            f'<span style="font-size: 9.5px; font-weight: 700; color: #4F6B5C">{price}</span></div>')

def fernly_email(x, y, w, subject=False, h=420):
    """Bold sample email from the fictional store fernly, for graphics where the EMAIL IS THE ANCHOR (email campaign cards).
    Elsewhere use quiet_email(). Complete structure; size h so it runs off the BOTTOM edge only, never the sides."""
    sub = ''
    if subject:
        sub = (f'<div style="margin: 0 -10px; padding: 9px 12px 8px; background: #FFFFFF; border-bottom: 1px solid {LINE}; display: flex; align-items: center; '
               f'font-size: 10.5px; font-weight: 700; white-space: nowrap">{merge_chip()}<span style="margin-left: 2px">, spring picks</span></div>')
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; background: #FFFDF7; border-radius: 18px; '
            f'box-shadow: 0 18px 40px rgba(60,30,120,0.22); overflow: hidden; padding: 0 10px; {NUN}">{sub}'
            f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 4px 7px">'
            f'<span style="font-size: 15px; font-weight: 800; color: {FERN_GREEN}; letter-spacing: -0.01em">fernly</span>'
            f'<span style="display: flex; gap: 10px; font-size: 8.5px; font-weight: 800; letter-spacing: 0.12em; color: {FERN_GREEN}">SHOP<span>PLANTS</span></span></div>'
            f'<div style="background: {FERN_GREEN}; border-radius: 14px; padding: 13px 14px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 5px">'
            f'<span style="font-size: 8.5px; font-weight: 800; letter-spacing: 0.16em; color: #FFCC99">THE SPRING EDIT</span>'
            f'<span style="font-size: 20px; line-height: 1.1; font-weight: 800; color: {FERN_CREAM}">Fresh picks for you, Grace</span>'
            f'<span style="font-size: 10.5px; line-height: 1.35; color: #CFE3D6">New arrivals, chosen from the plants you loved.</span>'
            f'<span style="margin-top: 3px; background: #FFCC99; color: #1F3B2D; font-size: 10.5px; font-weight: 800; padding: 7px 16px; border-radius: 999px">Shop the edit</span></div>'
            f'<div style="display: flex; gap: 8px; margin-top: 9px">{_product("#EAFCE8", "#3E8E5B", "#E8A87C", "Calathea", "$24")}{_product("#FEEBB9", "#5BAA6E", "#C97B5A", "Pilea", "$18")}</div>'
            f'<div style="padding: 10px 4px 2px; font-size: 10px; line-height: 1.45; color: #4F6B5C">Free delivery on orders over $40, and easy 30-day returns.</div>'
            f'<div style="margin-top: 10px; padding-top: 8px; border-top: 2px solid {PURPLE}; display: flex; flex-direction: column; align-items: center; gap: 2px; font-size: 8.5px; color: {MUTED}"><span>fernly · 14 Garden Row, Austin</span><span><span style="color: {PURPLE}; font-weight: 700">Manage preferences</span> · Unsubscribe</span></div></div>')

def mini_email(w=176, subject='Your picks are ready', headline='Picked for you, Grace', button='Shop now'):
    """Small email preview to sit beside a Send step (expanded message block)."""
    return (f'<div style="width: {w}px; box-sizing: border-box; background: #FFFFFF; border-radius: 14px; overflow: hidden; box-shadow: 0 14px 30px rgba(40,20,90,0.22); {NUN}">'
            f'<div style="padding: 8px 10px; border-bottom: 1px solid {LINE}; font-size: 10px; font-weight: 700; display: flex; align-items: center; white-space: nowrap; color: {INK}">'
            f'<span style="color: {MUTED}; font-weight: 600; margin-right: 5px">Subject</span>{subject}</div>'
            f'<div style="padding: 9px 10px 11px; display: flex; flex-direction: column; gap: 6px">'
            f'<div style="background: {FERN_GREEN}; border-radius: 9px; padding: 10px; display: flex; flex-direction: column; gap: 5px; align-items: flex-start">'
            f'<span style="font-size: 12.5px; font-weight: 800; color: {FERN_CREAM}; line-height: 1.15">{headline}</span>'
            f'<span style="background: #FFCC99; color: #1F3B2D; font-size: 9px; font-weight: 800; padding: 4px 10px; border-radius: 999px">{button}</span></div>'
            f'<div style="height: 5px; width: 90%; border-radius: 9px; background: #EEF0F4"></div><div style="height: 5px; width: 64%; border-radius: 9px; background: #EEF0F4"></div></div></div>')

# ---------------------------------------------------------------- phones and inbox (SMS / WhatsApp)
CH = {
    'sms': dict(name='SMS', icon='sms', tile='#1DB83A', bfg='#624C18', bbg='#FFFAEB', screen='#FFFFFF', inbg='#F0F1F4', outbg=PURPLE, outfg='#FFFFFF'),
    'wa': dict(name='WhatsApp', icon='wa', tile='#1DB83A', bfg='#0B4627', bbg='#E0FAEC', screen='#F6F1E8', inbg='#FFFFFF', outbg='#D3F5CE', outfg=INK),
}

def phone(x, y, w, ch, messages=None, h=440):
    """Phone mockup. messages: list of (side, html) with side 'in' (business) or 'out' (customer)."""
    c = CH[ch]
    messages = messages or [('in', 'Hi Grace, your Calathea ships today. Track it here: <span style="color: #335CFF">fern.ly/t/482</span>'),
                            ('out', "Thank you, can't wait!"),
                            ('in', 'Enjoy 10% off your next pick with code GREEN10.')]
    def bubble(side, html):
        if side == 'in':
            return (f'<div style="align-self: flex-start; max-width: 82%; background: {c["inbg"]}; color: {INK}; border-radius: 14px 14px 14px 4px; padding: 8px 10px; '
                    f'font-size: 11px; line-height: 1.4; font-weight: 600; box-shadow: 0 1px 2px rgba(14,18,27,0.06)">{html}</div>')
        return (f'<div style="align-self: flex-end; max-width: 75%; background: {c["outbg"]}; color: {c["outfg"]}; border-radius: 14px 14px 4px 14px; padding: 8px 10px; '
                f'font-size: 11px; line-height: 1.4; font-weight: 600">{html}</div>')
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; background: #1B1530; border-radius: 34px; padding: 7px; '
            f'box-shadow: 0 20px 44px rgba(40,20,90,0.30); {NUN}; color: {INK}">'
            f'<div style="height: {h - 14}px; border-radius: 28px; background: {c["screen"]}; overflow: hidden; display: flex; flex-direction: column">'
            f'<div style="display: flex; justify-content: center; padding-top: 7px"><span style="width: 62px; height: 16px; border-radius: 999px; background: #1B1530"></span></div>'
            f'<div style="display: flex; align-items: center; gap: 8px; padding: 9px 12px; background: #FFFFFF; border-bottom: 1px solid {LINE}">'
            f'<span style="width: 28px; height: 28px; border-radius: 999px; background: {FERN_GREEN}; color: {FERN_CREAM}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800">f</span>'
            f'<span style="flex: 1; font-size: 12.5px; font-weight: 800">fernly</span>{badge(c["name"], c["bfg"], c["bbg"], 9)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 7px; padding: 12px 10px">'
            f'<span style="align-self: center; font-size: 9px; font-weight: 700; color: {MUTED}">Today 10:24</span>'
            + ''.join(bubble(s, m) for s, m in messages) + '</div></div></div>')

def inbox_card(x, y, w, ch):
    c = CH[ch]
    def row(ini, av, name, txt, unread):
        dot = (f'<span style="width: 7px; height: 7px; border-radius: 999px; background: {PURPLE}; flex-shrink: 0"></span>' if unread else '<span style="width: 7px"></span>')
        return (f'<div style="display: flex; align-items: center; gap: 8px">'
                f'<span style="width: 24px; height: 24px; border-radius: 999px; background: {av}; color: #3A2E22; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 800; flex-shrink: 0">{ini}</span>'
                f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column"><span style="font-size: 10.5px; font-weight: 800">{name}</span>'
                f'<span style="font-size: 9.5px; color: {SLATE}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{txt}</span></div>{dot}</div>')
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; background: #FFFFFF; border: 2px solid {CARD_OUTLINE}; border-radius: 14px; '
            f'padding: 9px 11px 10px; box-shadow: 0 14px 30px rgba(60,30,120,0.18); display: flex; flex-direction: column; gap: 8px; {NUN}; color: {INK}">'
            f'<div style="display: flex; align-items: center; justify-content: space-between"><span style="{INT}; font-size: 10.5px; font-weight: 600">Inbox</span>{badge("2 new", c["bfg"], c["bbg"], 9)}</div>'
            f'{row("GL", "#F2EEE8", "Grace Lee", "Thank you, can&#39;t wait!", True)}{row("MR", "#FFE5CC", "Maya Ruiz", "Does it come in a bigger pot?", True)}</div>')

# ---------------------------------------------------------------- board files
FONTS_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
              '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Nunito:wght@600;700;800&amp;family=Manrope:wght@600;700;800&amp;display=swap" rel="stylesheet">')

def board(w, h, inner, radius=28):
    """Root of a scene. Background is the {{ground}} tweak; radius 0 for full-bleed covers."""
    return (f'<div style="width: {w}px; height: {h}px; position: relative; overflow: hidden; border-radius: {radius}px; background: {{{{ground}}}}; {NUN}; color: {INK}">\n{inner}\n</div>')

def write_board(path, w, h, root_html, title, ground=LAVENDER, options=(LAVENDER, ORCHID, APRICOT, CORAL), merge_tag='{{contact.first_name}}'):
    """Write a .dc.html board for the Design canvas: one colour tweak (ground) plus the merge tag value."""
    opts = json.dumps(list(options)).replace(' ', '')
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS_LINK}
<style>
body{{margin:0}}
</style>
</helmet>
{root_html}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"ground":{{"editor":"color","default":"{ground}","options":{opts}}},"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{ ground: this.props.ground ?? '{ground}', mergeTag: '{merge_tag}' }}; }}
}}
</script>
</body>
</html>
'''
    open(path, 'w').write(doc)
    return path

def write_preview(path, root_html, ground=LAVENDER, page_bg='#FFFFFF', merge_tag='{{contact.first_name}}'):
    """Plain HTML copy for the render check, with the tweak and merge tag filled in. Fonts are added by render.py."""
    body = root_html.replace('{{ground}}', ground).replace('{{mergeTag}}', merge_tag)
    open(path, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>/*FONTS*/body{{margin:0;background:{page_bg}}}</style></head><body>{body}</body></html>')
    return path


# ---------------------------------------------------------------- report cards (0.1.1)
def _card(x, y, w, h, inner, pad='10px 12px 12px'):
    hh = f' height: {h}px;' if h else ''
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px;{hh} box-sizing: border-box; background: #FFFFFF; {OUTLINE}; border-radius: 14px; '
            f'padding: {pad}; box-shadow: 0 14px 30px rgba(60,30,120,0.18); {NUN}; color: {INK}; display: flex; flex-direction: column; justify-content: space-between; gap: 8px">{inner}</div>')

def campaigns_list(x, y, w, h=None, rows=(('Spring Picks', '2,480 contacts', 'Sent'), ('Plant Care Tips', '2,312 contacts', 'Sent'), ('Summer Preview', 'Jun 2 · 2,540 contacts', 'Scheduled'))):
    def row(name, sub, st):
        b = status('Sent') if st == 'Sent' else badge(st, '#624C18', '#FFFAEB')
        return (f'<div style="display: flex; align-items: center; gap: 9px">{tile(icon("send_campaign", 14), PURPLE, 26, 8)}'
                f'<div style="flex: 1; display: flex; flex-direction: column; min-width: 0"><span style="font-size: 11.5px; font-weight: 800">{name}</span>'
                f'<span style="font-size: 9.5px; font-weight: 600; color: {SLATE}">{sub}</span></div>{b}</div>')
    return _card(x, y, w, h, f'<span style="{INT}; font-size: 10.5px; font-weight: 600">Email Campaigns</span>' + ''.join(row(*r) for r in rows))

def link_clicks(x, y, w, h=None, rows=(('fernly.co/spring-edit', '214'), ('fernly.co/calathea', '96'), ('fernly.co/gift-cards', '57'))):
    body = ''.join(f'<div style="display: flex; justify-content: space-between; {INT}; font-size: 10px; color: {SLATE}"><span style="color: #335CFF">{u}</span><span style="color: {INK}; font-weight: 600">{n}</span></div>' for u, n in rows)
    return _card(x, y, w, h, f'<span style="{INT}; font-size: 10.5px; font-weight: 600">Link Clicks</span><div style="display: flex; flex-direction: column; gap: 6px">{body}</div>', '9px 10px 10px')

def revenue_card(x, y, w, h=None, label='Revenue · Spring Picks', value='$12,840', bars=(30, 45, 38, 60, 72, 90)):
    b = ''.join(f'<div style="flex: 1; height: {v}%; border-radius: 4px; background: {PURPLE}"></div>' for v in bars)
    return _card(x, y, w, h, f'<span style="{INT}; font-size: 11px; font-weight: 600">{label}</span><span style="{INT}; font-size: 22px; font-weight: 600">{value}</span>'
                 f'<div style="display: flex; align-items: flex-end; gap: 6px; height: 30px">{b}</div>', '12px')

def grid4(x, y, w, h, gap=16, cards=(None, None, None, None), large=192, small=120):
    """Preferred 4-card layout: two large + two small placed diagonally.
    cards = (top-left LARGE, bottom-left SMALL, top-right SMALL, bottom-right LARGE); each a function f(x, y, w, h) -> html.
    Columns share the width, both end on the same line. Scale large/small so large + gap + small == h."""
    cw = (w - gap) // 2
    tl, bl, tr, br = cards
    return (tl(x, y, cw, large) + bl(x, y + large + gap, cw, small)
            + tr(x + cw + gap, y, cw, small) + br(x + cw + gap, y + small + gap, cw, large))

# ---------------------------------------------------------------- quiet sample email (0.1.1 default)
def _plant_svg(w, h):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 120 90" aria-hidden="true"><ellipse cx="38" cy="38" rx="11" ry="22" transform="rotate(-30 38 38)" fill="#9FD8B0"/>'
            f'<ellipse cx="60" cy="30" rx="11" ry="25" fill="#7CC796"/><ellipse cx="82" cy="38" rx="11" ry="22" transform="rotate(30 82 38)" fill="#9FD8B0"/>'
            f'<path d="M40 56h40l-5 30H45z" fill="#F4C9A6"/><circle cx="18" cy="70" r="5" fill="#FFE5CC"/><circle cx="104" cy="22" r="4" fill="#E4E5FF"/></svg>')

def _bar(pct, w=None):
    width = f'{w}px' if w else f'{pct}%'
    return f'<div style="height: 6px; width: {width}; border-radius: 9px; background: #EEF0F4"></div>'

def quiet_email(x, y, w, h, subject='Welcome to fernly, Grace', headline="Glad you're here, Grace", line='Plant tips and early access, twice a month.', button='Start here'):
    """Default sample email: complete, calm, illustration-led, so the flow and copy lead.
    White body, pale mint hero with a flat illustration, outline button, grey lines for body copy, footer.
    Make h run past the panel/frame bottom so the email continues off the BOTTOM edge only."""
    tiles = ''.join(f'<div style="flex: 1; background: {bg}; border-radius: 10px; padding: 6px 2px 8px; display: flex; flex-direction: column; align-items: center; gap: 5px">{_plant_svg(56, 42)}<div style="height: 5px; width: 60%; border-radius: 9px; background: #E6E9EE"></div></div>' for bg in ('#F7FBF8', '#FFF9F2', '#F6F6FD'))
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; background: #FFFFFF; border-radius: 18px; box-shadow: 0 18px 40px rgba(60,30,120,0.18); overflow: hidden; padding: 0 12px; {NUN}">'
            f'<div style="margin: 0 -12px; padding: 9px 12px 8px; border-bottom: 1px solid {LINE}; font-size: 10px; font-weight: 700; white-space: nowrap; color: {INK}"><span style="color: {MUTED}; font-weight: 600; margin-right: 5px">Subject</span>{subject}</div>'
            f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 2px 8px"><span style="font-size: 14px; font-weight: 800; color: #3E7A57">fernly</span><span style="display: flex; gap: 5px">{_bar(0, 18)}{_bar(0, 18)}</span></div>'
            f'<div style="background: #F1FAF4; border-radius: 14px; padding: 12px 12px 14px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 6px">{_plant_svg(120, 90)}'
            f'<span style="font-size: 16px; line-height: 1.15; font-weight: 800; color: #2F5D44">{headline}</span>'
            f'<span style="font-size: 10px; line-height: 1.4; color: #6B8577">{line}</span>'
            f'<span style="margin-top: 2px; border: 1.5px solid #7CC796; color: #2F5D44; font-size: 10px; font-weight: 800; padding: 5px 14px; border-radius: 999px">{button}</span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 2px 4px">{_bar(92)}{_bar(78)}{_bar(60)}</div>'
            f'<div style="display: flex; gap: 6px; margin-top: 8px">{tiles}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 2px 4px">{_bar(88)}{_bar(70)}</div>'
            f'<div style="margin-top: 10px; background: #F7FBF8; border-radius: 12px; padding: 10px; display: flex; align-items: center; gap: 10px">{_plant_svg(48, 36)}<div style="flex: 1; display: flex; flex-direction: column; gap: 5px">{_bar(90)}{_bar(60)}</div></div>'
            f'<div style="margin-top: 12px; padding-top: 8px; border-top: 1px solid {LINE}; display: flex; flex-direction: column; align-items: center; gap: 2px; font-size: 8.5px; color: {MUTED}"><span>fernly · 14 Garden Row, Austin</span><span><span style="color: {PURPLE}; font-weight: 700">Manage preferences</span> · Unsubscribe</span></div></div>')

# ---------------------------------------------------------------- scaling for large formats (0.1.1)
def scaled(x, y, html, w, h, k=1.7):
    """Place card-sized kit pieces on 1080+ formats: w/h are the piece's NATIVE size; k scales it from the top-left.
    Typical at 1080 wide: phone k≈2.2 (zoomed, cropped off the bottom), support cards k≈1.67, block flows k≈1.25."""
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; transform: scale({k}); transform-origin: top left">{html}</div>'


# ---- 0.1.2: connected cards and overlays -------------------------------------------------
def mini_card(x, y, w, mark, title, sub, extra=''):
    """Small outlined UI card: logo or tile, title, subline, optional extra row (badge, field, slots)."""
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; background: #FFFFFF; {OUTLINE}; border-radius: 14px; padding: 9px 11px; {SHADOW}; {NUN}; color: {INK}; display: flex; flex-direction: column; gap: 6px">'
            f'<div style="display: flex; align-items: center; gap: 8px"><span style="display: flex; border-radius: 8px; overflow: hidden">{mark}</span>'
            f'<div style="display: flex; flex-direction: column; line-height: 1.2"><span style="font-size: 11.5px; font-weight: 800">{title}</span><span style="font-size: 9.5px; font-weight: 600; color: {SLATE}">{sub}</span></div></div>{extra}</div>')

def outlined_pill(name, initials, sub):
    """contact_pill with the standard 2px outline (row overlays on product screens)."""
    return contact_pill(name, initials, sub).replace('border-radius: 999px; padding: 5px 12px 5px 5px;', 'border: 2px solid #D9B8F2; border-radius: 999px; padding: 5px 14px 5px 5px;')

def elbow(x0, y0, x1, y1, r=14):
    """SVG path: vertical from (x0,y0), rounded corner, then horizontal to (x1,y1)."""
    dy = 1 if y1 > y0 else -1; dx = 1 if x1 > x0 else -1
    return f'M{x0} {y0} V{y1 - dy*r} Q{x0} {y1} {x0 + dx*r} {y1} H{x1}'

def links(w, h, paths, ends, color='#FFFFFF'):
    """The one card-to-UI connector style (0.1.3): a solid 2.5px line in a quiet tone (white on light panels,
    #E4D6FB on purple), round caps, no dashes and no ringed dots. ends: [(x, y), ...] in pairs (start, target);
    only the target end gets a small solid dot. Place last so the dot sits on top of the edge it meets."""
    return (f'<svg style="position: absolute; left: 0; top: 0; pointer-events: none" width="{w}" height="{h}" aria-hidden="true">'
            + ''.join(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>' for d in paths)
            + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>' for i, (x, y) in enumerate(ends) if i % 2) + '</svg>')


# ---- 0.1.4: blog covers are 1920x1080 ----------------------------------------------------
BLOG_W, BLOG_H = 1920, 1080
def blog_cover(inner, panel):
    """Wrap a blog-cover scene into the 1920x1080 cover on ONE solid background colour (no panel over a lighter ground).
    Pass the same colour as the board's ground. The scene is laid out on a 1104x532 grid (anchor on the right with its
    top at y 48 and running past y 532; left column centred on y 266), scaled x1.7, centred horizontally and dropped
    120px so the anchor crops at the bottom edge."""
    return (f'<div style="position: absolute; inset: 0; background: {panel}; overflow: hidden">'
            f'<div style="position: absolute; left: 21px; top: 120px; width: 1104px; height: 532px; transform: scale(1.7); transform-origin: 0 0">{inner}</div></div>')
