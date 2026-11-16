class Animal:
    def __init__(self, name, color, is_alive):
        self.name = name
        self.color = color
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
