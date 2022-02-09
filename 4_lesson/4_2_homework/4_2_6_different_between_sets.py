"""
6. Напишите программу для поиска элементов в данном наборе A (set), которых нет в другом наборе B.
"""
from random import randint

A = {randint(0, 10) for _ in range(10)}
B = {randint(0, 10) for _ in range(10)}

different_set = A - B

if len(different_set) == 0:
    print("Во множество {blue}{a}{endcolor} и {blue}{b}{endcolor} не найдены различные элементы.".
          format(blue='\033[96m', endcolor='\033[0m', a=A, b=B))
else:
    print("Во множество A: {blue}{a}{endcolor} найдены элементы {blue}{ab}{endcolor}, "
          "которых нет \nво множестве B: {blue}{b}{endcolor}.".
          format(blue='\033[96m', endcolor='\033[0m', a=A, b=B, ab=different_set))

