# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_argument(arg1, arg2):  # аргументы прибывают отсюда
#         print(f"\nI get arguments {arg1} and {arg2}")
#         function_to_decorate(arg1, arg2)
#
#     return a_wrapper_accepting_argument
#
#
# @a_decorator_passing_arguments
# def hello_world(hello, world):
#     print(f"{hello} ------- {world}")
#
#
# hello_world("Hi", "World")

#
# def decorator_calculations(method_to_decorate):
#     def wrapper(self, discount):
#         discount = discount * 1.1
#         return method_to_decorate(self, discount)
#
#     return wrapper
#
#
# class Shop:
#
#     def __init__(self, price):
#         self.price = price
#
#     @decorator_calculations
#     def discount(self, multiple_to):
#         print(f"My price {self.price * multiple_to}")
#
#
# shop = Shop(30)
# shop.discount(0.8)
#
#
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Даная "обертка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print(f"I get args {args}")
#         print(f"I get kwargs {kwargs}")
#         function_to_decorate(*args, **kwargs)
#
#         print("Finish")
#
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument(*args, **kwargs):
#     print("Python is cool, no argument here.")
#
#
# function_with_no_argument(1, 23, 453, 63, a='say', b='hello')
import datetime
import time


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        t = datetime.datetime.now()
        print(f"Time now {t}")
        res = func(*args, **kwargs)
        print(f"Function result is {res}")
        print(func.__name__, datetime.datetime.now() - t)
        return res

    return wrapper


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        res = func(*args, **kwargs)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        return res

    return wrapper


@my_decorator
@benchmark
def sleep():
    print("Start")
    time.sleep(3)
    print("Finish")


sleep()
