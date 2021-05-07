"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

# def func (a)
number = input("Введите число: ")
a = tuple(number)
even = list()
odd = list()
for x in number:
    if int(x) % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(f' Количество четных чисел - {len(even)}')
print(f' Количество нечетных чисел - {len(odd)}')

"""
https://drive.google.com/file/d/1hTrvVBppJh53uUWi_PYPyPCejG49ACzl/view?usp=sharing
"""