# Challenge: Enhance the OOP concepts by adding a method to manage money.
# Requirements:
# Create a class named Account.
# Define a constructor that initializes the self.balance attribute to 0.
# Include a method named deposit that accepts one parameter, amount, and adds it to self.balance.
# Include a method named get_balance that simply returns the current self.balance.
# Create an Account object named my_account.
# Call my_account.deposit(250).
# Print the current balance using the get_balance method.

class Account:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
    def get_balance(self):
        return self.balance
my_account=Account()
my_account.deposit(250)
print(my_account.get_balance())
    
