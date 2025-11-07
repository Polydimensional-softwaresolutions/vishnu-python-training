#Basic Dog Class Create a class Dog with a constructor that takes name and breed as parameters and initializes them as instance attributes. 
# Create a Dog object and print its breed.

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
dog=Dog("Leo","german Shepherd")
print(dog.name, dog.breed)