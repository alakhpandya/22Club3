# Datatypes in Python:
"""
Numeric: int, float, complex
a = 7 + 3i, b = 5 + 7i
(7 + 3i)(5 + 7i)


a = 7 + 3j 
b = 5 + 7j
print(a * b)


collections:
string: Ordered & Immutable Collection Of Characters
"""
s1 = 		'students of this batch are going to rock the INDIAN software industry!'
# index: 	 0123456789..................
# -ve index:	 ......................................................987654321
print(s1)
print(type(s1))
print(len(s1))
print(s1[5])

# slicing
s2 = s1[9 : 59]
print(s1)	# Slicing will always return new data
print(s2)

# print(s1[600])
# print(s1[12 : 600])
# print(s1[12 : ])
# print(s1[ : 60])
# print(s1[ : ])

# print(s1[60])
# print(s1[-3])
"""
print(s1[0])

print(s1[30 : 3])
print("The end")
print(s1[-25 : -5])
print(s1[-30 : 50])
print(s1[30 : -3])

print(s1[4 : -3])


print(s1[3 : 55 : 3])
print(s1[55 : 3 : -1])
print(s1[ : : -1])
print(s1[ : : -3])
"""

# methods vs. functions
# function_name(oprand)
# oprand.method_name(arguments)

# Case related methods:
s2 = s1.capitalize()
print(s1)	# strings are immutable so, methods of strings cannot change the original string. Instead, they will return a new string.
print(s2)
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())