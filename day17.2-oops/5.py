# Create two distinct classes: Circle and Rectangle.
# In both classes, define a method named describe() that prints a unique self-description (e.g., "I have rounded edges" vs. "I have four sides").
# Create a list containing one object of each class.
# Use a loop to iterate through the list and call the describe() method on each object.

class Circle:
    def describe(self):
        print("I have Rounded edges")


class Rectangle:
    def describe(self):
        print("I have four sides")

cir=Circle()
rect=Rectangle()
list=[cir,rect]
for i in list:
    i.describe()

