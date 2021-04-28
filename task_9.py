"""
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

"""

from functools import reduce
a = input('Введите первое число: ')
b = input('Введите второе число: ')

if reduce(lambda x, y: x + y, list(map(int, a))) > reduce(lambda x, y: x + y, list(map(int, a))):
    print(f'Число с большей суммой {a}, сумма его цифр {reduce(lambda x, y: x + y, list(map(int, a)))}')
else:
    print(f'Число с большей суммой {b}, сумма его цифр {reduce(lambda x, y: x + y, list(map(int, b)))}')

"""
https://drive.google.com/file/d/1hTrvVBppJh53uUWi_PYPyPCejG49ACzl/view?usp=sharing
"""




