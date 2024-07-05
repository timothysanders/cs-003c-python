print("First domino.")
left1 = int(input("left value: "))
print()
right1 = int(input("right value: "))
print()

print("Second domino.")
left2 = int(input("left value: "))
print()
right2 = int(input("right value: "))
print()

matched = False
flip1 = left1 != right1
flip2 = left2 != right2
print(flip1, flip2)

if right1 == left2:
    print("Match without flipping")
    matched = True

if left1 == left2 and not matched and flip1:
    print("Match after flipping first domino")
    matched = True

if right1 == right2 and not matched and flip2:
    print("Match after flipping second domino")
    matched = True

if left1 == right2 and flip1 and flip2:
    print("Match after flipping both dominos")
    matched = True

if left1 != left2 and left1 != right2 and right1 != right2 and right1 != left2:
    print("No match")
