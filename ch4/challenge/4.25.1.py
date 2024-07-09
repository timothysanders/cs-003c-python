done = False
factor = 0.0

while not done:
    getSecond = True
    command = input("From unit (in, cm, m, again, quit): ")
    print()
    if command == "in":
        factor = 2.54  # Conversion factor from in to cm
        unit1 = command
    elif command == "cm":
        factor = 2.54
        unit1 = command
    elif command == "m":
        unit1 = command
    elif command == "again":
        getSecond = False
    elif command == "quit":
        done = True
        getSecond = False
    else:
        print("Sorry, unknown unit.")
        getSecond = False

    if getSecond:
        unit2 = input("To unit: ")
        print()
        if unit2 == "in":
            factor = factor / 2.54  # Convert factor from cm to in
        elif unit2 == "cm":
            if unit1 == "m":
                factor = 100
            elif unit1 == "in":
                factor = 1 / factor
        elif unit2 == "m":
            if unit1 == "in":
                factor = (1 / factor) / 100
        elif unit1 == unit2:
            factor = 0.0
        else:
            print("Sorry, unknown unit.")
            # Your code goes here
    if not done and factor != 0.0:
        value = float(input("Enter the value to be converted: "))
        print()
        print(value, unit1, "=", value * factor, unit2)
