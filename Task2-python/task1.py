#Write a program that asks the user to enter a number, and use try-except to handle the case when the user enters text instead of a number.

try:
    user_no=int(input("enter your number:"))
    print(f"your entered number is {user_no}:")
except:
    print("you entered invalid number")
     