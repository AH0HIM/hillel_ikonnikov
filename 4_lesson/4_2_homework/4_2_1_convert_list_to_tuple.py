"""
1. Напишите программу для преобразования списка в кортеж
"""
from random import randint

my_list = [randint(0, 20) for _ in range(5)]
print(f"type: {type(my_list)}, value: {my_list}")

my_tuple = tuple(my_list)
print(f"type: {type(my_tuple)}, value: {my_tuple}")
