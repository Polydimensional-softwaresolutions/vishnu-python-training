# 4. Employee Salary Calculation 
# Challenge: Design a payroll system that handles different employee types while securing pay rates and providing a single calculation point.
# Requirements:
# Inheritance: Create a base class Employee with a constructor taking name.
# Encapsulation: In Employee, encapsulate the base pay rate attribute (self._pay_rate = 25.00). Provide a public setter method set_pay_rate(new_rate) that validates the rate (must be $> 0$).
# Polymorphism: Create subclasses HourlyEmployee and SalaryEmployee. Both must implement a method calculate_weekly_pay():
# HourlyEmployee returns self._pay_rate * 40.
# SalaryEmployee returns a fixed value (e.g., 1200), ignoring the pay rate attribute.
# Abstraction: Define a report generator method (e.g., generate_paystub()) in the base class that simply calls the specialized calculate_weekly_pay() method, providing the abstract salary figure to the end user.

class Employee:
    def __init__(self,name):
        self.name=name
        self._pay_rate=25.00

    def set_pay_rate(self,new_rate):
        if new_rate > 0:
            self._pay_rate=new_rate
    
    def calculate_weekly_pay(self):
        return self._pay_rate
    
    def generate_paysub(self):
        weekly_pay=self.calculate_weekly_pay()
        return weekly_pay

class HourlyEmployee(Employee):
    def calculate_weekly_pay(self):
        return self._pay_rate * 40


class SalaryEmployee(Employee):
    def calculate_weekly_pay(self):
        return 1200

obj= Employee("vishu")
print(obj.calculate_weekly_pay())
hourly = HourlyEmployee("")
salary = SalaryEmployee("")

print(obj.generate_paysub())
print(hourly.generate_paysub())
print(salary.generate_paysub())




