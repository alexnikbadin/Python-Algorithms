"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Задача: поменять минимальное и максимальное число массива местами
"""

import random
import timeit
import cProfile


SIZE = 1000000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def func_2(array):
    max_el = 0
    min_el = 100
    for i, el in enumerate(array):
        if el > max_el:
            max_el = el
            a = i
        elif el < min_el:
            min_el = el
            b = i
    array[a], array[b] = array[b], array[a]
    return array

print(func_2(array))

# SIZE = 10_000
print(timeit.timeit('func_2(array)', number=100, globals=globals()))  # 0.09846482899999999

cProfile.run('func_2(array)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 func_2.py:17(func_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# SIZE = 100_000
print(timeit.timeit('func_2(array)', number=100, globals=globals()))  # 0.889030703

cProfile.run('func_2(array)')

"""
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.008    0.008    0.008    0.008 func_2.py:17(func_2)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# SIZE = 1_000_000

print(timeit.timeit('func_2(array)', number=100, globals=globals()))  # 8.801442241

cProfile.run('func_2(array)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.084    0.084 <string>:1(<module>)
        1    0.084    0.084    0.084    0.084 func_2.py:17(func_2)
        1    0.000    0.000    0.084    0.084 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Вывод:

timeit:
SIZE = 10_000   0.09846482899999999
SIZE = 100_000   0.889030703
SIZE = 1_000_000   8.801442241

cProfile 4 вызова:
SIZE = 10_000   tottime 0.001 
SIZE = 100_000   tottime 0.008
SIZE = 1_000_000   tottime 0.084

"""