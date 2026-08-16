class SavingsAccount(BankAccount):
    def __init__(self, owner, rate=0.05):
        super().__init__(owner)
        self.rate = rate

    def add_interest(self):
        self.balance *= 1 + self.rate

    def __str__(self):
        return f"{self.owner}: ₦{self.balance:,.0f}"

print(SavingsAccount('Kande'))
