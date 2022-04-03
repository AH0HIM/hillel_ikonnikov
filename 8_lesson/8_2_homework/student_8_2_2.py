"""
5. Изучите код программы с сегодняшнего занятия
6. Добавьте по 2 homeworks для каждого студента
7. Напишите метод для класса Student, который будет изменять status homework для конкретного задания
8. Добавьте класс Table, который должен содержать в себе всех студентов
9. Реализуйте метод в классе Table, для вывода информации о студентах и статусах homeworks в консоль
10. Добавьте 2 студента, проверьте, что метод из задания 5 работает для любого количества студентов
"""


class Homework:
    def __init__(self, homework_name, description, status):
        self.homework_name = homework_name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.homework_name}, {self.description}, {self.status}"

    def change_status(self, status):
        self.status = status


class Student:
    def __init__(self, name, points, place):
        self.name = name
        self.points = points
        self.place = place
        self.homeworks = []

    def __str__(self):
        messages = f'{self.name}, place: {self.place}, points: {self.points}'
        messages = messages + "\n\t\tHomeworks:\n"
        for homework in self.homeworks:
            messages += f"\t{homework} \n"
        return messages

    def add_homework(self, homework):
        self.homeworks.append(homework)


class Table:
    def __init__(self):
        self.students = []

    def __str__(self):
        message = "Students: \n"
        for student in self.students:
            message += f"\t{student} \n"
        return message

    def add_student(self, student):
        self.students.append(student)

    def add_homework_for_all_students(self, homework):
        for i in range(len(self.students)):
            students[i].add_homework(
                Homework(homework.homework_name, homework.description, homework.status))


students = [
    Student("Ярослав", 800, 1),
    Student("Илья", 700, 2),
    Student("Анна", 695, 3),
    Student("Алёна", 600, 4),
    Student("Ксения", 695, 5),
    Student("Сергей", 470, 6),
    Student("Владислав", 390, 7),
    Student("Игорь", 290, 8),
    Student("Андрей", 100, 9)
]

homeworks = [
    Homework("\t-\thomework_8", 'Exception\OOP', False),
    Homework("\t-\thomework_7", 'Работа с файлами', True),
    Homework("\t-\thomework_6", 'Лямбда функции', True),
    Homework("\t-\thomework_5", 'Git\Функции\Рекурсия', True),
    Homework("\t-\thomework_4", 'Кортежи\Множества', True),
    Homework("\t-\thomework_3", 'Циклы\Списки\Словари', True),
    Homework("\t-\thomework_2", 'Типы данных. Строки', True),
    Homework("\t-\thomework_1", 'Введение в Python', True)
]

table = Table()

for st in students:
    table.add_student(st)

for hm in homeworks:
    table.add_homework_for_all_students(hm)

print(table)
