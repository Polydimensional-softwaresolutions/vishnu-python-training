#Write a function build_gradebook(txt_file) that reads this file and organizes the data. 
# The function should return a single data structure where each student's name is a primary key, and its value is another data structure holding all their subjects and grades.

def build_gradebook(txt_file):
    gradebook={}
    with open(r"C:\Users\lenovo\Desktop\python training\text files\grades.txt","r")as file:
       for i in file:
           i=i.strip()
           parts=i.strip()
           name,subject,grade=parts
    try:
        grade = float(grade)
    except:
        print("Skipping malformed line...")
    
        if name not in gradebook:
          gradebook[name] = {}

        gradebook[name][subject] = grade


    print(f"Error: File not found.")
    return {}

    return gradebook
result = build_gradebook("grades.txt")
print(result)