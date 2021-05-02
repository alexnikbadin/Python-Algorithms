"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20 # взял 20 чтобы вероятность наличия повторов была выше
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_set = set(array)

mst_frqt = None
amount_mst_frqt = 0

for el in array_set:
    amount = array.count(el)
    if amount > amount_mst_frqt:
        amount_mst_frqt = amount
        mst_frqt = el

print(mst_frqt)