#Get Full Name In the Dog class from Q1, add a method bark() that returns the string "Woof! My name is [name]."

class Dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def bark(self):
        return (f"woof! my name is {self.name}")
        
dog=Dog("Leo",12)
print(dog.bark())
