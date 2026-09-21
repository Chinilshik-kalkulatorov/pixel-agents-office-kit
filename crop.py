#!/usr/bin/env python3
"""Render a layout.json and crop to a tile rectangle (inclusive), zoomed.
Usage: crop.py <layout.json> <out.png> --cols C0-C1 --rows R0-R1 [--zoom N] [--chars] [--grid] [--labels]
0-based tile coords. The crop includes the 1-tile strip above row R0 so wall art at row -1 shows."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_layout
a = sys.argv[1:]; src, out = a[0], a[1]
def rng(flag):
    x, y = a[a.index(flag) + 1].split('-'); return int(x), int(y)
c0, c1 = rng('--cols'); r0, r1 = rng('--rows')
zoom = int(a[a.index('--zoom') + 1]) if '--zoom' in a else 4
img, _ = render_layout.render(json.load(open(src)), zoom=zoom, chars='--chars' in a, grid='--grid' in a, labels='--labels' in a)
T = 16 * zoom; OY = 16 * zoom
img.crop((c0 * T, max(0, OY + r0 * T - T), (c1 + 1) * T, OY + (r1 + 1) * T)).save(out)
print(f'saved {out} cols {c0}-{c1} rows {r0}-{r1} zoom {zoom}')
