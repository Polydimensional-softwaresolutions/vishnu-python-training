'''Write a function get_unique_words(source_file, output_file).
This function must:
Try to read the contents of the source_file. If the file isn't found, it should print an error and stop.
Process the text: make everything lowercase and remove common punctuation (like ., ,, ?).
Find all the unique words in the entire file.
Write this list of unique words to the output_file, with each word on a new line, sorted alphabetically.
The function should return the total count of unique words found.'''

def get_unique_words(source_file,output_file):
    try:
        with open(r"C:\Users\lenovo\Desktop\python training\text files\source.txt","r")as source_file:
            text=source_file.writelines("Hello World!,My Name is Vishu")
            print(text.read())
    except:
        print("error and stop")
    
    t=text.lower()
    for i in source_file:
        text=text.replace(i)
        words=text.split()
        unique_words=sorted(set(words))
    with open(r"C:\Users\lenovo\Desktop\python training\text files\output.txt","w")as output_file:
            for words in unique_words:
                output_file.write(word+'\n')
    return len(get_unique_words)
count = get_unique_words(r"C:\Users\lenovo\Desktop\python training\text files\source.txt", r"C:\Users\lenovo\Desktop\python training\text files\output.txt")
print("Total unique words:", count)




