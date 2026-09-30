#!/usr/bin/env python3
"""Semantic diff: live ~/.pixel-agents/layout.json vs a built spec JSON.
Compares grid, tiles, tileColors, furniture keyed by (type,col,row) incl. color, carpetTiles, pets. uid differences listed separately."""
import json, sys, os
if len(sys.argv) < 2: print(__doc__.strip() + '\nUsage: diff_live.py [live.json] <built.json>'); sys.exit(1)
live = json.load(open(os.path.expanduser(sys.argv[1] if len(sys.argv) > 2 else '~/.pixel-agents/layout.json')))
spec = json.load(open(sys.argv[-1]))
diffs = 0
for k in ('version', 'cols', 'rows', 'layoutRevision'):
    if live.get(k) != spec.get(k): print(f'META {k}: live={live.get(k)} spec={spec.get(k)}'); diffs += 1
cols = live['cols']
def rc(i): return (i % cols, i // cols)
for key in ('tiles', 'tileColors', 'carpetTiles'):
    a, b = live.get(key) or [], spec.get(key) or []
    if len(a) != len(b): print(f'{key}: length live={len(a)} spec={len(b)}'); diffs += 1; continue
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y: print(f'{key} {rc(i)}: live={x} spec={y}'); diffs += 1
def fkey(it): return (it['type'], it['col'], it['row'])
lf = {}; sf = {}
for it in live['furniture']: lf.setdefault(fkey(it), []).append(it)
for it in spec['furniture']: sf.setdefault(fkey(it), []).append(it)
for k in sorted(set(lf) | set(sf), key=lambda k: (k[2], k[1], k[0])):
    a, b = lf.get(k, []), sf.get(k, [])
    if len(a) != len(b): print(f'FURN {k}: live x{len(a)} spec x{len(b)}'); diffs += 1; continue
    for x, y in zip(a, b):
        if x.get('color') != y.get('color'): print(f'FURN COLOR {k}: live={x.get("color")} spec={y.get("color")}'); diffs += 1
        extra = (set(x) ^ set(y)) - {'color'}
        if extra: print(f'FURN KEYS {k}: {extra}')
if live.get('pets') != spec.get('pets'): print('PETS live=', live.get('pets'), 'spec=', spec.get('pets')); diffs += 1
uid_changes = sum(1 for k in lf if k in sf and [i['uid'] for i in lf[k]] != [i['uid'] for i in sf[k]])
print(f'--- semantic differences: {diffs}   (uid-only differences: {uid_changes} items — expected, uids are transplanted from the live file on apply)')
print('extra top-level keys:', sorted(set(live) ^ set(spec)))
