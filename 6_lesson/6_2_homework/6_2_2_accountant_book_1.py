"""
2. Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся записи о номере заказа,
названии книги, количестве и стоимости одной книги, как представлено ниже, в таблице.
 _______________________________________________________________________________
| Order Number |    Book Title and Author           | Quantity | Price per Item |
|______________|____________________________________|__________|________________|
|    34587     | Learning Python, Mark Lutz         |    4     |     40.95      |
|    98762     | Programming Python, Mark Lutz      |    5     |     56.80      |
|    77226     | Head First Python, Paul Barry      |    3     |     32.95      |
|    88112     | Einfuhrung in Python3, Bernd Klein |    3     |     24.99      |
|______________|____________________________________|__________|________________|

Напишите программу на Python, которая на вход получает список списков:
[
    [34587, 'Learning Python, Mark Lutz',         4, 40.95],
    [98762, 'Programming Python, Mark Lutz',      5, 56.80],
    [77226, 'Head First Python, Paul Barry',      3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены на товары и
количества. Стоимость товара должна быть увеличена на $10, если стоимость заказа меньше $100.

Программа должна использовать lambda и map.
"""

order_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def calculate_orders(l):
    return list(map(
        lambda x: (x[0], round(x[2] * x[-1], 2) if round(x[2] * x[-1], 2) >= 100 else round(x[2] * x[-1], 2) + 10), l))


print(calculate_orders(order_list))
