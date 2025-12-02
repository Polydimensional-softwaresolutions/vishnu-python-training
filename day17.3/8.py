# Access Logging with Dictionary Lookup (File Handling, Dict, Loop) 
# Challenge: Read user data from a file and determine access permissions based on a dictionary of roles.
# Requirements:
# Create a class Authenticator.
# The constructor initializes a dictionary self.permissions = {'admin': True, 'guest': False}.
# Implement a method check_access(log_file) that reads the log_file line by line. Each line contains a username and role (separated by a comma).
# Use a loop to process the users. For each user, lookup the role in self.permissions and print whether that user is authorized.

class Authenticator:
    def __init__(self):
        self.permissions={'admin': True, 'guest': False}
    def check_access(self,log_file):
        with open(r"C:\Users\lenovo\Desktop\python training\text files\log_file.txt","r")as file:
            for i in file:
                username,role=i.split(",")
                self.permissions.get(role.strip(),False)
                if log_file:
                    print(username,"Authorised")
                else:
                    print(username,"not authorised")
obj=Authenticator()
obj.check_access(r"C:\Users\lenovo\Desktop\python training\text files\log_file.txt")


