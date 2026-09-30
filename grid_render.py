#!/usr/bin/env python3
"""Owner-facing grid render: layout -> PNG with a margin, grid lines and column/row numbers on all four sides.
Usage: grid_render.py <layout.json> <out.png> [--zoom N] [--chars]"""
import sys, os, json
sys.path.insert(0, os.path.expanduser('~/.pixel-agents/office-kit'))
import render_layout
from PIL import Image, ImageDraw, ImageFont
a = sys.argv[1:]; src, out = a[0], a[1]
Z = int(a[a.index('--zoom') + 1]) if '--zoom' in a else 4
L = json.load(open(src)); cols, rows = L['cols'], L['rows']
img, _ = render_layout.render(L, zoom=Z, chars='--chars' in a)
T = 16 * Z; OY = 16 * Z                       # render has a 1-tile strip on top for wall art at row -1
M = max(40, T // 2 + 12)                      # label margin
W, H = img.width + 2 * M, img.height + 2 * M
can = Image.new('RGBA', (W, H), (18, 18, 24, 255)); can.alpha_composite(img, (M, M))
d = ImageDraw.Draw(can)
font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', max(14, T // 3))
x0, y0 = M, M + OY                            # pixel origin of tile (0,0)
for c in range(cols + 1):
    x = x0 + c * T; d.line([(x, M), (x, y0 + rows * T)], fill=(255, 255, 255, 70), width=1)
for r in range(rows + 1):
    y = y0 + r * T; d.line([(M, y), (M + cols * T, y)], fill=(255, 255, 255, 70), width=1)
for c in range(0, cols + 1, 5):               # heavier line every 5 tiles
    x = x0 + c * T; d.line([(x, M), (x, y0 + rows * T)], fill=(255, 220, 90, 110), width=2)
for r in range(0, rows + 1, 5):
    y = y0 + r * T; d.line([(M, y), (M + cols * T, y)], fill=(255, 220, 90, 110), width=2)
def ctext(cx, cy, s, fill=(255, 225, 90, 255)):
    bb = d.textbbox((0, 0), s, font=font); w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - w / 2 - bb[0], cy - h / 2 - bb[1]), s, font=font, fill=fill)
for c in range(cols):
    cx = x0 + c * T + T / 2
    ctext(cx, M / 2, str(c)); ctext(cx, H - M / 2, str(c))
ctext(M / 2, M + OY / 2, '-1', fill=(150, 150, 170, 255)); ctext(W - M / 2, M + OY / 2, '-1', fill=(150, 150, 170, 255))
for r in range(rows):
    cy = y0 + r * T + T / 2
    ctext(M / 2, cy, str(r)); ctext(W - M / 2, cy, str(r))
can.convert('RGB').save(out)
print(f'saved {out} {can.size} zoom={Z}')
