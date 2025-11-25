# Create a base class Asset with a constructor that initializes a private attribute self._value.
# Create a subclass House that inherits from Asset.
# In House, define a method get_appraisal() that accesses the inherited private attribute using 
# a protected helper method (self._value convention) defined in the base class.

class Asset:
    def __init__(self,value):
        self.__value=value

    def _getter(self):
        return self.__value
class House(Asset):
    def get_appraisal(self):
        return self._getter()

obj=House(10000)
print(obj.get_appraisal())