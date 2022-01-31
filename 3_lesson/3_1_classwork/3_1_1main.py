


# x = "Hello World  asfdsgdgdfgafgfadgsfg"

# idx = 0
# size = len(x)
# while idx != size:
#     tmp = x[idx]
#     print(tmp)
#     idx += 1

# for item in x:
#     print(item)

# for idx in range(0, len(x)):
#     print(x[idx])

# arr1 = "HelloW"
# arr2 = "79853451234"
#
# # len(arr1)*len(arr2)
#
# for char in arr1:
#     pass
#
# x = 5
# while x != 0:
#     print("H", end=" ")

# for char in arr1:
#     print("[ ", end="")
#     for number in arr2:
#         if int(number) == 3:
#             continue
#         print(char + str(number) + " ",end="")
#     print("]\n")

# print(char)

"""

h = 4
w = 3

* * *
*   *
*   *
* * *

"""

# height = int(input("Enter height: "))
# width = int(input("Enter width: "))
# tmp_width = width
# while height != 0:
#     while tmp_width != 0:
#         print("*", end=" ")
#         tmp_width -= 1
#     print("")
#     tmp_width = width
#     height -= 1

# print("*"*width)
# for item in range(0, height-2):
#     print("*" + " "*(width-2) + "*")
# print("*"*width)

# x = "Hello"
# x[1] = "Y"

# import random
#
# LIST_SIZE = 5
# RANDOM_UPPER_BOUND = 200
#
# # Input
# l = []
# for _ in range(0, LIST_SIZE):
#     l.append(random.randint(0, RANDOM_UPPER_BOUND))
#
# # Algorithm
# sum = 0
# for item in l:
#     sum += item
#
# # Output
# print(f"List: {l}")
# print(f"Sum: {sum}")

# d = {}
# print(d)
#
# d[100] = "Hello"
# print(d)
#
# d[2] = "World"
# print(d)
#
# d[2] = "Some"
# print(d)
#
# del d[2]
# print(d)
#
# d["Hello"] = 100
# print(d)

# 54 45 324
# {54: "54", 45: "45", 324: "324"}

import random

d = dict()
for _ in range(0, 10):
    x = random.randint(0, 10)
    d[x] = str(x)

for key in d:
    print(type(key), end="")
    print(type(d[key]))

if 100 in d:
    print("5 is in dict")

print(d)
