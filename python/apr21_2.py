"""
Class Work:
Ask t (no of inputs) from the user. 
Next, ask t no of inputs from user and print their multiplicative tables from 1 to 10.

Constraints
1 <= t <= 1000

Example Input-1:
3
2
4
5

Example Output-1:
2 4 6 8 10 12 14 16 18 20
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50

Example input-2:
2
6
3

Example output-2:
6 12 18 24 30 36 42 48 54 60
3 6 9 12 15 18 21 24 27 30
"""
"""
t = int(input())        # 5
inputs = []
for i in range(t):
    inputs.append(int(input()))

for n in inputs:
    for j in range(1, 10):
        print(n * j, end = " ")
    print(n * 10)
"""
# hcf = highest common factor
"""
hcf(16, 24) = 8
factors of 16: 1, 2, 4, 8, 16
factors of 24: 1, 2, 3, 4, 6, 8, 12, 24

Ask an integer from user and print "Yes" if it is divisible by both 3 & 5. Otherwise print "No".
"""
# Homework:
"""
1. Numerical Derivative
Problem Description:
The derivative of a function is a value that tells us how much the output of a mathematical function would change, if we were to make a very, very tiny change in its input. In mathmetical terms, the limit definition of a derivative is defined as: lim Where x and h are both inputs to the function f. You can safely ignore the lim part in the expression.
Given the values of x and your task is to evaluate the expression for the function f(x) = 3x² + 2 and print the value obtained.

Input Format:
The input will contain two numbers.
The first line will be the x value.
The second line will be the h value.

Output Format:
The output would be a single line float value of the expression in problem description.
 
Input:
1
1
Output:
9.0

Note: The value of hwill always be more than for this problem.

2.Is the third one greater?
Problem Description:
Given three integer values as input, your task is to print True if the third number is greater than the first two else False.

Input Format:
Input will contain three lines denoting three integer values.

Output Format:
The output would be True if the condition holds else False.

Input:
1
2
3
Output:
True

Explanation:
Here 3 is greater than 1 and 3 is also greater than 2 and hence the output is True.

3.	Floors and Ceilings
Problem Description:
The floor function floor(x) is defined as the greatest integer less than or equal to the given number.
For example, floor(7.64)=7.
Likewise, the ceiling function ceil(x) is defined as the smallest integer greater than or equal to the given number.
For example, ceil(7.64)=8.
Given a number x as input, output its floor(x) and ceil(x) values.

Note: Assume that the input will never be an integer.

Input Format:
One line float value

Output Format:
Print two integers, first one denoting the floor value and second one the ceiling value of the given number.
 
Input:
7.64
Output:
7
8

Example Explanation:
The greatest integer that is less than or equal to 7.64 is clearly 7.
The smallest integer that is greater than or equal to 7.64 is clearly 8.

4. Multiply Chain
Problem Description:
Given a number n as input, multiply it with the number (n-1) and (n-2) and print the resultant output.

Input Format:
A single line containing an integer.

Output Format:
A single line output according to the problem description.

Input:
10
Output:
720

5.Module Trouble
Problem Description:
Shikha is trying to solve a hard math problem in which she is required to take the mod of a number x with y quite frequently. Given two numbers x and y write a program that helps Shikha do this easily. Assume that the value of y is always greater than 0.

Input Format:
Two lined inputs. The first line denotes the x value and the second one the y value.

Output Format:
Single number which is the mod of x with y.

Input:
100
11
Output:
1

6.Four average
Problem Description:
Given four numbers as input print their average value as output.

Input Format:
Four lines denoting four numbers.

Output Format:
Single number denoting the average value.

Input:
1
2
3
4
Output:
2.5

7.Odd/Even - without statements
Problem Description
Given an integer n as input, print True if it is odd and False if it is even. Solve this question with the concepts taught in the Lecture on Operators. DO NOT USE IF/ELSE.

Input Format:
A single line input containing the integer.

Output Format:
A single-line boolean value.

Input:
2
Output:
False

Example Explanation
The output is False because 2 is even.

8.Are the weights balanced?
Problem Description:
A weighing machine has two arms, a left arm, and a right arm. On both sides of the weighting machine we can put in weights and if both of those weights are equal, the arms of the machine will hang equally in the air, with none of them hanging below the other. This is hard to observe visually hence you are asked to write a program that takes in two weight values as input and outputs True if they will leave the machine balanced and False if they will leave the machine unbalanced.

Input Format:
The input will contain two lines denoting the weight values on the left and right arms of the machine

Output Format:
True if the machine is balanced. False if the machine is unbalanced.

Input:
64.0
63.0
Output:
False

9.Raised to the power
What do you think would be the output when we run the piece of code given below?
print(3 ** 2 ** 0)

a.	Error
b.	0
c.	3
d.	1

10.	What would be the output of the following piece of code?
print("abcd" < "abce")

a.	Error
b.	True
c.	False

"""

# Next Lecture- Some useful built in modules
marks = int(input("Marks: "))
print(marks >= 70)