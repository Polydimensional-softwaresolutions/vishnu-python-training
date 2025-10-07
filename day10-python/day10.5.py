#Write a program that checks if a file named test.txt exists or not before opening it

import os
if os.path.exists("test.txt"):
    print("file exist")
else:
    print("file does not exist")