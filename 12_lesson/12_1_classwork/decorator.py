# def cat():
#     def say():
#         return 'Meo'
#
#     print(say())
#
#
# cat()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# def animal(type="cat"):
#     def cat():
#         return "Meo!"
#
#     def dog():
#         return "Woof!"
#
#     if type == "cat":
#         return cat
#     else:
#         return dog
#
#
# print(animal()())


# def say_something():
#     return "Hello people!"
#
#
# def doSomethingBefore(func):
#     print("I'm something do")
#     print(func())
#
#
# doSomethingBefore(say_something())
#
#
# class Cat:
#
#     def say(self):
#         return "Meo"
#
#
# class Dog:
#
#     def say(self):
#         return "Woof"
#
#
# def doSomething(my_class):
#     print("I'm something do")
#     print(my_class.say())
#
#
# cat = Cat()
# dog = Dog()
#
# doSomething(cat)
# doSomething(dog)

# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра


def my_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию "обертку"

    def the_wrapper_around_the_original_function():
        print("I'm wrapper let's start")

        # Вызовем саму декорируемую функцию
        a_function_to_decorate()

        print("We finish our method")

    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.

def a_stand_alone_function():
    print("<<<<<<<<<<<<<<<<<<< I'm standalone function")


# a_stand_alone_function()
#
# a_stand_alone_function_decorated = my_decorator(a_stand_alone_function)
# a_stand_alone_function_decorated()


@my_decorator
def another_stand_alone_function():
    print(">>>>>>>>>>>>>>>>> I'm another stand alone function >>>>>>>>>>>>>>>>>")


another_stand_alone_function()