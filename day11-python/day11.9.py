#Write a program to read a file and replace every occurrence of the word "old" with "new".
#Save the modified content back to the same file.

with open(r"C:\Users\lenovo\Desktop\python training\text files\oldnew.txt","r")as f:
   a= f.read()
   modified=a.replace("old","new")
with open(r"C:\Users\lenovo\Desktop\python training\text files\oldnew.txt","w")as f:
   b= f.write(modified)
   print(modified)
