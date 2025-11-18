# 5. Inheritance with a Helper Method 
# Challenge: Create a shared method in the parent class and have the child class use it in a specialized function.
# Requirements:
# Create a base class Worker with a constructor for self.hourly_rate.
# In Worker, define a method _calculate_pay(hours) that returns hours * self.hourly_rate.
# Create a subclass Contractor that inherits from Worker.
# In Contractor, define a method get_weekly_salary(hours) that calls self._calculate_pay(hours) and adds a fixed $\$100$ bonus before returning the final amount.
# Create a Contractor object (rate $30) and call get_weekly_salary(40). Print the result.

class worker:
    def __init__(self,hourly_rate):
        self.hourly_rate=hourly_rate
    def _calculate_pay(self,hours):
        self.hours=hours
        return hours*self.hourly_rate
class contractor(worker):
    def get_weekly_salary(self,hours):
        amount=self._calculate_pay(hours)
        fixed_amount=100
        final_amount=fixed_amount+amount
        return final_amount
obj=contractor(30)
print(f"contractor final salary is: {obj.get_weekly_salary(40)}")



