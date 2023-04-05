# def armstrong(a):   # 153
#     return True if sum([int(digit)**len(str(a)) for digit in str(a)]) == a else False

"""
armstrong = lambda a : True if sum([int(digit)**len(str(a)) for digit in str(a)]) == a else False
    
x = int(input("Lower limit: "))
y = int(input("Upper limit: "))
print(f"Armstrong numbers between {x} & {y} are:")
for i in range(x, y+1):
    if armstrong(i): 
        print(i)
"""
# some imp built-in functions: map, filter, reduce
"""
def sqrt(n):
    return n ** 0.5
myList = [16,25,36,49,81]

# sqrtList = []
# for num in myList:
#     sqrtList.append(sqrt(num))
sqrtList = list(map(sqrt, myList))

print(sqrtList)
# o/p: [4.0, 5.0, 6.0, 7.0, 9.0]
"""
"""
def fact(n):

yourList = [2,3,4,5,6,7,8]

# Write your code using that factorial function & map here

print(factList)
# o/p: [2, 6, 24, 120, 720, 5040, 40320]
"""


# filter function

# Write a function here, that returns True or False based on whether the number given in its argument is Prime or not.

# num_list = [x for x in range(55, 155)]
num_list = []
for x in range(55, 155):
    num_list.append(x)

# Write additional code here that uses that function

print(primeList)
# output list must have only prime numbers from 55 to 154


