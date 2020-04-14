# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_e = 0
min_e = 0
s = len(array)
for i in range(s):
    if array[i] < array[min_e]:
        min_e = i
    elif array[i] > array[max_e]:
        max_e = i
print(f'мин элемент {array[min_e]} (инд {min_e + 1}), макс элемент {array[max_e]} (инд {max_e + 1})')

spam = array[min_e]
array[min_e] = array[max_e]
array[max_e] = spam

print(array)
