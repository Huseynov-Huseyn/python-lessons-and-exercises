from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError(f"Age must be positive! Your age is: {age}")
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        return f"{self.name} ({self.age} years old): {self.make_sound()}"

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __add__(self, other):
        return self.age + other.age
