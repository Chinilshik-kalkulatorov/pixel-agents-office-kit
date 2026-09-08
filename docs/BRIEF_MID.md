# Middle brief — the office the owner actually wants

The 35x25 office (875 tiles) was too big for the panel; the 15x12 one (180 tiles) was far too poor. The owner's decision:
**half the big one by area, three times the compact one — about 24 x 18 = 432 tiles.**

**Hard size rule:** `cols * rows` between 400 and 460, cols 22-26, rows 16-19. Best shapes: 24x18 (432), 25x17 (425),
23x19 (437), 24x17 (408).

Read first: `~/.pixel-agents/office-kit/BRIEF.md` (format, engine rules, full catalogue),
`~/.pixel-agents/office-kit/contact_sheet.png` (every sprite), `~/.pixel-agents/office-kit/floor_swatches.png`,
and both existing offices — `final_office.png` + `final_spec.py` (the big one, the design language to keep) and
`compact_office.png` + `compact_spec.py` (the too-small one, what to avoid).

## The programme — all six must be present

1. **CEO office** — the largest room, violet walls, dark parquet. Executive table with a PC and the chair FACING THE
   ROOM, two guest chairs across the desk, a lounge group (leather sofa + coffee table with a mug + one or two gold
   armchairs), a rug under the desk zone, bookshelves / a large painting / a clock on the wall, plants in the corners.
2. **CTO office** — clearly smaller, its own accent (navy), desk + PC facing the room, a velvet visitor chair, a rug,
   whiteboard or bookshelf, a plant.
3. **Meeting room** — a long table with two side PCs and four to six leather chairs, a whiteboard, a clock, a rug.
4. **Lobby / corridor** — runs across the plan, every room doors onto it, a runner rug, waiting sofas against the wall,
   paintings in a small-large-small rhythm, a plant at each end, and a **reception desk with the receptionist facing
   the lobby** (PC_BACK + CUSHIONED_CHAIR_FRONT).
5. **Open space** — 6 to 8 plain workstations (natural wood desks, grey-blue chairs) in a tidy row or two pods, a
   whiteboard, one bin, a plant. Deliberately simpler than the executive rooms.
6. **Cafe** — its own room with a checker or warm-tile floor, a counter with mugs and stools, at least two cafe tables
   with matching chairs, a plant, a painting.

Pets are welcome: `PETS = [0, 1]`.

## Geometry that works at this size (do the arithmetic before you draw)

A horizontal wall is drawn 2 tiles tall and **hides the floor row directly above it**, so a band of N floor rows shows
N-1. A working section for 18 rows:

```
row 0       outer wall            <- CEO / CTO / meeting-room wall art hangs here
rows 1-6    executive band        <- row 6 hidden; 5 visible rows
row 7       wall + one door per executive room, and the lobby's art hangs here
rows 8-10   lobby                 <- row 10 hidden; 2 visible rows
row 11      wall + doors to open space and cafe, carries the open space's art
rows 12-16  lower band            <- row 16 hidden; 4 visible rows
row 17      outer wall
```

Columns for 24: executive band = CTO 1-6 | wall 7 | CEO 8-15 | wall 16 | meeting 17-22; lower band = open space 1-13 |
wall 14 | cafe 15-22. Outer walls at 0 and 23.

- One workstation is 3 rows tall: `DESK_FRONT` at (c,r) + `PC_FRONT_OFF` at (c,r) + `CUSHIONED_CHAIR_BACK` at (c,r+2).
  A `DESK_FRONT` is 3 wide and can carry up to 3 PCs and 3 chairs (a bench). In a 4-visible-row band put the desks on
  the first row and keep the last row as a walking aisle.
- Executive facing the room: `CUSHIONED_CHAIR_FRONT` at (c,r), `DESK_FRONT`/`TABLE_FRONT` at (c-1,r+1), `PC_BACK` at (c,r+1).
- **Never seat anyone directly under a wall item** — the seated character's head covers it. Keep those columns bare.
- **Wall items 2 tiles tall** (CLOCK, SMALL_PAINTING, LARGE_PAINTING, WHITEBOARD, DOUBLE_BOOKSHELF, HANGING_PLANT) eat
  the hidden floor row of the room above, which can cut that room in two. `BOOKSHELF` (2x1) sits on the wall row only
  and is safe on interior walls. After every build, check the validator's region count is 1.
- A mug on a `DESK_FRONT` goes on the desk's occupied row (r+1), otherwise it floats above the counter.
- 1x2 plants (`PLANT`, `PLANT_2`, `CACTUS`) must not be placed on the last visible row — their base ends up behind the
  wall. Use `POT` (1x1) there.
- Rugs stop one tile short of walls and doors, and never cover a doorway.
- Recolours that read well: black leather `{h 265, s 10, b -24, c 20, colorize: True}`, cognac
  `{h 25, s 32, b -22, c 15, colorize: True}`, antique gold `{h 40, s 38, b -20, c 12, colorize: True}`, green velvet
  `{h 160, s 26, b -32, c 8, colorize: True}`, grey-blue fabric `{h 222, s 16, b -14, c 0, colorize: True}`,
  walnut furniture `{h 0, s -10, b -22, c 12}`. A leather sofa on a violet wall disappears — use cognac there.
- Keep about a third of every room's floor empty. Empty floor is what makes a room look expensive.

## Loop

Work in the directory given in your prompt. Write `spec.py`, then
`cd <workdir> && python3 ~/.pixel-agents/office-kit/office_kit.py all spec.py office`.
Read `office.png`, `office_chars.png` and `office_grid.png` after EVERY build, critique honestly, fix, rebuild —
at least 4 iterations. Final must be VALID, **one walkable region**, >= 20 seats, >= 12 facing PCs, and inside the size
rule. Keep your own messages short; never paste file contents back.
