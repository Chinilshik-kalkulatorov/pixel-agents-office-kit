#!/usr/bin/env python3
"""Refresh assets/ and furniture-catalog.json from an installed Pixel Agents extension.

Usage: sync_assets.py [path/to/extension]
Without an argument it searches the usual VS Code / Cursor / VSCodium extension folders and picks the newest version.
"""
import glob, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH = [
    '~/.vscode/extensions', '~/.vscode-insiders/extensions', '~/.vscode-server/extensions',
    '~/.cursor/extensions', '~/.vscodium/extensions', '~/.windsurf/extensions',
    '~/AppData/Roaming/Code/User/extensions',
]

def find_extension():
    found = []
    for base in SEARCH:
        found += glob.glob(os.path.join(os.path.expanduser(base), '*pixel-agents*'))
    if not found:
        return None
    def ver(p):
        tail = os.path.basename(p).rsplit('-', 1)[-1]
        try:
            return tuple(int(x) for x in tail.split('.'))
        except ValueError:
            return (0,)
    return sorted(found, key=ver)[-1]

def main():
    ext = sys.argv[1] if len(sys.argv) > 1 else find_extension()
    if not ext or not os.path.isdir(ext):
        sys.exit('Pixel Agents extension not found. Pass its folder as an argument.')
    src = os.path.join(ext, 'dist', 'webview', 'assets')
    if not os.path.isdir(src):
        sys.exit(f'No dist/webview/assets in {ext}')
    for sub in ('floors', 'walls', 'carpets', 'furniture', 'characters', 'pets'):
        s = os.path.join(src, sub)
        if not os.path.isdir(s):
            continue
        d = os.path.join(HERE, 'assets', sub)
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(s, d)
        print('synced', sub)
    cat = os.path.join(src, 'furniture-catalog.json')
    if os.path.exists(cat):
        shutil.copy2(cat, os.path.join(HERE, 'furniture-catalog.json'))
        print('synced furniture-catalog.json')
    print('done from', ext)

if __name__ == '__main__':
    main()
