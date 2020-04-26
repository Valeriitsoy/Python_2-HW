import random


def array(size=10):
    return [random.randint(-100, 99) for _ in range(size)]


list_ = array()
print(list_)


def sort_(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(list_)


sort_(list_)
