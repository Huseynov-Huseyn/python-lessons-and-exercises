from BankError import BankError


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount, message="Insufficient Funds "):
        self.balance = balance
        self.amount = amount
        super().__init__(f"{message},your balance: {balance:.2f} and amount: {amount:.2f}")
