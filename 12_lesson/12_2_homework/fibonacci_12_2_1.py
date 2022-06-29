"""
1. Написать две функции которые выводят сумму первых 100 элементов последовательности Фибоначчи. Одна из функций должна
использовать генератор;
2. Задекорировать созданные функции так, чтобы выводить время за которое эти функции выполняются
"""
import datetime


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = datetime.datetime.now()
        print(f"Time now {t}")
        res = func(*args, **kwargs)
        print(f"Function result is {res}")
        print(func.__name__, datetime.datetime.now() - t)
        return res

    return wrapper


# @benchmark
def fibonacci(n):
    a, y = 0, 1
    for _ in range(n):
        b = a
        a = b + y
        y = b
        print(b)


@benchmark
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

    for fib in fibonacci(100):


fibonacci_gen(100)