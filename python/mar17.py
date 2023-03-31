"""
Functions Examples:
1. Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.
2. Write a Python function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.


3. Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in ex-1 to find factorial of each one of them and using average function prints the average of factorials of them.

4. Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d

5. Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

6. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

7. Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.

8. Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

9. Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of her/his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

# p = """
# Comments
# """
# a = 5
# b = 5.5
# c = "myString"
# print(p)

# Comments
# myString = """I don't care what "others" say about me."""
# yourString = 'Dharmangi is a good girl.\nShe studies Diploma.'
# print(myString)
# print(yourString)

# ourString = '''He registered in all of the competitions he featured in: 312 in LaLiga, 105 in the Champions League, 22 in the Copa del Rey, six in the Club World Cup, four in the Spanish Super Cup and two in the UEFA Super Cup.

# Nobody throughout the club's history has scored as many goals as the Portuguese attacker, who boasts an impressive trophy haul as a Real Madrid player: four Champions League crowns, three Club World Cups and UEFA Super Cups apiece, two LaLiga titles, a pair of Copas del Rey and two Spanish Super Cups.'''
# print(ourString)


# Docstrings
'''
def average(a,b,c,d,e):
    # f = 5
    """This function returns average of 5 floating point numbers"""
    return (a+b+c+d+e)/5


import random

print(random.uniform.__doc__)
# random.random()
print(average.__doc__)
'''

# We put () after a function if & only if we want to call it.
"""
def myFunc():
    '''Docstring'''
    return "Hello World!"

# "hello".capitalize()
# print(myFunc.__doc__)

# deleting a function
# del myFunc
# myFunc()
yourFunc = myFunc
del myFunc
print(yourFunc())
"""

# Positional, Default
"""
def func1(a, b, c = 6):
    return a**2 + b**2 + c**2

print(func1(3, 5, 4))
"""
# Variable length arguments
"""
def avg(*args):
    print(sum(args)/len(args))

avg(10, 20, 30, 40, 55)
"""

# Passing collections to a function
def func2(m, n):
    print(m + n)

myList = [1,2,34,5,6,7]
yourList = [9,8,7,6,5,4]
func2(myList, yourList)
func2(5,7)
func2("5","7")

# Upcoming topics: key-word arguments, lambda functions, nesting of functions, passing functions as argument, scope of a variable- local variables, global variables & global keyword, Positional, Recursive functions