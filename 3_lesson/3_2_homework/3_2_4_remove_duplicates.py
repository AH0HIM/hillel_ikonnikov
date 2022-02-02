"""
6. Напишите программу, которая удаляет дубликаты элементов из списка.
"""
from random import randint

my_list = [randint(0, 10) for _ in range(10)]
new_list = []

for element in my_list:
    if element not in new_list:
        new_list.append(element)

print(f"Из списка удаленны все дубликаты: \n{my_list} \n{new_list}")
