import datetime
import random


class Bank_account:
    def __init__(self, account_nr, balance=0.0, bank_name="ING"):
        self.account_nr = account_nr
        self.balance = balance
        self.currency = "RON"
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.bank_name = bank_name
        self._pin = random.randint(1000, 9999)

    def add_money(self, money: float):
        self.balance += money
        return self.balance

    def withdraw_money(self, money: float):
        self.balance -= money
        return self.balance

    def show_balanced(self):
        return self.balance

    def get_pin(self):
        return self._pin