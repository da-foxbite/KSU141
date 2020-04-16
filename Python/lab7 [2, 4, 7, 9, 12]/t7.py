# 141, Суптеля Владислав
# 【Дата】:「19.03.20」
# 7. У списку чисел перевірити, чи всі елементи є унікальними, тобто кожне число зустрічається тільки один раз.
from random import randint

var = [randint(1, 24) for i in range(8)]
print(var)
setvar = set(var)
if len(var) == len(setvar):
    print("Все элементы уникальны.")
else:
    print("В списке имеются дубликаты.")
# 1) с помощью set() преобразуем список в множество
# 2) множество не содержит дубликаты элементов
# 3) ???
# 4) profit

# "стандартное решение":
# for i in range(8-1):
#     for j in range(i+1, 8):
#         if var[i] == var[j]:
#             print("В списке имеются дубликаты.")
#             quit()
# print("Все элементы уникальны.")
