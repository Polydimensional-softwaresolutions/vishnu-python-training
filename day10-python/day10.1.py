#Open a file named notes.txt and read its contents.

content=open("notes.txt","r")
print(content.read())
content.close()