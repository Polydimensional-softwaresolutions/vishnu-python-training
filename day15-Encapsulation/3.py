#Default Value Create a class LightBulb. 
#The constructor should take a wattage and initialize a default boolean attribute self.on to False.

class LightBulb:
    def __init__(self,wattage):
        self.wattage=wattage
        self.on=False
obj=LightBulb(100)
print(obj.wattage)