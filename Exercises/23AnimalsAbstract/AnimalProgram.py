"""
================================================================================
Exercise 23: Animals (Abstract Class, Inheritance, Polymorphism, Magic Methods)
Topics: ABC, @abstractmethod, inheritance, super(), override, polymorphism,
        __eq__, __gt__, __add__, TypeError
================================================================================

CONCEPTS (read first)
--------------------------------------------------------------------------------
- Inheritance: class Dog(Animal) means Dog gets everything Animal has
  (Java's `extends`).

- super(): calls the parent class. In a child constructor, super().__init__(...)
  initializes the inherited part, then the child adds its own attributes.

- Abstract class (like Java's abstract class): import ABC and abstractmethod from
  the `abc` module, inherit from ABC and put @abstractmethod above methods that
  have no real body. You CANNOT create an object of an abstract class (Python
  raises TypeError). Every child must implement all abstract methods, otherwise
  the child stays abstract too and cannot be instantiated.

- Override: a child writes its own version of a parent method (same name).

- Polymorphism: the same call gives different behavior depending on the real
  object type. You loop over a list of mixed objects and call the same method;
  each object runs its own version, with no if/isinstance checks.

- Magic methods let your objects work with operators. In each of them `self` is
  the LEFT object and `other` is the RIGHT object:
    __eq__(self, other)   for  a == b
    __gt__(self, other)   for  a > b
    __add__(self, other)  for  a + b

TASK
--------------------------------------------------------------------------------
Animal(ABC):
  - Constructor: Animal(name, age). If age is negative, raise ValueError with a
    message that shows the given age.
  - Abstract method make_sound() (returns the sound as a string).
  - Normal method describe(): returns a string like "Rex (3 years old): Woof".
    Inside it, call self.make_sound().
  - Magic methods (written in Animal):
        __eq__  : True if the ages are equal
        __gt__  : True if the left animal's age is greater
        __add__ : returns the sum of the two ages (a number, not a new animal)

Child classes:
  - Dog(Animal):  make_sound() returns "Woof"
  - Cat(Animal):  make_sound() returns "Meow"
  - Bird(Animal): extra attribute can_fly (default True).
                  Call super().__init__(name, age) in its constructor.
                  make_sound() returns "Tweet"

In main(), test each case in its OWN try block:
  1. Animal("X", 3) -> TypeError. Catch it with a general `except Exception`
     and read the message.
  2. Dog("Rex", -1) -> ValueError
  3. Put a Dog, a Cat and a Bird in ONE list. Loop over it and print
     describe() for each. There must be NO if/isinstance inside the loop.
     This is the main goal of the exercise: same code, different results.
  4. Compare two animals with ==, > and +, and print the results.
  5. Experiment: delete make_sound() from Bird and try Bird("Tom", 1).
     What happens? Then put the method back.
  Every block has finally: print("Done.")

EXPECTED OUTPUT (format is free, numbers must be right)
--------------------------------------------------------------------------------
Rex (3 years old): Woof
Luna (2 years old): Meow
Tom (1 years old): Tweet
Rex > Luna : True
Rex + Luna : 5
Rex == Luna : False

SELF-CHECK
--------------------------------------------------------------------------------
  [ ] Animal cannot be instantiated directly
  [ ] Every child implements make_sound()
  [ ] Bird.__init__ calls super().__init__(name, age)
  [ ] The polymorphism loop has no if/isinstance
  [ ] Negative age raises ValueError with the number in the message
================================================================================
"""


# Write ALL your code below this line.
def main():
    pass


if __name__ == '__main__':
    main()
