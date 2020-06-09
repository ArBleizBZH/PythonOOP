
class BankAccount:

    bank_name = "Mythical Honest Bank"
 
    def __init__(self, name, balance=0, bank = bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank
        
    def display(self):
         print(f'welcome to {self.bank}, {self.name}. \tYour balance is:  {self.balance}')
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
    
a1 = BankAccount('Mike', 200)
a2 = BankAccount('Tom')
a3 = BankAccount('Phil', 100, "First Thieves Bank")
 
a1.display()
a2.display()
a3.display()

