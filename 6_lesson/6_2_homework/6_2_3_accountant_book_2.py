"""
3. Добавьте к исходному списку еще несколько товаров
[
    [24387, ' на русском',                                                                    2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)',                                     12, 78.80],
    [87236, 'C Programming Absolute Beginner's Guide',                                       1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]
"""
import numpy as np

order_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

add_order_list = [
    [24387, 'на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, 'C Programming Absolute Beginner"s Guide', 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific ...', 9, 42.89]
]

order_list.extend(add_order_list)

print(np.array(order_list))
