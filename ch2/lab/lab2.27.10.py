# CS03C Lab 2 - 2.27.10
# Tim Sanders and Zoe Rodriguez
# 6/30/2024

# Collect user input data and store it in variables
user_input_car_cost = float(input("Please provide the cost your car in dollars: "))
# New lines and indentations are added after open parentheses to improve readability
user_input_yearly_mileage = int(
    input("Please provide the number of miles you will drive each year: ")
)
user_input_gas_gallon_cost = float(input("Enter the cost of gas per gallon: "))
user_input_mpg = int(input("Enter the miles per gallon of the car: "))
user_input_estimated_resale_value = float(
    input("Enter estimated resale value after 5 years: ")
)

# Define constant for the period over which the analysis will be run
OWNERSHIP_PERIOD = 5

# Calculates the total cost of ownership for the car
yearly_gallons_of_gas = user_input_yearly_mileage / user_input_mpg
total_gallons_of_gas = yearly_gallons_of_gas * OWNERSHIP_PERIOD
total_gas_cost = total_gallons_of_gas * user_input_gas_gallon_cost
ownership_expenditure = total_gas_cost + user_input_car_cost
total_ownership_cost = ownership_expenditure - user_input_estimated_resale_value

# Prints the total cost of ownership for the car
print("The total estimated cost of ownership over 5 years is: $%.2f" % total_ownership_cost)

# Sample Output
# Please provide the cost your car in dollars: 32970.00
# Please provide the number of miles you will drive each year: 15000
# Enter the cost of gas per gallon: 4.29
# Enter the miles per gallon of the car: 44
# Enter estimated resale value after 5 years: 18308.00
# The total estimated cost of ownership over 5 years is: $21974.50
