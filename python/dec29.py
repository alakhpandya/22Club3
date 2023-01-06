# list comprehension

# numbers = []
# for x in range(1, 101):
#     numbers.append(x)

# numbers = [x for x in range(1, 101)]

# for-else: break-else
"""
n = int(input("Enter any integer: "))   # 44
for x in range(2, n):
    if n % x == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""

# Collections in Python
"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset

Two special collections:
strings: Ordered & Immutable collections of characters              " "/ ' '
dictionaries: Unordered & Mutable collections of key-value pairs
"""
# tuple: Ordered & Immutable collection of members
# t1 = (12, 13, 45, -32.7, 13, 9.9, 0, 13, 24.6, 13)
# print(t1)
# print(type(t1))
# Ordered means:
"""
+ve & -ve index numbers
Access members through index nos
slicing with +ve & -ve index and with +ve/-ve step
"""
# print(t1[3])
# print(t1[-3])
# print(t1[2 : 8])        # slicing never changes the original data
# print(t1[1 : -3])
# print(t1[1 : -1 : 2])
# print(t1[10 : 1 : -2])

# Another way to create a tuple:
"""
t2 = 43, -606, 98.5, 0, 39.9, "Bootcamp", "Laptop"
print(t2)
print(type(t2))
# t2[2] = 1000      Not allowed

t3 = 43, -606
print(t3)
print(type(t3))
"""

# Creating single element tuple:
"""
t4 = (273,)
print(t4)
print(type(t4))

t5 = "Ahmedabad",
print(t5)
print(type(t5))
"""
t1 = (12, 13, 45, -32.7, 13, 9.9, 0, 13, 24.6, 13)
# print(t1.count(13))
# print(t1.count(130))
# t1.count(13, 5, 10)     # invalid

# print(t1.index(9.9))
# print(t1.index(19.9))
# print(t1.index(13))
# print(t1.index(13, 5, 10))



# HW
# Given the list of fruits, ask any fruit name from user & print whether that fruit is in the list or not.

# fruits = ["apple", "mango", "kiwi", "banana", "strawberry", "orange"]
# f = input("Enter any fruit name: ")
# Start writing your code from here 


# Next Class: Unpacking of collections/Multiple Assignment