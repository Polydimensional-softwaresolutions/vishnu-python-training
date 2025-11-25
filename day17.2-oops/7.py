# Create a class User. Initialize self._age to 0.
# Define a public setter method set_age(new_age) that checks if new_age is between 18 and 100.
# If valid, update self._age. If invalid, print an error message. This ensures controlled access to the attribute.

class User:
    def __init__(self):
          self._age=0
    def set_age(self,new_age):
        if new_age  > 18 and new_age < 100:
              print("user age is abouve 18")
              self._age=new_age
        else:
            print("error message age should be in between 18 to 100")
    
abc=User()
abc.set_age(30)
print(abc._age)


         
