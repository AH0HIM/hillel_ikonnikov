# @property декоратор может быть использован для определения методов в классе, которые действуют как атрибут
#
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def area(self):
#         return 2 * self.radius * math.pi
#
#
# circle = Circle(10)
#
# print(circle.radius)
#
# class Stundent:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def name(self):
#         print(f"My name is {self.first_name}")
#
#     @property
#     def email(self):
#         mail = f"{self.first_name}{self.last_name}@student.com"
#         return mail
#
#
# student = Stundent('Sam', 'Monday')
# student.name()
# print(student.email)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Using @cashed_property

from functools import cached_property


# A sample class

class Sample:

    def __init__(self):
        self.result = 50

    # @property
    @cached_property
    # a method to increase the value of
    # result by 50
    def increase(self):
        self.result = self.result + 50
        return self.result


obj = Sample()
print(obj.increase)
print(obj.increase)
print(obj.increase)
