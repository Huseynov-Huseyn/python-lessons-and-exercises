from Animal import Animal


class Dog(Animal):
    def __init__(self, name, color, is_alive, breed):
        # Calls constructor based on MRO
        super().__init__(name, color, is_alive)
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)
