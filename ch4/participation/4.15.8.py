string = input()
valid = True
i = 0

while valid and i < len(string):
    # To be valid, the string can only contain digits
    # and a sign character (+ or -) as the first character.
    # Your code goes here
    if not string[i].isdigit():
        if i == 0 and string[i] in "+-":
            valid = True
        else:
            valid = False
    i = i + 1

if valid:
    print("valid integer")
else:
    print("invalid integer")
