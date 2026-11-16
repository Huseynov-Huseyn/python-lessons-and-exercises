# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Objects must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"
from Car import Car
from Cat import Cat
from Dog import Dog

Animals = [Car(), Cat(), Dog()]
for animal in Animals:
    animal.speak()
    print(animal.is_alive)
