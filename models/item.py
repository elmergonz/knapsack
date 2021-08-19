class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __iter__(self):
        return iter((self.name, self.weight, self.value))
