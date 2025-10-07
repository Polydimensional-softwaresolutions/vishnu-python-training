#Write a program that counts how many lines are in a file

with open("C:\\Users\\lenovo\\Desktop\\text.txt") as f:
    a=f.read()
    print(a)
    b=f.readlines()
    print("Total lines are:" ,len(b))