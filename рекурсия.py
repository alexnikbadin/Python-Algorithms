
"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, то надо вывести число 6843.
"""

def reverse_(n):
    if n < 10:
        return n
    return int(str(n % 10)+str(reverse_(n//10)))

print(reverse_(int(input('Введите число: '))))


