import random
from unittest.mock import Mock, MagicMock


class ProductionClass:

    def method(self):
        x = random.randint(1, 100)
        value = self.some_method(x)  # -> 50
        if value == 50:
            print("got value", value)
        if value < 0:
            raise AssertionError("Assertion! Below Zero")
        return value

    def some_method(self, x=1):
        print("Generate data")
        y = random.randrange(x, 10000)
        return y  # 50 1 - 10000,


# Test or Override
# real = ProductionClass()
# random.randrange = MagicMock()
# random.randrange.return_value = 1000
#
# print("::", real.method())  # --> 1000
#
# import requests
# import json
#
# url = "https://www.youtube.com/"

# real.method() # 50, 0, -10, 9999
#
# ProductionClass.some_method = MagicMock()
# real.some_method.return_value = 50 # self.some_method()
# # real.some_method.side_effect = AssertionError
# real.method()
# real.some_method.assert_called_once_with(5)
