"""
================================================================================
Exercise 22: Student (Custom Exception, Property/Setter, Static and Class Methods)
Topics: custom exception, @property, @<name>.setter, validation, @staticmethod,
        @classmethod, raise
================================================================================

CONCEPTS (read first)
--------------------------------------------------------------------------------
- Custom exception: create your own error type by inheriting from Exception.
  Define it BEFORE the class that raises it. Raise it like any other exception,
  with a message that shows the real values.

- Property and setter: the real value is stored in an attribute with a single
  underscore (for example _grade). This underscore is only a convention that
  means "internal, do not touch from outside".
    * @property above a method named `grade` makes it the getter. It runs when
      you read student.grade.
    * @grade.setter above a method ALSO named `grade` makes it the setter. It
      runs when you write student.grade = 5, and it is the place for validation.
    * Both methods have the same name. The setter decorator is always
      @<property_name>.setter.
    * In the constructor write self.grade = grade (NOT self._grade = grade).
      Then the setter runs during object creation and the validation is written
      only once.

- @staticmethod: a helper function inside the class that needs neither self nor
  cls. It is called like Student.is_passing(70).

- @classmethod: receives the class itself as the first parameter (`cls`).
  Mostly used as an "alternative constructor": it parses some input and returns
  cls(...). It is called on the class: Student.from_string("Aysel-85").
  Useful string tool: text.split("-") returns a list of parts.

TASK
--------------------------------------------------------------------------------
Write the exception class first, then the Student class.

Exception class:
  InvalidGradeError(Exception)
  - You raise it with a message that shows the number, for example:
        "Grade must be between 0 and 100, given: 105"

Student(name, grade=0):
  - name (str) and _grade (single underscore).
  - `grade` property (getter) returns the grade.
  - `grade` setter: if the value is outside 0..100, raise InvalidGradeError.
    0 and 100 are allowed.
  - The constructor must assign with self.grade = grade so the setter runs.
  - @staticmethod is_passing(grade): True if grade >= 50, else False.
  - @classmethod from_string(cls, text): builds a student from "Aysel-85".
    If the format is wrong (the number of parts is not 2, or the grade is not a
    number), raise ValueError with a clear message.
  - __str__: "Aysel | 85 | Passed"  or  "Aysel | 40 | Failed"
    (use is_passing inside __str__).

In main(), test each case in its OWN try block:
  1. Create a valid student and print it.
  2. Student("Leyla", 105)                -> InvalidGradeError
  3. s.grade = -5 on an existing student  -> InvalidGradeError
  4. Student.from_string("Aysel-85")      -> works
     Student.from_string("Aysel85")       -> ValueError
     Student.from_string("Aysel-abc")     -> ValueError
  5. Every block has finally: print("Done.")

Order your except blocks from specific to general:
InvalidGradeError, ValueError, Exception.

EXPECTED OUTPUT (format is free)
--------------------------------------------------------------------------------
Aysel | 85 | Passed
Error: Grade must be between 0 and 100, given: 105
Error: Grade must be between 0 and 100, given: -5
...

SELF-CHECK
--------------------------------------------------------------------------------
  [ ] The constructor uses self.grade = grade (not self._grade)
  [ ] Getter and setter have the same name: grade
  [ ] 0 and 100 are accepted
  [ ] from_string tested with a correct AND wrong strings
  [ ] The exception class is defined above the Student class
================================================================================
"""

from InvalidGradeError import InvalidGradeError
# Write ALL your code below this line.
from Student import Student


def main():
    s1 = Student("Huseyn", 85)
    print(s1)
    try:
        s2 = Student("Muhammed", 125)
    except InvalidGradeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Done.")

    try:
        s2 = Student("Muhammed", 90)
        s2.grade = -5
    except InvalidGradeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Done.")

    try:
        s2 = Student.from_string("Huseyn-95")
    except InvalidGradeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Done.")

    try:
        s2 = Student.from_string("Huseyn95")
    except InvalidGradeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Done.")

    try:
        s2 = Student.from_string("Huseyn-as")
    except InvalidGradeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Done.")


if __name__ == '__main__':
    main()
