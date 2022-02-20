import random


def calc_file_lines(file_name):
    with open(file_name, 'r') as file:
        ret = 0
        for _ in file:
            ret += 1
    return ret

def calc_file_words(file_name):
    f = open(file_name, 'r')
    ret = 0
    for line in f:
        ret += len(line.split(" "))
    f.close()
    return ret

print(calc_file_words("test.txt"))

def write_to_file(file_name, container):
    f = open(file_name, 'w')
    for item in container:
        f.write(str(item) + ' ')
    f.close()

write_to_file("test2.txt", [random.randint(0, 100) for _ in range(10)])

def read_ints_from_file(file_name):
    f = open(file_name, 'r')
    ret = []
    for line in f:
        values = line.split(" ")
        values.pop()
        for item in values:
            ret.append(int(item))
    f.close()
    return ret

values = read_ints_from_file("test2.txt")
print(values)

print("===================================")

def TEST_read_ints_from_file_count_lines():
    values = read_ints_from_file("test_read_ints_from_file.txt")
    actual = 0
    # print(values)
    for _ in values:
        actual += 1
    expected = 10
    # print(f"expected: {expected}, actual: {actual}")
    assert actual == expected

def TEST_write_to_file():
    file_name = "TEST_write_to_file.txt"
    expected = [random.randint(0, 100) for _ in range(10)]
    write_to_file(file_name, expected)
    with open(file_name, 'r') as file:
        actual = file.read()
    actual = actual.split(" ")
    actual.pop()
    new_actual = []
    for item in actual:
        new_actual.append(int(item))
    actual = new_actual
    print(f"actual: {actual}, expected: {expected}")
    assert expected == actual

# TEST_read_ints_from_file_count_lines()
TEST_write_to_file()


