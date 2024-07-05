time1 = int(input("First time: "))
print()
suffix1 = input("suffix: ")
print()
time2 = int(input("Second time: "))
print()
suffix2 = input("suffix: ")
print()

# Compare the two times and determine whether the event occurs
# before the second event, at the same time, or after the second event.

# Print "Before", "Same", or "After"

if suffix1 == suffix2:
    if time2 > time1:
        print("Before")
    else:
        if time1 > time2:
            print("After")
        else:
            print("Same")
else:
    if suffix2 == "pm":
        print("Before")
    else:
        print("After")
