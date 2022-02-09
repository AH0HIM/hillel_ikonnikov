"""
8. Реализовать логику Union для двух списков (list), проверить работу алгоритма на set.union
"""
from random import randint

first_set = {randint(0, 10) for _ in range(10)}
second_set = {randint(0, 10) for _ in range(10)}

union_set = set.union(first_set, second_set)

print("Множество А: {blue}{a}{endcolor}, множество B: {blue}{b}{endcolor}.\n"
      "Результат объединения Union: {blue}{union}{endcolor}.".
      format(blue='\033[96m', endcolor='\033[0m', a=first_set, b=second_set, union=union_set))
print()

list1 = list(first_set)
list2 = list(second_set)
list_union = []

for i in list1:
    list_union.append(i)
for j in list2:
    if j not in list1:
        list_union.append(j)

for i in range(len(list_union)):
    for j in range(i + 1, len(list_union)):
        if list_union[j] < list_union[i]:
            list_union[j], list_union[i] = list_union[i], list_union[j]

print("Список А: {blue}{a}{endcolor}, список B: {blue}{b}{endcolor}.\n"
      "Результат объединения списков: {blue}{union}{endcolor}.".
      format(blue='\033[96m', endcolor='\033[0m', a=list1, b=list2, union=list_union))
