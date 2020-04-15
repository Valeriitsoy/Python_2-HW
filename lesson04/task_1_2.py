# Определить, какое число в массиве встречается чаще всего
import random
import timeit
import cProfile


def most_(n):
    array = [random.randint(0, 100) for _ in range(n)]
    # print(array)
    max_tuple = (0, array[0])
    for element in array:
        count = array.count(element)
        if count > max_tuple[0]:
            max_tuple = (count, element)
    if max_tuple[0] != 1:
        return f'Чаще всех повторяется {max_tuple[1]}, число повторяется {max_tuple[0]} раз(a).'
    else:
        return f'Одинаковых чисел нет'


print(timeit.timeit('most_(1000)', number=100, globals=globals()))  #1.8769949000000001
print(timeit.timeit('most_(2000)', number=100, globals=globals()))  #7.1532176000000005
print(timeit.timeit('most_(3000)', number=100, globals=globals()))  #16.1782679
print(timeit.timeit('most_(4000)', number=100, globals=globals()))  #28.5333505
print(timeit.timeit('most_(5000)', number=100, globals=globals()))  #47.5753119


cProfile.run('most_(100)')
# 631 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_1_2.py:7(most_)
#         1    0.000    0.000    0.001    0.001 task_1_2.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       100    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       126    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(200)')
# 1253 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#       200    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       200    0.000    0.000    0.001    0.000 random.py:244(randint)
#       200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_1_2.py:7(most_)
#         1    0.000    0.000    0.001    0.001 task_1_2.py:8(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       200    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       248    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(300)')
# 1895 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#       300    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       300    0.000    0.000    0.002    0.000 random.py:244(randint)
#       300    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.005    0.005 task_1_2.py:7(most_)
#         1    0.000    0.000    0.002    0.002 task_1_2.py:8(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       300    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       300    0.003    0.000    0.003    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       390    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(400)')
# 2522 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#       400    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       400    0.000    0.000    0.002    0.000 random.py:244(randint)
#       400    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.007    0.007 task_1_2.py:7(most_)
#         1    0.000    0.000    0.002    0.002 task_1_2.py:8(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       400    0.005    0.000    0.005    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       517    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(500)')
# 3139 function calls in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#       500    0.001    0.000    0.002    0.000 random.py:200(randrange)
#       500    0.000    0.000    0.002    0.000 random.py:244(randint)
#       500    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.010    0.010 task_1_2.py:7(most_)
#         1    0.000    0.000    0.002    0.002 task_1_2.py:8(<listcomp>)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       500    0.007    0.000    0.007    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       634    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
