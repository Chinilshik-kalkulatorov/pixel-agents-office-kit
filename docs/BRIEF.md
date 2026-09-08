# Pixel Agents office — designer brief

You are designing a pixel-art office layout for the VS Code extension **Pixel Agents** (Claude Code agents walk around a
tile office and sit at desks). The current office is a bland 2-room box. The owner wants a **premium, architecturally
believable company office**: a large luxurious **CEO office**, a smaller but tasteful **CTO office**, a simpler shared
floor for **designers / writers / testers / developers** ("like everybody else"), and a **buffet** (kitchen/café).
Optional extras that make it feel real: reception/lounge, meeting room, corridor. Everything must be connected
(one walkable region) and every seat reachable.

Tooling lives in: `.`
(durable copy: ~/.pixel-agents/office-kit). Use `python3 office_kit.py`. Reference sprites: `contact_sheet.png` (LOOK AT IT FIRST with Read).
The current (bland) office render for scale: `current_render.png` (21x22 grid, 10 top rows unused void).

## Workflow (mandatory loop)

1. `Read contact_sheet.png` to see every sprite.
2. Write `<workdir>/spec.py` (format below).
3. Run `cd <workdir> && python3 office_kit.py all spec.py office` → writes `office.json`, `office.png` (clean),
   `office_chars.png` (a placeholder character on every seat), `office_grid.png` (grid + col/row numbers).
   It prints `VALID` or `INVALID` with ERROR/WARN lines. Fix every ERROR. Warnings about sofas/benches w/o desks are fine.
4. `Read` the PNGs. Critique like an interior architect: hierarchy (CEO > CTO > staff), empty dead zones, clutter,
   alignment (desks in clean rows, symmetry where it helps), corridors, door placement, colour harmony, wall decor rhythm.
5. Fix and re-run. Do **at least 3 full iterations** (more if it still looks off). Stop only when VALID and it looks premium.

## Spec format (`spec.py`, plain Python)

```python
MAP = """
################################
#aaaaaaaaa#bbbbbbb#ccccccccccc#
#aaaaaaaaa#bbbbbbb#ccccccccccc#
#aaaaaaaaaabbbbbbbbccccccccccc#     <- a gap in a wall = a doorway (1-2 tiles)
################################
"""
# '#' wall, '.' void (outside), any other char = a floor "room key" defined in LEGEND.
LEGEND = {
  'a': {'tile': 7, 'color': {'h': 25, 's': 48, 'b': -43, 'c': -88}},   # tile 1..9 = floor pattern, color = colorize HSBC
}
WALL_COLOR = {'h': 214, 's': 30, 'b': -100, 'c': -55}     # default wall colour (colorize). None = raw beige sprite
WALL_COLORS = {'a': {'h': 265, 's': 35, 'b': -70, 'c': -40}}   # optional: walls touching room 'a' get this colour
FURNITURE = [
  ('DESK_FRONT', 2, 3),                                  # (type, col, row)
  ('CUSHIONED_CHAIR_BACK', 3, 5, {'h': 240, 's': 0, 'b': -10, 'c': 0}),   # optional 4th = colour override
]
CARPETS = [ {'variant': 0, 'col': 2, 'row': 2, 'w': 5, 'h': 4,          # optional rugs (rectangles, later = on top)
             'color': {'h': 265, 's': 45, 'b': -35, 'c': 0}, 'accent': {'h': 40, 's': 55, 'b': 15, 'c': 0}} ]
```

## Coordinates & mechanics (the engine's real rules — the validator enforces them)

- `col` = x (left→right), `row` = y (top→bottom), 0-based. `(col,row)` of an item = **top-left of its footprint**.
- Tile = 16 px. Grid max 64x64. Target overall size **28–36 cols × 18–24 rows** (bigger = agents look tiny).
- **backgroundTiles (bg)**: the top `bg` rows of a footprint are visual only — they do not block walking and may overlap
  walls, void or other items. The *occupied* rows are `row+bg … row+H-1`. Tall items (plants, chairs, desks) have bg=1.
- **Wall items** (`wall=1` below): the **bottom footprint row must be on WALL tiles**; upper rows hang above the wall
  (may be above the map, row can be -1). Two wall items may not overlap in any row. Hang them on the top wall of a room
  (e.g. top wall at row 4 → 2-tall item at row 3, BOOKSHELF (2x1) at row 4). Wall items on *interior* horizontal walls look
  great too (the wall between two rooms). Never on vertical wall runs (they'd float) — only where a wall tile has floor below it.
- **Floor items**: occupied rows must be on floor tiles (not wall/void) and must not overlap other items' occupied tiles.
  Exception: `surf=1` items (PC, COFFEE, HANGING_PLANT) may sit on desk/table tiles.
- **Seats**: every `chairs` item is a seat (each occupied tile of it). Facing: chair orientation `FRONT`→faces DOWN,
  `BACK`→faces UP, `SIDE`→faces RIGHT, `SIDE:left`→faces LEFT. Benches/sofas without orientation face the adjacent desk.
  Agents *prefer* seats that "face a PC" (electronics within 3 tiles straight ahead, incl. flanking). Aim for ≥ 12 seats
  total, ≥ 10 of them facing PCs. Put a seat at every workstation. Sofas are seats too (lounge/CEO guests).
- **Standard workstation (facing up)**: `DESK_FRONT` at (c,r) [3x2, bg1 → occupies row r+1]; `PC_FRONT_OFF` at (c+1, r)
  [sits on the desk]; chair at (c+1, r+2) using `CUSHIONED_CHAIR_BACK` (1x1) or `WOODEN_CHAIR_BACK` — **WOODEN_CHAIR_* is
  1x2 with bg1, so place it at row r+1 (its seat is the bottom tile r+2)**. The character sits at (c+1, r+2) facing UP.
- **Side workstations** (two agents across a long table): `TABLE_FRONT` at (c,r) [3x4, bg1]; `PC_SIDE` at (c, r) and
  `PC_SIDE:left` at (c+2, r) on the table; `WOODEN_CHAIR_SIDE` at (c-1, r) (seat (c-1, r+1) faces RIGHT) and
  `WOODEN_CHAIR_SIDE:left` at (c+3, r) (faces LEFT). Any `*_SIDE` type has a mirrored `*_SIDE:left` twin.
- **PC on/off**: `PC_FRONT_OFF` is the normal placed state (engine switches it ON when an agent sits). Use `PC_FRONT_OFF`,
  `PC_SIDE`, `PC_SIDE:left`, `PC_BACK`.
- **Walkability**: floor minus occupied tiles; seat tiles are reachable targets. Keep ≥1-tile corridors, doorways 1–2
  tiles wide (a floor tile in the wall line). All rooms must connect. Void outside; the building may be L/T-shaped.
- Walls auto-tile (1 tile thick). Interior walls separate rooms. A wall tile is coloured by the first adjacent room in
  `WALL_COLORS` (checks S, E, W, N) — so a room's top wall and side walls take that room's wall colour.

## Catalogue (type — footprint WxH, bg rows, flags)

| type | px | fp | bg | notes |
|---|---|---|---|---|
| DESK_FRONT | 48x32 | 3x2 | 1 | desk, front view (workstation) |
| DESK_SIDE | 16x64 | 1x4 | 1 | desk, side view (long, vertical) — also a counter |
| TABLE_FRONT | 48x64 | 3x4 | 1 | big table (meeting / executive / 2-side workstations) |
| SMALL_TABLE_FRONT | 32x32 | 2x2 | 1 | café table (front) |
| SMALL_TABLE_SIDE | 16x48 | 1x3 | 1 | café table (side) |
| COFFEE_TABLE | 32x32 | 2x2 | 0 | low lounge table (desk-flag: sofas around it become seats facing it) |
| CUSHIONED_CHAIR_FRONT / _BACK / _SIDE / _SIDE:left | 16x16 | 1x1 | 0 | green armchair (recolour for leather look) — seat |
| WOODEN_CHAIR_FRONT / _BACK / _SIDE / _SIDE:left | 16x32 | 1x2 | 1 | wooden chair — seat at bottom tile |
| CUSHIONED_BENCH | 16x16 | 1x1 | 0 | stool/bench — seat |
| WOODEN_BENCH | 16x16 | 1x1 | 0 | wooden stool — seat |
| SOFA_FRONT / SOFA_BACK | 32x16 | 2x1 | 0 | red sofa, 2 seats (recolour!) |
| SOFA_SIDE / SOFA_SIDE:left | 16x32 | 1x2 | 0 | sofa side view, 2 seats |
| PC_FRONT_OFF / PC_SIDE / PC_SIDE:left / PC_BACK | 16x32 | 1x2 | 1 | surf=1 electronics; place on desk tile |
| COFFEE | 16x16 | 1x1 | 0 | surf=1 mug — on café tables / counters |
| BIN | 16x16 | 1x1 | 0 | small bin |
| POT | 16x16 | 1x1 | 0 | small pot |
| PLANT / PLANT_2 | 16x32 | 1x2 | 1 | floor plants (bg1 → occupy 1 tile) |
| CACTUS | 16x32 | 1x2 | 1 | cactus |
| LARGE_PLANT | 32x48 | 2x3 | 2 | big fiddle-leaf (occupies bottom row only, 2 tiles) |
| BOOKSHELF | 32x16 | 2x1 | 0 | wall=1, short shelf |
| DOUBLE_BOOKSHELF | 32x32 | 2x2 | 0 | wall=1, tall shelf |
| WHITEBOARD | 32x32 | 2x2 | 0 | wall=1 |
| LARGE_PAINTING | 32x32 | 2x2 | 0 | wall=1 landscape painting |
| SMALL_PAINTING / SMALL_PAINTING_2 | 16x32 | 1x2 | 0 | wall=1 portraits |
| CLOCK | 16x32 | 1x2 | 0 | wall=1 |
| HANGING_PLANT | 16x32 | 1x2 | 0 | wall=1 & surf=1 |

## Floors (tile index → pattern; all are grayscale and *colorized* by `color`)

1, 2, 3 = plain (subtle noise variants) · 4 = large tiles with grout · 5 = fine grid tiles · 6, 7 = wood planks ·
8 = small checkerboard · 9 = large checkerboard.  `color = {h 0-360, s 0-100, b -100..100, c -100..100}`:
`b` darkens/lightens, `c` negative flattens the pattern (subtle), `s` low = muted. Current office reference:
wood `{h25,s48,b-43,c-88}`, blue `{h209,s39,b-25,c-80}`, wall `{h214,s30,b-100,c-55}` (almost black navy).
Suggested premium palette: walnut planks `{h22,s40,b-45,c-80}`, cool stone tiles `{h210,s10,b-15,c-85}`,
warm marble checker `{h35,s15,b0,c-70}`, deep violet wall `{h265,s35,b-75,c-45}`, charcoal wall `{h220,s12,b-85,c-40}`,
cream wall `{h40,s25,b-25,c-60}`. Pick one accent hue for the executive rooms and keep it out of the staff areas.

## Furniture colour overrides

`{'h': shift -180..180, 's': -100..100, 'b': -100..100, 'c': -100..100}` shifts the sprite's own colours (hue rotate).
Add `'colorize': True` to recolour from luminance (single hue): e.g. black leather sofa
`{'h': 265, 's': 12, 'b': -35, 'c': 10, 'colorize': True}`, violet armchair `{'h': 265, 's': 55, 'b': -15, 'c': 0, 'colorize': True}`,
dark walnut desk `{'h': 0, 's': -10, 'b': -22, 'c': 12}`. Use this to distinguish CEO (dark leather, walnut) from staff (natural).

## Quality bar (what the judges score)

1. Premium, believable architecture: distinct rooms with purpose; CEO office clearly the grandest (largest room, executive
   table/desk + PC, guest sofa group with coffee table, double bookshelves, large painting(s), plants, rug, clock);
   CTO office smaller but refined (desk+PC, whiteboard or bookshelf, plant, painting, rug).
2. Staff floor: ordered rows/pods of workstations (≥ 6–8 seats), whiteboard, bins, plants, clock — tidy, not luxurious.
3. Buffet: distinct floor (checker/tiles), counter (DESK_SIDE / SMALL_TABLE_SIDE with COFFEE mugs), café tables with
   seats, plants, a painting. Feels like a real kitchen corner.
4. Circulation: doorways placed logically, corridor/reception, nothing blocked, no dead pockets, no seat unreachable.
5. Composition: alignment, symmetry where appropriate, wall decor rhythm, colour harmony, no big empty floor holes,
   no clutter. Fits ~30x20; readable at a glance.
6. VALID from the validator, ≥ 12 seats, ≥ 10 facing PCs.
