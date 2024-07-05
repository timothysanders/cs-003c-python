hour = int(input("Hour: "))
suffix = input("Suffix: ")
time = "morning"
if suffix == "pm":
    if hour < 6:
        time = "afternoon"
else:
    time = "evening"
print("Good", time)
