"""
9. Создайте inner функцию для вычисления сложения следующим образом:
 - Создайте внешнюю функцию, которая будет принимать два параметра a и b;
 - Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
 - Наконец, внешняя функция добавит 5 и вернет ее.
"""

from random import randint

MIN_MAX = 1
MAX_NUM = 10
num1, num2 = randint(MIN_MAX, MAX_NUM), randint(MIN_MAX, MAX_NUM)


def outer(a, b):
    def inner():
        return a + b
    return inner() + 5


print(f"Параметры a: {num1} и b: {num2}\n"
      f"Результат сложения: {outer(num1, num2)}")
