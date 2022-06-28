LOCAL_VAR = "Docker"


class Parrot:

    # атрибуты класса
    species = "bird"

    # атрибуты экземпляра
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # методы класса
    def my_name_is(self) -> str:
        return f'My name is {self.name}'

    def print_local_var(self) -> str:
        return f'Local variable is {LOCAL_VAR}'


# создаем экземпляр класса
python = Parrot("python", 10)
cookie = Parrot("cookie", 15)


# получаем доступ к атрибутам класса
print(f"python - {python.__class__.species}")
print(f"cookie - {cookie.__class__.species}")
# TODO @classmethod to be continue

# получаем доступ к атрибутам экземпляра
print(f"{python.name} - {python.age} - year old")
print(f"{cookie.name} - {cookie.age} - year old")

# получаем доступ к методам класса
print(python.my_name_is())
print(python.print_local_var())
