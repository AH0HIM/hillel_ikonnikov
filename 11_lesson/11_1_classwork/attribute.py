# __new__(cls[, ...]) Конструктор. Создает экземпляр (объект) класса. Сам класс передается в качестве аргумента; Функция
# __init(self[, ...]) Инициализатор. Принимает свежесозданный объект класса из конструктора; Функция
# __del__(self) Деструктор. Вызывается при удалении объекта сборщика мусора; Функция
# __str__(self) Возвращает строковое преставление объекта; Функция
# __doc__ Документ класса; Строка (тип str)
# __dic__ Словарь, в котором хранится пространство имен класса; Словарь (тип dict)


class Dog:
    """Example class. To show magic method"""

    def __new__(cls, *args, **kwargs):
        print("Hello, I create object")
        return super(Dog, cls).__new__(cls)

    def __init__(self, name, age):
        print("Hello, I start initialization object")
        self.name = name
        self.age = age

    def __del__(self):
        class_name = self.__class__.__name__
        return f'{class_name} destroyed'

    def __str__(self):
        return f"Dog {self.name} with {self.age} year old. My class with name {self.__class__.__name__}"


obj = Dog('Rex', 3)
print(obj.__class__.__dict__)
print(obj)
print(Dog.__doc__)
