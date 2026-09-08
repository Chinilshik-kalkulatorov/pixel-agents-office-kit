# OFFICE v3 — база: большой дизайн 35x25, ужатый по указу владельца. 24 x 19 = 456 тайлов (52% от большого).
#
# Что сделано с большим офисом:
#   * горизонтальный холл во всю ширину (4 ряда) вырезан полностью;
#   * правая часть урезана: переговорная 8->6 колонок, кафе 11->6, оба правых компьютера убраны;
#   * центральный кабинет CEO 15->6 колонок;
#   * левая часть сохранена: кабинет CTO как был, рабочая комната с ВОСЕМЬЮ компьютерами как была;
#   * вместо холла — компактная входная зона по центру: диван слева, ресепшн справа, проход между ними,
#     двери налево в рабочую зону и направо в кафе; наверх — в кабинет CEO.
#   * верхняя полоса оставлена высокой (8 видимых рядов), как в большом офисе.
#
# rows: 0 стена | 1-9 верхняя полоса (ряд 9 скрыт) | 10 стена с дверями
#       | 11-17 нижняя полоса (ряд 17 скрыт) | 18 стена + вход с улицы
# cols: CTO 1-8 | стена 9 | CEO 10-15 | стена 16 | переговорная 17-22
#       снизу: рабочая 1-8 | стена 9 | вход 10-15 | стена 16 | кафе 17-22
MAP = """
########################
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
#cccccccc#EEEEEE#mmmmmm#
###cc#######EE#####mm###
#ssssssss#LLLLLL#bbbbbb#
#ssssssssLLLLLLL#bbbbbb#
#ssssssssLLLLLLLbbbbbbb#
#ssssssss#LLLLLLbbbbbbb#
#ssssssss#LLLLLL#bbbbbb#
#ssssssss#LLLLLL#bbbbbb#
#ssssssss#LLLLLL#bbbbbb#
############LL##########
"""

ESPRESSO = {'h': 24, 's': 22, 'b': -52, 'c': -80}   # CEO
WALNUT_F = {'h': 27, 's': 18, 'b': -38, 'c': -84}   # CTO / переговорная
MARBLE   = {'h': 38, 's': 10, 'b': -4,  'c': -80}   # входная зона
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # рабочая комната
CHECKER  = {'h': 34, 's': 20, 'b': -10, 'c': -60}   # кафе

LEGEND = {
  'E': {'tile': 4, 'color': ESPRESSO},
  'c': {'tile': 4, 'color': WALNUT_F},
  'm': {'tile': 4, 'color': WALNUT_F},
  'L': {'tile': 4, 'color': MARBLE},
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
  # ===== ЛЕВЫЙ КАБИНЕТ (CTO, cols 1-8, rows 1-8) — как в большом офисе, только растения приведены в порядок
  ('DOUBLE_BOOKSHELF', 1, -1), ('WHITEBOARD', 4, -1), ('CLOCK', 7, -1),
  ('CUSHIONED_CHAIR_FRONT', 4, 2, LEATHER),
  ('DESK_FRONT', 3, 3, WOOD_DARK), ('PC_BACK', 4, 3),
  ('CUSHIONED_CHAIR_BACK', 4, 5, VELVET_GRN),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, VELVET_GRN), ('COFFEE_TABLE', 2, 7, WOOD_DARK), ('COFFEE', 3, 7),
  ('LARGE_PLANT', 7, 6), ('PLANT_2', 1, 1),
  # ===== ЦЕНТРАЛЬНЫЙ КАБИНЕТ (CEO, cols 10-15) — с 15 колонок до 6, но полноценный
  ('DOUBLE_BOOKSHELF', 10, -1), ('CLOCK', 12, -1), ('LARGE_PAINTING', 14, -1),
  ('CUSHIONED_CHAIR_FRONT', 12, 2, GOLD_SEAT),
  ('DESK_FRONT', 11, 3, WOOD_DARK), ('PC_BACK', 12, 3), ('COFFEE', 13, 4),
  ('CUSHIONED_CHAIR_BACK', 11, 5, COGNAC), ('CUSHIONED_CHAIR_BACK', 13, 5, COGNAC),
  ('SOFA_SIDE', 10, 7, COGNAC), ('COFFEE_TABLE', 11, 7, WOOD_DARK), ('COFFEE', 12, 7),
  ('LARGE_PLANT', 14, 6),
  # ===== ПРАВЫЙ КАБИНЕТ (переговорная, cols 17-22) — полный редизайн, компьютеров нет
  ('WHITEBOARD', 17, -1), ('DOUBLE_BOOKSHELF', 19, -1), ('LARGE_PAINTING', 21, -1),
  ('CUSHIONED_CHAIR_FRONT', 19, 2, LEATHER),
  ('TABLE_FRONT', 18, 3, WOOD_DARK),
  ('CUSHIONED_CHAIR_SIDE', 17, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 17, 6, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 21, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 21, 6, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 19, 7, LEATHER),
  ('PLANT_2', 17, 7), ('PLANT', 22, 7),
  # ===== РАБОЧАЯ КОМНАТА (cols 1-8) — восемь компьютеров, как было
  ('WHITEBOARD', 1, 9), ('HANGING_PLANT', 5, 9), ('CLOCK', 8, 9),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 1, 11), ('PC_FRONT_OFF', 3, 11),
  ('CUSHIONED_CHAIR_BACK', 1, 13, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 13, STAFF_SEAT),
  ('DESK_FRONT', 5, 11), ('PC_FRONT_OFF', 5, 11), ('PC_FRONT_OFF', 7, 11),
  ('CUSHIONED_CHAIR_BACK', 5, 13, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 7, 13, STAFF_SEAT),
  ('DESK_FRONT', 1, 14), ('PC_FRONT_OFF', 1, 14), ('PC_FRONT_OFF', 3, 14),
  ('CUSHIONED_CHAIR_BACK', 1, 16, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 16, STAFF_SEAT),
  ('DESK_FRONT', 5, 14), ('PC_FRONT_OFF', 5, 14), ('PC_FRONT_OFF', 7, 14),
  ('CUSHIONED_CHAIR_BACK', 5, 16, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 7, 16, STAFF_SEAT),
  ('BIN', 8, 16),
  # ===== ВХОДНАЯ ЗОНА (cols 10-15) — диван слева со столиком за ним, ресепшн справа, проход по колонке 12
  ('LARGE_PAINTING', 10, 9), ('SMALL_PAINTING_2', 15, 9), ('PLANT_2', 15, 11),
  ('SMALL_TABLE_FRONT', 10, 13, WOOD_DARK), ('COFFEE', 11, 14),
  ('SOFA_FRONT', 10, 15, COGNAC),
  ('CUSHIONED_CHAIR_FRONT', 14, 13, LEATHER),
  ('DESK_FRONT', 13, 14, WOOD_DARK), ('PC_BACK', 14, 14),
  # ===== КАФЕ (cols 17-22) — стойка, столик и диван-уголок
  ('BOOKSHELF', 17, 10), ('HANGING_PLANT', 22, 9),
  ('DESK_FRONT', 17, 11, WOOD_DARK), ('COFFEE', 17, 12), ('COFFEE', 19, 12),
  ('WOODEN_BENCH', 17, 13, CAFE_SEAT), ('WOODEN_BENCH', 18, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 21, 11, WOOD_DARK), ('COFFEE', 21, 12),
  ('CUSHIONED_CHAIR_BACK', 21, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 22, 13, CAFE_SEAT),
  ('SOFA_SIDE', 17, 15, CAFE_SEAT), ('COFFEE_TABLE', 18, 15, WOOD_DARK), ('COFFEE', 18, 15),
  ('PLANT_2', 22, 15),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_CREAM  = {'h': 40, 's': 22, 'b': 0, 'c': -25}

CARPETS = [
  {'variant': 0, 'col': 11, 'row': 2, 'w': 3, 'h': 4, 'color': RUG_VIOLET, 'accent': RUG_GOLD},   # CEO
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 4, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 0, 'col': 18, 'row': 3, 'w': 3, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},     # переговорная
  {'variant': 1, 'col': 12, 'row': 16, 'w': 2, 'h': 1, 'color': RUG_CREAM, 'accent': RUG_GOLD},   # коврик у входа
]

PETS = [0, 1]
