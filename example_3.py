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
import collections
import platform


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = collections.deque(random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))

def func_3(array):
    i = array.index(max(array))
    j = array.index(min(array))
    array[i], array[j] = array[j], array[i]
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

print(func_3(array))
show(func_3(array))
print(platform.architecture())

"""
type(obj)=<class 'collections.deque'>, sys.getsizeof(obj)=624, obj=deque([59, 56, 46, 16, 46, 13, 53, 98, 32, 60])
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=59
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=46
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=16
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=46
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=13
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=53
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=98
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=32
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=60
('64bit', '')


Объем памяти занятый <class 'collections.deque'> = 624B
Общий объем памяти занятый <class 'int'> = 280В
Общая объем занятой памяти  = 904B

Процессор Intel Core i5 (64-битный)
Разрядность интепретатора ('64bit', '')

"""