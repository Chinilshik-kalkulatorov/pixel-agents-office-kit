# c_tiny - 15x10 (150 tiles). Extreme shrink of the 35x25 office.
# Rows: 0 wall | 1-4 exec band (row 4 hidden behind wall row 5) | 5 wall | 6-9 public band (all visible)
# Cols: 0 wall | 1-8 CEO / STAFF | 9 wall (2-tile passage rows 6-7) | 10-13 CTO / CAFE | 14 wall
MAP = """
###############
#EEEEEEEE#TTTT#
#EEEEEEEE#TTTT#
#EEEEEEEE#TTTT#
#EEEEEEEE#TTTT#
######ss##bb###
#sssssssssbbbb#
#sssssssssbbbb#
#ssssssss#bbbb#
#ssssssss#bbbb#
"""

ESPRESSO = {'h': 22, 's': 22, 'b': -55, 'c': -80}   # CEO
NAVYSTN  = {'h': 224, 's': 22, 'b': -40, 'c': -80}  # CTO
STONE    = {'h': 208, 's': 7,  'b': -14, 'c': -86}  # staff
CHECKER  = {'h': 36, 's': 14, 'b': -10, 'c': -78}   # cafe

LEGEND = {
  'E': {'tile': 4, 'color': ESPRESSO},
  'T': {'tile': 4, 'color': NAVYSTN},
  's': {'tile': 5, 'color': STONE},
  'b': {'tile': 9, 'color': CHECKER},
}

VIOLET_WALL = {'h': 265, 's': 35, 'b': -75, 'c': -45}
NAVY_WALL   = {'h': 228, 's': 32, 'b': -80, 'c': -45}
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
CREAM_WALL  = {'h': 38, 's': 18, 'b': -22, 'c': -55}
WALL_COLOR = CHARCOAL
WALL_COLORS = {'E': VIOLET_WALL, 'T': NAVY_WALL, 's': CHARCOAL, 'b': CREAM_WALL}

WOOD_DARK  = {'h': 0, 's': -12, 'b': -34, 'c': 14}
VELVET_VIO = {'h': 268, 's': 42, 'b': -26, 'c': 8, 'colorize': True}
CAFE_WOOD  = {'h': 0, 's': -8, 'b': -18, 'c': 10}
LEATHER    = {'h': 265, 's': 12, 'b': -16, 'c': 22, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ---------- CEO suite: cols 1-8, visible rows 1-3 ----------
  ('DOUBLE_BOOKSHELF', 2, -1), ('LARGE_PAINTING', 4, -1), ('CLOCK', 7, -1),
  ('PLANT', 1, 0), ('PLANT_2', 8, 0),
  ('SOFA_SIDE', 1, 2, COGNAC),
  ('CUSHIONED_CHAIR_FRONT', 5, 1, GOLD_SEAT),
  ('DESK_FRONT', 4, 2, WOOD_DARK), ('PC_BACK', 5, 2), ('COFFEE', 6, 2),
  ('CUSHIONED_CHAIR_SIDE', 3, 3, COGNAC), ('CUSHIONED_CHAIR_SIDE:left', 7, 3, COGNAC),
  # ---------- CTO office: cols 10-13, visible rows 1-3 ----------
  ('HANGING_PLANT', 10, -1), ('CLOCK', 11, -1), ('WHITEBOARD', 12, -1),
  ('CUSHIONED_CHAIR_FRONT', 12, 1, LEATHER),
  ('DESK_FRONT', 11, 2, WOOD_DARK), ('PC_BACK', 12, 2),
  ('CUSHIONED_CHAIR_SIDE', 10, 3, VELVET_GRN),
  ('BIN', 13, 1),
  # ---------- Staff floor: cols 1-8, rows 6-9 ----------
  ('WHITEBOARD', 1, 4), ('CLOCK', 4, 4),
  ('PLANT', 8, 5),
  ('TABLE_FRONT', 2, 6), ('PC_SIDE', 2, 6), ('PC_SIDE:left', 4, 6),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, STAFF_SEAT), ('CUSHIONED_CHAIR_SIDE', 1, 8, STAFF_SEAT),
  ('CUSHIONED_CHAIR_SIDE:left', 5, 7, STAFF_SEAT), ('CUSHIONED_CHAIR_SIDE:left', 5, 8, STAFF_SEAT),
  ('DESK_FRONT', 6, 7), ('PC_FRONT_OFF', 7, 7),
  ('CUSHIONED_CHAIR_BACK', 7, 9, STAFF_SEAT),
  ('BIN', 8, 9),
  # ---------- Buffet: cols 10-13, rows 6-9 ----------
  ('SMALL_PAINTING', 12, 4), ('HANGING_PLANT', 13, 4),
  ('DESK_SIDE', 13, 6, CAFE_WOOD), ('COFFEE', 13, 6), ('COFFEE', 13, 8),
  ('WOODEN_BENCH', 12, 6), ('WOODEN_BENCH', 12, 7),
  ('SMALL_TABLE_FRONT', 10, 8, CAFE_WOOD), ('COFFEE', 10, 8),
  ('CUSHIONED_CHAIR_FRONT', 10, 7, CAFE_SEAT), ('CUSHIONED_CHAIR_FRONT', 11, 7, CAFE_SEAT),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -38, 'c': -20}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 216, 's': 16, 'b': -6,  'c': -18}
RUG_SILVER = {'h': 220, 's': 10, 'b': 15, 'c': 0}
RUG_RUNNER = {'h': 265, 's': 26, 'b': -40, 'c': -20}

CARPETS = [
  {'variant': 0, 'col': 3, 'row': 2, 'w': 5, 'h': 2, 'color': RUG_VIOLET, 'accent': RUG_GOLD},
  {'variant': 2, 'col': 11, 'row': 2, 'w': 3, 'h': 2, 'color': RUG_NAVY, 'accent': RUG_SILVER},
  {'variant': 2, 'col': 1, 'row': 6, 'w': 9, 'h': 1, 'color': RUG_RUNNER, 'accent': RUG_GOLD},
]

PETS = [0, 1]
