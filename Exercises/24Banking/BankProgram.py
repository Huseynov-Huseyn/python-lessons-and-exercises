"""
================================================================================
EXERCISE 24: BANK APPLICATION
================================================================================

Build a console banking application by completing the files in the order below.
Each step introduces the classes and methods needed by the next step. In
particular, implement account-level transfer operations before writing Bank,
because Bank.transfer() uses them.

Do not write the menu until all earlier steps are complete. After each step,
write a few small checks of your own and fix problems before continuing.


PROJECT FILES
-------------
BankError.py
InvalidAmountError.py
InsufficientFundsError.py
AccountNotFoundError.py
InvalidPinError.py
AccountLockedError.py
WithdrawalLimitError.py
Transaction.py
Account.py
SavingAccount.py
CheckingAccount.py
Bank.py
BankProgram.py


RULES USED THROUGHOUT THE PROJECT
---------------------------------
1. Money is in AZN. Display every money amount with exactly two decimal places.
2. Every operation amount must be numeric and greater than zero.
3. The minimum opening deposit is 10.00 AZN.
4. A PIN is a string containing exactly four digits.
5. An owner name must be a string that is not empty after stripping spaces.
6. Three consecutive incorrect PIN attempts lock that account.
7. Keep each shared validation rule in one place. Reuse it instead of
   duplicating the same validation in several classes.


STEP 1 — CREATE THE BANK EXCEPTIONS
===================================
Files: BankError.py and the six specific error files listed above.

1. In BankError.py, define BankError as a subclass of Exception.
2. Define each specific bank error as a subclass of BankError:
   InvalidAmountError, InsufficientFundsError, AccountNotFoundError,
   InvalidPinError, AccountLockedError, and WithdrawalLimitError.
3. InvalidAmountError is used for an amount at or below zero and for an
   opening deposit below 10.00.
4. InsufficientFundsError must store `balance` and `amount` attributes. Its
   message must show both values.
5. AccountNotFoundError must store the missing account number.
6. InvalidPinError must store the number of attempts remaining. Do not keep
   the attempt count as a shared class variable in the exception class.
7. Give every exception a short, clear message. A single `except BankError`
   must catch all six specific errors.


STEP 2 — CREATE TRANSACTION RECORDS
==================================
File: Transaction.py

1. A Transaction stores `kind`, `amount`, and `balance_after`.
2. Accept exactly these kinds:
   DEPOSIT, WITHDRAW, TRANSFER IN, TRANSFER OUT, INTEREST, and FEE.
3. Reject any other kind with ValueError.
4. Implement `__str__` to return one readable line. Show money with two
   decimal places, for example:
   TRANSFER IN | 150.00 | balance: 900.00
5. Transaction objects are created by account classes when they change a
   balance. Bank and the menu must not create them directly.


STEP 3 — BUILD THE ABSTRACT ACCOUNT BASE CLASS
==============================================
File: Account.py

Create Account as an abstract base class. It holds behavior shared by both
account types. Complete this class before either subclass or Bank.

Constructor: `Account(owner, pin, initial_deposit)`
1. Add static methods to validate the owner name and PIN. Each returns True or
   False. Use these methods from the constructor.
2. Raise ValueError with a clear message for an invalid owner or PIN.
3. Raise InvalidAmountError when the opening deposit is below 10.00 or is not
   a valid positive money amount.
4. Store the PIN in a double-underscore private attribute. Never expose it in
   text output, representations, statements, or exception messages.
5. Start the failed-PIN counter at zero and the locked flag as False. These
   values belong to each account instance.
6. Assign account numbers in the form AZ0001, AZ0002, and so on. Advance the
   class counter only after the account has been successfully initialized.
7. Set the initial balance and record exactly one initial DEPOSIT transaction.

Balance and account identity
1. Provide a read-only property named `balance`. Assignment such as
   `account.balance = 5` must fail.
2. Provide a useful `__str__`, for example:
   AZ0001 | Aysel | SAVINGS | 918.00 AZN
   The account type should come from the subclass, and money uses two decimals.
3. `__repr__` shows the class name, account number, and owner, never the PIN.
4. `__lt__` compares account balances so `sorted(accounts)` works.
5. `__len__` returns the number of transactions.

PIN verification
1. Implement one method that checks a supplied PIN.
2. If the account is already locked, raise AccountLockedError immediately.
3. On a wrong PIN, increase this account's failed-attempt counter and raise
   InvalidPinError with the remaining attempts.
4. On the third consecutive wrong PIN, mark this account locked and raise
   AccountLockedError.
5. On a correct PIN, reset this account's failed-attempt counter to zero.

Shared account operations
1. `deposit(amount)` validates the amount, increases the balance, creates
   exactly one DEPOSIT transaction, and returns the new balance. Deposits are
   allowed even when the account is locked.
2. Define `withdraw(amount)` as the common public withdrawal operation. It
   validates the amount and delegates the account-specific balance/limit
   decision to an overridable method or a clearly defined subclass hook.
   On success it decreases the balance, records exactly one WITHDRAW
   transaction, and returns the new balance.
3. Implement a protected/internal balance-change helper that subclasses can
   use to update the balance and record a transaction of a specified allowed
   kind. This supports interest, fees, and transfers without mislabeling
   their transactions as ordinary withdrawals.
4. Implement `transfer_out(amount)` and `transfer_in(amount)` here, before
   writing Bank. Both validate the amount and return the new balance. The
   source operation records TRANSFER OUT; the destination operation records
   TRANSFER IN. `transfer_out` must apply the same account-specific withdrawal
   rules and limits as a normal withdrawal. `transfer_in` increases the
   balance and records one transaction.
5. Do not let a failed operation change the balance or transaction history.
6. Implement `statement()` to return a new list of readable text lines, one
   for each transaction. Do not expose the private PIN.
7. Declare `monthly_update()` as an abstract method. It returns the signed
   balance change: positive for interest, negative for a fee. The subclasses
   implement it.


STEP 4 — IMPLEMENT SAVINGS ACCOUNTS
===================================
File: SavingAccount.py

1. Create SavingAccount as a subclass of Account.
2. Accept an optional interest rate, defaulting to 0.02.
3. Each savings account has its own withdrawal counter, initially zero.
4. Allow at most three withdrawals between monthly updates. A fourth
   withdrawal raises WithdrawalLimitError without changing balance, counter,
   or transaction history.
5. TRANSFER OUT counts as a withdrawal and uses the same limit.
6. A savings balance must never fall below zero. If a withdrawal or transfer
   would do so, raise InsufficientFundsError with the real balance and amount.
7. `monthly_update()` adds balance multiplied by the interest rate, records
   exactly one INTEREST transaction, resets this account's withdrawal
   counter, and returns the interest amount.


STEP 5 — IMPLEMENT CHECKING ACCOUNTS
====================================
File: CheckingAccount.py

1. Create CheckingAccount as a subclass of Account.
2. Set the overdraft limit to 200.00 AZN. A withdrawal or transfer may leave
   the balance at -200.00, but never below it.
3. If a withdrawal or transfer would go below -200.00, raise
   InsufficientFundsError showing the balance before the operation and the
   requested amount. Do not change the balance or history on failure.
4. `monthly_update()` charges a 3.00 AZN fee, records exactly one FEE
   transaction, and returns -3.00. Charge the fee even if it takes the balance
   below the overdraft limit.


STEP 6 — BUILD THE BANK
======================
File: Bank.py

Only start this step after Account has `transfer_out()` and `transfer_in()`.

1. Define a class variable for the bank name.
2. Initialize an account dictionary mapping account numbers to account
   objects: `{account_number: account}`.
3. `open_account(kind, owner, pin, initial_deposit)` accepts `savings` or
   `checking`, ignoring letter case and surrounding spaces. It creates the
   matching subclass, stores it in the dictionary, and returns it. Unknown
   kinds raise ValueError.
4. Add a classmethod that builds a bank from lines in this format:
   savings,Aysel,1234,500
   Each line has kind, owner, PIN, and initial deposit. If a line is invalid,
   raise ValueError whose message includes its 1-based line number, and chain
   the original exception using `raise ... from ...`.
5. `find(number)` returns the account or raises AccountNotFoundError.
6. `deposit(number, amount)` finds the account and deposits without a PIN.
7. `withdraw(number, pin, amount)` finds the account, checks its PIN, then
   withdraws.
8. `transfer(from_number, to_number, amount, pin)` must follow this order:
   a. Reject identical source and destination numbers with ValueError.
   b. Find both accounts; if either is missing, make no changes.
   c. Validate the amount and check the source account PIN.
   d. Check that the source account allows the withdrawal, including its
      overdraft or savings limit, before changing either account.
   e. Only after all checks pass, apply one TRANSFER OUT to the source and
      one TRANSFER IN to the destination. A failed transfer changes neither
      balance nor history.
9. `balance_of(number, pin)` checks the PIN and returns the numeric balance.
10. `statement_of(number, pin)` checks the PIN and returns statement lines.
11. `total_balance()` returns the numeric sum of all account balances.
12. `ranking()` returns account objects ordered from highest balance to
    lowest.
13. `apply_monthly_updates()` calls `monthly_update()` on every account
    without checking its concrete type. Return a dictionary mapping account
    numbers to signed changes.
14. `__len__` returns the number of accounts. `__contains__` supports checks
    such as `"AZ0001" in bank`.


STEP 7 — WRITE THE CONSOLE MENU
===============================
File: BankProgram.py

1. Import Bank and the bank exception base class.
2. At startup, create a Bank containing two demo accounts using the
   classmethod that reads text lines.
3. Write one function for each menu action:
   - Open account
   - Deposit
   - Withdraw
   - Transfer
   - Show balance
   - Show statement
   - Show all accounts by balance
   - Apply monthly update
4. Repeatedly display this menu until the user chooses 0:

   1. Open account          5. Show balance
   2. Deposit               6. Show statement
   3. Withdraw              7. Show all accounts
   4. Transfer              8. Apply monthly update
   0. Exit

5. If the menu choice or a numeric amount cannot be parsed, show a short
   message and return to the menu. Do not let invalid input terminate the
   program.
6. Catch expected bank errors and ValueError, then catch any other Exception
   last. Print each error as a short `Error: ...` message.
7. Use a `finally` block after every attempted menu action to print a
   separator line, including when an action raises an error.
8. Format every displayed money amount with exactly two decimal places.


SUGGESTED MANUAL CHECKS
=======================
- Account cannot be instantiated directly.
- Invalid construction does not consume an account number.
- Invalid PINs, owner names, and opening deposits are rejected.
- `balance` is read-only and the PIN never appears in output.
- Three wrong PINs lock only the account receiving those attempts.
- Deposits work on a locked account; withdrawals require a valid PIN in Bank.
- Savings allows three withdrawals and rejects the fourth until monthly
  update; transfer out counts toward the same limit.
- Checking allows exactly -200.00 and rejects a result below -200.00.
- A failed transfer leaves both balances and both histories unchanged.
- Successful transfers create one TRANSFER OUT and one TRANSFER IN record.
- Monthly updates create INTEREST or FEE records and return signed changes.
- Ranking is highest balance first; `sorted(accounts)` works.
- Text input where a number is expected never crashes the menu.
================================================================================
"""
