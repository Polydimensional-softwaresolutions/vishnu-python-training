#Write a program to append the text "This is a new line." to an existing file.

with open("C:\\Users\lenovo\Desktop\data.txt","a") as f:
    f.write("\nThis is New Line ")
with open("C:\\Users\lenovo\Desktop\data.txt")as f:
    print(f.read())