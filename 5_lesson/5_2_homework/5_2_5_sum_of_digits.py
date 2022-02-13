"""
5. Дано натуральное число N. Вычислите сумму его цифр. Напишите рекурсивную функцию
"""


def sum_digits(n):
    if n == 0:
        return n
    else:
        return n + sum_digits(n - 1)


num = int(input())

print(f"Натуральное число: {num}. Сумма цифр равна: {sum_digits(num)}")
