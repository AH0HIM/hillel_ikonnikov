"""
5. Напишите программу, чтобы проверить, не имеют ли два заданных набора (set) общих элементов.
"""
from random import randint

my_set_a = {randint(0, 10) for _ in range(10)}
my_set_b = {randint(0, 10) for _ in range(10)}

intersection_set = my_set_a & my_set_b

if len(intersection_set) == 0:
    print("Множество {blue}{a}{endcolor} и {blue}{b}{endcolor} не имеют общих элементов.".
          format(blue='\033[96m', endcolor='\033[0m', a=my_set_a, b=my_set_b))
else:
    print("Множество {blue} {a} {endcolor} и {blue} {b} {endcolor} имеют общие элементы: {blue}{ab}{endcolor}.".
          format(blue='\033[96m', endcolor='\033[0m', a=my_set_a, b=my_set_b, ab=intersection_set))

