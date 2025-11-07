#Private Budget Create a class Budget. 
#The constructor must initialize a private attribute self._monthly_limit to 1500.

class Budget:
    def __init__(self):
        self.__monthly_limit=1500
    def monthly_limit(self):
        print("my monthly limit is:" ,self.__monthly_limit)
my=Budget()
my.monthly_limit()
    