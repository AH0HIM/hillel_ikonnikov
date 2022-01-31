


# void foo(){ z = x + y; cout << x; return 0; } Ctrl + /

"""
def foo():
    z = x + y
    print(z)
    return 0
"""

# base_year = 1000
#
# year = 5 + 2 * 3 - base_year
# year_in_different_form = 5 + 20 * 3 - base_year
#
# epoch = year / year_in_different_form
#
# x = (year,
#     epoch,
#     year_in_different_form,
#     base_year)


# x = 5
# print(x/2 - x//2)

# True
# False

# 5 - integer
# 3.14 float
# 'H' - char
# name = input("Enter your name: ")
# base_str = "Hello {name_user}"
# result = base_str.format(name_user=name)
# result = f'Hello {name}'
# print(result)

# age = int(input("Enter age: "))
#
# if age <= 18: # -> True
#     if age <= 7:
#         print("You are child!")
#     else:
#         print("You are young!")
# elif age > 18 and age < 40:
#     print("You are in a best age!")
# else: # -> False
#     print("I can't identify your age.")
#
# print("End")

year = int(input("Enter year of birth: "))

CURRENT_YEAR = 2022

if year > 0 and year < CURRENT_YEAR:
    user_age = CURRENT_YEAR - year
    print(f"Your age is {user_age}")
else:
    print(f"Entered year is not in bounds. Please enter value in 0 to {CURRENT_YEAR}")
