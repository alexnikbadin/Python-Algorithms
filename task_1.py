# """
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# """

a = int(input('Input the number, please: '))
b = a % 10
a = a // 10
c = a % 10
a = a // 10
d = a + b + c
e = a * b * c
print ("Сумма равна {}".format(d))
print ("Произведение равно {}".format(e))

# https://drive.google.com/file/d/1NnsU2yayMMyV9tT6rPJSF-VDbHG7zPLG/view?usp=sharing
