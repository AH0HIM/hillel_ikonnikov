"""
Дана следующая функция y=f(x):

y = 2x – 10, если x > 0
y = 0, если x = 0
y = 2 * |x| – 1, если x < 0

Найти значение функции по x, который вводиться с клавиатуры
"""
x = int(input("Введите значение x: "))
y = 0

if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
elif x < 0:
    y = 2 * abs(x) - 1

print("Значение функции по х:", y)
