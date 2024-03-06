current_savings = 0
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What portion of your annual salary do you want to save? "))
total_cost = float(input("How much does your dream house costs? "))
# annual_salary = 120000
# portion_saved = 1
# total_cost = 500000
total_months = 0
portion_down_payment = 0.25*total_cost

while(current_savings < portion_down_payment):
    print(current_savings)
    current_savings += annual_salary/12*portion_saved
    current_savings += current_savings * 0.04 / 12
    total_months += 1
    
print(total_months)

