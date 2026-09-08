# MIDDLE OFFICE — 24 x 18 = 432 tiles (big 35x25=875 halved, compact 15x12=180 tripled).
# rows: 0 wall | 1-6 exec band (row 6 hidden) | 7 wall+doors | 8-11 lobby (row 11 hidden)
#       | 12 wall+doors | 13-16 lower band (row 16 hidden) | 17 wall
# cols: CTO 1-6 | wall 7 | CEO 8-15 | wall 16 | meeting 17-22   /   open space 1-13 | wall 14 | cafe 15-22
# doors: row 7 -> CTO 3-4, CEO 11-12, meeting 19-20;  row 12 -> open space 6-7, cafe 18-19
MAP = """
########################
#cccccc#EEEEEEEE#mmmmmm#
#cccccc#EEEEEEEE#mmmmmm#
#cccccc#EEEEEEEE#mmmmmm#
#cccccc#EEEEEEEE#mmmmmm#
#cccccc#EEEEEEEE#mmmmmm#
#cccccc#EEEEEEEE#mmmmmm#
###cc######EE######mm###
#LLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLL#
######ss##########bb####
#sssssssssssss#bbbbbbbb#
#sssssssssssss#bbbbbbbb#
#sssssssssssss#bbbbbbbb#
#sssssssssssss#bbbbbbbb#
########################
"""

ESPRESSO = {'h': 24, 's': 22, 'b': -52, 'c': -80}   # CEO parquet
WALNUT_F = {'h': 27, 's': 18, 'b': -38, 'c': -84}   # CTO / meeting parquet
STONE_L  = {'h': 38, 's': 8,  'b': 0,   'c': -82}   # lobby slabs
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # open space
CHECKER  = {'h': 34, 's': 20, 'b': -10, 'c': -60}   # cafe

LEGEND = {
  'E': {'tile': 4, 'color': ESPRESSO},
  'c': {'tile': 4, 'color': WALNUT_F},
  'm': {'tile': 4, 'color': WALNUT_F},
  'L': {'tile': 4, 'color': STONE_L},
  's': {'tile': 5, 'color': STONE},
  'b': {'tile': 9, 'color': CHECKER},
}

VIOLET_WALL = {'h': 265, 's': 35, 'b': -75, 'c': -45}
NAVY_WALL   = {'h': 228, 's': 32, 'b': -80, 'c': -45}
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
CREAM_WALL  = {'h': 38, 's': 18, 'b': -22, 'c': -55}
WALL_COLOR = CHARCOAL
WALL_COLORS = {'E': VIOLET_WALL, 'c': NAVY_WALL, 'm': NAVY_WALL, 'L': CHARCOAL, 's': CHARCOAL, 'b': CREAM_WALL}

WOOD_DARK  = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER    = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ================= CEO (cols 8-15, rows 1-5) — largest room, boss faces the room
  ('DOUBLE_BOOKSHELF', 8, -1), ('LARGE_PAINTING', 10, -1), ('DOUBLE_BOOKSHELF', 14, -1),
  ('CUSHIONED_CHAIR_FRONT', 12, 1, GOLD_SEAT),
  ('DESK_FRONT', 11, 2, WOOD_DARK), ('PC_BACK', 12, 2), ('COFFEE', 13, 3),
  ('CUSHIONED_CHAIR_BACK', 11, 4, COGNAC), ('CUSHIONED_CHAIR_BACK', 13, 4, COGNAC),
  # lounge on the left: cognac sofa facing the coffee table, gold armchair on the side
  ('COFFEE_TABLE', 9, 3, WOOD_DARK), ('COFFEE', 10, 4),
  ('SOFA_BACK', 9, 5, COGNAC),
  ('LARGE_PLANT', 14, 3),
  # ================= CTO (cols 1-6, rows 1-5) — smaller, navy, its own accent
  ('WHITEBOARD', 1, -1), ('LARGE_PAINTING', 5, -1),
  ('CUSHIONED_CHAIR_FRONT', 3, 1, LEATHER),
  ('DESK_FRONT', 2, 2, WOOD_DARK), ('PC_BACK', 3, 2),
  ('CUSHIONED_CHAIR_BACK', 3, 4, VELVET_GRN),
  ('COFFEE_TABLE', 1, 4, WOOD_DARK), ('COFFEE', 1, 5), ('CUSHIONED_CHAIR_SIDE:left', 3, 5, VELVET_GRN),
  ('PLANT_2', 6, 1), ('BIN', 5, 5),
  # ================= Meeting room (cols 17-22, rows 1-5)
  ('WHITEBOARD', 17, -1), ('CLOCK', 20, -1), ('LARGE_PAINTING', 21, -1),
  ('TABLE_FRONT', 18, 2, WOOD_DARK), ('PC_SIDE', 18, 2), ('PC_SIDE:left', 20, 2),
  ('CUSHIONED_CHAIR_FRONT', 19, 1, LEATHER),
  ('CUSHIONED_CHAIR_SIDE', 17, 3, LEATHER), ('CUSHIONED_CHAIR_SIDE', 17, 5, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 21, 3, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 21, 5, LEATHER),
  ('PLANT', 22, 4),
  # ================= Lobby (cols 1-22, rows 8-10) — reception on the axis, waiting sofas, art
  ('SMALL_PAINTING', 5, 6), ('LARGE_PAINTING', 8, 6), ('SMALL_PAINTING_2', 15, 6), ('SMALL_PAINTING', 22, 6),
  ('CUSHIONED_CHAIR_FRONT', 12, 8, LEATHER),
  ('DESK_FRONT', 11, 9, WOOD_DARK), ('PC_BACK', 12, 9),
  ('SOFA_FRONT', 4, 8, COGNAC), ('COFFEE_TABLE', 4, 9, WOOD_DARK), ('COFFEE', 5, 10),
  ('SOFA_FRONT', 18, 8, COGNAC), ('COFFEE_TABLE', 18, 9, WOOD_DARK), ('COFFEE', 18, 10),
  ('LARGE_PLANT', 1, 8), ('LARGE_PLANT', 21, 8),
  # ================= Open space (cols 1-13, rows 13-15) — four bench desks, two seats each
  ('SMALL_PAINTING', 1, 11), ('WHITEBOARD', 4, 11), ('HANGING_PLANT', 9, 11), ('CLOCK', 12, 11),
  ('DESK_FRONT', 1, 13), ('PC_FRONT_OFF', 1, 13), ('PC_FRONT_OFF', 3, 13),
  ('CUSHIONED_CHAIR_BACK', 1, 15, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 15, STAFF_SEAT),
  ('DESK_FRONT', 5, 13), ('PC_FRONT_OFF', 5, 13), ('PC_FRONT_OFF', 7, 13),
  ('CUSHIONED_CHAIR_BACK', 5, 15, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 7, 15, STAFF_SEAT),
  ('DESK_FRONT', 9, 13), ('PC_FRONT_OFF', 9, 13), ('PC_FRONT_OFF', 11, 13),
  ('CUSHIONED_CHAIR_BACK', 9, 15, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 11, 15, STAFF_SEAT),
  ('PLANT', 4, 13), ('PLANT_2', 8, 13), ('BIN', 13, 15), ('CACTUS', 13, 13),
  # ================= Cafe (cols 15-22, rows 13-15) — counter with mugs, two tables
  ('BOOKSHELF', 15, 12), ('LARGE_PAINTING', 21, 11),
  ('DESK_FRONT', 15, 13, WOOD_DARK), ('COFFEE', 15, 14), ('COFFEE', 17, 14),
  ('WOODEN_BENCH', 15, 15, CAFE_SEAT), ('WOODEN_BENCH', 16, 15, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 19, 13, WOOD_DARK), ('COFFEE', 19, 14),
  ('CUSHIONED_CHAIR_SIDE', 18, 14, CAFE_SEAT), ('CUSHIONED_CHAIR_SIDE:left', 21, 14, CAFE_SEAT),
  ('PLANT_2', 22, 13), ('POT', 22, 15),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_CREAM  = {'h': 40, 's': 22, 'b': 0, 'c': -25}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_RUNNER = {'h': 265, 's': 24, 'b': -40, 'c': -22}

CARPETS = [
  {'variant': 0, 'col': 11, 'row': 2, 'w': 3, 'h': 3, 'color': RUG_CREAM, 'accent': RUG_VIOLET},  # CEO desk
  {'variant': 1, 'col': 8, 'row': 3, 'w': 3, 'h': 2, 'color': RUG_VIOLET, 'accent': RUG_GOLD},    # CEO lounge
  {'variant': 2, 'col': 2, 'row': 1, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 0, 'col': 18, 'row': 2, 'w': 3, 'h': 4, 'color': RUG_NAVY, 'accent': RUG_GOLD},     # meeting room
  {'variant': 1, 'col': 6, 'row': 9, 'w': 12, 'h': 1, 'color': RUG_RUNNER, 'accent': RUG_GOLD},   # lobby runner
]

PETS = [0, 1]
