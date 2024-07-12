n = int(input())

# Draw top half and middle of the triangle
for leftStars in range(n):
    for column in range(2 * n - 1):
        firstStar = n - 1 - leftStars
        lastStar = n - 1 + leftStars
        if column < firstStar or column > lastStar:
            print("-", end="")
        else:
            print("*", end="")

    print()

# Draw bottom half of the triangle
# Your code goes here
for leftStars in range(n - 1):
    for column in range(2 * n - 1):
        firstStar = leftStars + 1
        lastStar = 2 * n - 3 - leftStars
        if column < firstStar or column > lastStar:
            print("-", end="")
        else:
            print("*", end="")
    print()