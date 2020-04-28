# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def array(size=10):
    return [round(random.uniform(0, 49), 3) for _ in range(size)]


list_ = array()

print(list_)


def merge_(arr):

    if len(arr) <= 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        left = merge_(arr[:mid])
        right = merge_(arr[mid:])
    return merge(left, right)


def merge(left, right):

    result = []

    left_ = right_ = 0

    while left_ < len(left) and right_ < len(right):
        if left[left_] < right[right_]:
            result.append(left[left_])
            left_ += 1
        else:
            result.append(right[right_])
            right_ += 1

    result.extend(left[left_:])
    result.extend(right[right_:])

    return result


print(merge_(list_))





