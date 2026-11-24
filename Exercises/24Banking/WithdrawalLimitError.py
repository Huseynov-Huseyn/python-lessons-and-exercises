from BankError import BankError


class WithdrawalLimitError(BankError):
    def __init__(self, message="You reached Withdraw limit!"):
        super().__init__(message)
