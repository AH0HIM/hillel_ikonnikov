# # родительский класс
# class Bird:
#
#     def __init__(self):
#         print("Bird ready")
#
#     def who_is_this(self):
#         print("Bird")
#
#     def swim(self):
#         print("Can't swim")
#
#     def is_alive(self):
#         print("Yes")
#
#
# # дочерний класс
# class Penguin(Bird):
#
#     def __init__(self):
#         # вызов функции super()
#         super().__init__()
#         print("Penguin ready")
#
#     def who_is_this(self):
#         print("Penguin")
#
#     def class_is(self):
#         print(f"This is a class {self.__class__.__name__}")
#
#     def run(self):
#         print("Run better")
#
#
# peggy = Penguin()
# peggy.who_is_this()


class Animals:
    def method(self):
        print("I'm Animal")


class Dog(Animals):
    def method(self):
        super().method()
        print("I'm Dog")


class Cat(Animals):
    def method(self):
        super().method()
        print("I'm Cat")


class CatDog(Dog, Cat):
    def method(self):
        super().method()
        print("I'm CatDog")


cat_dog = CatDog()
print(cat_dog.method())

# порядок разрешения методов (MRO) - это способ, с помощью которого составляется линеаризация класса
