"""
4. Создайте функцию showEmployee() таким образом, чтобы она принимала имя сотрудника и его зарплату и отображала и то,
и другое. Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.
"""


def show_employee(name, salary=9000):
    print(f"Имя сотрудника: {name}. Зарплата сотрудника: {salary}")


show_employee("Илья")
show_employee("Николай", 1000)