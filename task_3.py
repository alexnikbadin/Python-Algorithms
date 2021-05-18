"""
3. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""
import random
SIZE = int(input('Введите нечетное число: '))
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def mediana(n):
    sort_lst = sorted(n)
    lst_len = len(n)
    i = (lst_len-1) // 2
    return (sort_lst[i])

print(mediana(array))