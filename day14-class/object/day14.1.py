# Challenge: Create a class named Student.
# Requirements:
# Define a constructor (__init__) that accepts two parameters: name (string) and grade (integer).
# Initialize the object's attributes: self.name and self.grade.
# Create an object named s1 with the name "Alice" and grade 95.
# Print the grade of the s1 object.

class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s1=student("Alice",95)
print(s1.grade)   