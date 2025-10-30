#A file data.txt contains multiple lines.
#Write a program to create a new file reversed.txt that contains all lines from data.txt in reverse order.

with open(r"C:\Users\lenovo\Desktop\python training\text files\data.txt","r") as original_file, open(r"C:\Users\lenovo\Desktop\python training\text files\reversed.txt","w")as reversed_file:
        for line in original_file:
         words = line.split() # returs a list 
         words.reverse()         # reverses the list
         reversed_line = "+".join(words) # create a line from list
         reversed_file.write(reversed_line+ "\n")
       
    
     
   
    
    
   