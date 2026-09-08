# REDESIGN v2 — 20 x 16 = 320 tiles (было 24x18=432). Горизонтальный холл убран полностью.
#
# Логика входа: человек входит снизу по центру -> компактная входная зона (диван слева со столиком за ним,
# ресепшн справа) -> свободный проход по колонке 10 -> налево в рабочую зону, направо в кафе.
#
# rows: 0 стена | 1-6 верхняя полоса (ряд 6 скрыт) -> видимые 1-5 | 7 стена с дверями
#       | 8-14 нижний открытый этаж (ряд 14 скрыт) -> видимые 8-13 | 15 стена + вход с улицы
# cols: CTO 1-5 | стена 6 | CEO 7-12 (самый широкий) | стена 13 | переговорная 14-18
#       снизу: опенспейс 1-7 | входная зона 8-13 | кафе 14-18   (без стен — зоны читаются полом)
MAP = """
####################
#ccccc#EEEEEE#mmmmm#
#ccccc#EEEEEE#mmmmm#
#ccccc#EEEEEE#mmmmm#
#ccccc#EEEEEE#mmmmm#
#ccccc#EEEEEE#mmmmm#
#ccccc#EEEEEE#mmmmm#
##cc#####EE#####mm##
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
#sssssssLLLLLLbbbbb#
##########LL########
"""

ESPRESSO = {'h': 24, 's': 22, 'b': -52, 'c': -80}   # CEO
WALNUT_F = {'h': 27, 's': 18, 'b': -38, 'c': -84}   # CTO / переговорная
MARBLE   = {'h': 38, 's': 8,  'b': 0,   'c': -82}   # входная зона
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # опенспейс
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
  # ===== ЛЕВЫЙ КАБИНЕТ (CTO, cols 1-6) — структура сохранена, наведён порядок
  ('WHITEBOARD', 1, -1), ('LARGE_PAINTING', 4, -1),
  ('CUSHIONED_CHAIR_FRONT', 3, 1, LEATHER),
  ('DESK_FRONT', 2, 2, WOOD_DARK), ('PC_BACK', 3, 2),
  ('CUSHIONED_CHAIR_BACK', 3, 4, VELVET_GRN),
  ('COFFEE_TABLE', 1, 4, WOOD_DARK), ('COFFEE', 1, 5),
  ('CUSHIONED_CHAIR_SIDE:left', 3, 5, VELVET_GRN),
  ('PLANT_2', 5, 4),
  # ===== ЦЕНТРАЛЬНЫЙ КАБИНЕТ (CEO, cols 8-12) — ужат с 8 до 5 колонок, но полноценный
  ('DOUBLE_BOOKSHELF', 7, -1), ('LARGE_PAINTING', 11, -1),
  ('CUSHIONED_CHAIR_FRONT', 10, 1, GOLD_SEAT),
  ('DESK_FRONT', 9, 2, WOOD_DARK), ('PC_BACK', 10, 2), ('COFFEE', 11, 3),
  ('CUSHIONED_CHAIR_BACK', 9, 4, COGNAC), ('CUSHIONED_CHAIR_BACK', 11, 4, COGNAC),
  ('COFFEE_TABLE', 7, 2, WOOD_DARK), ('COFFEE', 8, 3), ('SOFA_BACK', 7, 4, COGNAC), ('PLANT_2', 12, 4),
  # ===== ПРАВЫЙ КАБИНЕТ (переговорная, cols 14-18) — полный редизайн: стол на шесть мест
  ('WHITEBOARD', 14, -1), ('LARGE_PAINTING', 17, -1),
  ('SMALL_TABLE_FRONT', 16, 2, WOOD_DARK),
  ('CUSHIONED_CHAIR_FRONT', 16, 1, LEATHER),
  ('CUSHIONED_CHAIR_SIDE', 15, 3, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 18, 3, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 16, 4, LEATHER), ('CUSHIONED_CHAIR_BACK', 17, 4, LEATHER),
  ('PLANT', 14, 4), ('CACTUS', 14, 1),
  # ===== ВХОДНАЯ ЗОНА (cols 8-13) — диван со столиком слева, ресепшн справа, проход по колонке 10
  ('SMALL_PAINTING_2', 13, 6),
  ('SMALL_TABLE_FRONT', 8, 9, WOOD_DARK), ('COFFEE', 9, 10),
  ('SOFA_FRONT', 8, 12, COGNAC),
  ('PLANT_2', 13, 8), ('LARGE_PAINTING', 11, 6),
  ('CUSHIONED_CHAIR_FRONT', 12, 10, LEATHER),
  ('DESK_FRONT', 11, 11, WOOD_DARK), ('PC_BACK', 12, 11),
  # ===== ОПЕНСПЕЙС (cols 1-7) — восемь рабочих мест, концепция сохранена
  ('CLOCK', 1, 6), ('WHITEBOARD', 4, 6), ('HANGING_PLANT', 6, 6),
  ('DESK_FRONT', 1, 8), ('PC_FRONT_OFF', 1, 8), ('PC_FRONT_OFF', 3, 8),
  ('CUSHIONED_CHAIR_BACK', 1, 10, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 10, STAFF_SEAT),
  ('DESK_FRONT', 5, 8), ('PC_FRONT_OFF', 5, 8), ('PC_FRONT_OFF', 7, 8),
  ('CUSHIONED_CHAIR_BACK', 5, 10, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 7, 10, STAFF_SEAT),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 1, 11), ('PC_FRONT_OFF', 3, 11),
  ('CUSHIONED_CHAIR_BACK', 1, 13, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 13, STAFF_SEAT),
  ('DESK_FRONT', 5, 11), ('PC_FRONT_OFF', 5, 11), ('PC_FRONT_OFF', 7, 11),
  ('CUSHIONED_CHAIR_BACK', 5, 13, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 7, 13, STAFF_SEAT),
  # ===== КАФЕ (cols 14-18) — стойка, столик и диван-уголок, всё плотнее
  ('BOOKSHELF', 14, 7),
  ('DESK_FRONT', 14, 8, WOOD_DARK), ('COFFEE', 14, 9), ('COFFEE', 16, 9),
  ('WOODEN_BENCH', 14, 10, CAFE_SEAT), ('WOODEN_BENCH', 15, 10, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 17, 10, WOOD_DARK), ('COFFEE', 17, 11),
  ('CUSHIONED_CHAIR_BACK', 17, 12, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 18, 12, CAFE_SEAT),
  ('SOFA_SIDE', 14, 12, CAFE_SEAT), ('COFFEE_TABLE', 15, 12, WOOD_DARK), ('COFFEE', 15, 12),
  ('PLANT_2', 18, 8),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_CREAM  = {'h': 40, 's': 22, 'b': 0, 'c': -25}

CARPETS = [
  {'variant': 0, 'col': 9, 'row': 1, 'w': 3, 'h': 4, 'color': RUG_VIOLET, 'accent': RUG_GOLD},   # CEO
  {'variant': 2, 'col': 2, 'row': 1, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_GOLD},     # CTO
  {'variant': 0, 'col': 15, 'row': 1, 'w': 4, 'h': 4, 'color': RUG_NAVY, 'accent': RUG_GOLD},    # переговорная
  {'variant': 1, 'col': 10, 'row': 13, 'w': 2, 'h': 1, 'color': RUG_CREAM, 'accent': RUG_GOLD},   # коврик у входа
]

PETS = [0, 1]
