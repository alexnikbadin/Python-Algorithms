"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как массив, элементы которого это цифры числа.
 Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
 произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
import collections


first_num = collections.deque(input('Введите число: ').upper())
sec_num = collections.deque(input('Введите число: ').upper())
result = collections.deque
numbers_list = [str(el) for el in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
print(numbers_list)
if len(first_num) > len(sec_num):
  first_num, sec_num = sec_num, first_num
i = -1
x = 0
print(first_num)
print(sec_num)
# for el in sec_num:
#     a = numbers_list.index(el)
#     b = numbers_list.index(first_num[i])
#     result.append(numbers_list[(a + b + x) % 16])
#     if (a + b) >= 15:
#         x = 1
#     else:
#         x = 0
#     i -= 1
#     if i == -len(first_num) - 1:
#         break
# print(result)

