"""
http://pythontutor.ru/lessons/2d_arrays/problems/2d_max/

Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,
в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот,
у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""

n, m = [int(i) for i in input().split()]

lst = []
for i in range(n):
    lst.append([int(j) for j in input().split()])

_i = 0
_j = 0
_max = lst[_i][_j]
for i in range(n):
    if max(lst[i]) > _max:
        _max = max(lst[i])
        _i = i
        _j = lst[i].index(_max)

print(_i, _j)
