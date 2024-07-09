# Timothy Sanders and Zoraida Rodriguez
# CS03C - Fundamentals of Python
# 07/07/2024
import sys

TAX_RATE1 = 0.10
TAX_RATE2 = 0.15
TAX_RATE3 = 0.25
MAX_INCOME = 150000.00

# Changed variable to take first and last name
userFullName = input("Enter your first and last name: ")
# Validate that the user's name is only alpha characters
if not userFullName.replace(" ", "").isalpha():
    print("Entered name can only contain spaces or letters!")
    userFullName = input("Enter your first and last name: ")
    if not userFullName.replace(" ", "").isalpha():
        print("Entered name can only contain spaces or letters!")
        sys.exit("ERROR: Incorrect name entered.. exiting program")

# Program determines whether user is married or single to 
# calculate taxes and get required information
marriedStatus = input("Are you married? (Y/N): ")
# Validate input for
if marriedStatus.lower() != "y" and marriedStatus.lower() != "n":
    print("Incorrect value specified for marital status, please respond only with Y/N")
    marriedStatus = input("Are you married? (Y/N): ")
    if marriedStatus.lower() != "y" and marriedStatus.lower() != "n":
        print("Incorrect value specified for marital status, please respond only with Y/N")
        sys.exit("ERROR: Incorrect marital status entered.. exiting program")
if marriedStatus.lower() == "y":
    marriedStatus = True
    spouseFullName = input("Enter your spouse's first and last name: ")
    if not spouseFullName.replace(" ", "").isalpha():
        print("Entered name can only contain spaces or letters!")
        spouseFullName = input("Enter your spouse's first and last name: ")
        if not spouseFullName.replace(" ", "").isalpha():
            print("Entered name can only contain spaces or letters!")
            sys.exit("ERROR: Incorrect name entered.. exiting program")
    userEarnedSalary = input("Enter your salary: ")
    if not userEarnedSalary.replace(".", "").isdigit():
        print("Entered salary may only contain numbers!")
        userEarnedSalary = input("Enter your salary: ")
        if not userEarnedSalary.replace(".", "").isdigit():
            print("Entered salary may only contain numbers!")
            sys.exit("ERROR: Incorrect salary entered.. exiting program")
    earnedSalary = float(userEarnedSalary)
    userSpouseEarnedSalary = input("Enter your spouse's salary: ")
    if not userSpouseEarnedSalary.replace(".", "").isdigit():
        print("Entered salary may only contain numbers!")
        userSpouseEarnedSalary = input("Enter your spouse's salary: ")
        if not userSpouseEarnedSalary.replace(".", "").isdigit():
            print("Entered salary may only contain numbers!")
            sys.exit("ERROR: Incorrect salary entered.. exiting program")
    spouseEarnedSalary = float(userSpouseEarnedSalary)
    combinedSalary = earnedSalary + spouseEarnedSalary
    if combinedSalary <= 16000.00:
        taxesOwed = combinedSalary * TAX_RATE1
    elif combinedSalary <= 64000.00:
        taxesOwed = ((combinedSalary - 16000.00) * TAX_RATE2 + 1600.00)
    elif combinedSalary > 64000.00:
        taxesOwed = ((combinedSalary - 64000.00) * TAX_RATE3 + 8800.00)
elif marriedStatus.lower() == "n":
    marriedStatus = False
    userEarnedSalary = input("Enter your salary: ")
    if not userEarnedSalary.replace(".", "").isdigit():
        print("Entered salary may only contain numbers!")
        userEarnedSalary = input("Enter your salary: ")
        if not userEarnedSalary.replace(".", "").isdigit():
            print("Entered salary may only contain numbers!")
            sys.exit("ERROR: Incorrect salary entered.. exiting program")
    earnedSalary = float(userEarnedSalary)
    combinedSalary = earnedSalary
    if combinedSalary <= 8000.00:
        taxesOwed = combinedSalary * TAX_RATE1
    elif combinedSalary <= 32000.00:
        taxesOwed = ((combinedSalary - 8000.00) * TAX_RATE2 + 800.00)
    elif combinedSalary > 64000.00:
        taxesOwed = ((combinedSalary - 32000.00) * TAX_RATE3 + 4400.00)
else:
    print("Invalid input. Please enter Y or N.")
    sys.exit()

print("Taxes owed are $%.2f" % taxesOwed)

'''
Example program execution
$ python Lab3.35.25.py

Enter your first and last name: Tim Sanders
Are you married? (Y/N): y
Enter your spouse's first and last name: Danielle Sanders
Enter your salary: 15000
Enter your spouse's salary: 49000
Taxes owed are $8800.00
'''