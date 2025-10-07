#Create a file called numbers.txt and write numbers 1 to 5 into it, each on a new line.

#with open("C:\\Users\\lenovo\\Desktop\\note.txt","x")as f:
with open("C:\\Users\\lenovo\\Desktop\\numbers.txt","w")as f:
   
    for i in range(6):
      f.write(str(i) + "\n")
      print(i)
          