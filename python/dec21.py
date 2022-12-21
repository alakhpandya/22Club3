"""
7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
Ask user for quantity
Assume each item costs 100.
Calculate and print total amount to be paid by user.

8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750
----------------Thanks for shopping with us!---------------

case 2- when customer is eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------
"""

# leap year: 1. If it is not a century year: must be divisible by 4
# 2. If century year: must be divisible by 400
"""
year = int(input("Enter a year: "))
if year % 100 == 0:
    # century year
    if year % 400 == 0:
        print("Leap year.")
    else:
        print("Not a leap year.")
else:
    if year % 4 == 0:
        print("Leap year.")
    else:
        print("Not a leap year.")
"""
name = input("Enter your name: ")
# name = "Dhiraj Poojara"
contact = input("Mobile no: ")
# contact = "9876543210"
date = input("Enter date (dd/mm/yyyy): ")
# date = "21/12/2022"
print("Enter quantity & price for the following items:")
item1_quantity = int(input("Item 1 quantity: "))
item1_price = int(input("Item 1 price: "))
item2_quantity = int(input("Item 2 quantity: "))
item2_price = int(input("Item 2 price: "))
item3_quantity = int(input("Item 3 quantity: "))
item3_price = int(input("Item 3 price: "))
discount = 0

item1_total = item1_quantity * item1_price
item2_total = item2_quantity * item2_price
item3_total = item3_quantity * item3_price
grand_total = item1_total + item2_total + item3_total

if grand_total >= 1000:
    discount = round(grand_total * 0.1)

final_amount = grand_total - discount

print("Retail Invoice".center(100, "-"))
print(f"Customer Name: {name}")
print(f"Contact Number: {contact}")
print(f"Date of Invoice: {date}")
print("-" * 100)
print("Items\tPrice\tQuantity\tTotal".expandtabs(30))
print(f"Item 1\t{item1_price}\t{item1_quantity}\t{item1_total}".expandtabs(30))
print(f"Item 2\t{item2_price}\t{item2_quantity}\t{item2_total}".expandtabs(30))
print(f"Item 3\t{item3_price}\t{item3_quantity}\t{item3_total}".expandtabs(30))
print(" " * 89, "-" * 10)
if grand_total >= 1000:
    print("Grand Total: ".rjust(89) + f" {grand_total}")
    print("Discount: ".rjust(86) + f"    {discount}")
    print(" " * 89, "-" * 10)
print("Final Amount: ".rjust(89) + f" {final_amount}")
print("Thanks for shopping with us!".center(100, "-"))
