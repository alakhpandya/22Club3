# Implicit Memoization
from functools import lru_cache

@lru_cache(maxsize=3)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n-1) +fibo(n-2)

n=int(input("How many term you want"))
print("sr.no\tterm ")
for i in range(1,n+1):
    print(f"{i}\t{fibo(i)}")

# Decorators = wrapper function

"""
1. Write a function to calculate area and perimeter of a rectangle. Write a main program that takes length & bredth of 3 rectangular fields of a farmer and prints how many meters of fence for each field she will need to protect the farms from the stray animals. Also print area of each farm.

2. The government wants to develope lake-fronts of five lakes in the city. The government also needs to clean the weeds that have grown on the surface of the lakes. Help them estimate the cost of developement by writing a function that returns the circumference & area of a circle whose radius is given in its argument. Write a main program that takes the radii of five lakes from the user, uses the function and prints the cost of developing lake-front & cleaning the weeds for each lake. The cost of development is ₹ 23000/- per meter & cost for cleaning the weeds is ₹ 5000/- per square meter.
"""

def func():
    a = 5
    b = 10

    return (a, b)

p, q = func()