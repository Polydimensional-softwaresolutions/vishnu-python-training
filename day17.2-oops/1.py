# Create a base class Shape with a constructor that initializes self.color.
# Create a subclass Square that inherits from Shape.
# Add a method get_color() to the base class Shape that returns the color.
# Create a Square object and call the inherited get_color() method.

class Shape:
    def __init__(self,color):
        self.color=color
    
    def get_color(self):
        return self.color
    
class Square(Shape):
    def asdf(self):
        super().__init__(color="red")

square1=Square("Red")
a=square1.get_color()
print("The color is =" ,a)