fruits = []
for i in range(5):
    fruit = input(f"Enter your favorite fruit #{i+1}: ")
    fruits.append(fruit)

print("\nYour favorite fruits are:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Middle fruit:", fruits[2])


fruits[1] = "Mango"
print("\nAfter replacing the second fruit:", fruits)

fruits.append("Watermelon")
print("After adding Watermelon:", fruits)

del fruits[0]
print("After removing the first fruit:", fruits)

fruits.sort()
print("Sorted list:", fruits)

long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Fruits with more than 5 letters:", long_fruits)