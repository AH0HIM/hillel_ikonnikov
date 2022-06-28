# Используем инкапсуляцию данных

class People:

    def __init__(self):
        self.__password = "__password"    # protect
        self._username = "_username"      # privet
        self.name = "name"                # public

    def print_password(self):
        print(f"Password is: {self.__password}")

    def print_username(self):
        print(f"Username is: {self._username}")

    def set_pass(self, password):
        self.__password = password

    def set_username(self, username):
        self._username = username


c = People()
# print(c.name)
# print(c._username)
# print(c._People__password)
#
# print(c.__dict__)

# изменение цены
c.print_password()
c.print_username()

# используем функцию изменения цены
c.set_pass("New_password")
c.set_username("New_username")
c.print_password()
c.print_username()
