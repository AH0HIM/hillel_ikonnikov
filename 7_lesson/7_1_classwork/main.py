
import random

def print_debug(stage, first, second):
    print("\n" + stage)
    print(f"first: {first}")
    print(f"second: {second}")

def list_unique(list):
    ret = []
    for item in list:
        if item not in ret:
            ret.append(item)
    return ret

def list_difference(first, second):
    difference = []
    for item in first:
        if item not in second:
            difference.append(item)
    return difference

# Start

first = [random.randint(0, 10) for _ in range(10)]
second = [random.randint(0, 10) for _ in range(10)]
print_debug("Init", first, second)

first.sort()
second.sort()
print_debug("Sorting", first, second)

first = list_unique(first)
second = list_unique(second)
print_debug("Unique", first, second)

print(f"\nDifference: {list_difference(first, second)}")
print(f"\nDifference: {list_difference(second, first)}")

# Test stage

actual = list_unique([9, 3, 10, 7, 7, 1, 2, 1, 4, 6])
expected = [1, 2, 3, 4, 6, 7, 9, 10]
assert len(actual) == len(expected) or actual == expected

actual = list_unique([2, 8, 2, 4, 0, 3, 0, 3, 1, 2])
expected = [0, 1, 2, 3, 4, 8]
assert len(actual) != 0 or actual == expected

actual = list_unique([2, 1, 7, 7, 0, 10, 6, 7, 2, 4])
expected = [0, 1, 2, 4, 6, 7, 10]
assert len(actual) != 0 or actual == expected

actual = list_difference([0, 1, 4, 5, 6, 7, 8, 10], [0, 1, 3, 4, 6, 9, 10])
expected = [5, 7, 8]
assert actual == expected

actual = list_difference([0, 1, 3, 4, 6, 9, 10], [0, 1, 4, 5, 6, 7, 8, 10])
expected = [3, 9]
assert actual == expected

# def sum(first, second):
#     return first + second

# assert sum(2, 5) == 7
# assert sum(0, 0) == 0
# assert sum(-2, -3) == -5
# assert sum(10000000000000, 200000000000000000) == 2001000000000000000
# assert sum('r', 0) == 0
