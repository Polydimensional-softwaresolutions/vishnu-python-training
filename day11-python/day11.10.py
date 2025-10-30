#Write a program that reads a file data.txt and writes every 5th line into a new file sample.txt.

with open(r"C:\Users\lenovo\Desktop\python training\text files\data2.txt","r")as f,\
  open (r"C:\Users\lenovo\Desktop\python training\text files\sample.txt","w")as p:
    line = 0
    
    for line_text in f:
         line = line + 1
         if line % 5 == 0:
            p.write(line_text + "\n")