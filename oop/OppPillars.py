"""
OOP has four pillars:-
Abstraction:- Hiding the implementation details and showing only the necessary information to the user.
Encapsulation:- Binding data and methods together into a single unit.
Inheritance:- Creating a new class from an existing class, inheriting its properties and methods.
Polymorphism:- Using the same method name to perform different actions based on the object type.
"""

# Abstraction:- 

class Car:
    def __init__(self):
        self.acc = False 
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Starting the car...")  

        car1 = Car()
        car1.start()



# Encapsulation:- (we already create class and object adn encapsu;altion means binding data and methods together into a single unit.)


# ---------------------------------------------

# Q1: create account class with two attrubutes - balance and account no, create methods for debit credit adn printing the balance?

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")

    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}")

    def print_balance(self):
        print(f"Account Balance: {self.balance}")
        


# Create an instance of Account
acc1 = Account(1000, 123456)
print(acc1.balance)
print(acc1.account_no)

# Perform operations on the instance
acc1.debit(500)
acc1.credit(1000)
acc1.print_balance()

        