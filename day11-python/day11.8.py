#You are given a file students.txt where each line is in the format:-> name,marks
#Read the file and print the name of the student with the highest marks.

f=open(r"C:\Users\lenovo\Desktop\python training\text files\student.txt","w")
f.write("vishnu, 100")
f.write("\nharsha, 90")
f.write("\nsai, 90")
f=open(r"C:\Users\lenovo\Desktop\python training\text files\student.txt","r")
max_marks=0
top_student=" "
for line in f:
    name,marks=line.strip().split()
    marks=int(marks.strip())
    if marks>max_marks:
        max_marks=marks
        top_student=name.strip()
f.close()
print(top_student,max_marks)


