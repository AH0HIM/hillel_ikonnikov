# super() - это встроенная функция языка Python. Она возвращает прокси-объект,
# который делегирует вызовы методов классу-родителя (или собрату) текущего класса
# (или класса на выбор, если он указан, как параметр)


# class Base:
#     def price(self):
#         return 10
#
#
# class Sale(Base):
#     def price(self):
#         return super().price() * 0.9
#
#
# class Discount(Sale):
#     def price(self):
#         return super().price() * 0.8
#
#
# d = Discount()
# print(d.price())


#  ============================================================================
class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


print(B().y)
#  ============================================================================
