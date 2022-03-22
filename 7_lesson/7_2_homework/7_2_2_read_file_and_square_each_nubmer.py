"""
2. Напишите другую функцию, которая считывает первый файл и возводит каждое число в квадрат. Каждое полученное число
должно быть дозаписано в исходный файл в таком же формате.
"""

FILE_NAME = 'file'


def read_and_append():
    with open(f'{FILE_NAME}.txt', 'r+') as file:
        for line in file.readlines():
            res = []
            values = line.split()
            for item in values:
                res.append(int(item) ** 2)
            file.write(" ".join(map(str, res)) + '\n')


read_and_append()

print("##################{green} TEST STAGE {endcolor}##################".format(green='\033[32m', endcolor='\033[0m'))


def test_file_count_all_random_numbers():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        values = file.read()
        actual = 0
        expected = 2000

        for _ in values.split():
            actual += 1
        assert actual == expected, \
            f'\nКоличество всех чисел в файле не совпадает:\nActual: {actual}, Expected: {expected}'
        print("\nКоличество всех чисел в файле: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_count_all_random_numbers()


def test_file_count_all_completed_lines():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        values = file.readlines()[100:]
        actual = 0
        expected = 100
        for _ in values:
            actual += 1
        assert actual == expected, \
            f'\nКоличество всех строк в файле не совпадает:\nActual: {actual}, Expected: {expected}'
        print("\nКоличество дописанных строк в файле: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_count_all_completed_lines()


def test_file_count_numbers_in_all_completed_lines():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        actual = 0
        expected = 10
        for line in file.readlines()[100:]:
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


test_file_count_numbers_in_all_completed_lines()


def test_file_square_each_number():
    with open(f'{FILE_NAME}.txt', 'r') as file:
        actual = 0
        expected = 1000
        first_hundred_list = file.readlines()[:100]
        file.seek(0)
        second_hundred_list = file.readlines()[100:]
        for i, j in zip(first_hundred_list, second_hundred_list):
            for number, square in zip(i.split(), j.split()):
                if int(number) ** 2 == int(square):
                    actual += 1
                    continue
                else:
                    assert actual == expected, f'\nЧисло не возведено в квадрат:\nActual: ' \
                                               f'{int(number) ** 2}, Expected: {square}'
        print("\nКоличество чисел возведённых в квадрат: {green}{act}{endcolor} из {green}{exp}{endcolor}".
              format(green='\033[32m', endcolor='\033[0m', act=actual, exp=expected))


test_file_square_each_number()
