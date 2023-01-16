from classes.Person import Athlete


class Gym:
    def __init__(self):
        self.athletes = []

    def add(self):
        name = input("Enter name: ")
        sex = input("Enter f for female and m for male: ")
        age = float(input("Enter age(10 to 90): "))
        weight = float(input("Enter weight(25 to 130): "))
        if 10 <= age <= 90 and 25 <= weight <= 130:
            athlete = Athlete(name, sex, age, weight)
            self.athletes.append(athlete)
        else:
            print("Error in data")

    def find(self, name):
        for item in self.athletes:
            if item.name == name:
                return item

    def find_and_print(self):
        finding = self.find(input("Enter name: "))
        if finding is not None:
            sex = ""
            if finding.sex == "f":
                sex = "Female"
            elif finding.sex == "m":
                sex = "Male"
            print(f"""
            ------------------------------------------
            name: {finding.name}
            sex: {sex}
            age: {finding.age}
            weight: {finding.weight}
            program: {finding.program}
            ------------------------------------------
            """)
        else:
            print("Nothing Found")

    def print_all(self):
        counter = 1
        for item in self.athletes:
            print(f"{counter}.{item.name}")
            counter += 1
