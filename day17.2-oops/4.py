# Create a class Account. The constructor must initialize the private attribute self._balance to 0.
# Define a public method deposit(amount) that increases the balance.
# Define a public getter method get_balance() that returns the balance. This abstracts the internal data structure (_balance) from direct access.

class Account:
    def __init__(self):
        self._balance=0
    
    def deposit(self,amount):
        self.amount=amount
        self._balance+=amount
    
    def get_balance(self):
        return self._balance
    
acc=Account()
acc.deposit(100)
acc.deposit(200)
print(acc.get_balance())
