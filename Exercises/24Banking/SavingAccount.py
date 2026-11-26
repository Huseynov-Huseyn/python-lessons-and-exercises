from Account import Account
from InsufficientFundsError import InsufficientFundsError
from WithdrawalLimitError import WithdrawalLimitError


class SavingAccount(Account):
    ACCOUNT_TYPE = "SAVINGS"
    MAX_WITHDRAWALS = 3

    def __init__(self, owner, pin, initial_deposit, interest_rate=0.02):
        super().__init__(owner, pin, initial_deposit)
        self.interest_rate = interest_rate
        self.withdrawal_counter = 0

    def _check_withdrawal(self, amount):
        if self.withdrawal_counter >= self.MAX_WITHDRAWALS:
            raise WithdrawalLimitError()
        if (self.balance - amount) < 0:
            raise InsufficientFundsError(self.balance, amount)

    def _debit(self, amount, kind):
        new_balance = super()._debit(amount, kind)
        self.withdrawal_counter += 1
        return new_balance

    def monthly_update(self):
        interest_amount = self.balance * self.interest_rate
        self._apply_change(interest_amount, "INTEREST")
        self.withdrawal_counter = 0
        return interest_amount
