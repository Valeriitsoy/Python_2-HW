import timeit
import cProfile


def i_num(n):
    array = []
    for i in range(2, 1000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            array.append(i)
    for index, item in enumerate(array, 1):
        if index == n:
            return f'По индексу {index} простое число {item}'


print(timeit.timeit('i_num(50)', number=100, globals=globals()))  #0.6204102
print(timeit.timeit('i_num(60)', number=100, globals=globals()))  #0.6137082000000001
print(timeit.timeit('i_num(70)', number=100, globals=globals()))  #0.6154668999999999
print(timeit.timeit('i_num(80)', number=100, globals=globals()))  #0.6018986999999998
print(timeit.timeit('i_num(90)', number=100, globals=globals()))  #0.609359


cProfile.run('i_num(50)')
# 172 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2_2.py:5(i_num)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(60)')
# 172 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2_2.py:5(i_num)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(70)')
# 172 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2_2.py:5(i_num)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(80)')
# 172 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2_2.py:5(i_num)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('i_num(90)')
# 172 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_2_2.py:5(i_num)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

