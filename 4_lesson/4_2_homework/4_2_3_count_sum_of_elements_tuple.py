"""
3. Напишите программу для поэлементного вычисления суммы заданных кортежей. Результатом должен быть кортеж.

Input
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)

Output
(6, 9, 8, 6)
"""
tuple1 = (1, 2, 3, 5)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 3)
sum_col = []

for i in range(max(len(tuple1), len(tuple2), len(tuple3))):
    if i >= min(len(tuple1), len(tuple2), len(tuple3)):
        if len(tuple1) == i + 1 and len(tuple3) < len(tuple1) > len(tuple2):
            sum_col.append(tuple1[i] + 0)
        elif len(tuple1) == i + 1 and len(tuple1) == len(tuple2):
            sum_col.append(tuple1[i] + tuple2[i] + 0)

        elif len(tuple2) == i + 1 and len(tuple3) < len(tuple2) > len(tuple1):
            sum_col.append(tuple2[i] + 0)
        elif len(tuple2) == i + 1 and len(tuple1) < len(tuple2) == len(tuple3):
            sum_col.append(tuple2[i] + tuple3[i] + 0)

        elif len(tuple3) == i + 1 and len(tuple1) < len(tuple3) > len(tuple2):
            sum_col.append(tuple3[i] + 0)
        elif len(tuple3) == i + 1 and len(tuple2) < len(tuple3) == len(tuple1):
            sum_col.append(tuple3[i] + tuple1[i] + 0)
    else:
        sum_col.append(tuple1[i] + tuple2[i] + tuple3[i])

print("Output: ", tuple(sum_col))
