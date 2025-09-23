import random

for i in range(7):
    bot_number = random.randint(1,100)
    user_input = int(input("enter the guess of the user: "))
    
    if bot_number == user_input:
        print("yes you are correct")
        break
    
    print(f"Your guess is too {user_input}")
    
    if (bot_number - user_input) > 0:
        print("too low")
    else:
        print("too high")
        
    print(f"Remaining chances : { 6 - i }")