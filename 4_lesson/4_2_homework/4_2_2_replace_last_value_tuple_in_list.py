"""
2. Напишите программу для замены последнего значения кортежей в списке

Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]


for elem in range(len(sample_list)):
    for _ in sample_list[elem]:
        tmp_list = list(sample_list[elem])
        tmp_list[-1] = 100
        tmp_tuple = tuple(tmp_list)
        sample_list[elem] = tmp_tuple

print("Expected Output:", sample_list)

