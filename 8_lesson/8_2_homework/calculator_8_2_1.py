"""
1. Напишете интерактивный калькулятор. Предполагается, что пользовательский ввод представляет собой формулу, состоящую
из числа, оператора (как минимум + и -) и другого числа, разделенных пробелом (например, 1 + 1). Используйте str.split()
    a. Если входные данные не состоят из 3 элементов, генерируйте эксепшн FormulaError.
    b. Попробуйте преобразовать первый и третий элемент в float (float_value = float(str_value)). Поймайте любую
    возникающую ValueError и сгенерируйте вместо него FormulaError
    c. Если второй элемент не является «+» или «-», киньте эксепшн FormulaError
"""
import re


class FormulaError(Exception):
    pass


class Calculator:
    def __init__(self):
        self.result = 0
        self.numbers_stack = []
        self.operators_stack = []
        self.final_formula = []

    def calculate(self, operand_1, operand_2, operator):
        if operator == '+':
            self.result = operand_1 + operand_2
        if operator == '-':
            self.result = operand_1 - operand_2
        if operator == '*':
            self.result = operand_1 * operand_2
        if operator == '/':
            if operand_1 == 0 or operand_2 == 0:
                raise FormulaError(ZeroDivisionError)
            self.result = operand_1 / operand_2

        return self.result

    @staticmethod
    def get_operator(element):
        operators = ['+', '-', '*', '/', '(', ')']
        if element not in operators:
            return False
        return True

    def check_formula(self, formula):
        string = re.sub(' ', '', formula)
        if len(string) < 3:
            raise FormulaError("Входные данные меньше 3-х элементов")
        if string[1] not in '+-/*':
            raise FormulaError("Входные данные имеют не правильный оператор")
        for item in string.split():
            item_split = [i for i in re.split('([\+\-\*\/\(\)])', item) if i]
            self.final_formula += item_split

        return self.final_formula

    @staticmethod
    def rate_stack(down_operand, up_operand):
        type_1 = ['+', '-']
        type_2 = ['*', '/']
        type_3 = ['(']
        type_4 = [')']

        if down_operand in type_1:
            if up_operand in type_2 or up_operand in type_3:
                return -1
            else:
                return 1
        elif down_operand in type_2:
            if up_operand in type_3:
                return -1
            else:
                return 1
        elif down_operand in type_3:
            if up_operand in type_4:
                return 0
            else:
                return -1
        else:
            return -1

    def stack_flow(self, stack_list):
        for element in stack_list:
            operator = self.get_operator(element)
            try:
                if not operator:
                    self.numbers_stack.append(float(element))
                else:
                    while True:
                        if len(self.operators_stack) == 0:
                            self.operators_stack.append(element)
                            break
                        tag = self.rate_stack(self.operators_stack[-1], element)
                        if tag == -1:
                            self.operators_stack.append(element)
                            break
                        elif tag == 0:
                            self.operators_stack.pop()
                            break
                        elif tag == 1:
                            op = self.operators_stack.pop()
                            num2 = self.numbers_stack.pop()
                            num1 = self.numbers_stack.pop()
                            self.numbers_stack.append(self.calculate(num1, num2, op))
            except ValueError:
                raise FormulaError("Входные данные имеют не правильный формат")

        while len(self.operators_stack) != 0:
            op = self.operators_stack.pop()
            num2 = self.numbers_stack.pop()
            num1 = self.numbers_stack.pop()
            self.numbers_stack.append(self.calculate(num1, num2, op))

        return self.numbers_stack, self.operators_stack

    def get_result(self):
        print("Добро пожаловать в программу {green}'Калькулятор'{endcolor}!"
              .format(green='\033[32m', endcolor='\033[0m'))
        user_input = input("Введите формулу: ")
        formula = ''
        for i in user_input:
            if i != '=':
                formula = formula + str(i)
        formula_list = self.check_formula(formula)
        self.stack_flow(formula_list)
        print(f'{formula} = {int(self.result)}')
        while True:
            user_input = input("Введите снова формулу или 'q', если хотите закрыть программу:\n")
            if user_input == 'q':
                print("Программа {green}'Калькулятор'{endcolor} завершена!".
                      format(green='\033[32m', endcolor='\033[0m'))
                break
            else:
                formula = ''
                self.__init__()
                for i in user_input:
                    if i != '=':
                        formula = formula + str(i)
                formula_list = self.check_formula(formula)
                self.stack_flow(formula_list)
                print(f'{formula} = {int(self.result)}')


if __name__ == '__main__':
    result = Calculator()
    result.get_result()
