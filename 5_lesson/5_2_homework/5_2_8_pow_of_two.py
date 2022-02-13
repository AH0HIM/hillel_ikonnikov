"""
8. Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в
противном случае. 8 - YES, 3 - NO
"""


def pow_of_two(n):
    if n % 2:
        return "NO"
    if n > 2:
        return pow_of_two(n / 2)
    if n:
        return "YES"
    return "NO"


num = int(input())

print(pow_of_two(num))
