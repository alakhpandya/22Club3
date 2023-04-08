def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def primeCheck(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# num_list = [x for x in range(5, 15)]

# primeList = []
# for n in num_list:
#     if primeCheck(n):
#         primeList.append(n)

# primeList = filter(primeCheck, num_list)
# print(list(primeList))
# for x in primeList:
#     print(x)


# primeList = map(primeCheck, num_list)
# print(list(primeList))

# factList = list(filter(fact, num_list))
# print(factList)

# avg = lambda a, b : (a + b)/2

from functools import reduce

def absoluteSum(a, b):
    # Write a function here that takes two arguments and add them but, before addition it converts both the numbers in positive.
    sum = abs(a) + abs(b)
    return sum

transactions = [1000, -300, -200, 500, -20, 15, -900, 100, -20]
# print(sum(transactions))

# write a program that uses above function and finds total transcted amount.

# amount = 0
# for i in transactions:
#     amount = absoluteSum(amount, i)

amount = reduce(absoluteSum, transactions)

print(amount)