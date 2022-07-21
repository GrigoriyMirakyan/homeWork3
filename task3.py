"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

import math

arr = [1.1, 1.2, 3.1, 5, 10.01]
max = arr[0] - int(arr[0])
min = arr[0] - int(arr[0])
i = 0
while i < len(arr):
    num = arr[i] - int(arr[i])
    if num > max:
        max = num
    if num < min:
        min = num
    i += 1
dif = max - min
d = math.trunc(dif * 100) / 100.0
print(d)


