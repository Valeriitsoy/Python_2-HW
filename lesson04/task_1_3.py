# Определить, какое число в массиве встречается чаще всего
import random
import timeit
import cProfile


def most_(n):
    array = [random.randint(0, 100) for _ in range(n)]
    #print(array)
    number = sorted([(i, array.count(i)) for i in set(array)], key=lambda a: a[1])[-1]
    return f'Чаще всех повторяется {number[0]}, число повторяется {number[1]} раз(a).'


print(timeit.timeit('most_(1000)', number=100, globals=globals()))  #0.3313162
print(timeit.timeit('most_(2000)', number=100, globals=globals()))  #0.71717
print(timeit.timeit('most_(3000)', number=100, globals=globals()))  #1.01113
print(timeit.timeit('most_(4000)', number=100, globals=globals()))  #1.3218339000000001
print(timeit.timeit('most_(5000)', number=100, globals=globals()))  #1.6703192000000002

cProfile.run('most_(100)')
# 659 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#        60    0.000    0.000    0.000    0.000 task_1_3.py:10(<lambda>)
#         1    0.000    0.000    0.000    0.000 task_1_3.py:10(<listcomp>)
#         1    0.000    0.000    0.001    0.001 task_1_3.py:7(most_)
#         1    0.000    0.000    0.000    0.000 task_1_3.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        60    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       132    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(1000)')
# 5469 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#      1000    0.002    0.000    0.004    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.005    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
#       101    0.000    0.000    0.000    0.000 task_1_3.py:10(<lambda>)
#         1    0.000    0.000    0.003    0.003 task_1_3.py:10(<listcomp>)
#         1    0.000    0.000    0.009    0.009 task_1_3.py:7(most_)
#         1    0.001    0.001    0.005    0.005 task_1_3.py:8(<listcomp>)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       101    0.003    0.000    0.003    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1260    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(10000)')
# 52893 function calls in 0.062 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.062    0.062 <string>:1(<module>)
#     10000    0.013    0.000    0.026    0.000 random.py:200(randrange)
#     10000    0.006    0.000    0.033    0.000 random.py:244(randint)
#     10000    0.010    0.000    0.014    0.000 random.py:250(_randbelow_with_getrandbits)
#       101    0.000    0.000    0.000    0.000 task_1_3.py:10(<lambda>)
#         1    0.000    0.000    0.023    0.023 task_1_3.py:10(<listcomp>)
#         1    0.000    0.000    0.062    0.062 task_1_3.py:7(most_)
#         1    0.006    0.006    0.039    0.039 task_1_3.py:8(<listcomp>)
#         1    0.000    0.000    0.062    0.062 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#     10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#       101    0.023    0.000    0.023    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12684    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(100000)')
# 527028 function calls in 0.645 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.645    0.645 <string>:1(<module>)
#    100000    0.110    0.000    0.230    0.000 random.py:200(randrange)
#    100000    0.055    0.000    0.285    0.000 random.py:244(randint)
#    100000    0.083    0.000    0.120    0.000 random.py:250(_randbelow_with_getrandbits)
#       101    0.000    0.000    0.000    0.000 task_1_3.py:10(<lambda>)
#         1    0.000    0.000    0.302    0.302 task_1_3.py:10(<listcomp>)
#         1    0.002    0.002    0.645    0.645 task_1_3.py:7(most_)
#         1    0.056    0.056    0.340    0.340 task_1_3.py:8(<listcomp>)
#         1    0.000    0.000    0.645    0.645 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#    100000    0.014    0.000    0.014    0.000 {method 'bit_length' of 'int' objects}
#       101    0.302    0.003    0.302    0.003 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126819    0.023    0.000    0.023    0.000 {method 'getrandbits' of '_random.Random' objects}

