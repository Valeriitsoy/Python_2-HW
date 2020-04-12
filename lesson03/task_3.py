# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

s = len(array)
if array[0] > array[1]:
    first = 0
    second = 1
else:
    first = 1
    second = 0
for i in range(2, s):
    if array[i] < array[first]:
        spam = first
        first = i
        if array[spam] < array[second]:
            second = spam
    elif array[i] < array[second]:
        second = i
print(f'Минимальные числа в массиве {array[first]} (индекс {first + 1}) и {array[second]} (индекс {second + 1})')
