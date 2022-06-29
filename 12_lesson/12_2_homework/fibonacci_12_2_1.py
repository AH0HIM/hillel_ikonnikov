"""
1. Написать две функции которые выводят сумму первых 100 элементов последовательности Фибоначчи. Одна из функций должна
использовать генератор;
2. Задекорировать созданные функции так, чтобы выводить время за которое эти функции выполняются
"""
import datetime


def time_result(func):
    def wrapper(*args):
        time = datetime.datetime.now()
        res = func(*args)
        print("\nTime: ", datetime.datetime.now() - time)
        return res

    return wrapper


@time_result
def fibonacci():
    a, y = 0, 1
    for _ in range(100):
        b = a
        a = b + y
        y = b
        print(b, end=' ')


@time_result
def fibonacci_generator():
    def fibonacci_gen():
        a, b = 0, 1
        for i in range(100):
            a, b = b, a + b
            yield a

    for fib in fibonacci_gen():
        print(fib, end=' ')


fibonacci_generator()
fibonacci()
