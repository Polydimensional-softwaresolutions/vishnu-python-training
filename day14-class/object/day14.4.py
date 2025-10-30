# 4. Instance Counting (Advanced Constructor Use) 
# Challenge: Track how many objects of a class have been created.
# Requirements:
# Create a class named Robot.
# Define a class attribute named robot_count and set it to 0. (A class attribute is shared by all objects.)
# Define the constructor (__init__). Inside the constructor, increment the Robot.robot_count every time a new Robot object is created.
# Create three Robot objects: r1, r2, and r3.
# Print the final value of the class attribute Robot.robot_count.

class Robot:
    def __init__(self):
        self.robot_count=0
        self.robot_count+=1
r1=Robot()
r2=Robot()
r3=Robot()
print(r1.robot_count)
print(r2.robot_count)


        
