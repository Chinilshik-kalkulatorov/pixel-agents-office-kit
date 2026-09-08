# FINAL v5 — exec_classic skeleton + consensus grafts + 3-auditor fixes.
# cols 0..34 (35), rows 0..24 (25)
# Top band   rows 1-9  (9 hidden behind wall row 10): CTO 1-8 | CEO 10-24 | Board 26-33
# Lobby      rows 11-14 (14 hidden behind wall row 15): full width 1-33, T-shaped: hall cols 17-21 drops to street door
# Bottom     rows 16-23 (23 hidden behind wall row 24): Staff 1-15 | Hall 17-21 | Buffet 23-33
MAP = """
###################################
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEEEEE#mmmmmmmm#
####LL##########LLL##########LL####
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL#
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL#
#######LLL#######LLLLL######LL#####
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssss#LLLLL#bbbbbbbbbbb#
##################LLL##############
"""

ESPRESSO  = {'h': 24, 's': 20, 'b': -50, 'c': -82}   # CEO dark parquet
WALNUT    = {'h': 26, 's': 18, 'b': -38, 'c': -84}   # CTO / board parquet
STONE_L   = {'h': 38, 's': 8,  'b': 2,   'c': -82}   # lobby + hall pale slabs
STONE     = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # staff
CHECKER   = {'h': 36, 's': 14, 'b': -10, 'c': -80}   # buffet

LEGEND = {
  'E': {'tile': 4, 'color': ESPRESSO},
  'c': {'tile': 4, 'color': WALNUT},
  'm': {'tile': 4, 'color': WALNUT},
  'L': {'tile': 4, 'color': STONE_L},
  's': {'tile': 5, 'color': STONE},
  'b': {'tile': 9, 'color': CHECKER},
}

VIOLET_WALL = {'h': 265, 's': 35, 'b': -75, 'c': -45}
NAVY_WALL   = {'h': 228, 's': 32, 'b': -80, 'c': -45}
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
CREAM_WALL  = {'h': 38, 's': 18, 'b': -22, 'c': -55}
WALL_COLOR = CHARCOAL
WALL_COLORS = {
  'E': VIOLET_WALL,
  'm': VIOLET_WALL,     # board room is CEO-adjacent -> exec violet family
  'c': NAVY_WALL,       # CTO: its own navy identity
  'L': CHARCOAL,        # lobby = neutral gallery
  's': CHARCOAL,
  'b': CREAM_WALL,
}

WOOD_DARK   = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER     = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}   # black leather (keeps highlights)
COGNAC      = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}    # cognac leather guest chairs
GOLD_SEAT   = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}    # antique gold velvet
VELVET_GRN  = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}    # CTO visitor chair
STAFF_SEAT  = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}    # grey-blue fabric
CAFE_SEAT   = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}     # terracotta

FURNITURE = [
  # ---------------- CEO suite (cols 10-24, rows 1-8 visible) ----------------
  # wall: shelf 10-11 | portrait 12 | plant 13 | painting 14-15 | clock 17 | painting 19-20 | plant 21 | portrait 22 | shelf 23-24
  ('DOUBLE_BOOKSHELF', 10, -1), ('SMALL_PAINTING', 12, -1), ('LARGE_PAINTING', 14, -1), ('CLOCK', 17, -1),
  ('LARGE_PAINTING', 19, -1), ('SMALL_PAINTING_2', 22, -1), ('DOUBLE_BOOKSHELF', 23, -1),
  ('PLANT', 13, 0), ('PLANT', 21, 0),
  # desk group fills the rug rows 2-7; CEO faces the room
  ('CUSHIONED_CHAIR_FRONT', 17, 2, GOLD_SEAT),
  ('TABLE_FRONT', 16, 3, WOOD_DARK), ('PC_BACK', 17, 3), ('COFFEE', 18, 5),
  ('CUSHIONED_CHAIR_BACK', 16, 7, COGNAC), ('CUSHIONED_CHAIR_BACK', 18, 7, COGNAC),
  # lounges centred on the room (rows 4-5): leather sofa + gold armchairs around walnut coffee table with a mug
  ('SOFA_SIDE', 10, 4, LEATHER), ('COFFEE_TABLE', 11, 4, WOOD_DARK), ('COFFEE', 12, 4),
  ('CUSHIONED_CHAIR_SIDE:left', 13, 4, GOLD_SEAT), ('CUSHIONED_CHAIR_SIDE:left', 13, 5, GOLD_SEAT),
  ('CUSHIONED_CHAIR_SIDE', 21, 4, GOLD_SEAT), ('CUSHIONED_CHAIR_SIDE', 21, 5, GOLD_SEAT),
  ('COFFEE_TABLE', 22, 4, WOOD_DARK), ('COFFEE', 22, 4), ('SOFA_SIDE:left', 24, 4, LEATHER),
  ('LARGE_PLANT', 10, 6), ('LARGE_PLANT', 23, 6),
  # ---------------- CTO office (cols 1-8, rows 1-8 visible) ----------------
  ('DOUBLE_BOOKSHELF', 1, -1), ('WHITEBOARD', 4, -1), ('CLOCK', 7, -1),
  ('DESK_FRONT', 3, 3, WOOD_DARK), ('PC_BACK', 4, 3),
  ('CUSHIONED_CHAIR_FRONT', 4, 2, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 4, 5, VELVET_GRN),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, VELVET_GRN), ('COFFEE_TABLE', 2, 7, WOOD_DARK), ('COFFEE', 3, 7),
  ('LARGE_PLANT', 7, 5), ('BIN', 7, 4), ('PLANT_2', 1, 1),
  # ---------------- Board room (cols 26-33, rows 1-8 visible) ----------------
  ('WHITEBOARD', 26, -1), ('CLOCK', 29, -1), ('LARGE_PAINTING', 31, -1),
  ('TABLE_FRONT', 28, 3, WOOD_DARK), ('PC_SIDE', 28, 3), ('PC_SIDE:left', 30, 3),
  ('CUSHIONED_CHAIR_SIDE', 27, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 27, 6, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 31, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 31, 6, LEATHER),
  ('CUSHIONED_CHAIR_FRONT', 29, 2, LEATHER),
  ('PLANT', 26, 6), ('PLANT_2', 33, 6),
  # ---------------- Lobby (cols 1-33, rows 11-13 visible) ----------------
  # wall art mirrored about col 17: 7 | 10-11 | 13  and  21 | 23-24 | 27 ; sofas under bare wall at 8-9 / 25-26
  ('SMALL_PAINTING', 7, 9), ('LARGE_PAINTING', 10, 9), ('SMALL_PAINTING_2', 13, 9),
  ('SMALL_PAINTING_2', 21, 9), ('LARGE_PAINTING', 23, 9), ('SMALL_PAINTING', 27, 9),
  ('SOFA_FRONT', 8, 11, LEATHER), ('SOFA_FRONT', 25, 11, LEATHER),
  ('PLANT', 12, 10), ('PLANT', 22, 10),
  ('LARGE_PLANT', 1, 9), ('LARGE_PLANT', 32, 9),
  # reception hall (cols 17-21): clear threshold row 16, receptionist faces the street door
  ('CUSHIONED_CHAIR_FRONT', 19, 17, LEATHER),
  ('DESK_FRONT', 18, 18, WOOD_DARK), ('PC_BACK', 19, 18),
  ('PLANT', 17, 20), ('PLANT_2', 21, 20),
  # ---------------- Staff floor (cols 1-15, rows 16-22 visible) ----------------
  # top wall: portrait 1 | whiteboard 3-4 | plant 6 | door 7-9 | plant 10 | whiteboard 12-13 | clock 15
  ('SMALL_PAINTING', 1, 14), ('WHITEBOARD', 3, 14), ('HANGING_PLANT', 6, 14),
  ('HANGING_PLANT', 10, 14), ('WHITEBOARD', 12, 14), ('CLOCK', 15, 14),
  # pod row 1
  ('DESK_FRONT', 1, 16), ('DESK_FRONT', 4, 16), ('PC_FRONT_OFF', 2, 16), ('PC_FRONT_OFF', 5, 16),
  ('CUSHIONED_CHAIR_BACK', 2, 18, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 5, 18, STAFF_SEAT),
  ('DESK_FRONT', 10, 16), ('DESK_FRONT', 13, 16), ('PC_FRONT_OFF', 11, 16), ('PC_FRONT_OFF', 14, 16),
  ('CUSHIONED_CHAIR_BACK', 11, 18, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 14, 18, STAFF_SEAT),
  # pod row 2
  ('DESK_FRONT', 1, 20), ('DESK_FRONT', 4, 20), ('PC_FRONT_OFF', 2, 20), ('PC_FRONT_OFF', 5, 20),
  ('CUSHIONED_CHAIR_BACK', 2, 22, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 5, 22, STAFF_SEAT),
  ('DESK_FRONT', 10, 20), ('DESK_FRONT', 13, 20), ('PC_FRONT_OFF', 11, 20), ('PC_FRONT_OFF', 14, 20),
  ('CUSHIONED_CHAIR_BACK', 11, 22, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 14, 22, STAFF_SEAT),
  # bins and plants at the pod ends, aisle 7-9 fully clear
  ('BIN', 6, 18), ('BIN', 10, 18), ('PLANT', 6, 21), ('PLANT_2', 10, 21),
  # ---------------- Buffet (cols 23-33, rows 16-22 visible) ----------------
  # wall: bar shelf 24-25 | plant 27 | door 28-29 | plant 30 | painting 32-33
  ('BOOKSHELF', 24, 15), ('HANGING_PLANT', 27, 14), ('HANGING_PLANT', 30, 14), ('LARGE_PAINTING', 32, 14),
  # walnut bar counter with a barista lane (col 23) behind it, mugs, two stools facing it
  ('DESK_SIDE', 24, 16, WOOD_DARK), ('COFFEE', 24, 17), ('COFFEE', 24, 19),
  ('WOODEN_BENCH', 25, 17), ('WOODEN_BENCH', 25, 19),
  # 2x2 grid of matching walnut cafe tables with terracotta chairs
  ('SMALL_TABLE_FRONT', 26, 16, WOOD_DARK), ('COFFEE', 27, 17),
  ('CUSHIONED_CHAIR_BACK', 26, 18, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 27, 18, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 30, 16, WOOD_DARK), ('COFFEE', 30, 17),
  ('CUSHIONED_CHAIR_BACK', 30, 18, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 31, 18, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 26, 20, WOOD_DARK), ('COFFEE', 26, 21),
  ('CUSHIONED_CHAIR_BACK', 26, 22, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 27, 22, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 30, 20, WOOD_DARK), ('COFFEE', 31, 21),
  ('CUSHIONED_CHAIR_BACK', 30, 22, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 31, 22, CAFE_SEAT),
  # lounge corner under the bar: terracotta sofa + coffee table with a mug
  ('SOFA_SIDE', 23, 20, CAFE_SEAT), ('COFFEE_TABLE', 24, 20, WOOD_DARK), ('COFFEE', 25, 20),
  ('PLANT_2', 33, 16), ('LARGE_PLANT', 32, 20), ('BIN', 23, 22),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -38, 'c': -20}
RUG_VIOLET2 = {'h': 265, 's': 30, 'b': -45, 'c': -20}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -45, 'c': -20}
RUG_SILVER = {'h': 220, 's': 10, 'b': 15, 'c': 0}
RUG_RUNNER = {'h': 265, 's': 24, 'b': -42, 'c': -20}

CARPETS = [
  {'variant': 0, 'col': 15, 'row': 2, 'w': 5, 'h': 6, 'color': RUG_VIOLET, 'accent': RUG_GOLD},    # CEO desk zone
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},       # CTO (gold accent = #2 room)
  {'variant': 0, 'col': 27, 'row': 2, 'w': 5, 'h': 6, 'color': RUG_NAVY, 'accent': RUG_SILVER},   # board room, centred on col 29
  {'variant': 2, 'col': 3, 'row': 12, 'w': 29, 'h': 1, 'color': RUG_RUNNER, 'accent': RUG_GOLD},   # lobby runner, one row
  {'variant': 2, 'col': 18, 'row': 20, 'w': 3, 'h': 2, 'color': RUG_RUNNER, 'accent': RUG_GOLD},   # hall runner, ends above hidden row 23
]
