class Menu:
    def __init__(self, data: dict):
        self._data = data
        self.rules = []

    @property
    def _msg(self):
        counter = 1
        temp = "\n\n"
        for key in self._data.keys():
            temp += f"{counter}.{key}\n"
            counter += 1
        return temp

    def any_rules(self, inp):
        for item in self.rules:
            if item(inp):
                return True
        else:
            return False

    @property
    def _choices(self):
        counter = 1
        temp = {}
        for item in self._data.keys():
            temp[f"{counter}"] = item
            counter += 1
        return temp

    def run(self):
        while True:
            print(self._msg)
            inp = input("Choice a number(enter exit for exit):")
            if self.any_rules(inp) and self.rules:
                break
            if inp == "exit":
                break
            if inp in self._choices.keys():
                key = self._choices[inp]
                self._data[key]()
