# 2. Using Abstraction for Internal Calculation
# Challenge: Create a Payroll class where the detailed tax calculation is abstracted away from the main salary method.
# Requirements:
# Define a class Payroll with a constructor that initializes self.base_salary.
# Define a private method (using convention) self._calculate_tax(salary) that simply returns salary * 0.15 (15% tax).
# Define a public method get_net_salary() that calls the private tax method and returns the final net salary (base_salary - tax_amount).
# Create a Payroll object with a base salary of 5000.
# Print the result of get_net_salary(). The user gets the net salary without directly interacting with the tax formula.

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

