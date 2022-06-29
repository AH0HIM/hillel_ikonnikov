"""
1. Написать две функции которые выводят сумму первых 100 элементов последовательности Фибоначчи. Одна из функций должна
использовать генератор;
2. Задекорировать созданные функции так, чтобы выводить время за которое эти функции выполняются
"""
import datetime


def time_function(func):
    def wrapper(*args):
        t = datetime.datetime.now()
        res = func(*args)
        print(f"{func.__name__}, The sum of the first {n} elements: {func(*args)}")
        print(f"Function execution time: {datetime.datetime.now() - t}\n")
        return res

    return wrapper


@time_function
def fibonacci_1(n):
    fib1, fib2, fib_sum = 0, 1, 0
    for _ in range(n):
        fib_sum += fib1
        fib1, fib2 = fib2, fib1 + fib2
    return fib_sum


@time_function
def fibonacci_2(n):
    def fibonacci_generate(n):
        fib1, fib2 = 0, 1
        for _ in range(n):
            yield fib1
            fib1, fib2 = fib2, fib1 + fib2

    return sum(fibonacci_generate(n))


n = 100
fibonacci_1(n)
fibonacci_2(n)
