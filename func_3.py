"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их
Задача: поменять минимальное и максимальное число массива местами
"""

import random
import timeit
import cProfile


SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

def func_3(array):
    i = array.index(max(array))
    j = array.index(min(array))
    array[i], array[j] = array[j], array[i]
    return array

print(func_3(array))

# SIZE = 10_000

print(timeit.timeit('func_3(array)', number=100, globals=globals()))  # 0.05043334699999999

cProfile.run('func_3(array)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 func_3.py:16(func_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

# SIZE = 100_000

print(timeit.timeit('func_3(array)', number=100, globals=globals()))  # 0.39021350499999996

cProfile.run('func_3(array)')

"""
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.000    0.000    0.004    0.004 func_3.py:16(func_3)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

# SIZE = 1_000_000

print(timeit.timeit('func_3(array)', number=100, globals=globals()))  # 3.7304157799999995

cProfile.run('func_3(array)')

"""
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
        1    0.000    0.000    0.042    0.042 func_3.py:16(func_3)
        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
        1    0.022    0.022    0.022    0.022 {built-in method builtins.max}
        1    0.020    0.020    0.020    0.020 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

"""
Вывод:

timeit:
SIZE = 10_000   0.05043334699999999
SIZE = 100_000   0.39021350499999996
SIZE = 1_000_000   3.7304157799999995

cProfile:
SIZE = 10_000   tottime 0.000
SIZE = 100_000   tottime 0.004
SIZE = 1_000_000   tottime 0.042

Максимальные временные затраты на функции min и max

"""
