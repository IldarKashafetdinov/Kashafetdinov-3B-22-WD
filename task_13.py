class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def add_money(self, money):
        self.balance += money

    def withdraw_money(self, money):
        self.balance -= money


acc = BankAccount("Ildar", 0000000000000, 202020202020)

acc.add_money(100000000000000)
print(acc.balance)
