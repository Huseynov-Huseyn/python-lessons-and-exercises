"""
================================================================================
Exercise 21: Exception Handling Basics (Age and Phone Validation)
Topics: try / except / else / finally, ValueError, raise, except order
================================================================================

CONCEPTS (read first)
--------------------------------------------------------------------------------
- An exception is an error that happens while the program runs. If nobody
  handles it, the program crashes. try/except lets you handle it.
- try:     the code that might fail.
- except:  runs only if that type of exception happened. `except ValueError as e`
           gives you the error object `e`; print(e) shows its message.
- else:    runs only if NO exception happened.
- finally: runs ALWAYS, error or not (good for final messages and cleanup).
- Python raises some exceptions by itself, for example int("abc") raises
  ValueError and 10 / 0 raises ZeroDivisionError.
- You can raise an exception yourself with the `raise` keyword, for example
  raise ValueError("some message").
- Several except blocks are checked top to bottom and the FIRST match wins.
  Write them from specific to general. `except Exception` catches everything, so
  it must be LAST, otherwise the blocks below it can never run.
- Good error messages show the real values (for example the number that was
  given), not only a general sentence.

TASK
--------------------------------------------------------------------------------
No classes in this exercise, only functions.

parse_age(text):
  - Converts the text to int. If the text is not a number, Python raises
    ValueError by itself (do not catch it inside this function).
  - If the age is < 0 or > 120, YOU raise ValueError and the message shows the
    given number: "Age must be between 0 and 120, given: 150"
  - Otherwise return the age as int.

check_phone(phone):
  - The number must start with "+994" and its length must be 13.
  - If not, raise ValueError with a clear message that shows the given value.
  - If valid, return True.

In main(), test each case in its OWN try block:
  - parse_age with: "25", "abc", "150", "-3"
  - check_phone with: "+994501234567", "0501234567"

Every block must have:
  - except ValueError as e: print the message
  - else:                   print the successful result
  - finally:                print "Check finished."

Notice the difference: the message for "abc" is written by Python, the message
for "150" is written by you.

EXTRA EXPERIMENT
--------------------------------------------------------------------------------
Temporarily put `except Exception` ABOVE `except ValueError` in one block and see
what happens. Then put it back in the correct order.

EXPECTED OUTPUT (format is free)
--------------------------------------------------------------------------------
Age OK: 25
Check finished.
Error: invalid literal for int() with base 10: 'abc'
Check finished.
Error: Age must be between 0 and 120, given: 150
Check finished.
...

SELF-CHECK
--------------------------------------------------------------------------------
  [ ] Each scenario has its own try block
  [ ] else runs only on success, finally runs every time
  [ ] The range error message contains the real number
  [ ] `except Exception` (if used) is the LAST except block
================================================================================
"""


# Write ALL your code below this line.
def main():
    try:
        number = parse_age("25")
    except ValueError as e:
        print(e)
    else:
        print(number)
    finally:
        print("Check finished.")

    try:
        number = parse_age("abc")
    except ValueError as e:
        print(e)
    else:
        print(number)
    finally:
        print("Check finished.")

    try:
        number = parse_age("150")
    except ValueError as e:
        print(e)
    else:
        print(number)
    finally:
        print("Check finished.")

    try:
        number = parse_age("-3")
    except ValueError as e:
        print(e)
    else:
        print(number)
    finally:
        print("Check finished.")

    try:
        phone1 = check_phone("+994501234567")
    except ValueError as e:
        print(e)
    else:
        print(phone1)
    finally:
        print("Check finished.")

    try:
        phone1 = check_phone("0501234567")
    except ValueError as e:
        print(e)
    else:
        print(phone1)
    finally:
        print("Check finished.")


def parse_age(text):
    number_text = int(text)
    if number_text > 120 or number_text < 0:
        raise ValueError(f"Age must be between 0 and 120, given: {number_text}")
    return number_text


def check_phone(phone):
    if phone.startswith("+994") and len(phone) == 13:
        return True
    else:
        raise ValueError("The number must start with '+994' and its length must be 13.")


if __name__ == '__main__':
    main()
