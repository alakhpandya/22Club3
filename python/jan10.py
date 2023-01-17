# Collections in Python
"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset

Two special collections:
strings: Ordered & Immutable collections of characters              " "/ ' '
dictionaries: Unordered & Mutable collections of key-value pairs    {}
"""

# set: Unordered & Mutable collection of members in which repeatition is eliminated

# s1 = {1,2,3,4}
# print(s1)
# print(type(s1))

# Unordered means:
"""
NO indexing
NO Accessing through index
NO Slicing
"""
# print(s1[2])

# s2 = {15, 7, -17, 15, 0.78, 6, 15, 18, 15.47, 15, 98.2, 0, 15}
"""
print(s2)
print(type(s2))
print(len(s2))

print(min(s2))
print(max(s2))
print(sorted(s2))
print(sorted("python"))
"""
# A: students learning C++ = {Dharmangi, Khush, Krushnam}
# B: students learning Python = {Dharmangi, Khush, Krushnam, Vedangi, Tithi}

s1 = {15, 7, -17, 15, 0.78, 6, 15, 18, 15.47, 15, 98.2, 0, 15}
"""
# empty_set = {}
empty_set = set()
print(len(empty_set))
print(type(empty_set))

# Example of a dictionary:
result = {"Vedangi":95, "Khush":59, "Dharmangi":85}

mix_set  = {"Paneer Butter Masala", 3, "Veg Handi", 3, "Butter Nan", 2, "Cheese Nan", 2, "Plain Roti", 0.5}

# Another way to create any collection:
student_1 = list("Krushnam")
student_2 = tuple("Krushnam")
student_3 = set("Krushnam")
print(student_1)
print(student_2)
print(student_3)

myList = [1,2,3,4,5,6]
mySet = set(myList)
print(mySet)
"""
# set methods:
s1 = {15, 7, -17, 0.78, 6, 18, 15.47, 98.2, 0}

# s1.add(500)
# s1.clear()
# del s1

s2 = s1.copy()
s3 = s1

# print("s1 =", s1)
# print("s2 =", s2)
# print("s3 =", s3)

# s1.discard(15.47)
# s1.discard(15.47)
# print("s1 =", s1)
# s1.remove(98.2)
# s1.remove(98.2)
# print("s1 =", s1)

# print(s1.pop())

s2 = {101, 201, 301, 401, 6}
s1.update(s2)
print("length of s1 =", len(s1))
print("s1 =", s1)
print("s2 =", s2)

