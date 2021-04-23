# 5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

print(ord(first_letter))
print(ord(second_letter))
print(f'Количество символов между буквами: {ord(first_letter) - ord(second_letter)}')

# https://drive.google.com/file/d/1NnsU2yayMMyV9tT6rPJSF-VDbHG7zPLG/view?usp=sharing