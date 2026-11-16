from FileProcessingError import FileProcessingError
from MyCustomError import MyCustomError

err = MyCustomError("Invalid operation", 400)
print(err)


def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero not allowed!", 400)
    return a / b


try:
    divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")

try:
    raise FileProcessingError("Syntax error", "example.txt", 13)
except FileProcessingError as e:
    print(f"Caught an error: {e}")
