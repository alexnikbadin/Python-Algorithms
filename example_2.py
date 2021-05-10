"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

"""
import random
import sys
import platform


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for k, v in obj.items():
                show(k)
                show(v)
        else:
            for item in obj:
                show(item)

print(func_2(array))
show(func_2(array))
print(platform.architecture())

"""
type(obj)=<class 'list'>, sys.getsizeof(obj)=184, obj=[37, 100, 62, 91, 71, 7, 65, 91, 33, 20]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=37
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=62
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=91
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=71
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=7
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=65
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=91
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=33
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=20
('64bit', '')

Объем памяти занятый <class 'list'> = 184B
Общий объем памяти занятый <class 'int'> = 280В
Общая объем занятой памяти  = 464B
С точки зрения анализа затрат памяти <class 'list'> самый эффективный (почти в 4 раза меньше чем <class 'set'>
и в 3,4 раза меньше <class 'collections.deque'>)

Процессор Intel Core i5 (64-битный)
Разрядность интепретатора ('64bit', '')

"""