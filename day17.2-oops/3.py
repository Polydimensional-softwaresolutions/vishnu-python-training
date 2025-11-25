# Create a base class Vehicle with a method start() that prints "Vehicle starting."
# Create a subclass Car that inherits from Vehicle.
# Override the start() method in Car to print "Car engine starting silently."
# Define a function turn_on(obj) that calls obj.start(). Pass both a Vehicle and a Car object to this function.

class Vehicle:
    def start(self):
        print("vehicle stsarting...")

class Car(Vehicle):
    def start(self):
        print("Car engine starting silently...")

def turn_on(obj):
    obj.start()

veh=Vehicle()
car1=Car()
turn_on(veh)
turn_on(car1)