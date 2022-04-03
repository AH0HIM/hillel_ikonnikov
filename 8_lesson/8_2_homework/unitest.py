"""
2. Напишите минимум 5 тестов для каждой созданной функции
3. Добавьте возможность считать более длинные выражения:
    1 + 2 + 4
    1 + 2 - 1
    1 + 2 + 3 - 1 + 4 - 2
    1 + 2 + 32 - 1 + 4 * 20 + 100 - 200 + 551 / 2
4. Напишите соответствующие unit тесты
"""
import traceback
import calculator_8_2_1 as c


def result_message(actual, expected):
    stack = traceback.extract_stack()
    message = ''
    if actual == expected:
        message += "{green}SUCCESS{endcolor}".format(green='\033[32m', endcolor='\033[0m')
    else:
        message += "{red}FAILED{endcolor}".format(red='\033[31m', endcolor='\033[0m')
    print()
    print(message, 'from {}'.format(stack[-2][2]))


def test_calculate_adding():
    result_message(c.Calculator().calculate(2, 2, '+'), 4)
    result_message(c.Calculator().calculate(0, 0, '+'), 0)
    result_message(c.Calculator().calculate(-1, -1, '+'), -2)
    result_message(c.Calculator().calculate(100, 100, '+'), 200)
    result_message(c.Calculator().calculate(1.05, 7.33, '+'), 8.38)


def test_calculate_subtracting():
    result_message(c.Calculator().calculate(2, 2, '-'), 0)
    result_message(c.Calculator().calculate(0, 0, '-'), 0)
    result_message(c.Calculator().calculate(-1, -1, '-'), 0)
    result_message(c.Calculator().calculate(100, 100, '-'), 0)
    result_message(c.Calculator().calculate(1.05, 7.33, '-'), -6.28)


def test_calculate_multiplying():
    result_message(c.Calculator().calculate(2, 2, '*'), 4)
    result_message(c.Calculator().calculate(0, 0, '*'), 0)
    result_message(c.Calculator().calculate(-1, -1, '*'), 1)
    result_message(c.Calculator().calculate(100, 100, '*'), 10000)
    result_message(c.Calculator().calculate(1.05, 7.33, '*'), 7.6965)


def test_calculate_dividing():
    result_message(c.Calculator().calculate(2, 2, '/'), 1)
    result_message(c.Calculator().calculate(-1, -1, '/'), 1)
    result_message(c.Calculator().calculate(100, 100, '/'), 1)
    result_message(c.Calculator().calculate(-100, 100, '/'), -1)
    result_message(c.Calculator().calculate(1.05, 7.33, '/'), 0.14324693042291953)


task1 = '1 + 2 + 4'
task2 = '1 + 2 - 1'
task3 = '1 + 2 + 3 - 1 + 4 - 2'
task4 = '1 + 2 + 32 - 1 + 4 * 20 + 100 - 200 + 551 / 2'


def test_calculator():
    formula_list = c.Calculator().check_formula(task1)
    actual_result = int(sum(c.Calculator().stack_flow(formula_list)[0]))
    result_message(actual_result, 7)

    formula_list = c.Calculator().check_formula(task2)
    actual_result = int(sum(c.Calculator().stack_flow(formula_list)[0]))
    result_message(actual_result, 2)

    formula_list = c.Calculator().check_formula(task3)
    actual_result = int(sum(c.Calculator().stack_flow(formula_list)[0]))
    result_message(actual_result, 7)

    formula_list = c.Calculator().check_formula(task4)
    actual_result = int(sum(c.Calculator().stack_flow(formula_list)[0]))
    result_message(actual_result, 289)


test_calculate_adding()
test_calculate_subtracting()
test_calculate_multiplying()
test_calculate_dividing()
test_calculator()