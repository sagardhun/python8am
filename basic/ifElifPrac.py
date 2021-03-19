
#======================================================================================================================

# x = int(input("Enter 1 for addition: \n  2 for subtraction:\n   3 for multiplication:  \n 4 for division:"))
#
# if x == 1:
#     y = int(input("Enter first number:"))
#     z = int(input("Enter another number:"))
#     print("The sum of given numbers is: ", y + z)
# elif x == 2:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter another number:"))
#     print("The subctraction from first to second is:", a - b)
#
# elif x == 3:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter the second number:"))
#     print("The product of these two numbers is: ", a * b)
#
# elif x == 4:
#     a = int(input("Enter the first number:"))
#     b = int(input("Enter the denominator number:"))
#     print("The result of first divided by second is: ", a / b)
#
# else:
#     print("Enter vaplid number only.")
#=======================================================================================================================
#
#
# amount = 0
# package = 0
# tax = 0
# total_amount = 0
# grand_total = 0
#
# print("Welcome to COMPUTER BAZZAR:")
#
# print("1. DELL:(RS.20000)")
# print("2. MAC: (RS.50000)")
# print("3. TOSHIVA:(RS. 30000)")
#
# laptop = int(input("Choose the laptop by number"))
# quantity = int(input("Enter the quantity:"))
# if laptop == 1:
#     amount = 20000 * quantity
#     print("amount:", amount)
# elif laptop == 2:
#     amount = 50000 * quantity
# elif laptop == 3:
#     amount = 30000 * quantity
# else:
#     print("Enter valid option.")
#
# print("Enter packaging option:")
# print("1.Bag(Rs.1000")
# print("2.Plastic Bag(Rs.500)")
# print("3.GiftBag(Rs.5000)")
# print("4.None(Free)")
#
# pkg = int(input("Enter option:"))
# if pkg == 1:
#     package = 1000
# elif pkg == 2:
#     package = 500
# elif pkg == 3:
#     package = 5000
# else:
#     print("Enter valid option only.")
#
# total_amount = amount + package
#
# print("Total amount=", total_amount)
#
# print("Enter from which city you are:")
# print("1.Kathmandu(13%)")
# print("2.Lalitpur (0%)")
# print("3.Bhaktapur(0%)")
#
# city = int(input("Enter option:"))
#
# if city == 1:
#     tax = total_amount * 13 / 100
# elif city == 2:
#     tax = 0
# elif city == 3:
#     tax = 0
# else:
#     print("Enter valid option only.")
#
# grand_total = total_amount + tax
#
# print("Grand total=", grand_total)

#======================================================================================================================
# homedelivery1000    selfpicup free
# bag1000 plasticbag500  giftbox 5000 nobag
# ktm(13% vat)   bkt(0) ltp(0)
# total amount
# total price
# total
#======================================================================================================================


print("choose starting station number:")
print("1.station0\n2.station1\n3.station3")
