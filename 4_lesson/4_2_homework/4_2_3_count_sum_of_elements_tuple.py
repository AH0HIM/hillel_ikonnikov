"""
3. Напишите программу для поэлементного вычисления суммы заданных кортежей. Результатом должен быть кортеж.

Input
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)

Output
(6, 9, 8, 6)
"""

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

my_list = []
sum_col = []

for i in tuple1, tuple2, tuple3:
    my_list.append(i)

for col in range(len(my_list) + 1):
    col_count = 0
    for row in range(len(my_list)):
        col_count += my_list[row][col]
    sum_col.append(col_count)

print("Output: ", tuple(sum_col))
