import time
import random

class Bank:
    def __init__(self, name, name2, balance):
        self.balance = balance
        self.name = name
        self.name2 = name2

    def method_handler(self, method):
        if method == "Check Balance":
            self.check()
        elif method == "withdrawal":
            self.withdrawal()
        elif method == "deposit":
            self.deposit()

    def deposit(self):
        money = int(input("How much do you want to deposit: "))
        self.balance += money
        print("Your Balance is now $", self.balance)

        
        self.display_customer_details()

    def check(self):
        print("Your Balance is:", self.balance)

    def withdrawal(self):
        money = int(input("How much Do you want to withdraw $"))
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money
            print("Your Balance is now $", self.balance)

            
            self.display_customer_details()

    def display_customer_details(self):
        print("\n****************************************************\n")
        print("Customer Details: \nName:", self.name, self.name2, "\nAccount Number:", num, "\nBalance:", self.balance)

num = random.randint(1000, 9999)
print("Account Number", num)
name = input("Enter First name: ")
name2 = input("Enter Last name: ")
balance = 0
bank = Bank(name, name2, balance)

while True:
    method = input("Enter (Withdrawal, Deposit, Check Balance, or exit): ")
    if method.lower() == "exit":
        break

    bank.method_handler(method)