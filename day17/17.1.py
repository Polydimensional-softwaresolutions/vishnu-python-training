# 1. Basic Inheritance and Common Method 
# Challenge: Create a simple parent-child class structure where both classes use a shared method.
# Requirements:
# Create a base class Phone with a constructor that initializes self.model.
# In Phone, define a method ring() that prints: "The [model] is ringing."
# Create a subclass Smartphone that inherits from Phone.
# Create a Phone object (Model: "Cordless") and a Smartphone object (Model: "Galaxy").
# Call the ring() method on both objects.

class Phone:
    def __init__(self,model):
        self.model=model
    def ring(self):
        print(f"The {self.model} is Ringinng")
class SmartPhone(Phone):
    def __init__(self,model):
        self.model=model
    def ring(self):
        print(f"The {self.model} is Ringinng")
obj1=Phone("Cardless")
obj2=SmartPhone("Galaxy")
obj1.ring()
obj2.ring()
