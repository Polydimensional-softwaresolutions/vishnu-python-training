#Write a program to count how many times the word "Python" appears in a file named article.txt.

#word = "python"
#count = 0
with open(r"C:\Users\lenovo\Desktop\python training\text files\\article.txt", 'r') as f:
    """for line in f:
       words = line.split()
       print(words)
       for i in words:
              if(i==word):
               count=count+1
print("Occurrences of the word", word, ":", count)"""
    file=f.read()
    count=file.count("python")
    print(count)