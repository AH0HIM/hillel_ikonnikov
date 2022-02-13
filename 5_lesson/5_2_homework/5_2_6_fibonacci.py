"""
6. Напишите рекурсивную функцию для вычисления числа Фибоначчи
"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input())

print(f"Число Фибоначчи: {num} равно: {fibonacci(num)}")


