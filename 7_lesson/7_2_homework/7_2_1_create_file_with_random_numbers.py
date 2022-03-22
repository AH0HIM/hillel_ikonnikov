"""
1. Напишите функцию для создания файла и записи в него случайных чисел, каждое число записывается в файл через пробел,
но не больше 10ти чисел в строку. Всего случайных чисел должно быть 1000.
"""
from random import randint

MIN_NUM = 1
MAX_NUM = 100
RANGE_LIST = 10
RANGE_NUMS = 100
FILE_NAME = 'file'
RANDOM_LIST = [[randint(MIN_NUM, MAX_NUM) for _ in range(RANGE_LIST)] for j in range(RANGE_NUMS)]


def create_and_write(file_name, container):
    with open(f'{file_name}.txt', 'w') as file:
        for i in container:
            file.write(" ".join(map(str, i)) + '\n')


create_and_write(FILE_NAME, RANDOM_LIST)

print("##################{green} TEST STAGE {endcolor}##################".format(green='\033[32m', endcolor='\033[0m'))


def test_file_count_all_lines():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        values = file.readlines()
        actual = 0
        expected = 100
        for _ in values:
            actual += 1
        assert actual == expected, \
            f'\nКоличество всех строк в файле не совпадает:\nActual: {actual}, Expected: {expected}'
        print("\nКоличество всех строк в файле: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_count_all_lines()


def test_file_count_all_random_numbers():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        values = file.read()
        actual = 0
        expected = 1000
        for _ in values.split():
            actual += 1
        assert actual == expected, \
            f'\nКоличество всех чисел в файле не совпадает:\nActual: {actual}, Expected: {expected}'
        print("\nКоличество всех чисел в файле: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_count_all_random_numbers()


def test_file_count_numbers_in_all_line():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        actual = 0
        expected = 10
        for line in file.readlines():
            values = line.split()
            for _ in values:
                actual += 1
            if actual == 10:
                actual = 0
            else:
                assert actual == expected, \
                    f'\nКоличество чисел в каждой строке файла не совпадает:\nActual: {actual}, Expected: {expected}'
        actual = 10
        print("\nКоличество чисел в каждой строке файла: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_count_numbers_in_all_line()


def test_file_matching_generated_and_written_nums():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        actual = []
        expected = []
        for i in RANDOM_LIST:
            for j in i:
                expected.append(int(j))
        for item in file.read().split():
            actual.append(int(item))
        assert actual == expected, f'\nСгенерированные числа не совпадают с записанными числами в файле:' \
                                   f'\nActual: {actual[:5]}, Expected: {expected[:5]}'
        print("\nСгенерированные числа {green}{act}{endcolor} "
              "совпадают с записанными числами в файле {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual[:5], exp=expected[:5]))


test_file_matching_generated_and_written_nums()
