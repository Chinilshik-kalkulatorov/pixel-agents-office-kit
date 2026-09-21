# OFFICE v9 — 29 x 20 = 580. Поверх v8 по указу 09-21:
#   1. ПЕРЕГОВОРНАЯ переехала из правой комнаты (22-27) в центральную (10-20), на место CEO-люкса. Сдвиг ровно на 10 колонок
#      влево: ось стола/часов/кресла во главе = колонка 15 = ось комнаты. Ряды те же. Ковёр растянут на всю ширину комнаты
#      (10-20 x 2-7). Всё содержимое CEO-люкса удалено (ковёр, стол, кресла, лаунжи, шкафы, картины, часы, растения).
#   2. ПРАВАЯ КОМНАТА (22-27, ряды 1-9) очищена: только пол, стены и двери.
#   3. РАБОЧАЯ: все шесть столов с мониторами и креслами сдвинуты на ряд вниз (Y+1).
#      Растение и урна убраны из прохода 7-8 (иначе нижние кресла заперты). Картина переговорной на (17,-1): доска 12-13 и картина 17-18
#      зеркальны вокруг часов 15.
#   Y-диапазоны указа (10–28, 9–17) на сетке 29x20 невозможны; пункт 2 прочитан по заголовку: правая ВЕРХНЯЯ комната. Кухня не тронута.
#   Стены, двери, полы, ресепшн, кухня, CTO — без изменений.
#
# rows: 0 стена | 1-9 верх (ряд 9 скрыт) | 10 стена с дверями | 11-18 низ (ряд 18 скрыт) | 19 стена + вход
# cols верх: CTO 1-8 | стена 9 | ПЕРЕГОВОРНАЯ 10-20 | стена 21 | пустая комната 22-27 | стена 28
# cols низ:  рабочая 1-11 | стена 12 | ресепшн 13-15 | стена 16 | кухня 17-27 | стена 28
# двери: CTO→рабочая 7-8 · переговорная→ресепшн 14-15 (выход администратора) · переговорная↔правая (21, 2-3) ·
#        правая→кухня 22-23 · ресепшн↔рабочая (12, 14-15) · ресепшн↔кухня (16, 14-15) · с улицы 14-15
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
  # ===== ПЕРЕГОВОРНАЯ (cols 10-20) — перенесена из правой комнаты сдвигом на 10 колонок влево, ряды те же
  ('WHITEBOARD', 12, -1), ('CLOCK', 15, -1), ('LARGE_PAINTING', 17, -1),
  ('TABLE_FRONT', 14, 3, WOOD_DARK), ('PC_SIDE', 14, 3), ('PC_SIDE:left', 16, 3),
  ('CUSHIONED_CHAIR_SIDE', 13, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE', 13, 6, LEATHER),
  ('CUSHIONED_CHAIR_SIDE:left', 17, 4, LEATHER), ('CUSHIONED_CHAIR_SIDE:left', 17, 6, LEATHER),
  ('CUSHIONED_CHAIR_FRONT', 15, 2, LEATHER),
  ('PLANT', 12, 6), ('PLANT_2', 17, 7),
  # ===== ПРАВАЯ КОМНАТА (cols 22-27) — пустая: только пол, стены, двери
  # ===== РАБОЧАЯ КОМНАТА (cols 1-11) — столы, мониторы и кресла сдвинуты на ряд вниз (v9)
  ('SMALL_PAINTING', 1, 9), ('WHITEBOARD', 2, 9), ('HANGING_PLANT', 5, 9), ('CLOCK', 6, 9),
  ('HANGING_PLANT', 9, 9), ('WHITEBOARD', 10, 9),
  ('DESK_FRONT', 1, 12), ('PC_FRONT_OFF', 2, 12), ('CUSHIONED_CHAIR_BACK', 2, 14, STAFF_SEAT),
  ('DESK_FRONT', 4, 12), ('PC_FRONT_OFF', 5, 12), ('CUSHIONED_CHAIR_BACK', 5, 14, STAFF_SEAT),
  ('DESK_FRONT', 9, 12), ('PC_FRONT_OFF', 10, 12), ('CUSHIONED_CHAIR_BACK', 10, 14, STAFF_SEAT),
  ('DESK_FRONT', 1, 15), ('PC_FRONT_OFF', 2, 15), ('CUSHIONED_CHAIR_BACK', 2, 17, STAFF_SEAT),
  ('DESK_FRONT', 4, 15), ('PC_FRONT_OFF', 5, 15), ('CUSHIONED_CHAIR_BACK', 5, 17, STAFF_SEAT),
  ('DESK_FRONT', 9, 15), ('PC_FRONT_OFF', 10, 15), ('CUSHIONED_CHAIR_BACK', 10, 17, STAFF_SEAT),
  ('PLANT', 4, 10), ('BIN', 11, 17),   # были в проходе (7,16)/(8,17): после сдвига столов запирали нижний ряд кресел. Растение → единственная чистая клетка у стены; урна → глухой угол того же ряда
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
  {'variant': 2, 'col': 2, 'row': 2, 'w': 5, 'h': 5, 'color': RUG_NAVY, 'accent': RUG_GOLD},      # CTO
  {'variant': 2, 'col': 10, 'row': 2, 'w': 11, 'h': 6, 'color': RUG_NAVY, 'accent': RUG_SILVER},  # переговорная — во всю ширину комнаты; variant 2: кант внутри тайла, не торчит в дверь (21,2)
  {'variant': 2, 'col': 13, 'row': 15, 'w': 3, 'h': 3, 'color': RUG_NAVY, 'accent': RUG_SILVER},  # ковёр администратора
]

PETS = [0, 1]
