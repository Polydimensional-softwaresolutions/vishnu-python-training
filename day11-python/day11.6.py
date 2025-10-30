#A log file log.txt contains both normal messages and error messages (lines starting with "ERROR:").
#Create a new file errors.txt that contains only the error lines.

with open(r"C:\Users\lenovo\Desktop\python training\text files\log.txt","r")as logfile,\
     open(r"C:\Users\lenovo\Desktop\python training\text files\errors.txt","w")as errorfile:
     for i in logfile:
        if i.startswith("Error:"):
            errorfile.writelines(i)