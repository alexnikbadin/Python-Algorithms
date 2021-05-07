"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего.

"""
import collections

number = int(input('Введите количество компаний: '))
companies = collections.deque()
incomes = collections.Counter()
for el in range(number):
    companies.append(input('Введите название компании: '))
for el in companies:
    incomes[el] += sum([int(input('Введите прибыль за 1 квартал: ')),
                        int(input('Введите прибыль за 2 квартал: ')),
                        int(input('Введите прибыль за 3 квартал: ')),
                        int(input('Введите прибыль за 4 квартал: '))])
average = sum(incomes.values()) / 4 / number
for key, value in incomes.items():
    if value / 4 < average:
        print(f'Прибыль компании {key} ниже средней')
    else:
        print(f'Прибыль компании {key} выше средней')