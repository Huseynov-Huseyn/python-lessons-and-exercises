from Account import Account
from InsufficientFundsError import InsufficientFundsError


class CheckingAccount(Account):
    ACCOUNT_TYPE = "CHECKING"
    OVERDRAFT_LIMIT = -200
    MONTHLY_FEE = -3.00

    def _check_withdrawal(self, amount):
        if (self.balance - amount) < self.OVERDRAFT_LIMIT:
            raise InsufficientFundsError(self.balance, amount)

    def monthly_update(self):
        self._apply_change(self.MONTHLY_FEE, "FEE")
        return self.MONTHLY_FEE
