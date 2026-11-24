from BankError import BankError


class InvalidPinError(BankError):
    def __init__(self, attempts_left, message="Wrong PIN!"):
        self.attempts_left = attempts_left
        super().__init__(f"{message} Attempts left: {attempts_left}")
