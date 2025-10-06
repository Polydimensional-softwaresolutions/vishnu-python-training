#Write a program that prints "Program started" and "Program ended" using finally, no matter what happens in between.
p="program started"
print(p)
try:
    divide_two_numbers=2/0
    print(divide_two_numbers)
except:
    print("program not started, not diveded by zero")
finally:
    print("program ended")    