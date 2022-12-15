"""
x = 20
y = int(input("Enter y: "))
if y > 10:
    x *= 2
print(f"x = {x}\ny = {y}")
"""
# shorthand if:
"""
x = 20
y = int(input("Enter y: "))
if y > 10: x *= 2
print(f"x = {x}\ny = {y}")
"""

# if-else
"""
marks = int(input("Enter marks: "))

if marks >= 24:
    print("Pass")
else:
    print("Fail")

# shorthand if-else
print("Pass") if marks >= 24 else print("Fail")
"""

# if-else ladder
"""
n = float(input("Enter any number: "))
if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")
"""
# shorthand: There is no shorthand of if-else ladder

"""
PAR = 10

strokes
PAR             =>  PAR
PAR - 1         =>  Birdy
PAR - 2 to 2    =>  Eagle
1               =>  Hole in One!
PAR + 1         =>  Bogey
PAR + 2         =>  Double Bogey
PAR + 3 or more =>  Go Home
"""
# IMP: There is no switch-case in Python

a = float(input("Enter two numbers:\n"))
b = float(input())

op = input("Enter the operation (+, -, * or /) :")

if op == "+":
    print(f"{a} + {b} = {a + b}")

elif op == "-":
    print(f"{a} - {b} = {a - b}")

elif op == "*":
    print(f"{a} * {b} = {a * b}")

elif op == "/":
    print(f"{a} / {b} = {a / b}")

else:
    print("Invalid operation, please try again...")

# if-else examples:
"""
1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A

2. Write a Python program to find whether a given year is a leap year or not. 
Test Data : 2016
Expected Output :
2016 is a leap year.

3. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52
Expected Execution:
1st Number = 12
2nd Number = 25
3rd Number = 52

52 is the largest number.

4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
Test Data : 
x-coordinate: 7
y-coordinate: 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.

5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
The candidate is not eligible.


6. Take values of length and breadth of a rectangle from user and check if it is square or not.

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

9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the final salary.
"""