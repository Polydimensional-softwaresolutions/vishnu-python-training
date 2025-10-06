#Write a function print_items(*args) that takes any number of arguments and prints them one by one.

def items(*args):
    for items in args:
        print(items)
items("apple","banana",1,3,2.55)