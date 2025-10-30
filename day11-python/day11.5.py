#You have a file input.txt.
#Create a new file output.txt that contains only those lines that are not empty.

with open ("C:\\Users\\lenovo\\Desktop\\python training\\text files\\input.txt","r")as f:
    line=f.readlines()
    for i in line:
       p=i.strip() 
with open ("C:\\Users\\lenovo\\Desktop\\python training\\text files\\output.txt","w")as o:
    o.writelines(p)
with open ("C:\\Users\\lenovo\\Desktop\\python training\\text files\\output.txt","r")as o:
    print(o.read())
   