# Getter Method In the Budget class, define a public method get_current_limit() that 
# simply returns the value of the private attribute self._monthly_limit.

class Budget:
    def __init__(self):
        self.__monthly_limit=1500
    def monthly_limit(self):
        print("my monthly limit is:" ,self.__monthly_limit)
    def set_limit(self,new_limit):
        if new_limit>= 1000:
            self.__monthly_limit=new_limit
            print("my new monthly limit is:", self.__monthly_limit)
        else:
            print("error occured, must be above 1000")
    def get_current_limit(self):
        return self.__monthly_limit
obj=Budget()
print(obj.get_current_limit())
