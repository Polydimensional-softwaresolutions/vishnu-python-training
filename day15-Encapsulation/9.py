# Secret Access In the Agent class, define a public method authenticate(key) 
# that checks if the provided key matches self.__secret_code. If it matches, 
# return the secret code; otherwise, return "Access Denied."

class Agent:
    def __init__(self,secret_code):
        self.__secret_code=secret_code
    def authenticate(self,key):
        match key:
            case _:
                if key==self.__secret_code:
                    return self.__secret_code
                else:
                    return ("Access Denied")
my=Agent('007')
print('secret code is:', my.authenticate("007"))
print( my.authenticate("123"))
