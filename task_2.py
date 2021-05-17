"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random
SIZE = 10
MAX_ITEM = 50
array = [round(random.random() * MAX_ITEM, 2) for _ in range(SIZE)]
print(array)

def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len (left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i = i + 1
            else:
                data[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            data[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            data[k] = right_half[j]
            j = j + 1
            k = k + 1
    return data


print(mergeSort(array))
