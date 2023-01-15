class Sport:
    def __init__(self, name: str, numberOrTime: int):
        self._name = name
        if name.lower() == "plank":
            self._time = numberOrTime
        else:
            self._number = numberOrTime

    @property
    def name(self):
        return self._name

    @property
    def time(self):
        if self._name.lower() == "plank":
            return self._time

    @property
    def number(self):
        if self._name.lower() != "plank":
            return self._time