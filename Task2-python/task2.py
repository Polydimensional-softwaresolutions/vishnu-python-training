#Write a program that divides two numbers and catches the error if the user tries to divide by zero.
try:
    my_number=6
    user_number=int(input("enter user number:"))
    divide_two_numbers= my_number/user_number
    print(f"result of the divided two numbers is {divide_two_numbers}:")
except:
      print("you cannot divide with zero")  