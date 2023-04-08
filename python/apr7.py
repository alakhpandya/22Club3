# passing functions as argument
"""
Ask 5 integers from user & print average of their factorials.

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def avg(a, b, c, d, e):
    return (a + b + c + d + e)/5

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(avg(fact(a), fact(b), fact(c), fact(d), fact(e)))
"""
# Nesting of functions
"""
def avg(a, b, c, d, e):
    def fact(n):
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
    return (fact(a) + fact(b) + fact(c) + fact(d) + fact(e))/5

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(avg(a, b, c, d, e))
"""

# scope of a variable- local variables, global variables & global keyword
"""
var1 = 10           # global variable

def func1():
    # var1 = 15
    global var1
    var1 += 1
    print("var1 through func1:", var1)
    # var2 += 1
    print("var2 through func1:", var2)
    # print("var3 through func1:", var3)
    var4 = 40                               # local variable of func1
    print("var4 through func1:", var4)
    def func2():            # local scope
        print("var4 through func2:", var4)

    func2()
    return var4

def func3():
    # print("var4 through func3:", var4)
    pass

var2 = 20           # global variable for all the functions CALLED after this point.
var1 += 1
var4 = func1()
# var3 = 30
# print("var4 through main:", var4)
# func2()
print("var1 through main:", var1)
"""

# Recursive functions: a function calling itself is called recursive function

"""
# 5! = 5 x 4 x 3 x 2 x 1

5! = 5 x 4! = 120
4! = 4 x 3! = 24
3! = 3 x 2! = 6
2! = 2 x 1! = 2
1! = 1 x 0! = 1
0! = 1

Recursive Definition of Factorial:
n! = n x (n-1)!     # Recursive Step
0! = 1              # Non-Recursive/Basis Step
"""
"""
def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1)

print(recursive_fact(5))
"""
# Write a recursive function to compute nth term of an Arithmetic Progression with 'a' as its first term & 'd' as common difference.