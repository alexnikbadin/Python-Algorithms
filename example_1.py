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

def func_1(array):
    seq = sorted(array)
    seq[0], seq[-1] = seq[-1], seq[0]
    return set(seq)

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


print(func_1(array))
show(func_1(array))
print(platform.architecture())

"""
type(obj)=<class 'set'>, sys.getsizeof(obj)=728, obj={37, 42, 12, 46, 49, 55, 88, 57, 92, 95}
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=37
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=46
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=49
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=55
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=88
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=57
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=92
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=95
('64bit', '')

Объем памяти занятый <class 'set'> = 728B
Общий объем памяти занятый <class 'int'> = 280В
Общая объем занятой памяти  = 1008B
С точки зрения анализа затрат памяти <class 'set'> самый затратный (почти в 4 раза больше чем <class 'list'>)

Процессор Intel Core i5 (64-битный)
Разрядность интепретатора ('64bit', '')


"""