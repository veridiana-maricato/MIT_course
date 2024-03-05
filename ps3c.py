current_savings = 0
annual_salary = 150000
total_cost = 1000000
semi_annual_raise = .07
total_months = 36
portion_down_payment = 0.25*total_cost

portion_saved = 0.5
heighest = 1
prev_heighest = heighest
lowest = 0 
prev_lowest = lowest
guessed = False
number_of_tries = 0


def earn_monthly_money():
    global total_months, annual_salary, semi_annual_raise, current_savings, portion_saved
    current_savings = 0

    for month in range(36):
        if ((total_months - 1) % 6 == 0 and total_months !=1): 
            annual_salary = annual_salary * (1+semi_annual_raise) # annual raise

        current_savings += annual_salary/12*portion_saved # savings of each month

        current_savings += current_savings * 0.04 / 12 # monthly investment money


while not guessed:
    earn_monthly_money()
    portion_saved = round(((heighest + lowest) / 2), 6)


    if(current_savings < portion_down_payment - 100):
        prev_lowest = lowest
        heighest = prev_heighest
        lowest = round(((heighest + lowest) / 2), 10)

        print(int(current_savings), "current savings up")        
        print("lowest:", lowest)
        print("heighest:", heighest)
        print("portion_saved:", portion_saved)
        print("-------------------------------")

    elif(current_savings > portion_down_payment + 100):
        lowest = prev_lowest
        prev_heighest = heighest
        heighest = round(((heighest + lowest) / 2), 10)
        
        print(int(current_savings), "current savings down")
        print("lowest:", lowest)
        
        print("heighest:", heighest)
        print("portion_saved:", portion_saved)
        print("-------------------------------")


    number_of_tries += 1
    print(portion_saved)

    if (portion_down_payment - 100 < current_savings < portion_down_payment + 100):
        print(number_of_tries, portion_saved, current_savings)
        guessed = True








    






