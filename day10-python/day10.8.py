#Write a program that deletes a file named oldfile.txt (only if it exists)

import os
if  os.path.exists("notes.txt"):
    os.remove("notes.txt")
else:
    print("file does not exist")