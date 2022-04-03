#
#
#
# class NegativeException(ArithmeticError):
#     pass
#
# def positive_sum(first, second):
#     if first < 0:
#         raise NegativeException("The first element is negative.")
#     if second < 0:
#         raise NegativeException("The Second element is negative.")
#     return first + second
#
# ##################################
# print(positive_sum(-5, -10))
# try:
#     print(positive_sum(5, 10))
#
#     # positive_sum(5, -10)
#     # positive_sum(-5, 10)
#     print(positive_sum(-5, -10))
# except Exception:
#     print("Program Exit!")
#
# # assert calc("2 + 3") == 5
# # assert calc("2+3") == 5
# # assert calc("2+3 - 5") == 0
# # assert calc("2-3 - 5") == -6


class FordMustang:
    def drive(self):
        pass


class Shelby(FordMustang):
    def drive(self):
        print("Drive Shelby")


class GT(FordMustang):
    def drive(self):
        print("Drive GT")


class Emach(FordMustang):
    def drive(self):
        print("Drive Emach")


# car = FordMustang()

cars = [Shelby(), GT(), Shelby(), Shelby(), Emach()]

for car in cars:
    car.drive()


# def print(x):
#     pass
#
# def print(x, y):
#     pass
#
# def print(x, y, z):
#     pass

class Employee:

    def __init__(self, name):
        self._name = name

    def __eq__(self, other):
        return self._name == other._name


a = Employee("Ivan")
b = Employee("Ivan")
ret = a == b  # a.__eq__(b)
print(f"{a == b}")
