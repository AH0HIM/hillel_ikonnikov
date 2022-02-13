"""
2. Напишите функцию Python для суммирования всех чисел в списке.
"""
from random import randint

MIN_MAX = 0
MAX_NUM = 10

my_list = [randint(MIN_MAX, MAX_NUM) for _ in range(MAX_NUM)]


def sum_of_num_in_list(item):
    count = 0
    for i in item:
        count += i
    return count


result = sum_of_num_in_list(my_list)

print(f"Сумма всех числе в списке {my_list}: {result}")
