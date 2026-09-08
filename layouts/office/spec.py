# OFFICE v4 — 24 x 19 = 456. База: большой офис, порезанный по указам владельца.
#
# Правки этого захода:
#   * диван у входа стоит ВЕРТИКАЛЬНО;
#   * стол администратора там, куда владелец его сам поставил — (10,11), в одном шаге от прохода;
#   * рабочая комната: 8 компьютеров -> 6 (убраны правый верхний и правый нижний);
#   * входная зона ужата с 6 колонок до 4;
#   * кухня расширена с 6 до 8 колонок и собрана как в большом офисе: барная стойка с полками и табуретами,
#     сетка столиков, диван-уголок, растения;
#   * верхняя полоса переработана от большого офиса: CTO как был, кабинет CEO с лаунж-группой, переговорная.
#
# rows: 0 стена | 1-9 верх (ряд 9 скрыт) | 10 стена с дверями | 11-17 низ (ряд 17 скрыт) | 18 стена + вход
# cols верх:  CTO 1-8 | стена 9 | CEO 10-16 | стена 17 | переговорная 18-22
# cols низ:   рабочая 1-8 | стена 9 | вход 10-13 | стена 14 | кухня 15-22
MAP = """
########################
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
#cccccccc#EEEEEEE#mmmmm#
###cc######EE######mm###
#ssssssss#LLLL#bbbbbbbb#
#ssssssss#LLLL#bbbbbbbb#
#ssssssssLLLLLbbbbbbbbb#
#ssssssssLLLLLbbbbbbbbb#
#ssssssss#LLLL#bbbbbbbb#
#ssssssss#LLLL#bbbbbbbb#
#ssssssss#LLLL#bbbbbbbb#
############LL##########
"""

ESPRESSO = {'h': 24, 's': 22, 'b': -52, 'c': -80}   # CEO
WALNUT_F = {'h': 27, 's': 18, 'b': -38, 'c': -84}   # CTO / переговорная
MARBLE   = {'h': 38, 's': 10, 'b': -4,  'c': -80}   # входная зона
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # рабочая комната
CHECKER  = {'h': 34, 's': 20, 'b': -10, 'c': -60}   # кухня

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
  # ===== ЛЕВЫЙ КАБИНЕТ (CTO, cols 1-8) — как в большом офисе
  ('DOUBLE_BOOKSHELF', 1, -1), ('WHITEBOARD', 4, -1), ('CLOCK', 7, -1),
  ('CUSHIONED_CHAIR_FRONT', 4, 2, LEATHER),
  ('DESK_FRONT', 3, 3, WOOD_DARK), ('PC_BACK', 4, 3),
  ('CUSHIONED_CHAIR_BACK', 4, 5, VELVET_GRN),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, VELVET_GRN), ('COFFEE_TABLE', 2, 7, WOOD_DARK), ('COFFEE', 3, 7),
  ('LARGE_PLANT', 7, 6), ('PLANT_2', 1, 1),
  # ===== КАБИНЕТ CEO (cols 10-16) — стол по центру, гости, лаунж-группа слева, зелень справа
  ('DOUBLE_BOOKSHELF', 10, -1), ('LARGE_PAINTING', 12, -1), ('CLOCK', 15, -1),
  ('CUSHIONED_CHAIR_FRONT', 13, 2, GOLD_SEAT),
  ('DESK_FRONT', 12, 3, WOOD_DARK), ('PC_BACK', 13, 3), ('COFFEE', 14, 4),
  ('CUSHIONED_CHAIR_BACK', 12, 5, COGNAC), ('CUSHIONED_CHAIR_BACK', 14, 5, COGNAC),
  ('SOFA_SIDE', 10, 6, COGNAC), ('COFFEE_TABLE', 11, 6, WOOD_DARK), ('COFFEE', 12, 7),
  ('LARGE_PLANT', 15, 6), ('PLANT_2', 16, 1),
  # ===== ПЕРЕГОВОРНАЯ (cols 18-22) — стол на шесть мест, доска, картина, ковёр
  ('WHITEBOARD', 18, -1), ('LARGE_PAINTING', 21, -1),
  ('CUSHIONED_CHAIR_FRONT', 20, 2, LEATHER),
  ('TABLE_FRONT', 19, 3, WOOD_DARK),
  ('CUSHIONED_CHAIR_SIDE', 18, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 18, 6, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 22, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 22, 6, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 20, 7, LEATHER),
  ('PLANT_2', 18, 7),
  # ===== РАБОЧАЯ КОМНАТА (cols 1-8) — ШЕСТЬ компьютеров: правый верхний и правый нижний убраны
  ('WHITEBOARD', 1, 9), ('HANGING_PLANT', 5, 9), ('CLOCK', 8, 9),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 1, 11), ('PC_FRONT_OFF', 3, 11),
  ('CUSHIONED_CHAIR_BACK', 1, 13, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 13, STAFF_SEAT),
  ('DESK_FRONT', 5, 11), ('PC_FRONT_OFF', 6, 11),
  ('CUSHIONED_CHAIR_BACK', 6, 13, STAFF_SEAT),
  ('DESK_FRONT', 1, 14), ('PC_FRONT_OFF', 1, 14), ('PC_FRONT_OFF', 3, 14),
  ('CUSHIONED_CHAIR_BACK', 1, 16, STAFF_SEAT), ('CUSHIONED_CHAIR_BACK', 3, 16, STAFF_SEAT),
  ('DESK_FRONT', 5, 14), ('PC_FRONT_OFF', 6, 14),
  ('CUSHIONED_CHAIR_BACK', 6, 16, STAFF_SEAT),
  ('PLANT_2', 7, 15), ('BIN', 8, 16),
  # ===== ВХОДНАЯ ЗОНА (cols 10-13) — ужата вдвое; стол администратора там, где его поставил владелец
  ('SMALL_PAINTING', 10, 9), ('SMALL_PAINTING_2', 13, 9),
  ('DESK_FRONT', 10, 11, WOOD_DARK), ('PC_BACK', 11, 11), ('CUSHIONED_CHAIR_FRONT', 11, 11, LEATHER),
  ('SOFA_SIDE', 10, 14, COGNAC),                                  # диван стоит вертикально
  ('COFFEE_TABLE', 11, 14, WOOD_DARK), ('COFFEE', 12, 14),
  # ===== КУХНЯ (cols 15-22) — расширена, собрана как буфет большого офиса
  ('BOOKSHELF', 15, 10), ('BOOKSHELF', 17, 10), ('LARGE_PAINTING', 21, 9),
  ('DESK_FRONT', 15, 11, WOOD_DARK), ('COFFEE', 15, 12), ('COFFEE', 17, 12),
  ('WOODEN_BENCH', 15, 13, CAFE_SEAT), ('WOODEN_BENCH', 16, 13, CAFE_SEAT), ('WOODEN_BENCH', 17, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 19, 11, WOOD_DARK), ('COFFEE', 19, 12),
  ('CUSHIONED_CHAIR_BACK', 19, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 20, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 19, 14, WOOD_DARK), ('COFFEE', 20, 15),
  ('CUSHIONED_CHAIR_BACK', 19, 16, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 20, 16, CAFE_SEAT),
  ('SOFA_SIDE', 15, 15, CAFE_SEAT), ('COFFEE_TABLE', 16, 15, WOOD_DARK), ('COFFEE', 16, 15),
  ('PLANT_2', 22, 11), ('PLANT', 22, 14), ('POT', 22, 16),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_CREAM  = {'h': 40, 's': 22, 'b': 0, 'c': -25}

CARPETS = [
  {'variant': 0, 'col': 12, 'row': 2, 'w': 3, 'h': 4, 'color': RUG_VIOLET, 'accent': RUG_GOLD},   # CEO
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 4, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 0, 'col': 19, 'row': 3, 'w': 3, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},     # переговорная
  {'variant': 1, 'col': 12, 'row': 16, 'w': 2, 'h': 1, 'color': RUG_CREAM, 'accent': RUG_GOLD},   # коврик у входа
]

PETS = [0, 1]
