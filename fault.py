"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

def rabin_karp(s):
    h_subs = hashlib.sha1(s.encode('utf-8')).hexdigest()
    for i in range(len(s)):
       return h_subs

print(rabin_karp(input(': ')))
# print(rabin_karp(input('Введите строку: '), input('Введите подстроку: ')))