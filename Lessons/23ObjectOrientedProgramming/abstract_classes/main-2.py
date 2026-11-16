# Abstract class = a class that cannot be instantiated on its own(cannot be subclassed)
#                  They can contain abstract methods,which are declared but have no implementation
#                  Benefits:
#                  1. Prevents instantiation of the class itself
#                  2. Requires children to use inherited abstract methods


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car!")

    def stop(self):
        print("You stop the car!")

    # vehicle1=Vehicle() cannot create an object from abstract class


car1 = Car()
print(car1)
