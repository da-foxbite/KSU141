# 141, Суптеля Владислав
# 【Дата】:「09.03.20」
# 12. Дана послідовність натуральних чисел (одне число в рядку), що завершується числом 0.
# Виведіть перше, третє, п'яте і т.д. з введених чисел. Завершальний нуль виводити не потрібно.

def oddRev(x, i):
    if i >= 0:
        oddRev(x, i-1)                            # i -> счётчик; -1 из-за последнего элемента (0)
        if i % 2 == 0:
            print(x[i])
x = []
a = int(input("「Введите число」: "))
while a != 0:
    x.append(a)                                   # вносим в массив
    a = int(input("「Введите число」: "))         # второй input чтобы while работал
oddRev(x, len(x)-1)                               # не учитываем последний элемент (ноль)
