# Create a base class Product with a constructor for self.id.
# Create an intermediate class Electronic that inherits from Product and adds a warranty_months attribute.
# Create a final class Smartphone that inherits from Electronic.
# Add a public method get_summary() in Smartphone that retrieves the ID (from Product) and warranty (from Electronic), abstracting the multi-level attribute lookup.

class Product:
    def __init__(self,id):
        self.id=id

class Electronic(Product):
    def __init__(self, id,waranty_months):
        super().__init__(id)
        self.warranty=waranty_months
        

class Smartphone(Electronic):
    def get_summary(self):
        print("id is:",self.id ,"and" , "warranty months is:",self.warranty,"months")
        return self.id , self.warranty
obj=Smartphone(12345,12)
final=obj.get_summary()

