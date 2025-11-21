# 2. Vehicle Manufacturing Factory 
# Challenge: Model vehicle production where different vehicles share core processes but have specialized implementations and secured data.
# Requirements:
# Inheritance: Create a base class Vehicle with a constructor taking model.
# Encapsulation: In Vehicle, encapsulate a mileage attribute (self._mileage) and provide a public getter method get_mileage().
# Polymorphism: Create two subclasses, Car and Motorcycle. In both subclasses, implement a method assemble() that prints the base assembly steps but adds a specialization (e.g., Car: "Installing 4 doors" vs. Motorcycle: "Installing 2 wheels").
# Abstraction: In the base class Vehicle, define a public method build_unit() that internally calls the specialized assemble() method, abstracting the specific build process from the factory floor operator.

class vehicle:
    def __init__(self,model):
        self.model=model
        self._mileage=0
    def get_mileage(self):
        return self._mileage
    def build_unit(self):
        print(f"building the special {self.model} model")
        self.assemble()

class car(vehicle):

    def assemble(self):
        print("installing 4 doors")
        print("installing steering")
        print("installin car engine")

class motorcycle(vehicle):

    def assemble(self):
        print("installing 2 wheels")
        print("installing head light")
        print("installing motorcycle engine")
obj1=car("Honda")
obj2=motorcycle("ktm")
obj1.build_unit()
obj2.build_unit()

        