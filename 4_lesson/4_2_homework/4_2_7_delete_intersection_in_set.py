"""
7. Напишите программу, которая удаляет пересечение 2-го набора из 1-го набора.
"""
from random import randint

first_set = {randint(0, 10) for _ in range(10)}
second_set = {randint(0, 10) for _ in range(10)}

intersection_set = first_set & second_set

print("Пересечения {blue}{с}{endcolor} из 2-го набора {blue}{b}{endcolor} удаляем из 1-го набора {blue}{a}{endcolor}.".
      format(blue='\033[96m', endcolor='\033[0m', a=first_set, b=second_set, с=intersection_set))

first_set.difference_update(first_set & second_set)

print("Результат 1-го набора: {blue}{c}{endcolor}".format(blue='\033[96m', endcolor='\033[0m', c=first_set))
