"""
7. Напишите программу, которая копирует список
"""
from random import randint

my_list = [randint(0, 10) for i in range(10)]
new_list = my_list.copy()  # new_list = my_list[:]

print("Список", my_list, "и копия списка", new_list)
