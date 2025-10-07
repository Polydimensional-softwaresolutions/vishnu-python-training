#Write a program that opens a file, reads its content, and prints the total number of characters in it.

file = open("notes.text","r")
print(file.read())
print(len(file.readlines()))
