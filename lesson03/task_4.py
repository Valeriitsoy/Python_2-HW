# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 4
MIN_ITEM = -100
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')


array = []
for line in matrix:
    for i, item in enumerate(line):
        array.append(item)

s = len(array)
max_el = array[0]
min_el = array[0]
for a in range(s):
    if array[a] < min_el:
        min_el = array[a]
    elif array[a] > max_el:
        max_el = array[a]

c = len(matrix[0])
most = min_el - 1
for j in range(c):
    least = max_el + 1
    for e in range(c):
        if matrix[e][j] < least:
            least = matrix[e][j]
    if least > most:
        most = least

print(f'Максимальный элемент среди минимальных {most}')
