#!/usr/bin/env python3
"""Engine-faithful reachability (pixel-agents 1.3.0 webview bundle):
 blockedTiles = Qt(furniture)  -> every non-bg footprint tile of EVERY item (chairs + wall items included)
 isWalkable   = sr(): in bounds, tile != WALL(0), != VOID(255), not in blockedTiles
 pathfinding  = lr(): 4-neighbour BFS; target must be walkable; own seat unblocked via withOwnSeatUnblocked
"""
import json, sys
from collections import deque
CAT = {e['id']: e for e in json.load(open('/Users/Bilol/.vscode/extensions/pablodelucca.pixel-agents-1.3.0/dist/webview/assets/furniture-catalog.json'))}
def ent(t):
    base = t.split(':')[0]
    return CAT.get(base)
L = json.load(open(sys.argv[1]))
cols, rows, tiles = L['cols'], L['rows'], L['tiles']
hidden = set(int(x) for x in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['9', '18']))
blocked = set(); seats = []
unknown = []
for it in L['furniture']:
    e = ent(it['type'])
    if not e: unknown.append(it['type']); continue
    bg = e.get('backgroundTiles') or 0
    for dr in range(e['footprintH']):
        if dr < bg: continue
        for dc in range(e['footprintW']):
            k = (it['col'] + dc, it['row'] + dr)
            blocked.add(k)
            if e['category'] == 'chairs': seats.append((k, it['type']))
print('unknown types:', unknown)
def walk(c, r, bl):
    return 0 <= c < cols and 0 <= r < rows and tiles[r * cols + c] not in (0, 255) and (c, r) not in bl
def bfs(starts, bl, forbid=frozenset()):
    seen = {}; q = deque()
    for s in starts:
        if walk(*s, bl) and s not in forbid: seen[s] = None; q.append(s)
    while q:
        c, r = q.popleft()
        for dc, dr in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            n = (c + dc, r + dr)
            if n in seen or n in forbid or not walk(*n, bl): continue
            seen[n] = (c, r); q.append(n)
    return seen
def path(seen, t):
    p = []
    while t is not None: p.append(t); t = seen[t]
    return p[::-1]
entr = [(14, rows - 1), (15, rows - 1)]
print('entrance tiles:', [(e, tiles[e[1] * cols + e[0]]) for e in entr])
base = bfs(entr, blocked)
print(f'walkable from entrance (all chairs blocked): {len(base)} tiles')
allwalk = [(c, r) for r in range(rows) for c in range(cols) if walk(c, r, blocked)]
print('walkable total:', len(allwalk), ' unreachable walkable tiles:', sorted(set(allwalk) - set(base)))
# hidden-row lateral tiles: hidden-row tiles that are NOT directly above a door opening
def door_cols(wall_row):
    return {c for c in range(cols) if tiles[wall_row * cols + c] not in (0, 255)}
lateral = set()
for hr in hidden:
    dc_ = door_cols(hr + 1) if hr + 1 < rows else set()
    for c in range(cols):
        if c not in dc_: lateral.add((c, hr))
print('door columns under hidden rows:', {hr: sorted(door_cols(hr + 1)) for hr in hidden})
ok = 0
for (k, t) in sorted(seats, key=lambda s: (s[0][1], s[0][0])):
    bl = blocked - {k}
    seen = bfs(entr, bl)
    if k not in seen:
        print(f'UNREACHABLE seat {t}@{k}'); continue
    ok += 1
    p = path(seen, k)
    seen2 = bfs(entr, bl, forbid=frozenset(lateral))
    hid_on_path = [x for x in p if x[1] in hidden]
    tag = ''
    if k not in seen2: tag = '  <-- ONLY via lateral travel along hidden row'
    # free neighbours (approach tiles) of the seat
    nb = [(k[0] + dc, k[1] + dr) for dc, dr in ((0, -1), (0, 1), (-1, 0), (1, 0))]
    free = [n for n in nb if n in seen]
    print(f'seat {t:28s}@{k}  steps={len(p)-1:3d}  approach={free}  hidden-row tiles on shortest path={hid_on_path}{tag}')
print(f'{ok}/{len(seats)} seats reachable under engine rules')
