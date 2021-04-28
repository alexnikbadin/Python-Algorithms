"""

5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


Не совсем получилось

"""


for x in range(32, 128):
    if x % 10 == 0:
        print(x, chr(x), end=" ")
    else:
        print(x, chr(x))


"""
https://drive.google.com/file/d/1hTrvVBppJh53uUWi_PYPyPCejG49ACzl/view?usp=sharing
"""