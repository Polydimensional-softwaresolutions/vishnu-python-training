# 4. Hierarchical Asset Management (Inheritance, Polymorphism, List) 
# Challenge: Model an asset hierarchy where total value is calculated polymorphically.
# Requirements:
# Inheritance: Create a base class Asset with a constructor initializing self.name and self.value.
# Create a subclass Portfolio that inherits from Asset but also contains a list attribute self.assets to store other Asset objects.
# Polymorphism: Override a method get_total_value() in Portfolio. This method must loop through its assets list and sum the value of all contained objects, adding it to its own base value. The base Asset class just returns its own value.
# Create a Portfolio object containing a few simple Asset objects and print its total value.

class Asset:
    def __init__(self,name,value):
        self.name=name
        self.value=value

class Portfolio(Asset):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.assets=[]
    def add_asset(self,asset):
        self.assets.append(asset)
    def get_total_value(self):
        value=self.value
        for i in self.assets:
            value=value+i.value
        return value
obj1=Asset("stock",1000)
obj2=Asset("gov land",5000)

portf=Portfolio("value asset",1000)
portf.add_asset(obj1)
portf.add_asset(obj2)
print(portf.get_total_value())
