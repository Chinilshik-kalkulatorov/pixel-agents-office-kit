# OFFICE v8 — 29 x 20 = 580. Поверх v7 по указу 09-14:
#   * ВЕРХ = верх БОЛЬШОГО офиса (35x25), ужатый в 29: CTO (синий) 1-8 | CEO-люкс (фиолет) 10-20 | переговорная (фиолет) 22-27.
#     CTO и переговорная — как в большом; CEO — стол лицом в комнату на фиолетовом ковре, два гостя, две лаунж-группы
#     по бокам (диван + столик с кружкой + два золотых кресла), растения у стены по бокам кресла CEO.
#   * КУХНЯ: верхняя стена как в большом — полка 18-19 | растение 21 | ДВЕРЬ 22-23 | растение 24 | картина 26-27.
#     Кривая дверь в углу (колонка 17) закрыта.
#   * РУЧНЫЕ ПРАВКИ ВЛАДЕЛЬЦА из живого layout.json: дверь рабочая↔ресепшн поднята на ряды 14-15; стойка администратора
#     на ряд 12 (занимает 13). Дверь 14-15 сверху ОТКРЫТА ЗАНОВО как дверь CEO→ресепшн (иначе администратор заперт:
#     стойка во всю ширину, живой файл INVALID).
#   * Правило цвета стен на стыках исправлено в office_kit (S, E, W, SE, SW, N) — пятна над рабочей ушли.
#
# rows: 0 стена | 1-9 верх (ряд 9 скрыт) | 10 стена с дверями | 11-18 низ (ряд 18 скрыт) | 19 стена + вход
# cols верх: CTO 1-8 | стена 9 | CEO 10-20 | стена 21 | переговорная 22-27 | стена 28
# cols низ:  рабочая 1-11 | стена 12 | ресепшн 13-15 | стена 16 | кухня 17-27 | стена 28
# двери: CTO→рабочая 7-8 · CEO→ресепшн 14-15 (выход администратора) · CEO↔переговорная (21, 2-3) · переговорная→кухня 22-23 · ресепшн↔рабочая (12, 14-15) ·
#        ресепшн↔кухня (16, 14-15) — вровень с левой · с улицы 14-15
MAP = """
#############################
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEEEmmmmmm#
#cccccccc#EEEEEEEEEEEEmmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#cccccccc#EEEEEEEEEEE#mmmmmm#
#######cc#####EE######mm#####
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#ssssssssssssLLLbbbbbbbbbbbb#
#sssssssssssLLLLbbbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
#sssssssssss#LLL#bbbbbbbbbbb#
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
GREEN_WALL  = {'h': 168, 's': 30, 'b': -78, 'c': -45}   # не используется в v8 (переговорная = фиолет, как в большом)
CHARCOAL    = {'h': 220, 's': 12, 'b': -85, 'c': -40}
CREAM_WALL  = {'h': 38, 's': 18, 'b': -22, 'c': -55}
WALL_COLOR = CHARCOAL
WALL_COLORS = {'E': VIOLET_WALL, 'c': NAVY_WALL, 'm': VIOLET_WALL, 'L': CHARCOAL, 's': CHARCOAL, 'b': CREAM_WALL}
WALL_TILE_COLORS = {(16, 10): CREAM_WALL}   # шапка стены ресепшн|кухня: соседняя дверь 14-15 красила её в фиолет

WOOD_DARK  = {'h': 0, 's': -10, 'b': -22, 'c': 12}
LEATHER    = {'h': 265, 's': 10, 'b': -24, 'c': 20, 'colorize': True}
COGNAC     = {'h': 25, 's': 32, 'b': -22, 'c': 15, 'colorize': True}
GOLD_SEAT  = {'h': 40, 's': 38, 'b': -20, 'c': 12, 'colorize': True}
VELVET_GRN = {'h': 160, 's': 26, 'b': -32, 'c': 8, 'colorize': True}
STAFF_SEAT = {'h': 222, 's': 16, 'b': -14, 'c': 0, 'colorize': True}
CAFE_SEAT  = {'h': 20, 's': 40, 'b': -20, 'c': 8, 'colorize': True}

FURNITURE = [
  # ===== CTO (cols 1-8) — как в большом офисе
  ('DOUBLE_BOOKSHELF', 1, -1), ('WHITEBOARD', 4, -1), ('CLOCK', 7, -1),
  ('DESK_FRONT', 3, 3, WOOD_DARK), ('PC_BACK', 4, 3),
  ('CUSHIONED_CHAIR_FRONT', 4, 2, LEATHER),
  ('CUSHIONED_CHAIR_BACK', 4, 5, VELVET_GRN),
  ('CUSHIONED_CHAIR_SIDE', 1, 7, VELVET_GRN), ('COFFEE_TABLE', 2, 7, WOOD_DARK), ('COFFEE', 3, 7),
  ('LARGE_PLANT', 7, 5), ('BIN', 7, 4), ('PLANT_2', 1, 1),
  # ===== CEO-люкс (cols 10-20) — большой офис, ужатый с 15 до 11 колонок
  # стена: шкаф 10-11 | картина 12-13 | [14] | часы 15 | [16] | картина 17-18 | шкаф 19-20
  ('DOUBLE_BOOKSHELF', 10, -1), ('LARGE_PAINTING', 12, -1), ('CLOCK', 15, -1),
  ('LARGE_PAINTING', 17, -1), ('DOUBLE_BOOKSHELF', 19, -1),
  ('PLANT', 14, 0), ('PLANT', 16, 0),   # у стены по бокам кресла CEO, стена над ними пустая
  ('CUSHIONED_CHAIR_FRONT', 15, 2, GOLD_SEAT),
  ('TABLE_FRONT', 14, 3, WOOD_DARK), ('PC_BACK', 15, 3), ('COFFEE', 16, 5),
  ('CUSHIONED_CHAIR_BACK', 14, 7, COGNAC), ('CUSHIONED_CHAIR_BACK', 16, 7, COGNAC),
  # лаунж слева: диван у стены, столик с кружкой, два золотых кресла под столиком
  ('SOFA_SIDE', 10, 4, COGNAC), ('COFFEE_TABLE', 11, 4, WOOD_DARK), ('COFFEE', 12, 4),
  ('CUSHIONED_CHAIR_BACK', 11, 6, GOLD_SEAT), ('CUSHIONED_CHAIR_BACK', 12, 6, GOLD_SEAT),
  # лаунж справа — зеркально
  ('COFFEE_TABLE', 18, 4, WOOD_DARK), ('COFFEE', 18, 4), ('SOFA_SIDE:left', 20, 4, COGNAC),
  ('CUSHIONED_CHAIR_BACK', 18, 6, GOLD_SEAT), ('CUSHIONED_CHAIR_BACK', 19, 6, GOLD_SEAT),
  ('PLANT', 10, 7), ('PLANT_2', 20, 7),
  # ===== ПЕРЕГОВОРНАЯ (cols 22-27) — как в большом, ужата с 8 до 6 колонок
  ('WHITEBOARD', 22, -1), ('CLOCK', 25, -1), ('LARGE_PAINTING', 26, -1),
  ('TABLE_FRONT', 24, 3, WOOD_DARK), ('PC_SIDE', 24, 3), ('PC_SIDE:left', 26, 3),
  ('CUSHIONED_CHAIR_SIDE', 23, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 23, 6, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 27, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 27, 6, LEATHER),
  ('CUSHIONED_CHAIR_FRONT', 25, 2, LEATHER),
  ('PLANT', 22, 6), ('PLANT_2', 27, 7),
  # ===== РАБОЧАЯ КОМНАТА (cols 1-11) — без изменений (v7)
  ('SMALL_PAINTING', 1, 9), ('WHITEBOARD', 2, 9), ('HANGING_PLANT', 5, 9), ('CLOCK', 6, 9),
  ('HANGING_PLANT', 9, 9), ('WHITEBOARD', 10, 9),
  ('DESK_FRONT', 1, 11), ('PC_FRONT_OFF', 2, 11), ('CUSHIONED_CHAIR_BACK', 2, 13, STAFF_SEAT),
  ('DESK_FRONT', 4, 11), ('PC_FRONT_OFF', 5, 11), ('CUSHIONED_CHAIR_BACK', 5, 13, STAFF_SEAT),
  ('DESK_FRONT', 9, 11), ('PC_FRONT_OFF', 10, 11), ('CUSHIONED_CHAIR_BACK', 10, 13, STAFF_SEAT),
  ('DESK_FRONT', 1, 14), ('PC_FRONT_OFF', 2, 14), ('CUSHIONED_CHAIR_BACK', 2, 16, STAFF_SEAT),
  ('DESK_FRONT', 4, 14), ('PC_FRONT_OFF', 5, 14), ('CUSHIONED_CHAIR_BACK', 5, 16, STAFF_SEAT),
  ('DESK_FRONT', 9, 14), ('PC_FRONT_OFF', 10, 14), ('CUSHIONED_CHAIR_BACK', 10, 16, STAFF_SEAT),
  ('PLANT', 7, 16), ('BIN', 8, 17),
  # ===== РЕСЕПШН (cols 13-15) — стойка на ряду 12 (ручная правка владельца), диван владельца, ковёр
  ('SMALL_PAINTING', 13, 9),
  ('PLANT_2', 13, 11),
  ('CUSHIONED_CHAIR_FRONT', 14, 12, LEATHER),
  ('DESK_FRONT', 13, 12, WOOD_DARK), ('PC_BACK', 14, 12),
  ('SOFA_SIDE', 13, 15, CAFE_SEAT),
  # ===== КУХНЯ (cols 17-27) — точь-в-точь буфет большого офиса (без изменений v7)
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
  ('SOFA_SIDE', 17, 16, CAFE_SEAT), ('COFFEE_TABLE', 18, 16, WOOD_DARK), ('COFFEE', 19, 16),
  ('PLANT_2', 27, 11), ('LARGE_PLANT', 26, 15), ('BIN', 22, 17),
]

RUG_VIOLET = {'h': 265, 's': 36, 'b': -36, 'c': -22}
RUG_GOLD   = {'h': 42, 's': 55, 'b': 12, 'c': 0}
RUG_NAVY   = {'h': 228, 's': 28, 'b': -42, 'c': -20}
RUG_SILVER = {'h': 220, 's': 10, 'b': 15, 'c': 0}

CARPETS = [
  {'variant': 0, 'col': 13, 'row': 2, 'w': 5, 'h': 6, 'color': RUG_VIOLET, 'accent': RUG_GOLD},   # CEO — рабочая зона
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 0, 'col': 23, 'row': 2, 'w': 5, 'h': 6, 'color': RUG_NAVY, 'accent': RUG_SILVER},   # переговорная
  {'variant': 2, 'col': 13, 'row': 15, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_SILVER},  # ковёр администратора
]

PETS = [0, 1]
