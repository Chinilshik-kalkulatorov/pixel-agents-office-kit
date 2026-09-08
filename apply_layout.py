#!/usr/bin/env python3
"""Apply a layout JSON to ~/.pixel-agents/layout.json (atomic write, like the extension does).
Usage: apply_layout.py <layout.json>
The running extension watches the file (fs.watch + poll) and reloads it live."""
import json, os, sys, shutil, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import office_kit

src = sys.argv[1]
dst = os.path.expanduser('~/.pixel-agents/layout.json')
layout = json.load(open(src))
ok, errs, warns, seats = office_kit.validate(layout, verbose=True)
if not ok:
    print('refusing to apply an INVALID layout'); sys.exit(1)
cur_rev = 0
if os.path.exists(dst):
    try: cur_rev = json.load(open(dst)).get('layoutRevision', 0) or 0
    except Exception: pass
    stamp = time.strftime('%Y-%m-%d_%H%M%S')
    bak = os.path.expanduser(f'~/.pixel-agents/layout_backup_{stamp}.json')
    shutil.copy2(dst, bak); print('backup ->', bak)
layout['layoutRevision'] = max(1, cur_rev)
layout['version'] = 1
tmp = dst + '.tmp'
with open(tmp, 'w') as f: json.dump(layout, f, indent=2)
os.replace(tmp, dst)
print(f'applied {src} -> {dst}  ({layout["cols"]}x{layout["rows"]}, {len(layout["furniture"])} items, {len(seats)} seats)')
