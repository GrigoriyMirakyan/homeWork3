"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

numbers = [2, 3, 4, 5, 6]


def calculation(arr):
    calc = []
    i = 0
    j = -1
    n = 0
    while i < len(arr) / 2:
        mul_nums = arr[i] * arr[j]
        calc.insert(n, mul_nums)
        i += 1
        j += -1
        n += 1
    return calc


calc_number = calculation(numbers)

print(calc_number)
