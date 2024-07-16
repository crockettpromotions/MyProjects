"""A way to visualize your finances"""

# Title
print('Financial Visualizer')

# Inputs
annual_salary = float(input('Annual Salary: '))
rent = float(input('Monthly Housing: '))
bills = float(input('Monthly Bills: '))
food = float(input('Weekly Food: '))
travel = float(input('Annual Travel: '))

# Making sure inputs are numbers
if annual_salary.is_integer() and rent.is_integer() and bills.is_integer() and food.is_integer() and travel.is_integer():
    print('All inputs confirmed valid')
else:
    print('Invalid input, please try again')

# Taxes
if annual_salary <= 10000:
    tax = annual_salary * .05
elif 10000 < annual_salary <= 40000:
    tax = annual_salary * .1
elif 40000 < annual_salary <= 80000:
    tax = annual_salary * .15
elif 80000 < annual_salary:
    tax = annual_salary * .25

# Convert to annual
annual_rent = rent * 12
annual_bills = bills * 12
annual_food = food * 12
annual_travel = travel * 12
