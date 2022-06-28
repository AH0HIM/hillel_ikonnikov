from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def printing_class(cls):
        print(f"Class is {cls.__name__}")

    @staticmethod
    def is_adult(age):
        return age > 18

    def print_name(self):
        return self.name


# Person.printing_class()
person1 = Person("Sarah", 25)

print(person1.name)