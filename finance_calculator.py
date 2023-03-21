import math 

print(
    "---------------------------------------"
    "\ninvestment - to caluculate the amount of interest you'll earn on your invesement"
    "\nbond - to calculate the amount you'll have to pay on a home loan"
    "\n---------------------------------------"
)
calculation = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: "
)
if calculation.upper() == "INVESTMENT":
    deposit = float(input("Enter the amount you are depositing: "))
    interest = float(input("Enter the interest rate: ").replace("%",""))
    years = int(input("Enter the number of years you are investing for: "))
    interest_type = input("Enter 'simple' or 'compound' to determine the type of interest: ")
    if interest_type.upper() == "SIMPLE":
        interest = deposit * (interest / 100) * years
        #{:.2f} is used to round the number to 2 decimal places
        #resource: https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14.
        print(f"Your interest is R{interest:.2f}")
    else:
        interest = deposit * math.pow(1 + interest / 100,years)
        print(f"Your interest is R{interest:.2f}")
elif calculation.upper() == "BOND":
    house_value = float(input("Enter the present value of the house: "))
    interest = float(input("Enter the interest rate: ").replace("%",""))
    months = int(input("Enter the number of months you are paying over: "))
    interest = (interest / 100) / 12
    bond = (interest * house_value) / (1 - math.pow(1 + interest,-months))
    print(f"Your bond is R{bond:.2f}")
else:
    print("Your input is invalid. Please choose either 'investment' or 'bond'.")
