# Strictly Private Secret Create a class Agent. The constructor must accept and initialize a 
# strictly private attribute self.__secret_code (using double underscore).

class Agent:
    def __init__(self,secret_code):
        self.__secret_code=secret_code
    def getter(self):
        print(f"Agent id:{self.__secret_code}")
my=Agent('007')
my.getter()