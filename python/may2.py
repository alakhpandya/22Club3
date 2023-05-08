"""
import math

print(dir(math))

print(math.pi)
print(math.floor(-3.4))
# math.sin()
print(math.e)

import cmath
"""

# Creating infinite in Python
"""
a = float("inf")
b = float(input())
print(b < a)
print(a)
"""

# time module
# import time

# print(dir(time))
# print(time.time())

# Epoch: 1st January, 1970, 00:00:00
"""
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n-1) +fibo(n-2)

n=int(input("How many term you want"))
print("sr.no\tterm ")
t1 = time.time()
for i in range(1,n+1):
    fibo(i)
t2 = time.time()
print(f"Execution time = {t2 - t1}")
"""
"""
import timeit

tl = timeit.timeit(stmt="l=[1,2,3,4,5,6,7,8,9,10]", number=1000000)
tt = timeit.timeit(stmt="l=(1,2,3,4,5,6,7,8,9,10)", number=1000000)
print("difference =", tl - tt)
"""
# Class work:
"""
1. Calculate floor of A / 200 where A is to be taken from user without using math.floor()
"""

# HW:
# Please check in exercise folder for new homework (Assignment 6)