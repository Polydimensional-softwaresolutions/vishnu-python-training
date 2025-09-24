fruits = []
fruit1 = input("enter your 1st fav fruit:")
fruit2 = input("enter your 2nd fav fruit:")
fruit3 = input("enter your 3rd fav fruit:")
fruit4 = input("enter your 4th fav fruit:")
fruit5 = input("enter your 5th fav fruit:")

fruits.append(fruit1)
fruits.append(fruit2)
fruits.append(fruit3)
fruits.append(fruit4)
fruits.append(fruit5)

print("Your favorite fruits are:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Middle fruit:", fruits[2])

fruits[1] = "Mango"
print("After replacing the second fruit:", fruits)

fruits.append("Watermelon")
print("After adding Watermelon:", fruits)

del fruits[0]
print("After removing the first fruit:", fruits)

fruits.sort()
print("Sorted list:", fruits)

long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Fruits with more than 5 letters:", long_fruits)