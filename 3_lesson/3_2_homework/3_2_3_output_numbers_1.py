"""
4. Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
или в порядке убывания если A > B
"""
from random import randint

a, b = randint(0, 10), randint(0, 10)

if a < b:
    print(f"Все числа от {a} до {b} в порядке возрастания:")
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    print(f"Все числа от {a} до {b} в порядке убывания:")
    for i in range(a, b - 1, -1):
        print(i, end=" ")
