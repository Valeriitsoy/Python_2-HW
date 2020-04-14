# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

number = array[0]
max_count = 1
s = len(array)
for i in range(s - 1):
    count = 1
    for a in range(i + 1, s):
        if array[i] == array[a]:
            count += 1
    if count > max_count:
        max_count = count
        number = array[i]

if max_count > 1:
    print(f'число {number} встречается чаще всего, {max_count} раз.')
else:
    print("Одинаковых чисел нет")
