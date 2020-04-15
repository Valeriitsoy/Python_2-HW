# ВЫВОД Квадратичная сложность, код быстрее чем второй (во втором коде
# функция append срабатывает много раз)
import timeit
import cProfile


def i_num(n):
    sieve = [i for i in range(1000)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    # print(res)
    for index, item in enumerate(res, 1):
        if index == n:
            return f'По индексу {index} простое число {item}'


print(timeit.timeit('i_num(400)', number=100, globals=globals()))  #0.1185379
print(timeit.timeit('i_num(500)', number=100, globals=globals()))  #0.22518080000000001
print(timeit.timeit('i_num(600)', number=100, globals=globals()))  #0.32121869999999997
print(timeit.timeit('i_num(700)', number=100, globals=globals()))  #0.40761749999999997
print(timeit.timeit('i_num(800)', number=100, globals=globals()))  #0.5095604999999999

cProfile.run('i_num(400)')
# 6 function calls in 0.029 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.029    0.029 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 task_2.py:14(<listcomp>)
#         1    0.001    0.001    0.026    0.026 task_2.py:5(i_num)
#         1    0.010    0.010    0.010    0.010 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(500)')
# 6 function calls in 0.017 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.017    0.017 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.015    0.015 task_2.py:5(i_num)
#         1    0.006    0.006    0.006    0.006 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(600)')
# 6 function calls in 0.016 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.016    0.016 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.014    0.014 task_2.py:5(i_num)
#         1    0.006    0.006    0.006    0.006 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(700)')
# 6 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.015    0.015 <string>:1(<module>)
#         1    0.007    0.007    0.007    0.007 task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.013    0.013 task_2.py:5(i_num)
#         1    0.005    0.005    0.005    0.005 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(800)')
# 6 function calls in 0.013 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.013    0.013 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.012    0.012 task_2.py:5(i_num)
#         1    0.005    0.005    0.005    0.005 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
