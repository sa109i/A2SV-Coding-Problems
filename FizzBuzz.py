class Item:
    def __init__(self, age: int):
        self.age = age

    def birthYear(self) -> int:
        return 2023 - self.age

item1 = Item('21')
print(item1.birthYear())
