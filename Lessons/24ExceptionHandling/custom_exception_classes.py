class BankError(Exception):
    "Exception class of whole project"


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f"Balance: {balance}$, requested {amount}$")
        self.balance = balance
        self.amount = amount


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(e)
    print(e.amount - e.balance)
