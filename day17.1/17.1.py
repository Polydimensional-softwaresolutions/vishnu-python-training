# 1. Payment Processor System 
# Challenge: Design a system to process different types of payments while ensuring data security and a unified interface.
# Requirements:
# Inheritance: Create a base class PaymentMethod with a constructor taking amount.
# Polymorphism: In PaymentMethod, define a method process_payment() that raises a NotImplementedError. Create subclasses CreditCardPayment and WireTransferPayment, and implement process_payment() in each to return a different success message (e.g., "Card validated..." vs. "Bank transfer initiated...").
# Encapsulation: In CreditCardPayment, strictly encapsulate the card number attribute (self.__card_number).
# Abstraction: Create a public function (outside the classes) called execute_transaction(payment_object) that takes any PaymentMethod object and calls its process_payment(), abstracting whether it's a card or a wire transfer.

class PaymentMethod:
    def __init__(self,amount):
        self.amount=amount
    def process_payment(self):
        raise NotImplementedError
class CreditCardPayment(PaymentMethod):
    def __init__(self,amount,card_number):
        super().__init__(amount)
        self.__card_number=card_number
    
    def process_payment(self):
        return (f"card is validated and amount of {self.amount} is credited by the card number ending with {self.__card_number} ")
         
class WireTransferPayment(PaymentMethod):
    def __init__(self,amount):
        self.amount=amount
            
    def process_payment(self):
        return ("bank transfer initiated...")
def execute_transaction(payment_object):
    return payment_object.process_payment()

obj1=CreditCardPayment(100,1234567890)
obj2=WireTransferPayment(150)

print(execute_transaction(obj1))
print(execute_transaction(obj2))


