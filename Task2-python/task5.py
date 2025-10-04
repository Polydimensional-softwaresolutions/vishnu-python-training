'''Write a program that divides two numbers.
If the user enters invalid input, show an error message.
Always print "Done" in the finally block.'''

my_number=10
user_number=input("user number:")
try:
    result=my_number/user_number
    print(result) 
except:
    print("Error: not valid number")
else:
    print("result is",result)
finally:
    print("Done")