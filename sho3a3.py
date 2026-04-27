class Sho3a3:
    def __init__(self, numbers: list):
        self.sho3a3 = numbers
        self._shape = (1, len(numbers))

    def __repr__(self):
        return f"sho3a3:{self.sho3a3}"

    def __str__(self):
        return self.__repr__()
