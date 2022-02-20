"""
5. Используя filter() оставьте только книги, количество которых больше 5ти.

"""
import numpy as np

order_list = [
    [24387, 'на русском', 2, 4.59],
    [87236, 'C Programming Absolute Beginner"s Guide', 1, 23.55],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [58132, 'Effective Modern C++: 42 Specific ...', 9, 42.89],
    [98762, 'Programming Python, Mark Lutz', 5, 56.8],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.8]
]

my_filter_list = list(filter(lambda x: x[2] > 5, order_list))

print(np.array(my_filter_list))