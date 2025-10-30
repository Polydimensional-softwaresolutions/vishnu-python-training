#Write a program that safely opens a file entered by the user.
#If the file doesn’t exist, create it and write "File created successfully".
#(Think: use exception handling + file modes.)

import os
user_file_path=input("enter your file path:")
try:
   if os.path.exists(user_file_path):
    print('The file exists')
   else:
    with open(user_file_path,"w")as file:
      new_file=file.write("File created successfully")
    print(new_file)
except:
  print("file created ")

