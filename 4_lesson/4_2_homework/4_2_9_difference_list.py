"""
9. Реализовать логику Difference для двух списков (list), проверить работу алгоритма на set.difference
"""
from random import randint

first_set = {randint(0, 10) for _ in range(10)}
second_set = {randint(0, 10) for _ in range(10)}

different_set = set.difference(first_set - second_set)

print("Множество А: {blue}{a}{endcolor}, множество B: {blue}{b}{endcolor}.\n"
      "Результат разницы Difference: {blue}{diff}{endcolor}.".
      format(blue='\033[96m', endcolor='\033[0m', a=first_set, b=second_set, diff=different_set))
print()


list1 = list(first_set)
list2 = list(second_set)

different_list = list1[::]

for elem in list2:
    if elem in different_list:
        different_list.remove(elem)

print("Список А: {blue}{a}{endcolor}, список B: {blue}{b}{endcolor}.\n"
      "Результат разницы списков: {blue}{union}{endcolor}.".
      format(blue='\033[96m', endcolor='\033[0m', a=list1, b=list2, union=different_list))