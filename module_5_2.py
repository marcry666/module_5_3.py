class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, new_floor + 1):
            if new_floor < 1 or new_floor > self.numbers_of_floors:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __str__(self):
        return f'Названеие: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __len__(self):
        return self.numbers_of_floors

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        self.numbers_of_floors = self.numbers_of_floors + value
        return self.numbers_of_floors

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.numbers_of_floors += value
            return self
        return NotImplemented
    # с __iadd__ не совсем понял как именно реализовать метод, прибег к помощи чпт

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
