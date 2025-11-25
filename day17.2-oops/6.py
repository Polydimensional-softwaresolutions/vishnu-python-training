# Create a class Calculator.
# Define a private method self.__apply_tax(total) that returns total * 1.05.
# Define a public method get_final_price(base_price) that calls the private method internally and returns the result. 
# The user only calls get_final_price(), hiding the tax calculation details (Abstraction).

class Calculator:
    def __apply_tax(self,total):
        self.total=total
        return total * 1.05
    def get_final_price(self,base_price):
        return self.__apply_tax(base_price)
    

cal=Calculator()
print(cal.get_final_price(100))


    