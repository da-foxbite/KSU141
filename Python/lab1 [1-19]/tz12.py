# 141, Суптеля Владислав
# Дата: 20.02.20
# 12. Дано значення кута α в градусах (0 ≤ α < 360). Обчислити значення цього ж кута в радіанах, враховуючи,
# що 180 ° = π радіанів. У якості значення π використовувати 3.14.

import math
a = float(input("「a」[в градусах]: "))
print("【{0}】[в радианах] = {1}".format(a, math.radians(a)))
