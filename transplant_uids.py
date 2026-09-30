#!/usr/bin/env python3
"""Carry furniture uids over from the live layout by key (type, col, row) so agents keep their seats.
Usage: transplant_uids.py <built.json> <out.json> [live.json]"""
import json, sys, os
built = json.load(open(sys.argv[1])); out = sys.argv[2]
live = json.load(open(os.path.expanduser(sys.argv[3] if len(sys.argv) > 3 else '~/.pixel-agents/layout.json')))
CAT = {e['id']: e for e in json.load(open(os.path.expanduser('~/.pixel-agents/office-kit/furniture-catalog.json')))}
def is_chair(t): return (CAT.get(t.split(':')[0]) or {}).get('category') == 'chairs'
pool = {}
for it in live['furniture']: pool.setdefault((it['type'], it['col'], it['row']), []).append(it['uid'])
kept, fresh = [], []
for it in built['furniture']:
    k = (it['type'], it['col'], it['row'])
    if pool.get(k):
        it['uid'] = pool[k].pop(0); kept.append(k)
    else:
        fresh.append(k)
uids = [it['uid'] for it in built['furniture']]
assert len(uids) == len(set(uids)), 'duplicate uids after transplant'
live_chairs = {it['uid']: (it['type'], it['col'], it['row']) for it in live['furniture'] if is_chair(it['type'])}
new_uids = set(uids)
print(f'kept live uid: {len(kept)} items, new uid: {len(fresh)} items, total {len(uids)} (all unique)')
print('chairs keeping their live uid:', sorted([k for k in kept if is_chair(k[0])], key=lambda k: (k[2], k[1])))
print('live chairs whose uid disappears (their agents get re-seated):', sorted([v for u, v in live_chairs.items() if u not in new_uids], key=lambda k: (k[2], k[1])))
json.dump(built, open(out, 'w'), indent=1)
print('wrote', out)
