# *args - tuple() произвольное число позиционных аргументов
# *kwargs - dict() произвольное число именованных аргументов

# def func(*args):
#     for arg in args:
#         print(arg)
#
#
# func(10)
#
# scores = [19, 92, 93, 94, 65]
#
#
# def printScores(student, *scores):
#     print(f"Student Name: {student}")
#     total_score = 0
#     for score in scores:
#         total_score += score
#     print(f"Total score: {total_score}")
#
#
# printScores("Jonathan", *scores)

animals = {'dog': 'Brock', 'fish': ["Larry", "Curly", "Moe"], 'turtle': 'Shelldon'}


def printPetName(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


printPetName("Jonathan", **animals)
