from lesson_13.classwork_13_1.hillel_package import Creator, Manager, print


class MainApp:
    def __init__(self, manager_name, creator_name):
        self.manager_name = manager_name
        self.creator_name = creator_name
        self.manager = Manager(manager_name, "main request")
        self.creator = Creator(creator_name)

    def run(self):
        self.manager.proceed_request()
        self.creator.create_package("default path")


if __name__ == "__main__":
    print("Run myApp")
    app = MainApp("John", "Sarah")
    app.run()
    print("Done")