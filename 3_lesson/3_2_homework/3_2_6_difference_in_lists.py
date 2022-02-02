"""
8. Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список.
Вывести результат на экран.
"""

from random import randint

first_list = [randint(0, 20) for _ in range(5)]
second_lst = [randint(0, 20) for _ in range(5)]
difference_list = list()

for element in first_list:
    if element not in second_lst:
        difference_list.append(element)

print(first_list, second_lst, difference_list, sep="\n")
