"""
3. Напишите функцию func () так, чтобы она могла принимать аргументы переменной длины и выводить все значения
аргументов с индексом аргумента.
"""
from random import randint

MIN_MAX = 0
MAX_NUM = 10

my_list = [randint(MIN_MAX, MAX_NUM) for _ in range(randint(MIN_MAX, MAX_NUM))]


def func(*args):
    for i in range(len(args)):
        print(f"Под индексом {i}: {args[i]}")


func(*my_list)
