# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def arr_(m):
    return [random.randint(0, 100) for _ in range(2 * m + 1)]


array_ = arr_(5)
print(array_)


def g_sort(array):
    i = 1
    size = len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


def median(arr):
    print(arr)
    if len(arr) % 2 == 1:
        return f'Медиана = {arr[int(len(arr) / 2)]}'
    else:
        return f'Медиана = {0.5 * (arr[int(len(arr) / 2 - 1)] + arr[int(len(arr) / 2)])}'


print(median(g_sort(array_)))
