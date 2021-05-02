"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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
print(max_el)
print(min_el)
print(array)
