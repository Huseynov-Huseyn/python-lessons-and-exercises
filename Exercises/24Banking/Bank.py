from AccountNotFoundError import AccountNotFoundError
from BankError import BankError
from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount


class Bank:
    BANK_NAME = "Master Bank"
    # {Account_number:Account}
    ACCOUNT_TYPES = ["savings", "checking"]

    def __init__(self):
        self.accounts = dict()

    def open_account(self, kind, owner, pin, initial_deposit):
        kind = kind.lower().strip()
        account = None
        if kind not in self.ACCOUNT_TYPES:
            raise ValueError("Unknown kind!")
        elif kind == "savings":
            saving_account = SavingAccount(owner, pin, initial_deposit)
            self.accounts[saving_account.account_number] = saving_account
            account = saving_account
        elif kind == "checking":
            checking_account = CheckingAccount(owner, pin, initial_deposit)
            self.accounts[checking_account.account_number] = checking_account
            account = checking_account
        return account

    @classmethod
    def from_lines(cls, lines):
        bank = cls()
        for line_number, line in enumerate(lines, start=1):
            try:
                parts = [part.strip() for part in line.split(",")]
                kind, owner, pin, deposit_text = parts
                deposit = float(deposit_text)
                bank.open_account(kind, owner, pin, deposit)
            except (ValueError, BankError) as e:
                raise ValueError(f"Line {line_number} is invalid: {e}") from e
        return bank

    def find(self, number):
        if number not in self.accounts:
            raise AccountNotFoundError(number)
        return self.accounts[number]

    def deposit(self, number, amount):
        account = self.find(number)
        return account.deposit(amount)

    def withdraw(self, number, pin, amount):
        account = self.find(number)
        account.check_pin(pin)
        return account.withdraw(amount)

    def transfer(self, from_number, to_number, amount, pin):
        if from_number == to_number:
            raise ValueError("In transfer, source and destination must be different")
        from_account = self.find(from_number)
        to_account = self.find(to_number)
        from_account.validate_amount(amount)
        from_account.check_pin(pin)
        from_account._check_withdrawal(amount)
        from_account.transfer_out(amount)
        to_account.transfer_in(amount)
        return from_account.balance

    def balance_of(self, number, pin):
        account = self.find(number)
        account.check_pin(pin)
        return account.balance

    def statement_of(self, number, pin):
        account = self.find(number)
        account.check_pin(pin)
        return account.statement()

    def total_balance(self):
        total = 0
        all_accounts = self.accounts.values()
        for account in all_accounts:
            total += account.balance
        return total

    def ranking(self):
        return sorted(self.accounts.values(), reverse=True)

    def apply_monthly_updates(self):
        accounts = self.accounts.values()
        accounts_monthly_change = dict()
        for account in accounts:
            accounts_monthly_change[account.account_number] = account.monthly_update()
        return accounts_monthly_change

    def __len__(self):
        return len(self.accounts)

    def __contains__(self, item):
        return item in self.accounts
