from BankError import BankError


class InvalidAmountError(BankError):
    def __init__(self, message="Invalid amount"):
        super().__init__(message)
