# Synthesis brief — final Pixel Agents office

Six concept designs were built and judged by a 3-judge panel. Winner: **exec_classic** (2 of 3 first places), runner-up
**brand_violet**. The final must be built by grafting the panel's consensus improvements onto the winner's skeleton.
Read the base design first: `layouts/exec_classic/spec.py` (+ `office.png`, `office_grid.png`). Then read the
donor specs/renders you graft from: `layouts/brand_violet/`, `layouts/boutique/`, `layouts/compact/`,
`layouts/tech_loft/` (each has `spec.py`, `office.png`, `office_grid.png`). `.` =
`.`.
Rules/format/catalogue: `BRIEF.md`. Floor colour swatches: `floor_swatches.png`.

## Consensus graft list (all three judges) — implement ALL of these

1. **Lobby spine instead of the reception box.** Turn the middle of the plan into a full-width (or near full-width)
   lobby/corridor that every room doors onto: CEO, CTO, board room from above; staff floor and buffet from below.
   Nobody should have to walk through the buffet or the staff floor to reach another room. Keep the street entrance in
   the outer wall (bottom) with a reception desk + receptionist facing it (PC_BACK), but keep the entrance axis clear:
   waiting sofas pushed back against the walls between doors, a runner rug (CARPETS) along the axis, paintings in a
   small-large-small rhythm on the lobby wall, a plant at each end. (Donors: boutique corridor, brand_violet lobby.)
2. **CEO suite = one room, one message.** Keep it the largest room, on the central axis, violet walls, executive
   TABLE_FRONT + PC_BACK so the CEO faces the room, two guest chairs facing the CEO. Use at most TWO rugs (one under the
   desk zone, one under the lounge) so the wood floor shows around them — never three. Lounge: black-leather sofas +
   gold armchair(s) + walnut/brass coffee table with a mug (brand_violet recipe). Wall: bookshelf / painting / clock /
   painting / bookshelf symmetric rhythm; fiddle-leaf plants in the corners. Fix the "walnut = red brick" problem:
   lower saturation / flatten (see swatches; e.g. `{h 24, s 26, b -40, c -84}` or tile 4/5 large tiles in a warm tone).
3. **CTO office = smaller but refined, its own identity.** Desk centred on its own rug, CTO facing the room (PC_BACK),
   one velvet visitor chair, a reading nook (coffee table + armchair), whiteboard + one painting + a double bookshelf,
   plant. Give it a distinct but coherent wall colour (deep navy or deep green — one accent, not a rainbow).
4. **Board room** (from exec_classic) stays next to the CEO, doors onto the lobby: long TABLE_FRONT with PC_SIDE and
   PC_SIDE:left, leather chairs, whiteboard, clock, painting, rug.
5. **Staff floor = bench pods.** Eight workstations as four 2-desk bench pods (two DESK_FRONT touching), plant column
   between pods, bins at pod ends, a 3-wide aisle that lands exactly on the door from the lobby. Top-wall rhythm:
   portrait – whiteboard – hanging plant – clock – hanging plant – whiteboard – portrait (tech_loft). Staff chairs
   plain (grey-blue fabric or wooden), natural wood desks — clearly simpler than the executive rooms. Optionally one
   4-seat side table (TABLE_FRONT + PC_SIDE/PC_SIDE:left) as a tester/dev pod. Target ≥ 10 seats facing PCs on this floor.
6. **Buffet = a real café** (tech_loft recipe): cream/warm walls, warm marble checker floor, a walnut bar counter with
   mugs and a barista lane behind it, BOOKSHELF "bar shelves" on the wall above the bar, a tidy 2x2 grid of matching café
   tables with matching chairs (not stools jammed above and below each table), one sofa + coffee-table lounge corner,
   painting + hanging plants flanking the buffet door, plants in corners. No window bar clutter.
7. **Palette discipline**: at most 4 wall colours in the whole plan (CEO violet, exec navy/green, staff charcoal, buffet
   cream) and 4 floor treatments. Brand violet (h≈265) + gold (h≈40) accents only in the executive rooms and the lobby
   runner. Rugs must not be flat saturated slabs: keep `s` ≤ 45 and `b` ≤ -30 on violet rugs.

## Engine visual gotchas (learned from the renders — respect them)

- Horizontal walls render 2 tiles tall: the wall sprite covers the floor row directly ABOVE the wall tile. So the last
  floor row of every room (the row just above its bottom wall) is hidden (still walkable). Keep furniture off that row,
  and count rooms as (visible rows = floor rows - 1). Do not put rugs on that row either.
- Doorways cut in vertical walls show only the upper tile (the wall segment below paints over the second) — still make
  them 2 tiles tall for circulation; visually they read as a 1-tile notch. Doorways in horizontal walls read cleanly.
- Wall items go only on horizontal wall runs that have floor below them (top walls of rooms, and interior horizontal
  walls). Never on vertical walls.
- PC_BACK on the far side of a table + CUSHIONED_CHAIR_FRONT above it = "executive faces the room". PC_FRONT_OFF +
  *_CHAIR_BACK below = "worker faces the wall". Use the former for CEO/CTO/receptionist, the latter for staff.
- WOODEN_CHAIR_* is 1x2 (bg 1): place at seatRow-1. CUSHIONED_* and benches are 1x1: place at seatRow.
- A rug under a doorway looks wrong; stop rugs one tile short of doors and walls.
- Overall size: keep within 36 x 24. Fewer, larger, well-ordered rooms beat many tiny ones.

## Deliverable

Work in `<workdir>` (given in your prompt). Write `spec.py`, run
`cd <workdir> && python3 office_kit.py all spec.py office`, Read `office.png`, `office_chars.png`, `office_grid.png`,
critique, fix, rebuild — at least 4 iterations, and keep going until it is VALID and every graft item above is visibly
implemented. Final: VALID, ≥ 14 seats, ≥ 10 facing PCs, one walkable region, every room doored onto the lobby.
Return the structured summary requested in your prompt.
