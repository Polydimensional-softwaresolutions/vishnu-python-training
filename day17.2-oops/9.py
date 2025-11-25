# Create a function outside any class called process_data(item).
# If item is a string, print "Processing as text."
# If item is a list, print "Processing as collection."
# Call process_data() with a string and then with a list. 
# This simulates polymorphism by having one function handle different data types (a form of ad-hoc polymorphism).

def process_data(item):
    if isinstance(item,str):
        print("processig as text")
    elif isinstance(item,list):
        print("processing as collection.")

process_data("item")
process_data([1,2,3])

