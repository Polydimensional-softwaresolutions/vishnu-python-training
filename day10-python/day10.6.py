#Write a program that copies the content of one file (source.txt) into another file (destination.txt).

with open("C:\\Users\\lenovo\\Desktop\\firstfile.txt","r") as firstfile ,open("C:\\Users\\lenovo\\Desktop\\secondfile.txt","w") as secondfile : 
    
    for line in firstfile:
        secondfile.write(line)
        print(line)
