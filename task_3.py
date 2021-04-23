# 3. По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = int(input('Введите координату x1 точки A: '))
y1 = int(input('Введите координату y1 точки A: '))

x2 = int(input('Введите координату x2 точки B: '))
y2 = int(input('Введите координату y2 точки B: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f"y = {k} * x + {b}")


# https://drive.google.com/file/d/1NnsU2yayMMyV9tT6rPJSF-VDbHG7zPLG/view?usp=sharing