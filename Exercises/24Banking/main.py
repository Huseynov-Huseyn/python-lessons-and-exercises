from Bank import Bank

#    1. Open account          5. Show balance
#    2. Deposit               6. Show statement
#    3. Withdraw              7. Show all accounts
#    4. Transfer              8. Apply monthly update
#    0. Exit
MENU = {"1": "Open account", "2": "Deposit", "3": "Withdraw", "4": "Transfer", "5": "Show balance",
        "6": "Show statement", "7": "Show all accounts", "8": "Apply monthly update", "0": "Exit"}
bank = Bank.from_lines(["savings,Aysel,1234,500", "checking,Ali,3334,600"])


def main():
    is_running = True
    while is_running:
        show_menu()
        try:
            select = int(input("Select: "))
        except ValueError as e:
            print("Please enter a valid number!")
            continue
        if select == 0:
            is_running = False


def open_account():
    kind = input("Kind (savings/checking): ")
    owner = input("Owner: ")
    pin = input("PIN: ")
    initial_deposit = float(input("Initial deposit: "))
    account = bank.open_account(kind, owner, pin, initial_deposit)
    print(f"Account opened: {account}")


def deposit():
    number = input("Account number: ")
    amount = float(input("Deposit's amount: "))
    response = bank.deposit(number, amount)
    print(f"New balance: {response}")


def withdraw():
    number = input("Account number: ")
    pin = input("PIN: ")
    amount = float(input("Deposit's amount: "))
    response = bank.withdraw(number, pin, amount)
    print(f"Withdraw completed, new balance:{response}")


def transfer():
    from_number = input("Your account number: ")
    to_number = input("Destination account's number: ")
    pin = input("PIN: ")
    amount = float(input("Deposit's amount: "))
    response = bank.transfer(from_number, to_number, amount, pin)
    print(f"Transfer completed, your balance: {response}")


def show_balance():
    number = input("Account number: ")
    pin = input("PIN: ")
    response = bank.balance_of(number, pin)
    print(f"You have {response} AZN")


def show_statement():
    number = input("Account number: ")
    pin = input("PIN: ")
    response = bank.statement_of(number, pin)
    print(response)


def show_all_accounts_balance():
    response = bank.ranking()
    print(response)


def monthly_update():
    response = bank.apply_monthly_updates()
    print(response)


def show_menu():
    for i in range(1, 5):
        left = f"{i}. {MENU[str(i)]}"
        right = f"{i + 4}. {MENU[str(i + 4)]}"
        print(f"{left:<25}{right}")
    print(f"0. {MENU['0']}")


if __name__ == "__main__":
    main()
