# 5. Abstraction vs. Encapsulation Distinction 
# Challenge: Explain the difference between Abstraction and Encapsulation using the Payroll class (from Q2) as an example.
# Requirements:
# In your own words, define Encapsulation as it relates to the _calculate_tax method and the base_salary attribute.
# In your own words, define Abstraction as it relates to the get_net_salary method.
# Explain why you must use Encapsulation (hiding the tax formula) to achieve Abstraction (simplifying the net salary calculation).

class payroll:
    def __init__(self,base_salary):
        self.base_salary=base_salary
    def _calculate_tax(self,salary):
         return salary * 0.15
    def get_net_salary(self):
        tax_amount=(self._calculate_tax(self.base_salary))
        net_salary=(self.base_salary-tax_amount)
        return net_salary
my_tax=payroll(5000)
print(my_tax.get_net_salary())

1.Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

-->.the _calculate_tax and base_salary are encapsulated.
-->._calculate_tax is private method means its not access directly.
-->.in _calculate_tax salary*0.15 formula is hidden from the user ,dont need to know the how tax is cpmputed.

2.Abstraction is the process of hiding the complex implementation details and showing only the essential features of an object to the user.
-->the get_net_salary() method provides a simple and clear function for the user.

3.