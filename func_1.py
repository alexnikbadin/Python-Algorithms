"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Задача: поменять минимальное и максимальное число массива местами
"""

import random
import timeit
import cProfile


SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

def func_1(array):
    seq = sorted(array)
    seq[0], seq[-1] = seq[-1], seq[0]
    return seq

print(func_1(array))

# SIZE = 10_000
print(timeit.timeit('func_1(array)', number=100, globals=globals()))  # 0.165067762

cProfile.run('func_1(array)')

"""
5 function calls in 0.001 seconds
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 Lesson_4.py:42(func_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# SIZE = 100_000

print(timeit.timeit('func_1(array)', number=100, globals=globals()))  # 1.381823029

cProfile.run('func_1(array)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
        1    0.000    0.000    0.019    0.019 Lesson_4.py:42(func_1)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        1    0.019    0.019    0.019    0.019 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# SIZE = 1_000_000

print(timeit.timeit('func_1(array)', number=100, globals=globals()))  # 13.715516505

cProfile.run('func_1(array)')

"""
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.158    0.158 <string>:1(<module>)
        1    0.000    0.000    0.154    0.154 Lesson_4.py:42(func_1)
        1    0.000    0.000    0.158    0.158 {built-in method builtins.exec}
        1    0.154    0.154    0.154    0.154 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
"""
Вывод:

timeit:
SIZE = 10_000   0.165067762
SIZE = 100_000   1.381823029
SIZE = 1_000_000   13.715516505

cProfile 5 вызовов:
SIZE = 10_000   tottime 0.001 
SIZE = 100_000   tottime 0.019
SIZE = 1_000_000   tottime 0.154

Максимальные временные затраты на sorted

"""