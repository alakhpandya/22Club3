def fibo(n):
    if n==1 or n==2:
        return 1
    else :
        return fibo(n-1) +fibo(n-2)

n=int(input("How many term you want"))
print("sr.no\tterm ")
for i in range(1,n+1):
    print(f"{i}\t{fibo(i)}")

# HW: To be submitted to: dishantshah1417@gmail.com on or before 4:00pm 14th April, 2023, Friday.
"""
1. Problem Description: Given a name A as input. Print "Hello A", where A is the name in input.

    Problem Constraints:
    1 <= len(A) <= 15
    Characters in A are in lowercase English Alphabets.

    Input Format:
    There is a single input line, which is the string A.

    Output Format:
    Print in a single line "Hello A" without quotes.

    Examples 
    Input 1:
    Ram
    Output 1:
    Hello Ram

    Input 2:
    Shyam
    Output 2:
    Hello Shyam

2. Problem Description: Print the first five letters of the English alphabet i.e. A, B, C, D and E.

    Output Format
    Print the characters in separate lines.

    Example Output
    A
    B
    C
    D
    E

3. Problem Description: Given two numbers A and B. Concatenate the two numbers and print it.

    Problem Constraints
    1 <= A, B <= 104

    Input Format:
    There are two input lines
    The first line has a single integer A.
    The second line has a single integer B.

    Output Format
    Print in a single line the concatenated number.

    Examples 
    Input 1:
    4
    5
    Output 1:-
    45

    Input 2:
    16
    2
    Output 2:-
    162

4. Problem Description: Given two names A and B as input, print "A says Hi to B", where A and B are the names in input.

    Problem Constraints
    1 <= len(A), len(B) <= 15
    Characters in A and B are in lowercase English Alphabets.

    Input Format:
    There are two input lines
    The first line has a string A.
    The second line has a string B.

    Output Format:
    Print in a single line A says Hi to B.

    Examples 
    Input:
    Ram
    Shyam

    Output:
    Ram says Hi to Shyam

5. What will be the output of the following snippet of python code?

    print(type(1)) 
    print(type(str(True) + '1')) 
    print(type(float(int(0.1)))) 
    print(type(True)) 
    print(type(Float(1))) 

    a.
    int
    str
    float
    bool
    Error

    b.
    str
    str
    float
    int
    float

    c.
    int
    int
    float
    int
    float

    d.
    The code will produce an error and nothing will be printed.
"""