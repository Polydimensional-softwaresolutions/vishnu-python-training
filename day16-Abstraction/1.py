# 1. Simple Abstraction with a Method Call 
# Challenge: Create a class Phone that demonstrates how a user interacts with a high-level function without needing to know the complex steps behind it.
# Requirements:
# Define a class Phone.
# Define a constructor that initializes self.number.
# Define a public method Phone(recipient_number) that prints a simplified sequence of steps:
# "Dialing network..."
# "Authenticating signal..."
# "Call connected to [recipient_number]."
# The user (you) only sees and calls Phone(). This hides the network details (the abstraction).
# Create a Phone object and call Phone("555-1234").


class Phone():
    def __init__(self,number):
        self.number=number
    def phone1(self,recipient_number):
        self.recipient_number=recipient_number
        print("dialing network...")
        print("Authenticating signal...")
        print(f"Call connected to {recipient_number}.")
phone=Phone("555-1234")
phone.phone1("555-1234")

        
