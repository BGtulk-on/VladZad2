class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
        
    def __str__(self):
        return f"Savings Account ({self.account_number}) balance: {self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, fee=5):
        super().__init__(account_number, balance)
        self.fee = fee
        
    def deduct_fees(self):
        self.balance -= self.fee
        
    def __str__(self):
        return f"Checking Account ({self.account_number}) balance: {self.balance}"

savings = SavingsAccount("123605", 1000)
checkingsb = CheckingAccount("97800", 1000)

savings.add_interest()
checkingsb.deduct_fees()
checkingsb.withdraw(195)

print(savings)
print(checkingsb)
