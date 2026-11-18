"""
================================================================================
Exercise 20: Book Class (Class Basics)
Topics: class, __init__, self, attributes, methods, __str__, class variable
================================================================================

CONCEPTS (read first)
--------------------------------------------------------------------------------
- A class is a blueprint. An object is one thing created from that blueprint.
- __init__ is the constructor. It runs automatically when you create an object.
- `self` is the object itself (Java's `this`). It is the first parameter of every
  normal method, and you do not pass it when calling the method.
- Attributes (instance variables) are created by assigning to self.<name>.
  Every object has its own copy.
- A class variable is defined directly in the class body, outside any method.
  It is shared by all objects. Change it through the class name, not through
  self (self.x += 1 would create a separate instance attribute instead).
- __str__ is called by print(obj). It must RETURN a string, not print it.

Java -> Python: constructor = __init__, this = self, toString() = __str__,
static field = class variable.

TASK
--------------------------------------------------------------------------------
Write a `Book` class for a library.

Constructor: Book(title, author, pages)
  - Also create an attribute `is_borrowed`. It starts as False and is NOT a
    constructor parameter.

Class variable:
  - total_books: starts at 0, increases by 1 every time a Book is created.

Methods:
  - borrow()    : marks the book as borrowed.
  - give_back() : marks the book as returned.

Magic method:
  - __str__ returns one of these formats:
        "Atomic Habits | James Clear | 320 pages | Available"
        "Atomic Habits | James Clear | 320 pages | Borrowed"

In main():
  1. Create 3 books.
  2. Borrow one of them.
  3. Print all 3 books.
  4. Print Book.total_books (must be 3).
  5. Give the borrowed book back and print it again.

EXPECTED OUTPUT (format is free, values must be right)
--------------------------------------------------------------------------------
Atomic Habits | James Clear | 320 pages | Borrowed
Clean Code | Robert Martin | 464 pages | Available
Sapiens | Yuval Harari | 443 pages | Available
total_books = 3
Atomic Habits | James Clear | 320 pages | Available

SELF-CHECK
--------------------------------------------------------------------------------
  [ ] Every method has `self` as the first parameter
  [ ] is_borrowed is not a constructor parameter
  [ ] total_books is shared (not reset for every new book)
  [ ] __str__ returns a string (it does not print)
================================================================================
"""


# Write ALL your code below this line.
def main():
    pass


if __name__ == '__main__':
    main()
