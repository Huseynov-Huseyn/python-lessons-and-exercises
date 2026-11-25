class Transaction:
    KINDS = ["DEPOSIT", "WITHDRAW", "TRANSFER IN", "TRANSFER OUT", "INTEREST", "FEE"]

    def __init__(self, kind, amount, balance_after):
        if kind not in self.KINDS:
            raise ValueError(f"Unacceptable transaction kind: {kind!r}")
        self.kind = kind
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"{self.kind} | {self.amount:.2f} | balance: {self.balance_after:.2f}"
