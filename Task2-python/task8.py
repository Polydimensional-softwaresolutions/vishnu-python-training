#Write a function print_details(**kwargs) that takes name, age, and city as keyword arguments and prints them.

def print_details(**kwargs):
    print("details of a person:")
    for key,value in kwargs.items():
        print(f"{key}={value}")
print_details(name="vishu",age=33,city="Hyd")
    