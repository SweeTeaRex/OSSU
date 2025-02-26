yearly_salary = float(input("Enter your yearly salary: "))
monthly_salary = yearly_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = int(input("Enter the cost of your dream home: "))
raiseSemi = float(input("Semianual raise, as decimal: "))

r = float(0.05)
monthly_r = r/12

down_payment_percent = 0.25
amount_saved = 0
portion_down_payment = cost_of_dream_home*0.25
months = 0

while amount_saved < portion_down_payment:
    amount_saved = amount_saved + (amount_saved*monthly_r)
    amount_saved = amount_saved + monthly_salary*portion_saved
    months+= 1
    if(months%6 == 0):
        yearly_salary = yearly_salary + (yearly_salary*raiseSemi)
        monthly_salary = yearly_salary/12

print(f"Down payment needed: ", portion_down_payment)
print(f"Yearly salary: ", yearly_salary)
print(f"Down payment percent: ", down_payment_percent)
print(f"Number of months needed: ", months)