# Compact brief — the office must shrink ~5-6x

The owner says the current office (35x25 = 875 tiles) is far too big: at the panel's default zoom it does not fit on
screen and the agents look lost in it. Build the same company, **five to six times smaller in area**, and make it look
*better* — denser, richer, more interesting — not just cropped.

**Hard size rule:** cols 14-18, rows 9-12, and `cols * rows <= 190`. Good shapes: 16x11 (176), 15x12 (180), 17x11 (187),
16x10 (160), 15x10 (150). Smaller is better as long as it still reads as a real company.

Read first: `docs/BRIEF.md` (format, engine rules, full catalogue, coordinates),
`docs/contact_sheet.png` (every sprite), `docs/floor_swatches.png`
(floor patterns x colours), and the current big office `layouts/big/office.png` +
`layouts/big/spec.py` (the design language to compress: violet CEO suite, navy CTO, charcoal
lobby with a runner, grey-blue staff pods, cream cafe).

## What must survive the shrink

1. **CEO office** — the largest room, unmistakably the boss: executive desk with a PC, chair FACING THE ROOM, at least
   one guest seat or a small lounge (sofa or armchair + coffee table with a mug), a rug, wall decor (bookshelf /
   painting / clock), a plant. Violet walls + dark floor is the house style.
2. **CTO office** — smaller, refined, its own accent colour: desk + PC facing the room, a visitor chair, a rug, one
   bookshelf or whiteboard, a plant.
3. **Staff floor** — 3 to 6 plain workstations in a tidy row or pods (natural wood desks, grey-blue chairs), a
   whiteboard, a bin, a plant. Deliberately simpler than the executive rooms.
4. **Buffet / cafe** — checker or tile floor, a counter with mugs, at least one cafe table with seats, a plant.
5. **Circulation** — every room opens onto a shared corridor, hall or the staff floor without passing through another
   private room; one walkable region; nothing blocked.

Anything else (board room, reception, waiting sofas, gallery corridor) is optional — include it only if it still
looks uncramped at this size.

## Compact-scale mechanics (memorise these — they decide whether a room fits)

- A horizontal wall is drawn 2 tiles tall and **hides the floor row directly above it**. A band of 4 floor rows shows
  only 3. Plan bands as: wall row, 4 floor rows (last one hidden), wall row, 4 floor rows (last one hidden), wall row
  → 11 rows total.
- **One desk unit is exactly 3 rows tall.** Worker facing his screen: `DESK_FRONT` at (c,r), `PC_FRONT_OFF` at (c+1,r),
  chair `CUSHIONED_CHAIR_BACK` at (c+1,r+2). Executive facing the room: chair `CUSHIONED_CHAIR_FRONT` at (c+1,r),
  `DESK_FRONT` at (c,r+1), `PC_BACK` at (c+1,r+1). Both occupy rows r..r+2, so one unit fills a 3-visible-row room.
- A `DESK_FRONT` is 3 tiles wide. Two side by side = 6 cols. Budget columns before you draw the map.
- Wall items hang only on horizontal walls (bottom footprint row on the wall tile, floor below). At this scale use
  1-2 per room wall — a small painting or clock is often enough; a `DOUBLE_BOOKSHELF` (2x2) is the strongest luxury cue.
- Doors: leave a 1-2 tile gap in the wall. At this size a single 2-tile door per room is right.
- Rugs (`CARPETS`) stop one tile short of walls and doors and never sit on the hidden row.
- Pets are allowed and welcome: `PETS = [0, 1]` puts Claudio and Gitcat wandering the office (extension 1.4.1+).

## Ideas to make small look richer, not poorer

- Fewer, bigger gestures: one large painting beats three small ones; one bold rug beats two timid ones.
- Colour does the work at this scale: give each room a distinct wall colour and floor pattern so the plan reads as
  four rooms even when each is tiny.
- Use furniture recolours to sell materials: black leather `{h 265, s 10, b -24, c 20, colorize: True}`, antique gold
  `{h 40, s 38, b -20, c 12, colorize: True}`, cognac `{h 25, s 32, b -22, c 15, colorize: True}`, walnut
  `{h 0, s -10, b -22, c 12}`, grey-blue fabric `{h 222, s 16, b -14, c 0, colorize: True}`.
- A tiny courtyard, a planted nook, or a two-tile corridor with a runner adds depth without eating space.
- Keep at least a third of the floor empty — agents need to walk, and empty floor is what makes a room look expensive.

## Deliverable and loop

Work in the directory given in your prompt. Write `spec.py`, then:
`cd <workdir> && python3 office_kit.py all spec.py office`
It prints VALID/INVALID with ERROR lines and writes `office.png`, `office_chars.png`, `office_grid.png`.
Read the PNGs after EVERY build, critique honestly, fix, rebuild — at least 4 iterations.
Final must be VALID, one walkable region, **>= 8 seats, >= 6 facing PCs**, and within the size rule.
Keep your own messages short; do not paste file contents back.
