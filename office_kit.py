#!/usr/bin/env python3
"""Office kit for Pixel Agents layouts.

  office_kit.py build <spec.py> <out.json>     build layout.json from a spec module
  office_kit.py validate <layout.json>         validate a layout (exit 1 on errors)
  office_kit.py render <layout.json> <out.png> [--zoom N] [--chars] [--grid] [--labels]
  office_kit.py all <spec.py> <name>           build + validate + render (name.json / name.png / name_grid.png)

Spec module (plain Python file) must define:
  MAP: str  multi-line ASCII map. '#' = wall, '.' = void, any other char = floor room key.
  LEGEND: dict  room key -> {'tile': 1..9, 'color': {'h','s','b','c'}}  (floor pattern + colorize)
  WALL_COLOR: {'h','s','b','c'}                 default wall colorize (None = raw sprite)
  WALL_COLORS: dict  optional, room key -> wall color; a wall tile takes the color of the
                     first adjacent (S, E, W, N order) floor room key found in this dict.
  FURNITURE: list of tuples (type, col, row) or (type, col, row, color_dict)
  CARPETS: list of dicts {'variant':0..2, 'col','row','w','h', 'color':{...}, 'accent':{...}}  (optional)
  PETS: list of ints (pet type idx)  (optional)
"""
import json, os, sys, importlib.util, hashlib
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'furniture-catalog.json')
AUTO_ON_FACING_DEPTH = 3

def catalog():
    cat = {}
    for e in json.load(open(CATALOG_PATH)):
        cat[e['id']] = dict(e)
    for k in list(cat):
        e = cat[k]
        if e.get('mirrorSide') and e.get('orientation') == 'side':
            le = dict(e); le['orientation'] = 'left'
            cat[k + ':left'] = le
    return cat

# ------------------------------------------------------------------ build
def load_spec(path):
    spec = importlib.util.spec_from_file_location('spec', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def build(spec):
    lines = [l for l in spec.MAP.strip('\n').split('\n')]
    lines = [l.rstrip() for l in lines if l.strip() != '']
    cols = max(len(l) for l in lines); rows = len(lines)
    lines = [l.ljust(cols, '.') for l in lines]
    legend = spec.LEGEND
    wall_color = getattr(spec, 'WALL_COLOR', None)
    wall_colors = getattr(spec, 'WALL_COLORS', {}) or {}
    tiles, tcol = [], []
    for r in range(rows):
        for c in range(cols):
            ch = lines[r][c]
            if ch == '#':
                tiles.append(0)
                wc = wall_color
                for dr, dc in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] in wall_colors:
                        wc = wall_colors[lines[rr][cc]]; break
                tcol.append(dict(wc) if wc else None)
            elif ch == '.':
                tiles.append(255); tcol.append(None)
            else:
                if ch not in legend: raise SystemExit(f'MAP char {ch!r} at ({c},{r}) not in LEGEND')
                room = legend[ch]
                tiles.append(int(room['tile'])); tcol.append(dict(room['color']))
    furniture = []
    for i, f in enumerate(spec.FURNITURE):
        t, c, r = f[0], int(f[1]), int(f[2])
        color = f[3] if len(f) > 3 and f[3] else None
        uid = 'f-' + hashlib.md5(f'{i}-{t}-{c}-{r}'.encode()).hexdigest()[:10]
        item = {'uid': uid, 'type': t, 'col': c, 'row': r}
        if color: item['color'] = dict(color)
        furniture.append(item)
    layout = {'version': 1, 'cols': cols, 'rows': rows, 'layoutRevision': 1,
              'tiles': tiles, 'tileColors': tcol, 'furniture': furniture}
    carpets = getattr(spec, 'CARPETS', None)
    if carpets:
        ct = [None] * (cols * rows)
        for order, cp in enumerate(carpets, start=1):
            for r in range(cp['row'], cp['row'] + cp['h']):
                for c in range(cp['col'], cp['col'] + cp['w']):
                    if 0 <= r < rows and 0 <= c < cols and tiles[r * cols + c] not in (0, 255):
                        t = {'variant': int(cp.get('variant', 0)), 'order': order}
                        if cp.get('color'): t['color'] = {**cp['color'], 'colorize': True}
                        if cp.get('accent'): t['accentColor'] = {**cp['accent'], 'colorize': True}
                        ct[r * cols + c] = t
        layout['carpetTiles'] = ct
    pets = getattr(spec, 'PETS', None)
    if pets:
        layout['pets'] = [{'id': f'pet-{i}-{p}', 'petType': int(p)} for i, p in enumerate(pets)]
    return layout

# ------------------------------------------------------------------ validate
def footprint(e, it, skip_bg=True):
    bg = (e.get('backgroundTiles') or 0) if skip_bg else 0
    for dr in range(bg, e['footprintH']):
        for dc in range(e['footprintW']):
            yield it['col'] + dc, it['row'] + dr

def validate(layout, verbose=True):
    errs, warns, info = [], [], []
    cat = catalog()
    cols, rows = layout['cols'], layout['rows']
    tiles = layout['tiles']
    if len(tiles) != cols * rows: errs.append(f'tiles length {len(tiles)} != {cols*rows}')
    tc = layout.get('tileColors')
    if tc is not None and len(tc) != cols * rows: errs.append('tileColors length mismatch')
    if cols > 64 or rows > 64: errs.append('grid exceeds 64x64')
    def tile(c, r):
        if c < 0 or r < 0 or c >= cols or r >= rows: return None
        return tiles[r * cols + c]
    furn = layout.get('furniture', [])
    uids = set()
    occupied = {}   # (c,r) -> uid  (non-bg rows)
    desk_tiles = set(); elec = set()
    for it in furn:
        if it['uid'] in uids: errs.append(f'duplicate uid {it["uid"]}')
        uids.add(it['uid'])
        e = cat.get(it['type'])
        if not e: errs.append(f'unknown type {it["type"]}'); continue
        if e['isDesk']:
            for k in footprint(e, it, skip_bg=False): desk_tiles.add(k)
        if e['category'] == 'electronics':
            for k in footprint(e, it, skip_bg=False): elec.add(k)
    for it in furn:
        e = cat.get(it['type'])
        if not e: continue
        w, h = e['footprintW'], e['footprintH']
        c, r = it['col'], it['row']
        name = f'{it["type"]}@({c},{r})'
        if e.get('canPlaceOnWalls'):
            br = r + h - 1
            if c < 0 or c + w > cols or br < 0 or br >= rows: errs.append(f'{name} out of bounds'); continue
            for dc in range(w):
                if tile(c + dc, br) != 0: errs.append(f'{name} wall item: bottom row tile ({c+dc},{br}) is not WALL')
        else:
            if c < 0 or r < 0 or c + w > cols or r + h > rows: errs.append(f'{name} out of bounds'); continue
            for (cc, rr) in footprint(e, it):
                t = tile(cc, rr)
                if t == 255: errs.append(f'{name} on VOID at ({cc},{rr})')
                elif t == 0: errs.append(f'{name} overlaps WALL at ({cc},{rr})')
        for k in footprint(e, it):
            if k in occupied:
                if e.get('canPlaceOnSurfaces') and k in desk_tiles: continue
                other = occupied[k]
                errs.append(f'{name} overlaps {other} at {k}')
            else:
                occupied[k] = name
        if e.get('canPlaceOnSurfaces') and e['category'] == 'electronics':
            on_desk = all(k in desk_tiles for k in footprint(e, it))
            if not on_desk: warns.append(f'{name} electronics not fully on a desk surface')
    # seats
    seats = []
    dirs = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
    for it in furn:
        e = cat.get(it['type'])
        if not e or e['category'] != 'chairs': continue
        o = e.get('orientation')
        for (cc, rr) in footprint(e, it):
            if o: facing = {'front': 'down', 'back': 'up', 'left': 'left', 'right': 'right', 'side': 'right'}[o]
            else:
                facing = 'down'
                for f, (dc, dr) in (('up', (0, -1)), ('down', (0, 1)), ('left', (-1, 0)), ('right', (1, 0))):
                    if (cc + dc, rr + dr) in desk_tiles: facing = f; break
            dc, dr = dirs[facing]
            pc = False
            for d in range(1, AUTO_ON_FACING_DEPTH + 1):
                tcx, tcy = cc + dc * d, rr + dr * d
                if (tcx, tcy) in elec: pc = True; break
                if dc != 0 and ((tcx, tcy - 1) in elec or (tcx, tcy + 1) in elec): pc = True; break
                if dc == 0 and ((tcx - 1, tcy) in elec or (tcx + 1, tcy) in elec): pc = True; break
            near_desk = any((cc + ddc, rr + ddr) in desk_tiles for ddc, ddr in dirs.values())
            seats.append({'col': cc, 'row': rr, 'facing': facing, 'pc': pc, 'desk': near_desk, 'type': it['type']})
    seat_tiles = {(s['col'], s['row']) for s in seats}
    # walkability
    blocked = set(k for k in occupied) - seat_tiles
    walk = set()
    for r in range(rows):
        for c in range(cols):
            t = tiles[r * cols + c]
            if t not in (0, 255) and (c, r) not in blocked: walk.add((c, r))
    if not walk: errs.append('no walkable tiles')
    comps = []; seen = set()
    for start in sorted(walk):
        if start in seen: continue
        q = deque([start]); comp = {start}; seen.add(start)
        while q:
            c, r = q.popleft()
            for dc, dr in dirs.values():
                n = (c + dc, r + dr)
                if n in walk and n not in seen: seen.add(n); comp.add(n); q.append(n)
        comps.append(comp)
    comps.sort(key=len, reverse=True)
    main = comps[0] if comps else set()
    unreachable_seats = [s for s in seats if (s['col'], s['row']) not in main]
    for s in unreachable_seats: errs.append(f'seat {s["type"]}@({s["col"]},{s["row"]}) unreachable from main walkable area')
    if len(comps) > 1:
        for comp in comps[1:]:
            if len(comp) >= 3: warns.append(f'isolated walkable pocket of {len(comp)} tiles near {sorted(comp)[0]}')
    pc_seats = [s for s in seats if s['pc']]
    info.append(f'grid {cols}x{rows}, furniture {len(furn)}, seats {len(seats)} (facing PC: {len(pc_seats)}, at desk: {sum(1 for s in seats if s["desk"])}), walkable {len(walk)} tiles in {len(comps)} region(s)')
    nodesk = [s for s in seats if not s['desk'] and s['type'] not in ('SOFA_FRONT', 'SOFA_BACK', 'SOFA_SIDE', 'SOFA_SIDE:left', 'CUSHIONED_BENCH', 'WOODEN_BENCH')]
    for s in nodesk: warns.append(f'chair {s["type"]}@({s["col"]},{s["row"]}) has no adjacent desk')
    ok = not errs
    if verbose:
        for e in errs: print('ERROR:', e)
        for w in warns: print('WARN:', w)
        for i in info: print('INFO:', i)
        print('VALID' if ok else 'INVALID')
    return ok, errs, warns, seats

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    cmd = a[0]
    if cmd == 'build':
        layout = build(load_spec(a[1]))
        json.dump(layout, open(a[2], 'w'), indent=1)
        print(f'built {a[2]} {layout["cols"]}x{layout["rows"]} furniture={len(layout["furniture"])}')
    elif cmd == 'validate':
        ok, *_ = validate(json.load(open(a[1])))
        sys.exit(0 if ok else 1)
    elif cmd == 'render':
        sys.path.insert(0, HERE)
        import render_layout
        sys.argv = ['render_layout.py'] + a[1:]
        render_layout.main()
    elif cmd == 'all':
        spec_path, name = a[1], a[2]
        layout = build(load_spec(spec_path))
        jp = f'{name}.json'; json.dump(layout, open(jp, 'w'), indent=1)
        print(f'built {jp} {layout["cols"]}x{layout["rows"]} furniture={len(layout["furniture"])}')
        ok, *_ = validate(layout)
        sys.path.insert(0, HERE)
        import render_layout
        img, missing = render_layout.render(layout, zoom=2, chars=False)
        img.save(f'{name}.png'); print(f'saved {name}.png {img.size} (no characters)')
        img1, _ = render_layout.render(layout, zoom=2, chars=True)
        img1.save(f'{name}_chars.png'); print(f'saved {name}_chars.png (placeholder character on every seat)')
        img2, _ = render_layout.render(layout, zoom=2, chars=False, grid=True, labels=True)
        img2.save(f'{name}_grid.png'); print(f'saved {name}_grid.png (grid + col/row labels)')
        if missing: print('UNKNOWN TYPES:', sorted(set(missing)))
        sys.exit(0 if ok else 1)
    else:
        print(__doc__); sys.exit(1)

if __name__ == '__main__':
    main()
