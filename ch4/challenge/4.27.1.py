from math import sqrt

n = int(input("Enter a positive integer: "))
print()

print("  n | Root of n")
print("----|----------")

for x in range(0, n + 1):
    print("%3d |  %.6f" % (x, sqrt(x)))