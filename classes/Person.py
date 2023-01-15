class Person:
    def __init__(self, name: str, sex: str, age: float, weight: float):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight

    def __str__(self):
        return self.name


class Athlete(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.program = Program(self)


test = Athlete("ali", "m", 17, 60, "test")
test.print()
