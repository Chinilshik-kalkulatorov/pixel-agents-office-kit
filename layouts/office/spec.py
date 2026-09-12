# OFFICE v7 — 29 x 20 = 580. Поверх v6:
#   * КУХНЯ — точь-в-точь как в большом офисе (фото): полка над стойкой, подвесные растения по бокам двери,
#     стойка с проходом бариста слева, диван с журнальным столиком слева внизу, четыре столика, растения справа.
#     Дверь из зала в кухню ужата до одной клетки (колонка 17), чтобы полка встала на своё место.
#   * КАБИНЕТ CEO = ЛЕВЫЙ (синий): диван на двоих слева с журнальным столиком, рабочая зона справа сверху
#     (золотое кресло, два монитора, кружка, урна), гостевое кресло, свой фиолетовый ковёр, растения.
#   * ЗАЛ и ПРАВЫЙ КАБИНЕТ возвращены как были в v5 (зал с горизонтальным столом; правый — стол боком,
#     хозяин и гость друг напротив друга, диван с журнальным столиком, зелёная стена).
#
# rows: 0 стена | 1-9 верх (ряд 9 скрыт) | 10 стена с дверями | 11-18 низ (ряд 18 скрыт) | 19 стена + вход
# cols верх: CEO 1-8 | стена 9 | ЗАЛ 10-19 | стена 20 | КАБИНЕТ 21-27 | стена 28
# cols низ:  рабочая 1-11 | стена 12 | ресепшн 13-15 | стена 16 | кухня 17-27 | стена 28
MAP = """
#############################
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#cccccccc#EEEEEEEEEE#mmmmmmm#
#######cc#####EE#E####mm#####
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssssLLLL#bbbbbbbbbbb#
#sssssssssssLLLLbbbbbbbbbbbb#
#sssssssssss#LLLbbbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
##############LL#############
"""

ESPRESSO = {'h': 24, 's': 20, 'b': -50, 'c': -82}   # зал
WALNUT   = {'h': 26, 's': 18, 'b': -38, 'c': -84}   # кабинеты
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
WALL_COLORS = {'E': VIOLET_WALL, 'c': NAVY_WALL, 'm': GREEN_WALL, 'L': CHARCOAL, 's': CHARCOAL, 'b': CREAM_WALL}

WOOD_DARK  = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER    = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ===== КАБИНЕТ CEO (левый, cols 1-8) — доработан: диван на двоих слева, рабочая зона справа сверху
  ('DOUBLE_BOOKSHELF', 1, -1), ('LARGE_PAINTING', 3, -1), ('CLOCK', 5, -1), ('SMALL_PAINTING_2', 7, -1),
  ('CUSHIONED_CHAIR_FRONT', 6, 1, GOLD_SEAT),
  ('DESK_FRONT', 5, 2, WOOD_DARK), ('PC_BACK', 5, 2), ('PC_BACK', 6, 2), ('COFFEE', 7, 3),
  ('CUSHIONED_CHAIR_BACK', 6, 4, VELVET_GRN),
  ('SOFA_SIDE', 1, 3, COGNAC), ('COFFEE_TABLE', 2, 3, WOOD_DARK), ('COFFEE', 3, 3),
  ('LARGE_PLANT', 7, 5), ('PLANT_2', 1, 6), ('BIN', 8, 4),
  # ===== ЗАЛ (cols 10-19) — как было
  ('DOUBLE_BOOKSHELF', 10, -1), ('LARGE_PAINTING', 12, -1), ('CLOCK', 15, -1),
  ('LARGE_PAINTING', 16, -1), ('DOUBLE_BOOKSHELF', 18, -1),
  ('TABLE_FRONT', 12, 3, WOOD_DARK), ('TABLE_FRONT', 15, 3, WOOD_DARK),
  ('PC_SIDE', 12, 3), ('PC_SIDE:left', 17, 3),
  ('CUSHIONED_CHAIR_FRONT', 13, 2, LEATHER), ('CUSHIONED_CHAIR_FRONT', 16, 2, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 13, 7, LEATHER), ('CUSHIONED_CHAIR_BACK', 16, 7, LEATHER),
  ('CUSHIONED_CHAIR_SIDE', 11, 5, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 18, 5, LEATHER),
  ('LARGE_PLANT', 10, 6), ('LARGE_PLANT', 18, 6),
  # ===== ПРАВЫЙ КАБИНЕТ (cols 21-27) — как был: стол боком, хозяин и гость друг напротив друга
  ('WHITEBOARD', 21, -1), ('LARGE_PAINTING', 24, -1), ('CLOCK', 27, -1),
  ('DESK_SIDE', 23, 2, WOOD_DARK), ('PC_SIDE:left', 23, 3),
  ('CUSHIONED_CHAIR_SIDE:left', 24, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 22, 4, VELVET_GRN),
  ('SOFA_FRONT', 26, 5, COGNAC), ('COFFEE_TABLE', 26, 6, WOOD_DARK), ('COFFEE', 27, 6),
  ('LARGE_PLANT', 21, 6), ('PLANT_2', 27, 1), ('BIN', 21, 2),
  # ===== РАБОЧАЯ КОМНАТА (cols 1-11) — шесть компьютеров, правые столы упёрты в стену
  ('SMALL_PAINTING', 1, 9), ('WHITEBOARD', 2, 9), ('HANGING_PLANT', 5, 9), ('CLOCK', 6, 9),
  ('HANGING_PLANT', 9, 9), ('WHITEBOARD', 10, 9),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 2, 11), ('CUSHIONED_CHAIR_BACK', 2, 13, STAFF_SEAT),
  ('DESK_FRONT', 4, 11), ('PC_FRONT_OFF', 5, 11), ('CUSHIONED_CHAIR_BACK', 5, 13, STAFF_SEAT),
  ('DESK_FRONT', 9, 11), ('PC_FRONT_OFF', 10, 11), ('CUSHIONED_CHAIR_BACK', 10, 13, STAFF_SEAT),
  ('DESK_FRONT', 1, 14), ('PC_FRONT_OFF', 2, 14), ('CUSHIONED_CHAIR_BACK', 2, 16, STAFF_SEAT),
  ('DESK_FRONT', 4, 14), ('PC_FRONT_OFF', 5, 14), ('CUSHIONED_CHAIR_BACK', 5, 16, STAFF_SEAT),
  ('DESK_FRONT', 9, 14), ('PC_FRONT_OFF', 10, 14), ('CUSHIONED_CHAIR_BACK', 10, 16, STAFF_SEAT),
  ('PLANT', 7, 16), ('BIN', 8, 17),
  # ===== РЕСЕПШН (cols 13-15) — стойка во всю ширину, диван владельца, ковёр
  ('SMALL_PAINTING', 13, 9),
  ('PLANT_2', 13, 11),
  ('CUSHIONED_CHAIR_FRONT', 14, 12, LEATHER),
  ('DESK_FRONT', 13, 13, WOOD_DARK), ('PC_BACK', 14, 13),
  ('SOFA_SIDE', 13, 15, CAFE_SEAT),
  # ===== КУХНЯ (cols 17-27) — точь-в-точь как в большом офисе
  ('BOOKSHELF', 18, 10), ('HANGING_PLANT', 21, 9), ('HANGING_PLANT', 24, 9), ('LARGE_PAINTING', 26, 9),
  ('DESK_SIDE', 18, 11, WOOD_DARK), ('COFFEE', 18, 12), ('COFFEE', 18, 14),
  ('WOODEN_BENCH', 19, 12), ('WOODEN_BENCH', 19, 14),
  ('SMALL_TABLE_FRONT', 20, 11, WOOD_DARK), ('COFFEE', 21, 12),
  ('CUSHIONED_CHAIR_BACK', 20, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 21, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 24, 11, WOOD_DARK), ('COFFEE', 24, 12),
  ('CUSHIONED_CHAIR_BACK', 24, 13, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 25, 13, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 20, 15, WOOD_DARK), ('COFFEE', 20, 16),
  ('CUSHIONED_CHAIR_BACK', 20, 17, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 21, 17, CAFE_SEAT),
  ('SMALL_TABLE_FRONT', 24, 15, WOOD_DARK), ('COFFEE', 25, 16),
  ('CUSHIONED_CHAIR_BACK', 24, 17, CAFE_SEAT), ('CUSHIONED_CHAIR_BACK', 25, 17, CAFE_SEAT),
  ('SOFA_SIDE', 17, 15, CAFE_SEAT), ('COFFEE_TABLE', 18, 15, WOOD_DARK), ('COFFEE', 19, 15),
  ('PLANT_2', 27, 11), ('LARGE_PLANT', 26, 15), ('BIN', 19, 17),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_GREEN  = {'h': 168, 's': 26, 'b': -44, 'c': -20}
RUG_SILVER = {'h': 220, 's': 10, 'b': 15, 'c': 0}

CARPETS = [
  {'variant': 0, 'col': 5, 'row': 1, 'w': 3, 'h': 4, 'color': RUG_VIOLET, 'accent': RUG_GOLD},    # CEO — свой цвет
  {'variant': 0, 'col': 11, 'row': 3, 'w': 8, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},     # зал
  {'variant': 0, 'col': 22, 'row': 2, 'w': 4, 'h': 5, 'color': RUG_GREEN, 'accent': RUG_GOLD},    # правый кабинет
  {'variant': 2, 'col': 13, 'row': 15, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_SILVER},  # ковёр администратора
]

PETS = [0, 1]
