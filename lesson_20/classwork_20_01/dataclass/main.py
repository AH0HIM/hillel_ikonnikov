import inspect
from dataclasses import dataclass, asdict, field
from pprint import pprint


# class Person:
#     def __init__(self, name: str, age: int, job: str):
#         self.name = name
#         self.age = age
#         self.job = job
#
#
# @dataclass
# class Person_class:
#     name: str
#     age: int
#     job: str
#
#
# p1 = Person('Joe', '11', 'QA')
# p2 = Person_class('Tom', '22', 'AQA')


# print(p1)
# print(p2)
#
# print(asdict(p2))


@dataclass()
class Student:
    name: str
    age: int

@dataclass
@dataclass()
class Teacher(Student):
    my_list: list


teacher = Teacher('Joe', 22, [1, 2, 3])
print(teacher)

# t_1 = Teacher([1, 2, 3])
#
# print(t_1)
