"""
7. Напишите функцию для умножения всех чисел в списке. Рекурсивно
"""
from random import randint

MIN_MAX = 1
MAX_NUM = 5

my_list = [randint(MIN_MAX, MAX_NUM) for _ in range(MAX_NUM)]


def multi_nums(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        return list_num[0] * multi_nums(list_num[1:])


print(f"Список: {my_list}. Сумма умножения всех чисел: {multi_nums(my_list)}")
