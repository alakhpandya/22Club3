# Upcoming topics: nesting of functions, passing functions as argument, scope of a variable- local variables, global variables & global keyword, Positional, Recursive functions


# key-word arguments
"""
def avg(**kwargs):
    print(kwargs)

# avg(109,120,130)
# avg(physics = 24, maths = 25, english = 26)


def percentage(marks):
    total_marks = sum(marks.values())
    percent = total_marks / len(marks)
    return percent

result = {"C" : 98, "C++" : 100, "html" : 99}
print(percentage(result))


def func1(a, c, b = 3, d = 4, *abc, **abcd):
    pass

def func2(*args, a):
    pass

func2(1,2,3,4)
"""

# lambda functions


# def sqrt(n):
#     return n ** 0.5
"""
sqrt = lambda n : n ** 0.5
print(sqrt(25))

average = lambda a, b : print((a + b)/2)
x = average(10, 50)
print(x)

func1 = lambda : print("Hello World!")
func1()
"""
# Write a function to scan a 3x3 matrix from user and return it to the main program. Print the array in the main program
