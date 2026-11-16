# Polymorphism = the same method name or operation behaves differently
#   depending on the object it is called on
# Polymorphism -> two ways to achieve
# Inheritance = An object could be treated of the same type as a parent class
# Duck typing = Objects must have necessary attribute/methods
from Circle import Circle
from Triangle import Triangle

circles = Circle(5)
triangles = Triangle(5, 10)
shapes = [circles, triangles]
for shape in shapes:
    print(f"{shape.area()}cm")
