# CS03C Lab 2 - 2.27.5
# Timothy Sanders and Zoraida Rodriguez
# 6/30/2024

# Declare first and second integer inputs. 
user_value_one = int(input("Please enter a single integer value: "))
user_value_two = int(input("Please enter a second integer value: "))

# Define each variable based on the user input and its corresponding formulas.
calculated_sum = user_value_one + user_value_two
calculated_difference = user_value_one - user_value_two
calculated_product = user_value_one * user_value_two
calculated_average = (user_value_one + user_value_two) / 2
calculated_distance = abs(user_value_one - user_value_two)
calculated_minimum = min(user_value_one, user_value_two)
calculated_maximum = max(user_value_one, user_value_two)

# Print the results of the formulas.
# Each formula inputs correct alignments to the right.
print("%-20s %5d" % ("Sum:", calculated_sum))
print("%-20s %5d" % ("Difference:", calculated_difference))
print("%-20s %5d" % ("Product:", calculated_product))
# Average is rounded to two decimal places.
# Error exists where integers do not aligned with higher integer values
print("%-20s %8.2f" % ("Average:", calculated_average))
print("%-20s %5d" % ("Distance:", calculated_distance))
print("%-20s %5d" % ("Minimum:", calculated_minimum))
print("%-20s %5d" % ("Maximum:", calculated_maximum))

# Sample Output
# Please enter a single integer value: 5
# Please enter a second integer value: 10
# Sum:                15
# Difference:         -5
# Product:            50
# Average:             7.5
# Distance:            5
# Minimum:             5
# Maximum:            10
