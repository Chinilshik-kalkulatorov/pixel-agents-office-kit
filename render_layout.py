#!/usr/bin/env python3
"""Faithful offline renderer for Pixel Agents layout.json -> PNG.

Replicates webview engine: floor colorize (Photoshop-style), wall auto-tiling
(bitmask N1 E2 S4 W8, 16x32 pieces anchored at tile bottom), carpets
(marching squares, dual-color), furniture (z-sorted, ':left' mirrored,
per-item color adjust/colorize), optional placeholder characters on seats.

Usage: render_layout.py <layout.json> <out.png> [--zoom N] [--chars] [--grid]
"""
import json, os, sys, colorsys
from PIL import Image, ImageDraw

ASSETS = os.environ.get('PIXEL_ASSETS', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets'))
CATALOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'furniture-catalog.json')
TILE = 16
WALL_COLOR_HEX = '#3A3A5C'
CARPET_DEFAULT = {'h': 0, 's': 71, 'b': -32, 'c': 0, 'colorize': True}
CARPET_DEFAULT_ACCENT = {'h': 34, 's': 64, 'b': 21, 'c': 0, 'colorize': True}

# ---------------------------------------------------------------- color math
def hsl_to_rgb(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60.0
    x = c * (1 - abs((hp % 2) - 1))
    if hp < 1: r1, g1, b1 = c, x, 0
    elif hp < 2: r1, g1, b1 = x, c, 0
    elif hp < 3: r1, g1, b1 = 0, c, x
    elif hp < 4: r1, g1, b1 = 0, x, c
    elif hp < 5: r1, g1, b1 = x, 0, c
    else: r1, g1, b1 = c, 0, x
    m = l - c / 2
    cl = lambda v: max(0, min(255, round((v + m) * 255)))
    return cl(r1), cl(g1), cl(b1)

def rgb_to_hsl(r, g, b):
    rf, gf, bf = r / 255, g / 255, b / 255
    mx, mn = max(rf, gf, bf), min(rf, gf, bf)
    l = (mx + mn) / 2
    if mx == mn: return 0, 0, l
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == rf: h = ((gf - bf) / d + (6 if gf < bf else 0)) * 60
    elif mx == gf: h = ((bf - rf) / d + 2) * 60
    else: h = ((rf - gf) / d + 4) * 60
    return h, s, l

def apply_bc(lightness, b, c):
    if c: lightness = 0.5 + (lightness - 0.5) * ((100 + c) / 100)
    if b: lightness = lightness + b / 200
    return max(0.0, min(1.0, lightness))

def colorize_img(im, col):
    """Photoshop colorize: luminance -> HSL(h,s)."""
    h, s, b, c = col['h'], col['s'], col['b'], col['c']
    out = Image.new('RGBA', im.size)
    src = im.load(); dst = out.load()
    cache = {}
    for y in range(im.height):
        for x in range(im.width):
            r, g, bb, a = src[x, y]
            if a == 0: continue
            key = (r, g, bb)
            if key not in cache:
                lum = (0.299 * r + 0.587 * g + 0.114 * bb) / 255
                cache[key] = hsl_to_rgb(h, s / 100, apply_bc(lum, b, c))
            dst[x, y] = cache[key] + (a,)
    return out

def adjust_img(im, col):
    h, s, b, c = col['h'], col['s'], col['b'], col['c']
    out = Image.new('RGBA', im.size)
    src = im.load(); dst = out.load()
    cache = {}
    for y in range(im.height):
        for x in range(im.width):
            r, g, bb, a = src[x, y]
            if a == 0: continue
            key = (r, g, bb)
            if key not in cache:
                oh, os_, ol = rgb_to_hsl(r, g, bb)
                nh = (oh + h) % 360
                ns = max(0, min(1, os_ + s / 100))
                cache[key] = hsl_to_rgb(nh, ns, apply_bc(ol, b, c))
            dst[x, y] = cache[key] + (a,)
    return out

def flat_colorize(im, col):
    h, s, b, c = col['h'], col['s'], col['b'], col['c']
    rgb = hsl_to_rgb(h, s / 100, apply_bc(0.5, b, c))
    out = Image.new('RGBA', im.size)
    src = im.load(); dst = out.load()
    for y in range(im.height):
        for x in range(im.width):
            a = src[x, y][3]
            if a: dst[x, y] = rgb + (a,)
    return out

def wall_hex(col):
    return hsl_to_rgb(col['h'], col['s'] / 100, apply_bc(0.5, col['b'], col['c']))

# ---------------------------------------------------------------- assets
_cache = {}
def load(p):
    if p not in _cache: _cache[p] = Image.open(p).convert('RGBA')
    return _cache[p]

def floors():
    return [load(f'{ASSETS}/floors/floor_{i}.png') for i in range(9)]

def wall_pieces():
    w = load(f'{ASSETS}/walls/wall_0.png')
    return [w.crop(((m % 4) * 16, (m // 4) * 32, (m % 4) * 16 + 16, (m // 4) * 32 + 32)) for m in range(16)]

def carpet_sets():
    sets = []
    for i in range(3):
        p = f'{ASSETS}/carpets/carpet_{i}.png'
        if not os.path.exists(p): break
        sh = load(p)
        sets.append([sh.crop(((m % 4) * 16, (m // 4) * 16, (m % 4) * 16 + 16, (m // 4) * 16 + 16)) for m in range(16)])
    return sets

def catalog():
    cat = {}
    for e in json.load(open(CATALOG_PATH)):
        e = dict(e)
        cat[e['id']] = e
    # virtual :left entries
    for k in list(cat):
        e = cat[k]
        if e.get('mirrorSide') and e.get('orientation') == 'side':
            le = dict(e); le['orientation'] = 'left'; le['virtual_left'] = True
            cat[k + ':left'] = le
    return cat

def entry_sprite(e):
    return load(f"{ASSETS}/{e['furniturePath']}")

# ---------------------------------------------------------------- seats
def seats_of(furniture, cat):
    desk = set()
    for it in furniture:
        e = cat.get(it['type'])
        if not e or not e['isDesk']: continue
        for dr in range(e['footprintH']):
            for dc in range(e['footprintW']):
                desk.add((it['col'] + dc, it['row'] + dr))
    out = []
    dirs = [((0, -1), 'up'), ((0, 1), 'down'), ((-1, 0), 'left'), ((1, 0), 'right')]
    for it in furniture:
        e = cat.get(it['type'])
        if not e or e['category'] != 'chairs': continue
        bg = e.get('backgroundTiles', 0) or 0
        for dr in range(bg, e['footprintH']):
            for dc in range(e['footprintW']):
                tc, tr = it['col'] + dc, it['row'] + dr
                o = e.get('orientation')
                if o: facing = {'front': 'down', 'back': 'up', 'left': 'left', 'right': 'right', 'side': 'right'}[o]
                else:
                    facing = 'down'
                    for (ddc, ddr), f in dirs:
                        if (tc + ddc, tr + ddr) in desk: facing = f; break
                out.append({'col': tc, 'row': tr, 'facing': facing, 'uid': it['uid']})
    return out

# ---------------------------------------------------------------- render
def render(layout, zoom=2, chars=False, grid=False, labels=False):
    cols, rows = layout['cols'], layout['rows']
    tiles = layout['tiles']; tcol = layout.get('tileColors') or [None] * len(tiles)
    cat = catalog(); fl = floors(); wp = wall_pieces(); cs = carpet_sets()
    W, H = cols * TILE, rows * TILE
    img = Image.new('RGBA', (W, H + 16), (30, 30, 36, 255))  # extra top for tall walls
    OY = 16
    tm = [[tiles[r * cols + c] for c in range(cols)] for r in range(rows)]
    # floors
    fcache = {}
    for r in range(rows):
        for c in range(cols):
            t = tm[r][c]
            if t == 255: continue
            if t == 0:
                col = tcol[r * cols + c]
                rgb = wall_hex(col) if col else (0x3A, 0x3A, 0x5C)
                img.paste(rgb + (255,), (c * TILE, OY + r * TILE, c * TILE + TILE, OY + r * TILE + TILE))
                continue
            col = tcol[r * cols + c] or {'h': 0, 's': 0, 'b': 0, 'c': 0}
            key = (t, col['h'], col['s'], col['b'], col['c'])
            if key not in fcache:
                base = fl[t - 1] if 1 <= t <= 9 else fl[0]
                fcache[key] = colorize_img(base, col)
            img.paste(fcache[key], (c * TILE, OY + r * TILE))
    # carpets
    ct = layout.get('carpetTiles')
    if ct and cs:
        pal = []
        for vs in cs:
            uniq = set()
            for sp in vs:
                for px in sp.getdata():
                    if px[3]: uniq.add(px[:3])
            srt = sorted(uniq, key=lambda p: 0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
            pal.append((srt[0], srt[-1]) if srt else (None, None))
        def pkey(t):
            c1 = t.get('color') or CARPET_DEFAULT; c2 = t.get('accentColor') or CARPET_DEFAULT_ACCENT
            return (c1['h'], c1['s'], c1['b'], c1['c'], c2['h'], c2['s'], c2['b'], c2['c'])
        def has(cc, rr, var, pk):
            if cc < 0 or rr < 0 or cc >= cols or rr >= rows: return False
            t = ct[rr * cols + cc]
            return bool(t) and t['variant'] == var and pkey(t) == pk
        ccache = {}
        for jy in range(rows + 1):
            for jx in range(cols + 1):
                groups = {}
                for (cc, rr) in [(jx - 1, jy - 1), (jx, jy - 1), (jx, jy), (jx - 1, jy)]:
                    if cc < 0 or rr < 0 or cc >= cols or rr >= rows: continue
                    t = ct[rr * cols + cc]
                    if not t: continue
                    k = (t['variant'], pkey(t))
                    o = t.get('order', 0) or 0
                    if k not in groups or o > groups[k][1]: groups[k] = (t, o)
                for (var, pk), (t, o) in sorted(groups.items(), key=lambda kv: kv[1][1]):
                    if var >= len(cs): continue
                    ms = 0
                    if has(jx - 1, jy - 1, var, pk): ms |= 1
                    if has(jx, jy - 1, var, pk): ms |= 2
                    if has(jx, jy, var, pk): ms |= 4
                    if has(jx - 1, jy, var, pk): ms |= 8
                    if ms == 0: continue
                    key = (var, ms, pk)
                    if key not in ccache:
                        base = cs[var][ms]; main, acc = pal[var]
                        if main is None: continue
                        acc = acc or main
                        mm = Image.new('RGBA', base.size); am = Image.new('RGBA', base.size)
                        bp = base.load(); mp = mm.load(); ap = am.load()
                        for y in range(16):
                            for x in range(16):
                                p = bp[x, y]
                                if not p[3]: continue
                                if p[:3] == main: mp[x, y] = p
                                if p[:3] == acc: ap[x, y] = p
                        c1 = t.get('color') or CARPET_DEFAULT; c2 = t.get('accentColor') or CARPET_DEFAULT_ACCENT
                        m1 = flat_colorize(mm, c1); m2 = flat_colorize(am, c2)
                        merged = Image.alpha_composite(m1, m2)
                        ccache[key] = merged
                    img.alpha_composite(ccache[key], (jx * TILE - 8, OY + jy * TILE - 8))
    # drawables
    draw = []
    for r in range(rows):
        for c in range(cols):
            if tm[r][c] != 0: continue
            m = 0
            if r > 0 and tm[r - 1][c] == 0: m |= 1
            if c < cols - 1 and tm[r][c + 1] == 0: m |= 2
            if r < rows - 1 and tm[r + 1][c] == 0: m |= 4
            if c > 0 and tm[r][c - 1] == 0: m |= 8
            sp = wp[m]
            col = tcol[r * cols + c]
            if col: sp = colorize_img(sp, col)
            draw.append(((r + 1) * TILE, 0, sp, c * TILE, r * TILE + 16 - 32, False))
    furn = layout.get('furniture', [])
    deskZ = {}
    for it in furn:
        e = cat.get(it['type'])
        if not e or not e['isDesk']: continue
        z = it['row'] * TILE + e['height']
        for dr in range(e['footprintH']):
            for dc in range(e['footprintW']):
                k = (it['col'] + dc, it['row'] + dr)
                if k not in deskZ or z > deskZ[k]: deskZ[k] = z
    missing = []
    for i, it in enumerate(furn):
        e = cat.get(it['type'])
        if not e: missing.append(it['type']); continue
        sp = entry_sprite(e)
        x, y = it['col'] * TILE, it['row'] * TILE
        z = y + e['height']
        if e['category'] == 'chairs':
            z = (it['row'] + e['footprintH']) * TILE + 1 if e.get('orientation') == 'back' else (it['row'] + 1) * TILE
        if e.get('canPlaceOnSurfaces'):
            for dr in range(e['footprintH']):
                for dc in range(e['footprintW']):
                    dz = deskZ.get((it['col'] + dc, it['row'] + dr))
                    if dz is not None and dz + 0.5 > z: z = dz + 0.5
        if it.get('color'):
            cc = it['color']
            sp = colorize_img(sp, cc) if cc.get('colorize') else adjust_img(sp, cc)
        mirrored = bool(e.get('virtual_left'))
        draw.append((z, 1, sp, x, y, mirrored))
    # characters placeholder on seats
    if chars:
        sheet = load(f'{ASSETS}/characters/char_0.png')
        frames = {'down': sheet.crop((0, 0, 16, 32)), 'up': sheet.crop((0, 32, 16, 64)), 'right': sheet.crop((0, 64, 16, 96))}
        frames['left'] = frames['right'].transpose(Image.FLIP_LEFT_RIGHT)
        for s in seats_of(furn, cat):
            sp = frames[s['facing']]
            draw.append(((s['row'] + 1) * TILE + 0.25, 1, sp, s['col'] * TILE, s['row'] * TILE - 16, False))
    draw.sort(key=lambda d: (d[0], d[1]))
    for z, _, sp, x, y, mir in draw:
        if mir: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
        img.alpha_composite(sp, (x, OY + y))
    if zoom != 1:
        img = img.resize((img.width * zoom, img.height * zoom), Image.NEAREST)
    if grid:
        d = ImageDraw.Draw(img)
        for c in range(cols + 1): d.line([(c * TILE * zoom, 0), (c * TILE * zoom, img.height)], fill=(255, 255, 255, 40))
        for r in range(rows + 1): d.line([(0, OY * zoom + r * TILE * zoom), (img.width, OY * zoom + r * TILE * zoom)], fill=(255, 255, 255, 40))
        if labels:
            for c in range(cols): d.text((c * TILE * zoom + 2, 2), str(c), fill=(255, 255, 0, 200))
            for r in range(rows): d.text((2, OY * zoom + r * TILE * zoom + 2), str(r), fill=(255, 255, 0, 200))
    return img, missing

def main():
    a = sys.argv[1:]
    if len(a) < 2:
        print(__doc__); sys.exit(1)
    src, out = a[0], a[1]
    zoom = int(a[a.index('--zoom') + 1]) if '--zoom' in a else 2
    layout = json.load(open(src))
    img, missing = render(layout, zoom=zoom, chars='--chars' in a, grid='--grid' in a, labels='--labels' in a)
    img.save(out)
    print(f'saved {out} {img.size} cols={layout["cols"]} rows={layout["rows"]} furniture={len(layout.get("furniture", []))}')
    if missing: print('UNKNOWN TYPES:', sorted(set(missing)))

if __name__ == '__main__':
    main()
