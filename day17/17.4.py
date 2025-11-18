# 4. Simple Polymorphism in a List 
# Challenge: Demonstrate polymorphism by putting different class objects into a list and calling a common method.
# Requirements:
# Create two distinct classes: Square and Circle.
# Define a method in both classes named draw().
# Square.draw() should print "Drawing four straight sides."
# Circle.draw() should print "Drawing a continuous curve."
# Create a list named shapes containing one Square object and one Circle object.
# Use a loop to iterate through the shapes list and call the draw() method on each item.

class Square:
    def draw(self):
        print("Drawing four straight sides.")
class Circle:
    def draw(self):
        print("Drawing a continuous curve.")

obj1=Square()
obj2=Circle()
shapes=[obj1,obj2]
for i in shapes:
    i.draw()
