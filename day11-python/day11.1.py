#You have a file named students.txt where each line contains a student’s name. 
# Write a program to read all names and print only those starting with the letter "A".

with open("C:\\Users\lenovo\Desktop\python training\students.txt","r")as file:
  
    for i in file:
        if i.startswith("A"):
            print(i)


