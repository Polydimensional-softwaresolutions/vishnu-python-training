bill=int(input("bill: "))
tip_percentage=int(input("tip%:"))
tip_amount=(tip_percentage / 100) * bill
total_amount=bill+tip_amount
people=int(input("enter the no of people attend:"))

per_person_amount= total_amount/people

print(f"The ampount each person should pay is {per_person_amount}")
