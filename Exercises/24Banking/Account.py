import math
from abc import ABC, abstractmethod

from AccountLockedError import AccountLockedError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError
from Transaction import Transaction


class Account(ABC):
    account_counter = 1
    ACCOUNT_TYPE = "ACCOUNT"
    max_failed_pin_attempt = 3

    def __init__(self, owner, pin, initial_deposit):
        if not self.validate_owner(owner):
            raise ValueError("Owner must be a non-empty string")
        self.owner = owner
        if not self.validate_pin(pin):
            raise ValueError("PIN must be a string of exactly 4 digits")
        self.__pin = pin
        self.validate_amount(initial_deposit)
        if initial_deposit < 10:
            raise InvalidAmountError("Initial deposit must be at least 10.00 AZN")
        self._balance = 0
        self.failed_pin_counter = 0
        self.is_locked = False
        self.account_number = f"AZ{Account.account_counter:04d}"
        self.transactions = list()
        self._apply_change(initial_deposit, "DEPOSIT")
        Account.account_counter += 1

    @staticmethod
    def validate_owner(owner):
        if not isinstance(owner, str) or len(owner.strip()) == 0:
            return False
        return True

    @staticmethod
    def validate_pin(pin):
        if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            return False
        return True

    @staticmethod
    def validate_amount(amount):
        if (not isinstance(amount, (int, float))
                or isinstance(amount, bool)
                or not math.isfinite(amount)
                or amount <= 0):
            raise InvalidAmountError("Amount must be a number greater than zero")

    @abstractmethod
    def _check_withdrawal(self, amount):
        """Subclass raises an exception when the withdrawal is not allowed."""

    def _apply_change(self, change, kind):
        new_balance = self._balance + change
        record = Transaction(kind, abs(change), new_balance)
        self._balance = new_balance
        self.transactions.append(record)
        return new_balance

    def _debit(self, amount, kind):
        self.validate_amount(amount)
        self._check_withdrawal(amount)
        return self._apply_change(-amount, kind)

    def check_pin(self, pin):
        if self.is_locked:
            raise AccountLockedError()
        if self.__pin != pin:
            self.failed_pin_counter += 1
            if self.failed_pin_counter >= self.max_failed_pin_attempt:
                self.is_locked = True
                raise AccountLockedError()
            raise InvalidPinError(self.max_failed_pin_attempt - self.failed_pin_counter)
        self.failed_pin_counter = 0
        return True

    def deposit(self, amount):
        self.validate_amount(amount)
        return self._apply_change(amount, "DEPOSIT")

    def withdraw(self, amount):
        return self._debit(amount, "WITHDRAW")

    def transfer_out(self, amount):
        return self._debit(amount, "TRANSFER OUT")

    def transfer_in(self, amount):
        self.validate_amount(amount)
        return self._apply_change(amount, "TRANSFER IN")

    def statement(self):
        return [str(t) for t in self.transactions]

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def monthly_update(self):
        """Signed balance change: positive for interest, negative for a fee."""

    def __str__(self):
        return f"{self.account_number} | {self.owner} | {self.ACCOUNT_TYPE} | {self.balance:.2f} AZN"

    def __repr__(self):
        return f"{self.__class__.__name__} | {self.account_number} | {self.owner}"

    def __lt__(self, other):
        return self.balance < other.balance

    def __len__(self):
        return len(self.transactions)
