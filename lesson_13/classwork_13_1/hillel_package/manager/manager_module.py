from lesson_13.classwork_13_1 import hillel_package
from lesson_13.classwork_13_1.hillel_package.creator.creator_module import Creator


class Manager:
    """Class to represent manager"""
    DEFAULT_MANAGER = 'Jordan'

    def __init__(self, name, request):
        self.name = name
        self.request = request
        self.creators = []

    def add_creator(self, name):
        creator = Creator(name)
        self.creators.append(creator)
        return creator

    def proceed_request(self):
        print(f"Running {self.name} request {self.request}")


if __name__ == "__main__":
    mc = hillel_package.creator.MainClass()
    mc.hello(f"Hello from {__file__}")
    manager = Manager("Jordan", "empty")
    manager.proceed_request()
