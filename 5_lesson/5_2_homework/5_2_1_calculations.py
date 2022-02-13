"""
1. Напишите функцию calculations () так, чтобы она могла принимать две переменные и вычислять их сложение и вычитание.
А также он должен возвращать как сложение, так и вычитание за один вызов возврата.
"""
from random import randint

MIN_NUM = 1
MAX_NUM = 2


def calculations(x, y):
    return x + y, x - y


x, y = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
var1, var2 = calculations(x, y)

print("Результат {x} + {y}: {blue}{var1}{endcolor}\n"
      "Результат {x} - {y}: {blue}{var2}{endcolor}"
      .format(blue="\33[96m", endcolor='\33[0m', var1=var1, var2=var2, x=x, y=y))
