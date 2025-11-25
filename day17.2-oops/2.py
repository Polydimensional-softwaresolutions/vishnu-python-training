# Create a base class Employee with a constructor initializing self.name.
# Create a subclass Manager that inherits from Employee.
# In Manager, use super().__init__(name) and initialize a new private attribute self._team_size.
# Create a Manager object and attempt to access _team_size directly (note the conventional warning/failure).

class Employee:
    def __init__(self,name):
        self.name=name

class Manager(Employee):
    def __init__(self,name,team_size):
        super().__init__(name)
        self._team_size=team_size
    
mang=Manager("vishu",5)
mag=mang._team_size
print('The team size is = ', mag)