"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = -5
b = -1

for i, el in enumerate(array):
    if a < el < 0:
        a = el
        b = i
print(f'Максимальное отрицательное число = {a}, а его индекс: {b}')




