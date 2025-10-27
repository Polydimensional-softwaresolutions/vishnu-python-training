'''Write a function register_user(username).
The function should first check if the username already exists in a file called users.txt. You should read the file to find out; assume each username is on a new line.
If the username is already in the file, the function should print "Error: Username taken." and return False.
If the username is new, the function should append the new username to the end of users.txt and return True.
Your function must also handle the case where users.txt doesn't exist yet (it should create it and add the user)'''

def register_user(username):
    try:
        with open (r"C:\Users\lenovo\Desktop\python training\text files\user.txt","r") as file:
           file.readline()
    except:
     if username in file:
        print("Error:username taken")
        return False
    with open(r"C:\Users\lenovo\Desktop\python training\text files\user.txt","a") as file:
        file.write(username + "\n")
    return True
        
