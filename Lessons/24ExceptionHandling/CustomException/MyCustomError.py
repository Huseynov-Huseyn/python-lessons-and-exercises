class MyCustomError(Exception):
    """Exceptions raised for custom error scenarios"""

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        # passage the message to the base exception class
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
