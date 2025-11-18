# 2. Constructor Extension with super() 
# Challenge: Use super() to correctly pass attributes up to the parent constructor.
# Requirements:
# Create a base class Vegetable with a constructor that initializes self.color.
# Create a subclass Carrot that inherits from Vegetable.
# The Carrot constructor must take a weight parameter. Inside the constructor, use super().__init__(color="Orange") to set the color automatically.
# Initialize self.weight in the Carrot constructor.
# Create a Carrot object (weight 0.5) and print its color and weight.


class Vegetable:
    def __init__(self,color):
        self.color=color
class Carrot(Vegetable):
    def __init__(self,weight):
        super().__init__(color="orange")
        self.weight=weight

obj1=Carrot(0.5)
print(f"Carrot color is: {obj1.color}")
print(f"carrot weight is: {obj1.weight}") 