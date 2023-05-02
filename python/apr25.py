"""
1.	Angles Of Valid Triangle?
    Problem Description
    You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.
    A triangle is valid if sum of its angles equals to 180.
    Problem Constraints
    1 <= A, B, C <= 180

    Input Format
    First line of the input contains an integer A.
    Second line of the input contains an integer B.
    Third line of the input contains an integer C.

    Output Format
    Print 1 if the triangle having given sides is valid, else print 0.

    Example Input
    Input 1:
    60
    60
    60
    Input 2:
    30
    40
    50
    Example Output
    Output 1:
    1 
    Output 2:
    0

2.	Profit Or Loss
    Problem Description
    You are given the Cost Price C and Selling Price S of a Product. You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss. It is guaranteed that Cost Price and Selling Price are not equal.
    Problem Constraints
    1 <= C, S <= 109, C ≠ S
    Input Format
    First line of the input contains a single integer C.
    Second line of the input contains a single integer S.
    Output Format
    Print two integers in separate lines.
    First integer denotes whether there is a profit or loss. If there is a profit, print 1, else print -1.
    Second integer is a non-negative integer denoting the absolute value of total profit or loss.
    Example Input
    Input 1:
    2
    4
    Input 2:
    4
    1
    Example Output
    Output 1:
    1
    2
    Output 2:
    -1
    3
3.	Max of two
    Problem Description
    Write a program to input two numbers(A & B) from user and print the maximum element among A & B in each line.
    Problem Constraints
    1 <= A <= 1000000
    1 <= B <= 1000000
    Input Format
    First line is a single integer A.
    Second line is a single integer B.
    Output Format
    One line containing the greater integer A or B.
    Example Input
    Input 1:
    5 
    6
    Input 2:
    1000 
    10000
    Example Output
    Output 1:
    6
    Output 2:
    10000


4.	Valid Statements
    Which of the following are valid statements in python: Assume that the variable ‘a’ has already been declared:

    a. if a>=2:
        print("TRUE")
    b. if (a=>2):
        print("TRUE")
    c. if (a%2!=0):
        print("TRUE")
    d. if a//3=1:
        print("TRUE")

5.	Roller Coaster Ride
    Problem Description
    Write a program that takes the age of the user as input and tells them if they're old enough to ride a roller coaster. The minimum age to ride the roller coaster in this question is 13.
    Input Format
    There is only 1 single line in the input, which is the age of the user.
    Output Format
    Print the following if user can ride the roller coaster:
    You can ride the roller coaster!
    Print the following if user can't ride the roller coaster:
    You can't ride the roller coaster.
    Example Input
    Input 1:-
    9
    Input 2:-
    13
    Example Output
    Output 1:-
    You can't ride the roller coaster.
    Output 2:-
    You can ride the roller coaster!

6.	Temperature Flow Chart
    The following flowchart is given. What would be the output if Temp=19?
    
    A)	Above Freezing
    B)	No Output
    C)	Below Freezing
    D)	Error
"""
# from sys import getsizeof
# l1 = [x for x in range(1, 101)]
# squares = map(lambda n : n ** 2, l1)
# # print(getsizeof(squares))
# for x in squares:
#     print(x, end=", ")

"""
1.	Class Performance 2
    Problem Description
    You have been given a dataset for marks of 2 subjects, scored by students of classes ClassA and ClassB. You now want to compare the performances of class A and class B by finding out the average performance of the classes. Write a program to find if class A performed better. Print True is Class A is strictly better else return False.
    Input Format
    There are 4 lines in the input.
    The first and second lines are marks of subjects for Class A.
    The third and fourth lines are marks of subjects for Class B.
    Output Format
    Print True if class A is strictly better else False.
    Example Input
    Input 1:-
    80
    27
    54
    61
    Input 2:-
    54
    61
    80
    27
    Example Output
    Output 1:-
    False
    Output 2:-
    True
    Sample Exaplanation
    Explanation 1:-
    The average marks of class A is (80 + 27)/2 = 53.5, and the average of class B is (54 + 61)/2 = 57.5, so class B's average
    is better hence False is printed.

    Explanation 2:-
    The average marks of class A is(54 + 61)/2 = 57.5, and the average of class B is(80 + 27)/2 = 53.5, so class A's average is better hence True is printed.

2.	Min of two
    Problem Description
    Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.
    Problem Constraints
    1 <= A <= 1000000
    1 <= B <= 1000000

    Input Format
    First line is a single integer A.
    Second line is a single integer B.

    Output Format
    One line containing an integer as per the question.

    Example Input
    Input 1:
    5 
    6
    Input 2:
    1000 
    10000
    Example Output
    Output 1:
    5
    Output 2:
    1000

3.	All correct about x
    You have been given the following piece of code. Assume that x has already been declared.
    
    if x > 2:
        x = x*2
    if x > 4:
        x = 0
    print(x)
    Select the correct statement regarding this code.
    A.	Output will always be equal to 0
    B.	If x > 2 and x < 4, final value of x will be double the initial value
    C.	For x in 0 < x < 4 the output will always be 0
    D.	For x > 2, output will be equal to 0

4.	If-else output
    What will be the output of the following code:
    x = 2
    if x==2:
        x = 3
    x = 4
    else:
        x = 5
    print(x)

    A.	3
    B.	4
    C.	5
    D.	Error

5.	Guide the coordinate
    Problem Description
    Given the (x, y) coordinates of a point on a 2D plane, write a program that transforms these coordinates according to the conditions given below.
    •	If the sum of x and y coordinates is a multiple of 5, then increment both the coordinates by 1 and print.
    •	If the x coordinate is even and the y coordinate is odd, then increment y by 1 and print both.
    •	If the y coordinate is even and the x coordinate is odd, then increment x by 1 and print both.
    Input Format
    Two lines containing integer x and y.
    Output Format
    Two lines containing transformed integer values of x and y.
    Sample Input
    15
    10
    Sample Output
    16
    11
"""


# Next Class: time, timeit, datetime modules
"""
m = int(input())
if m == 1: print("January")
elif m == 2: print("February")
else: print("December")
"""