from BankError import BankError


class AccountLockedError(BankError):
    def __init__(self, message="Bank account locked!"):
        super().__init__(message)
