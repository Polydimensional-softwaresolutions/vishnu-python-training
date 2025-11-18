# 3. Method Overriding (Specialization) 
# Challenge: Override a parent method in the child class to provide specialized behavior.
# Requirements:
# Create a base class Vehicle with a method start_engine() that prints "Engine turned on."
# Create a subclass ElectricCar that inherits from Vehicle.
# Override the start_engine() method in ElectricCar to print "Battery initialized. Engine is silent."
# Create a Vehicle object and an ElectricCar object. Call start_engine() on both to show the override.

class Vehicle:
    def start_engine(self):
        print("engine turned on...")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Battery initialized. Engine is silent.")
obj1=Vehicle()
Obj2=ElectricCar()
obj1.start_engine()
Obj2.start_engine()


