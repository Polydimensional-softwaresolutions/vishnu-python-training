#Setter Validation In the Budget class, define a public method set_limit(new_limit) 
#that only updates self._monthly_limit if new_limit is greater than 1000. Otherwise, print an error.

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
my=Budget()
my.monthly_limit()
my.set_limit(1100)
my.set_limit(100)