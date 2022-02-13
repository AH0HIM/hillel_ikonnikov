#
#
#
# def sum(x, y):
#     return x + y
#
# def mult(x, y):
#     return x * y
#
# def pow(x, y):
#     return x ** y
#
# def custom_calc(x, y):
#     return x * y - 100 + x
#
#
# def calculate(action, x, y):
#     return action(x, y)
#
# # result = calculate(action=custom_calc, x=5, y=10)
# #
# # custom_calc(5, 10)
# # mult(5, 10)
#
# actions = [sum, pow, custom_calc, mult, mult, pow, sum]
#
# x = 5
# y = 10
#
# for action in actions:
#     calculate(action, x, y)
#
# # print(result)


# def cat_print():
#     print("Hello Cat")
#
# def dog_print():
#     print("Hello Dog")
#
# def placeholder():
#     print("Unknown")
#
#
# def get_printer(type):
#     if "Cat" == type: return cat_print
#     if "Dog" == type: return dog_print
#     else: return placeholder
#
# animals = ["Cat", "Cat", "Cat", "Dog", "Dog", "Pig", "Dog", "Dog", "Cat", "Cat", "Dog", "Dog"]
#
# for animal in animals:
#     action = get_printer(animal)
#     action()
#
#
# print(dog_print)




# ret = (lambda x, y: x * y)(2, 5)
#
# print(ret)

def calculate(action, x, y):
    return action(x, y)

print(calculate(lambda x, y: x + y, 2, 5))
print(calculate(lambda x, y: x * y, 2, 5))
print(calculate(lambda x, y: x / y, 2, 5))


#
# def get_printer(type):
#     if "Cat" == type: return lambda : "Hello CAT"
#     if "Dog" == type: return lambda : "Hello Dog"
#     if "Separator" == type: return lambda : "! "
#     else: return lambda : "Unknown"
#
# def sum(*args):
#     ret = ""
#     for func in args:
#         ret += func()
#     return ret
#
#
# print( sum(get_printer("Dog"), get_printer("Separator"), get_printer("Cat")) )

L = [1, 2, 3, 4]
print(type(filter(lambda x: True, L)))