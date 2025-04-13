import random

class BankAccount:
    def __init__(self, owner, balance, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.has_overdraft and amount > self.balance:
            return "Withdrawal denied: insufficient funds and no overdraft protection."
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account {self.account_no} - Balance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def withdraw(self):
        return "No withdrawals permitted"



account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500, has_overdraft=True)

print(account1.deposit(200))     
print(account1.withdraw(300))      
print(account1.withdraw(1000))    

print(account2.deposit(100))        
print(account2.withdraw(700))      


print(account1)
print(account2)

savings = SavingsAccount("Charlie", 2000)

print(savings.withdraw())         
print(savings)                      