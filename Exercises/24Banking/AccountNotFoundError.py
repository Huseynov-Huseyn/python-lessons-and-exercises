from BankError import BankError


class AccountNotFoundError(BankError):
    def __init__(self, account_number, message="Account cannot find. "):
        self.account_number = account_number
        super().__init__(message + f"Account number: {account_number}")
