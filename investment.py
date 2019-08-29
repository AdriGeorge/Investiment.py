""" This program calculates the 'possible' return 
    of an investment that has a fixed annual return """


# Method for calculating the return 
# on an investiment with a recurring deposit

def investment_fund(investment, time, recurrence):
    if recurrence == 1:
        deposited = investment*time*12
        total_for_one = investment + investment * annual_return/12
        total = total_for_one
        for month in range(1, time*12):
            total += total*(annual_return/12) + total_for_one
        effettive_earning = float(total-time*12*investment)
        
    elif recurrence == 2:
        deposited = investment*time*2
        total_for_one = investment + investment * annual_return/2
        total = total_for_one
        for semester in range(1, time*2):
            total += total*(annual_return/2) + total_for_one
        effettive_earning = float(total-time*2*investment)
        
    elif recurrence == 3:
        deposited = investment*time
        total_for_one = investment + investment* annual_return
        total = total_for_one
        for year in range(1,time):
            total+=total*annual_return + total_for_one
        effettive_earning = float(total-time*investment)
        
    return f"Total: {int(total)}\n";\
           f"Deposited: {int(deposited)}\n;"\
           f"Earning: {int(effettive_earning)}\n"       


# Method for calculating the return 
# on an investiment with a tantum deposit   
    
def tantum_fund(tantum, time):
    total = tantum
    for year in range(1,time):
        total += total * annual_return
    effettive_earning = float(total-tantum)
    return f"Total: {int(total)}\n";\
           f"Earning: {int(effettive_earning)}\n"     


print("WELCOME!")
while True:
    try: 
        annual_return = float(input("Annual return (%): ")) 
    except ValueError:
        print('Only number!')
        break
    annual_return /= 100
    choice = input("Constant investment(1) or Tantum(2)?: ")
    if choice == "1":  
        recurrence = int(input("How often do you want to deposit? Every month(1) Every 6 month(2) Every year(3): "))
        if recurrence < 1 or recurrence > 3:
            print("You can only select: 1 ,2 or 3! Restart!")
            break
        investment = float(input("How much (Euro)?: "))
        time = int(input("How long (years)?: "))
        money = investment_fund(investment, time, recurrence)
    elif choice == "2":
        tantum = int(input("How much (Euro)?"))
        time = int(input("How long would you like to keep the money in this fund (years)?: "))
        money = tantum_fund(tantum, time)
    else:
        print("You can only select: 1 or 2! Restart!")
        break
    print(money+"\n")
    
    replace = input("New investment? (y/n): ")
    if replace != "y":
        break
    
    
