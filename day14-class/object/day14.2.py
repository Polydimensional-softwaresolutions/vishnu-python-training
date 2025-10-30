# Challenge: Create a class named Rectangle to calculate area.
# Requirements:
# Define a constructor (__init__) that accepts length and width.
# Include a method named get_area that calculates and returns the area of the rectangle (length * width).
# Create a Rectangle object named rect1 with length 10 and width 5.
# Call the get_area method on rect1 and print the result.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        area=self.length*self.width
        print(area)
rect1=Rectangle(10,5)
rect1.get_area()
