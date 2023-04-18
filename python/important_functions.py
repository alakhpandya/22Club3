PI = 3.141596

def avg(a, b):
    return (a + b)/2

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


def perfectNumberChecking(n):
    fact = 0
    for i in range(1, n):
        if n % i == 0:
            fact += i
    return True if fact == n else False