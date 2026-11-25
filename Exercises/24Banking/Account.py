from abc import ABC, abstractmethod

from InvalidAmountError import InvalidAmountError


class Account(ABC):
    def __init__(self, owner, pin, initial_deposit):
        if not self.validate_owner(owner):
            raise ValueError("Owner must be a non-empty string")
        self.owner = owner
        if not self.validate_pin(pin):
            raise ValueError("PIN must be a string of exactly 4 digits")
        self.__pin = pin
        if not isinstance(initial_deposit, (int, float)) or isinstance(initial_deposit, bool) or initial_deposit < 10:
            raise InvalidAmountError("Initial deposit must be at least 10.00 Azn")
        self._balance = initial_deposit

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

    @property
    def get_balance(self):
        return self._balance

    @abstractmethod
    def monthly_update(self):
        pass
