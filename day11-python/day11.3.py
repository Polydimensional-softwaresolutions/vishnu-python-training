#You have a file numbers.txt with one number per line.Read all numbers, calculate their average, and print it.

f=open("C:\\Users\lenovo\Desktop\python training\\numbers.txt","r")
numbers=[int(i) for i in f ]
   
sum_of_number=sum(numbers)
total_numbers=len(numbers)
average=sum_of_number/total_numbers
print("Total numbers:" ,total_numbers)
print("sum:", sum_of_number)
print("average:", average)
f.close()