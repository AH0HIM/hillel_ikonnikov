"""
7. Напишите программу, которая копирует список
"""
from random import randint

my_list = [randint(0, 10) for _ in range(10)]
new_list = list()
for element in my_list:
    new_list.append(element)

print("Список", my_list, "и копия списка", new_list)
