# Определить, какое число в массиве встречается чаще всего
# ВЫВОД. Мой первый код самый долгий, квадратичная сложность. Самый быстрый код
# получилось реализовать только в третьем варианте кода, линейная сложность.
import random
import timeit
import cProfile


def most_(n):
    array = [random.randint(0, 100) for _ in range(n)]
    # print(array)
    number = array[0]
    max_count = 1
    s = len(array)
    for i in range(s):
        count = 1
        for a in range(i + 1, s):
            if array[i] == array[a]:
                count += 1
        if count > max_count:
            max_count = count
            number = array[i]
    if max_count > 1:
        return f'число {number} встречается чаще всего, {max_count} раз(a).'
    else:
        return f'Одинаковых чисел нет'


print(timeit.timeit('most_(1000)', number=100, globals=globals()))  #7.597839
print(timeit.timeit('most_(2000)', number=100, globals=globals()))  #30.5362104
print(timeit.timeit('most_(3000)', number=100, globals=globals()))  #72.53979380000001
print(timeit.timeit('most_(4000)', number=100, globals=globals()))  #127.63803689999999
print(timeit.timeit('most_(5000)', number=100, globals=globals()))  #200.60876670000002


cProfile.run('most_(100)')
# 536 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.001    0.001    0.001    0.001 task_1.py:7(most_)
#         1    0.000    0.000    0.000    0.000 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       130    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(200)')
# 1063 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#       200    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       200    0.000    0.000    0.001    0.000 random.py:244(randint)
#       200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.003    0.003    0.003    0.003 task_1.py:7(most_)
#         1    0.000    0.000    0.001    0.001 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       257    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(300)')
# 1600 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#       300    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       300    0.000    0.000    0.001    0.000 random.py:244(randint)
#       300    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.006    0.006    0.007    0.007 task_1.py:7(most_)
#         1    0.000    0.000    0.001    0.001 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       300    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       394    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(400)')
# 2106 function calls in 0.013 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#       400    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       400    0.000    0.000    0.001    0.000 random.py:244(randint)
#       400    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.012    0.012    0.013    0.013 task_1.py:7(most_)
#         1    0.000    0.000    0.001    0.001 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       500    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('most_(500)')
# 2644 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#       500    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       500    0.000    0.000    0.001    0.000 random.py:244(randint)
#       500    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.023    0.023    0.025    0.025 task_1.py:7(most_)
#         1    0.000    0.000    0.002    0.002 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       638    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
