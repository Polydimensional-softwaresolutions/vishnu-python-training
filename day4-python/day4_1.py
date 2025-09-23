for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 15 == 0:
        print("Fizz Buzz")
    else:
        print(number)
