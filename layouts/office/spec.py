# OFFICE v5 — большой офис 35x25, порезанный по указам. 32 x 20 = 640 тайлов.
#
# Что сделано:
#   1. КОРИДОР между верхом и низом вырезан целиком — нижняя часть поднята вплотную к верхней.
#      Верхние кабинеты НЕ растянуты: у них те же 8 видимых рядов, что в большом офисе.
#   2. Рабочая комната: правый столбец столов (верхний и нижний) убран, стена сдвинута налево
#      с колонки 16 на колонку 13. Осталось 6 компьютеров. В новой стене дверь.
#   3. Центральный кабинет -> ЗАЛ: боковые зоны отдыха убраны полностью, стол развёрнут
#      горизонтально (две секции в линию), кресла по обеим сторонам.
#   4. Правый зал -> КАБИНЕТ, непохожий на левый: стол боком, начальник и гость сидят
#      друг напротив друга через стол, своя зелёная стена, диван с журнальным столиком.
#   5. Кухня ЗЕРКАЛЬНА: барная стойка с проходом бариста и табуретами теперь справа,
#      диван-уголок тоже справа, сетка столиков слева.
#   6. Левый кабинет (CTO) не тронут.
#
# rows: 0 стена | 1-9 верх (ряд 9 скрыт) | 10 стена с дверями | 11-18 низ (ряд 18 скрыт) | 19 стена + вход
# cols верх: CTO 1-8 | стена 9 | ЗАЛ 10-21 | стена 22 | КАБИНЕТ 23-30 | стена 31
# cols низ:  рабочая 1-12 | стена 13 | ресепшн 14-18 | стена 19 | кухня 20-30 | стена 31
MAP = """
################################
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
#cccccccc#EEEEEEEEEEEE#mmmmmmmm#
####cc#########EE#########mm####
#ssssssssssss#LLLLL#bbbbbbbbbbb#
#ssssssssssss#LLLLL#bbbbbbbbbbb#
#sssssssssssssLLLLLLbbbbbbbbbbb#
#sssssssssssssLLLLLLbbbbbbbbbbb#
#ssssssssssss#LLLLL#bbbbbbbbbbb#
#ssssssssssss#LLLLL#bbbbbbbbbbb#
#ssssssssssss#LLLLL#bbbbbbbbbbb#
#ssssssssssss#LLLLL#bbbbbbbbbbb#
################LL##############
"""

ESPRESSO = {'h': 24, 's': 20, 'b': -50, 'c': -82}   # зал
WALNUT   = {'h': 26, 's': 18, 'b': -38, 'c': -84}   # CTO / правый кабинет
STONE_L  = {'h': 38, 's': 8,  'b': 2,   'c': -82}   # ресепшн
STONE    = {'h': 212, 's': 10, 'b': -24, 'c': -85}  # рабочая
CHECKER  = {'h': 36, 's': 14, 'b': -10, 'c': -80}   # кухня

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
GREEN_WALL  = {'h': 168, 's': 30, 'b': -78, 'c': -45}
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
CREAM_WALL  = {'h': 38, 's': 18, 'b': -22, 'c': -55}
WALL_COLOR = CHARCOAL
WALL_COLORS = {
  'E': VIOLET_WALL,     # зал
  'c': NAVY_WALL,       # левый кабинет
  'm': GREEN_WALL,      # правый кабинет — своя стена
  'L': CHARCOAL,
  's': CHARCOAL,
  'b': CREAM_WALL,
}

WOOD_DARK  = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER    = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ===== ЛЕВЫЙ КАБИНЕТ (CTO, cols 1-8) — не тронут
  ('DOUBLE_BOOKSHELF', 1, -1), ('WHITEBOARD', 4, -1), ('CLOCK', 7, -1),
  ('CUSHIONED_CHAIR_FRONT', 4, 2, LEATHER),
  ('DESK_FRONT', 3, 3, WOOD_DARK), ('PC_BACK', 4, 3),
  ('CUSHIONED_CHAIR_BACK', 4, 5, VELVET_GRN),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, VELVET_GRN), ('COFFEE_TABLE', 2, 7, WOOD_DARK), ('COFFEE', 3, 7),
  ('LARGE_PLANT', 7, 5), ('BIN', 7, 4), ('PLANT_2', 1, 1),
  # ===== ЗАЛ (cols 10-21) — зоны отдыха убраны, стол горизонтальный, кресла с двух сторон
  ('DOUBLE_BOOKSHELF', 10, -1), ('LARGE_PAINTING', 13, -1), ('CLOCK', 16, -1),
  ('LARGE_PAINTING', 18, -1), ('DOUBLE_BOOKSHELF', 20, -1),
  ('TABLE_FRONT', 13, 3, WOOD_DARK), ('TABLE_FRONT', 16, 3, WOOD_DARK),
  ('PC_SIDE', 13, 3), ('PC_SIDE:left', 18, 3),
  ('CUSHIONED_CHAIR_FRONT', 14, 2, LEATHER), ('CUSHIONED_CHAIR_FRONT', 17, 2, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 14, 7, LEATHER), ('CUSHIONED_CHAIR_BACK', 17, 7, LEATHER),
  ('CUSHIONED_CHAIR_SIDE', 12, 5, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 19, 5, LEATHER),
  ('LARGE_PLANT', 10, 6), ('LARGE_PLANT', 20, 6),
  ('PLANT', 11, 1), ('PLANT', 20, 1),
  # ===== ПРАВЫЙ КАБИНЕТ (cols 23-30) — стол боком, хозяин и гость лицом друг к другу
  ('WHITEBOARD', 23, -1), ('LARGE_PAINTING', 26, -1), ('CLOCK', 29, -1),
  ('DESK_SIDE', 25, 2, WOOD_DARK), ('PC_SIDE:left', 25, 3),
  ('CUSHIONED_CHAIR_SIDE:left', 26, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 24, 4, VELVET_GRN),
  ('SOFA_FRONT', 28, 5, COGNAC), ('COFFEE_TABLE', 28, 6, WOOD_DARK), ('COFFEE', 29, 6),
  ('LARGE_PLANT', 23, 6), ('PLANT_2', 30, 1), ('BIN', 23, 2),
  # ===== РАБОЧАЯ КОМНАТА (cols 1-12) — шесть компьютеров, правый столбец снесён
  ('SMALL_PAINTING', 1, 9), ('WHITEBOARD', 2, 9), ('HANGING_PLANT', 6, 9), ('CLOCK', 8, 9),
  ('WHITEBOARD', 10, 9), ('HANGING_PLANT', 12, 9),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 2, 11), ('CUSHIONED_CHAIR_BACK', 2, 13, STAFF_SEAT),
  ('DESK_FRONT', 4, 11), ('PC_FRONT_OFF', 5, 11), ('CUSHIONED_CHAIR_BACK', 5, 13, STAFF_SEAT),
  ('DESK_FRONT', 9, 11), ('PC_FRONT_OFF', 10, 11), ('CUSHIONED_CHAIR_BACK', 10, 13, STAFF_SEAT),
  ('DESK_FRONT', 1, 14), ('PC_FRONT_OFF', 2, 14), ('CUSHIONED_CHAIR_BACK', 2, 16, STAFF_SEAT),
  ('DESK_FRONT', 4, 14), ('PC_FRONT_OFF', 5, 14), ('CUSHIONED_CHAIR_BACK', 5, 16, STAFF_SEAT),
  ('DESK_FRONT', 9, 14), ('PC_FRONT_OFF', 10, 14), ('CUSHIONED_CHAIR_BACK', 10, 16, STAFF_SEAT),
  ('BIN', 7, 13), ('PLANT_2', 7, 16), ('PLANT', 12, 15),
  # ===== РЕСЕПШН (cols 14-18) — администратор лицом ко входу с улицы
  ('SMALL_PAINTING', 14, 9), ('SMALL_PAINTING_2', 18, 9),
  ('CUSHIONED_CHAIR_FRONT', 16, 12, LEATHER),
  ('DESK_FRONT', 15, 13, WOOD_DARK), ('PC_BACK', 16, 13),
  ('PLANT', 14, 16), ('PLANT_2', 18, 16),
  # ===== КУХНЯ (cols 20-30) — ЗЕРКАЛЬНО: стойка и диван справа, столики слева
  ('LARGE_PAINTING', 20, 9), ('HANGING_PLANT', 23, 9), ('BOOKSHELF', 28, 10),
  ('DESK_SIDE', 29, 11, WOOD_DARK), ('COFFEE', 29, 12), ('COFFEE', 29, 14),
  ('WOODEN_BENCH', 28, 12, CAFE_SEAT), ('WOODEN_BENCH', 28, 14, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 21, 11, WOOD_DARK), ('COFFEE', 21, 12),
  ('CUSHIONED_CHAIR_BACK', 21, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 22, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 25, 11, WOOD_DARK), ('COFFEE', 25, 12),
  ('CUSHIONED_CHAIR_BACK', 25, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 26, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 21, 15, WOOD_DARK), ('COFFEE', 21, 16),
  ('CUSHIONED_CHAIR_BACK', 21, 17, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 22, 17, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 25, 15, WOOD_DARK), ('COFFEE', 25, 16),
  ('CUSHIONED_CHAIR_BACK', 25, 17, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 26, 17, CAFE_SEAT),
  ('COFFEE_TABLE', 28, 16, WOOD_DARK), ('COFFEE', 28, 16), ('SOFA_SIDE:left', 30, 16, CAFE_SEAT),
  ('PLANT_2', 20, 11), ('BIN', 30, 11),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_GREEN  = {'h': 168, 's': 26, 'b': -44, 'c': -20}

CARPETS = [
  {'variant': 0, 'col': 12, 'row': 3, 'w': 8, 'h': 5, 'color': RUG_VIOLET, 'accent': RUG_GOLD},   # зал
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 4, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 0, 'col': 24, 'row': 2, 'w': 4, 'h': 5, 'color': RUG_GREEN, 'accent': RUG_GOLD},    # правый кабинет
]

PETS = [0, 1]
