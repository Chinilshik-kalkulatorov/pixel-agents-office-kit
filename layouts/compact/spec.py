# COMPACT FINAL — 15x12 = 180 tiles (was 35x25 = 875, ~4.9x smaller by area).
# Base: the corridor concept. Grafts: dense bench desks + CEO lounge (c_bands), cafe counter (c_rich).
#
# rows: 0 wall (CEO/CTO art hangs here) | 1-4 exec band, row 4 hidden | 5 wall + two doors
#       6 corridor strip (marble + runner) | 7-10 open floor, row 10 hidden | 11 outer wall
# cols: CEO 1-7 | pier col 8 | CTO 9-13   /   staff 1-10 | cafe 11-13
# Seats never sit under wall art: CEO head col 3, sofa heads cols 6-7, CTO head col 11 are left bare.
MAP = """
###############
#EEEEEEE#ccccc#
#EEEEEEE#ccccc#
#EEEEEEE#ccccc#
#EEEEEEE#ccccc#
####LL####LL###
#LLLLLLLLLLLLL#
#ssssssssssbbb#
#ssssssssssbbb#
#ssssssssssbbb#
#ssssssssssbbb#
###############
"""

ESPRESSO = {'h': 24, 's': 22, 'b': -52, 'c': -80}   # CEO parquet
WALNUT_F = {'h': 27, 's': 18, 'b': -38, 'c': -84}   # CTO parquet
STONE_L  = {'h': 218, 's': 7,  'b': -6,  'c': -84}  # corridor slabs
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # staff floor
CHECKER  = {'h': 34, 's': 20, 'b': -10, 'c': -60}   # cafe

LEGEND = {
  'E': {'tile': 4, 'color': ESPRESSO},
  'c': {'tile': 4, 'color': WALNUT_F},
  'L': {'tile': 2, 'color': STONE_L},
  's': {'tile': 5, 'color': STONE},
  'b': {'tile': 9, 'color': CHECKER},
}

VIOLET_WALL = {'h': 265, 's': 35, 'b': -75, 'c': -45}
NAVY_WALL   = {'h': 228, 's': 32, 'b': -80, 'c': -45}
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
WALL_COLOR = CHARCOAL
WALL_COLORS = {'E': VIOLET_WALL, 'c': NAVY_WALL, 'L': CHARCOAL, 's': CHARCOAL, 'b': CHARCOAL}

WOOD_DARK  = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER    = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ---- CEO (cols 1-7, rows 1-3): desk + guest chair on the left, lounge on the right
  ('DOUBLE_BOOKSHELF', 1, -1), ('LARGE_PAINTING', 4, -1),
  ('CUSHIONED_CHAIR_FRONT', 3, 1, GOLD_SEAT),
  ('DESK_FRONT', 2, 2, WOOD_DARK), ('PC_BACK', 3, 2), ('COFFEE', 4, 3),
  ('CUSHIONED_CHAIR_SIDE', 1, 3, COGNAC),
  ('SOFA_FRONT', 6, 1, LEATHER), ('COFFEE_TABLE', 6, 2, WOOD_DARK), ('COFFEE', 7, 2),
  ('CUSHIONED_CHAIR_SIDE', 5, 2, GOLD_SEAT),
  ('PLANT', 1, 1),
  # ---- CTO (cols 9-13, rows 1-3): smaller, navy, green velvet visitor chair
  ('WHITEBOARD', 9, -1), ('CLOCK', 13, -1),
  ('CUSHIONED_CHAIR_FRONT', 11, 1, LEATHER),
  ('DESK_FRONT', 10, 2, WOOD_DARK), ('PC_BACK', 11, 2),
  ('CUSHIONED_CHAIR_SIDE:left', 13, 3, VELVET_GRN),
  ('PLANT_2', 9, 1), ('BIN', 13, 1),
  # ---- Corridor (row 6): runner, art on the row-5 wall, a tall plant at each end
  ('BOOKSHELF', 2, 5), ('LARGE_PAINTING', 7, 4), ('BOOKSHELF', 12, 5),
  ('LARGE_PLANT', 1, 4), ('LARGE_PLANT', 12, 4), ('CUSHIONED_BENCH', 9, 6, COGNAC),
  # ---- Staff floor (cols 1-10, rows 7-9): two bench desks, three seats each
  ('DESK_FRONT', 1, 7), ('PC_FRONT_OFF', 1, 7), ('PC_FRONT_OFF', 2, 7), ('PC_FRONT_OFF', 3, 7),
  ('CUSHIONED_CHAIR_BACK', 1, 9, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 2, 9, STAFF_SEAT),
  ('CUSHIONED_CHAIR_BACK', 3, 9, STAFF_SEAT),
  ('DESK_FRONT', 5, 7), ('PC_FRONT_OFF', 5, 7), ('PC_FRONT_OFF', 6, 7), ('PC_FRONT_OFF', 7, 7),
  ('CUSHIONED_CHAIR_BACK', 5, 9, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 6, 9, STAFF_SEAT),
  ('CUSHIONED_CHAIR_BACK', 7, 9, STAFF_SEAT),
  ('PLANT', 9, 7), ('BIN', 4, 9), ('BIN', 8, 9),
  # ---- Cafe (cols 11-13, rows 7-9): counter with mugs, three stools
  ('DESK_FRONT', 11, 7, WOOD_DARK), ('COFFEE', 12, 7), ('COFFEE', 13, 7),
  ('WOODEN_BENCH', 11, 9, CAFE_SEAT), ('WOODEN_BENCH', 12, 9, CAFE_SEAT), ('WOODEN_BENCH', 13, 9, CAFE_SEAT),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_CREAM  = {'h': 40, 's': 22, 'b': 0, 'c': -25}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_RUNNER = {'h': 265, 's': 24, 'b': -40, 'c': -22}

CARPETS = [
  {'variant': 0, 'col': 2, 'row': 1, 'w': 3, 'h': 3, 'color': RUG_CREAM, 'accent': RUG_VIOLET},  # CEO desk
  {'variant': 2, 'col': 10, 'row': 1, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_GOLD},    # CTO
  {'variant': 1, 'col': 3, 'row': 6, 'w': 9, 'h': 1, 'color': RUG_RUNNER, 'accent': RUG_GOLD},   # corridor runner
]

PETS = [0, 1]
