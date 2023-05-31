class BankAccount:
    account_name = ""
    account_balance = 0.0

    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.account_balance = starting_balance

    def depositMoney(self, amount):
        self.account_balance += amount

    def withdrawMoney(self, amount):
        self.account_balance -= amount

    def get_balance(self):
        string = str(self.account_name + " has a balance of $" + "{:.2f}".format(self.account_balance))
        return string