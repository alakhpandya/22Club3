"""
classResult = {'sdfdf': 45, 'dgg': 2, 'jdf': 67, 'tyu': 23, 'nihar': 100}
rList = []
for pair in classResult.items():
    rList.append(pair)
print("Original-", rList)
j = 0
while j < len(rList):
    i = 0
    while i < len(rList)-1:
        if rList[i][1] > rList[i+1][1]:
            rList[i], rList[i+1] = rList[i+1], rList[i]
        i += 1
    j += 1
print("Sorted-", rList)
sortedResult = {}
for key, value in rList:
    sortedResult[key] = value
print(sortedResult)
"""
"""
9. Write a Python program to split a given dictionary of lists into list of dictionaries. Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
"""
result = {
    'Science': [88, 89, 62, 95, 99], 
    'Language': [77, 78, 84, 80, 91],
    'Programming': [98, 88, 78, 68, 95]
}

markssheets = []
n = len(result['Science'])
for i in range(n):
    individualMarksheet = {}
    for key in result:          # key: Science, Language
        marks = result[key][i]              # marks = 88, 77
        individualMarksheet[key] = marks    # iM = {'Science', 88}
    # print(individualMarksheet)
    markssheets.append(individualMarksheet)

print(markssheets)
"""
# Output
"""
markssheets = [
    {'Science': 88, 'Language': 77}, 
    {'Science': 89, 'Language': 78}, 
    {'Science': 62, 'Language': 84}, 
    {'Science': 95, 'Language': 80}
]
"""
# Write a Python function that prints whether the number given by user is prime or not. Also write a main program that asks an integer from user & passes to the function.
"""
def primeCheck(n):
    # n = int(input("n = "))
    for i in range(2, n):
        if n % i == 0:
            # print("Not Prime.")
            return False
            break
    else:
        # print("Prime.")
        return True

a = int(input("Enter two integers:\n"))
b = int(input())
ans = abs(a - b)
if primeCheck(ans) == True:
    print("ans/3 =", ans/3)
else:
    print("ans/2 =", ans/2)
"""
# cutting the above program short

def primeCheck(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


a = int(input("Enter two integers:\n")) # 1
b = int(input())                        # 100
"""
ans = abs(a - b)
if primeCheck(ans):
    print("ans/3 =", ans/3)
else:
    print("ans/2 =", ans/2)
"""
for i in range(a, b+1):
    if primeCheck(i):
        print(i)