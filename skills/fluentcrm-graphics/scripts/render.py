"""Render check for FluentCRM boards.

Usage:
  python3 render.py preview.html out.png WIDTH HEIGHT [--scale 2]
  python3 render.py --sheet out.png a.png b.png ...        # contact sheet of several renders
  python3 render.py --measure preview.html W H "Label text" # print the bounding box of the element holding that text

Needs Playwright for Python and a Chromium/Chrome. Fonts: Google Fonts is often blocked in
sandboxes, so the script installs Nunito, Inter and Manrope from npm (@fontsource) into
~/.cache/fluentcrm-fonts on first use and inlines @font-face rules. If npm is unavailable it
falls back to the Google Fonts link, and warns that text metrics may differ.
"""
import os, sys, glob, subprocess, shutil

CACHE = os.path.expanduser('~/.cache/fluentcrm-fonts')
FAMILIES = {'Nunito': [600, 700, 800], 'Inter': [400, 500, 600, 700], 'Manrope': [600, 700, 800]}

def font_css():
    os.makedirs(CACHE, exist_ok=True)
    css = []
    for fam, weights in FAMILIES.items():
        pkg = f'@fontsource/{fam.lower()}'
        dirs = glob.glob(os.path.join(CACHE, f'fontsource-{fam.lower()}-*', 'package'))
        if not dirs and shutil.which('npm'):
            try:
                tgz = subprocess.run(['npm', 'pack', pkg], cwd=CACHE, capture_output=True, text=True, timeout=120).stdout.strip().splitlines()[-1]
                out = os.path.join(CACHE, tgz[:-4]); os.makedirs(out, exist_ok=True)
                subprocess.run(['tar', 'xzf', os.path.join(CACHE, tgz), '-C', out], check=True)
                dirs = glob.glob(os.path.join(CACHE, f'fontsource-{fam.lower()}-*', 'package'))
            except Exception as e:
                print(f'warn: could not fetch {pkg}: {e}', file=sys.stderr)
        if not dirs:
            return None
        for w in weights:
            f = os.path.join(dirs[0], 'files', f'{fam.lower()}-latin-{w}-normal.woff2')
            if os.path.exists(f):
                css.append(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{f}')}}")
    return ''.join(css)

def prepare(preview):
    html = open(preview).read()
    css = font_css()
    if css is None:
        print('warn: fonts not installed locally; using Google Fonts link (may be blocked).', file=sys.stderr)
        css = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Nunito:wght@600;700;800&family=Manrope:wght@600;700;800&display=swap');"
    tmp = preview + '.render.html'
    open(tmp, 'w').write(html.replace('/*FONTS*/', css))
    return tmp

def browser(p):
    for exe in [None, '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser']:
        try:
            return p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        except Exception:
            continue
    raise SystemExit('No Chromium available: run `python3 -m playwright install chromium`.')

def shoot(preview, out, w, h, scale=2):
    from playwright.sync_api import sync_playwright
    tmp = prepare(preview)
    with sync_playwright() as p:
        b = browser(p); pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=scale)
        pg.goto('file://' + os.path.abspath(tmp)); pg.wait_for_timeout(500)
        pg.screenshot(path=out); b.close()
    print(out)

def measure(preview, w, h, text):
    from playwright.sync_api import sync_playwright
    tmp = prepare(preview)
    with sync_playwright() as p:
        b = browser(p); pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto('file://' + os.path.abspath(tmp)); pg.wait_for_timeout(400)
        r = pg.evaluate('''(t)=>{const e=[...document.querySelectorAll("span")].find(x=>x.textContent.trim()==t);
            if(!e) return null; const r=e.parentElement.getBoundingClientRect(); return [r.left,r.top,r.right,r.bottom].map(Math.round)}''', text)
        b.close()
    print(r)

def sheet(out, files, pad=20, bg='#2A1650'):
    from PIL import Image
    ims = [Image.open(f) for f in files]
    W = max(i.width for i in ims) + 2*pad
    H = sum(i.height for i in ims) + pad*(len(ims)+1)
    S = Image.new('RGB', (W, H), bg); y = pad
    for i in ims:
        S.paste(i, (pad, y)); y += i.height + pad
    S.save(out); print(out)

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--sheet':
        sheet(a[1], a[2:])
    elif a and a[0] == '--measure':
        measure(a[1], int(a[2]), int(a[3]), a[4])
    else:
        scale = 2
        if '--scale' in a:
            i = a.index('--scale'); scale = float(a[i+1]); a = a[:i] + a[i+2:]
        shoot(a[0], a[1], int(a[2]), int(a[3]), scale)
