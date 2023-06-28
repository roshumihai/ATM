import json
import string
import time

from classes import Bank_account
import random

MENU = [
    "balance",
    "pin"
]
ACCOUNT_LEN = 20
counts = 2


def is_float(number_str):
    try:
        float(number_str)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    try:
        with open("bank_account.json", "r") as f:
            file= json.load(f)
    except Exception as e:
        pass

    user = input("Enter username: ")
    if user not in file:
        print("User not found!")

        answer = input("Create a new account? y/n: ")
        if answer.lower() == "y":
            new_account_nr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=ACCOUNT_LEN))

            user = input("Enter your username: ")
            money = input("Enter the amount you want to add to your account? ")

            while not is_float(money):
                print("You need to enter a valorical value like 12 or 12.2!")
                money = input("Enter the amount you want to add to your account?")
            money = float(money)

            account = Bank_account(new_account_nr, money)

            file[user] = {
                "account_nr": account.account_nr,
                "balance": account.balance,
                "currency": account.currency,
                "creation_date": account.creation_date,
                "bank_name": account.bank_name,
                "pin": account.get_pin()
            }
            print(f"Your pin is {file[user]['pin']}")
            print("Do not share your pin with anyone.")
            print()
            with open("bank_account.json", "w") as f:
                new_account = json.dumps(file, indent=4)
                f.write(new_account)
        else:
            print("Goodbye! Have a nice day.")
            quit()

    print(f"Hello {user}! Welcome.")
    pin = input("Enter pin: ")
    while not pin.isdigit():
        print("You need to enter a numerical value like '1234'!")
        pin = input("Enter pin: ")
    pin = int(pin)

    while not pin == file[user]["pin"]:
        print("Incorrect pin, Try again!")
        pin = input("Enter pin: ")
        while not pin.isdigit():
            print("You need to enter a numerical value like '1234'!")
            pin = input("Enter pin: ")
        pin = int(pin)
        counts -= 1
        if counts == 0:
            print("You entered pin too many times. Try again later!")
            quit()

    if pin == file[user]["pin"]:

        account = Bank_account(file[user]["account_nr"], file[user]["balance"])

        choice = input(f"What would you like to do? ( {MENU[0]}(1) / {MENU[1]}(2) / quit ) > ")
        while choice.lower() != "q" and choice.lower() != "quit":
            if choice.lower() == MENU[0].lower() or choice.lower() == "1":
                choice2 = input("Add too your balance(1) / Withdraw(2) / Check your balance(3) /quit(q) >  ")
                while choice2 != "q" and choice2 != "quit":
                    if choice2 == "1":
                        amount = input("Add amount: ")
                        while not is_float(amount):
                            amount = input("Add amount: ")
                        amount = float(amount)
                        file[user]["balance"] = account.add_money(amount)
                        print(f"Your balance is now {file[user]['balance']} {file[user]['currency']}")
                        print()
                        time.sleep(2)

                        with open("bank_account.json", "w") as f:
                            new_file = json.dumps(file, indent=4)
                            f.write(new_file)
                        break
                    if choice2 == "2":
                        amount = input("Amount to withdraw: ")
                        while not is_float(amount):
                            amount = input("Amount to withdraw: ")
                        amount = float(amount)
                        while amount > file[user]["balance"]:
                            print(f"You don't have enough money in the account.\nYour balance is {file[user]['balance']}")
                            print()
                            amount = input("Amount to withdraw: ")
                            while not is_float(amount):
                                amount = input("Amount to withdraw: ")
                            amount = float(amount)
                            time.sleep(1)
                        file[user]["balance"] = account.withdraw_money(amount)
                        print(f"Your balance is now {file[user]['balance']} {file[user]['currency']}")
                        print()
                        time.sleep(2)

                        with open("bank_account.json", "w") as f:
                            new_file = json.dumps(file, indent=4)
                            f.write(new_file)
                        break

                    if choice2 == "3":
                        print(f"Your balance is: {account.balance} {account.currency}")
                        print()
                        time.sleep(2)
                        break
            elif choice.lower() == MENU[1].lower() or choice == "2":
                choice2 = input("See your pin(1) / Change pin(2) / quit(q) > ")
                if choice2 == "1":
                    print(file[user]['pin'])
                    print()
                    time.sleep(2)
                elif choice2 == "2":
                    try:
                        with open("bank_account.json", "r") as f:
                            file = json.load(f)
                    except Exception as e:
                        print(f"Error opening json. Error: {e}")
                    old_pin = input("Enter old pin: ")

                    while file[user]["pin"] != int(old_pin):
                        if old_pin == "q" or old_pin == "quit":
                            break
                        print("You entered a wrong pin.")
                        print()
                        old_pin = input("Enter old pin: ")
                        try:
                            old_pin = int(old_pin)
                        except Exception as e:
                            pass

                    new_pin = input("Enter new pin: ")
                    while not new_pin.isdigit():
                        print("You need to enter numerical values, like '1234'!")
                        new_pin = input("Enter new pin: ")
                    new_pin = int(new_pin)
                    new_pin2 = input("Enter new pin again: ")
                    while not new_pin2.isdigit():
                        print("You need to enter numerical values, like '1234'!")
                    new_pin2 = int(new_pin2)
                    while new_pin != new_pin2:
                        print("Don't match. Try again!")
                        print()
                        new_pin = input("Enter new pin: ")
                        while not new_pin.isdigit():
                            print("You need to enter numerical values, like '1234'!")
                            new_pin = input("Enter new pin: ")
                        new_pin = int(new_pin)
                        new_pin2 = input("Enter new pin again: ")
                        while not new_pin2.isdigit():
                            print("You need to enter numerical values, like '1234'!")
                        new_pin2 = int(new_pin2)
                    file[user]["pin"] = new_pin
                    print(f"Your new pin is: {file[user]['pin']}")
                    print()
                    with open("bank_account.json", "w") as f:
                        new_file = json.dumps(file, indent=4)
                        f.write(new_file)
                    time.sleep(2)

            choice = input(f"What would you like to do ({MENU[0]}(1) / {MENU[1]}(2) / quit(q)):")