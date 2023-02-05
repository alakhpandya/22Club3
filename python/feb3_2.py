# functions

# a = 5
# b = 10

def sayHello():
    print("Hello!")

sayHello()

def printAverage(x, y):
    avg = (x + y)/2
    # print(f"Average of {x} & {y} is: {avg}")
    return avg

printAverage(10, 20)

a = float(input("a : "))
b = float(input("b : "))
avg = printAverage(a, b)
ans = avg + 10
print(ans)
"""
20 lines
Armstrong
10 lines
Armstrong
25 lines
Armstrong
"""