


# l = [1, 2, 3]
# print(f"type: {type(l)}, value: {l}")
# l[0] = 100
# t = tuple(l)
# print(f"type: {type(t)}, value: {t}")
# new = list(t)
# print(f"type: {type(new)}, value: {new}")


# t = ("Ivan", 26, "CTO", "Address")
#
# name, age, pos, addr = t
# name = "Petr"
# print(f"name: {name}, age: {age}, possition: {pos}, addr: {addr}")
# print(t)

# import copy
#
# l = [1, [100, 200, ['s', 'd']], 3, 4, 5]
# # l2 = l
# # l2 = l.copy()
# l2 = copy.deepcopy(l)
# l2[1][2][0] = 1000000
# print(f"l1: {l}\nl2: {l2}")

# lst_tuples = [(1,2), (2,3,5), (3,4), (2,3,4,2)]
# print(f"lst_tuples: {lst_tuples}")
# new_list = []
# for item in lst_tuples:
#     new_list.append(list(item))
# # lst_tuples[0][0] = 100
# print(f"new_list: {new_list}")
# new_list[0][0] = 100
# print(f"new_list: {new_list}")
# lst_tuples = new_list


# l = [[], [], [[],[[],[],[],[],[],[],[],[],[]],[],[],[]]]
# table = l[2][1][0]
# table[2]["Ivan"][0]
# print(len([2][4]))

# nums = [(1,2,6), (2,3,-6), (3,4), (2,2,2,2)]
# sum = []
#
# for item in nums:
#     s = 0
#     for i in item:
#         s += i
#     sum.append(s)
# print(sum)

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7, 8}
s3 = {8}

s4 = s1 & s2 & s3
if len(s4) == 0:
    print("No")
else:
    print(f"YES {s4}")













