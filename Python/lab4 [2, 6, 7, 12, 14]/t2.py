# 141, Суптеля Владислав
# 【Дата】:「09.03.20」
# 2. Дано перший член і знаменник геометричної прогресії.
# Написати рекурсивну функцію знаходження n-го члена прогресії і знаходження суми n перших членів прогресії.

a, q, n = map(int, input("「Начальный элемент」,「Коэффициент」,「Номер искомого элемента」: ").split())
def geomrec(a,q,n,S):
    if n == 1:
        S += a                            # добавляем начальный эл в сумму
        return a, S
    else:
        temp, S = geomrec(a, q, n-1, S)   # нач эл, коеф, пред перед искомым эл, сумма; temp == a
        temp *= q                         # умножаем полученный из предыдущего temp эл на коеф
        S += temp                         # заносим
        return temp, S
S = 0
A, S = geomrec(a,q,n,S)
print(S)                                  # сумма
print(A)                                  # искомый элемент
