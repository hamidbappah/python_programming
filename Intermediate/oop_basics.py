class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount

acct = BankAccount("Zainab", 5000)
acct.deposit(2500)    # balance: 7500
