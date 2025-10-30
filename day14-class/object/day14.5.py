# 5. Car Speed Modification 
# Challenge: Use an object's methods to change its state (attributes).
# Requirements:
# Create a class named Car.
# Define a constructor that initializes self.speed to 0.
# Create a method named accelerate that increases self.speed by 10.
# Create a method named brake that decreases self.speed by 7 (ensure speed never goes below 0).
# Create a Car object named sports_car.
# Call sports_car.accelerate() three times.
# Call sports_car.brake() once.
# Print the final value of sports_car.speed.

class car:
    def __init__(self):
        self.speed=0
    def accelerate(self):
        self.speed+=10
    def brake(self):
        if self.speed>=7:
         self.speed-=7

sports_car=car()
sports_car.accelerate()
sports_car.accelerate()
sports_car.accelerate()
sports_car.brake()
sports_car.brake()
print(sports_car.speed)
