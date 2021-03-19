# x=20
# y=30
#
# if x>y:
#     print("x is greater than y")
# else:
#     print("y is greater than x")

# x = 30
# y = 20
# z = 20

# if x > y and x > z:
#     print("x is greatest.")
# elif y > x and y > z:
#     print("y is greatest.")
# else:
#     print("z is greatest.")


p = int(input("Enter the principle amount:"))
t = float(input("Enter the time period in year:"))
r = float(input("Enter the rate of interest:"))

total = p * t * r / 100

print("The total interest amount= ",total)
