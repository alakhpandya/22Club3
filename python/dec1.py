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

# list: Ordered & Mutable collection of members
numbers = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 100]
# index     0  1    2     3   4
#          -9 -8    -7
"""
print(len(numbers))
print(numbers)
print(type(numbers))
characters = list('Krushnam')
print(characters)

print(min(numbers))
print(max(numbers))
sorted_numbers = sorted(numbers)    # sorted() will always give you a NEW LIST
print(numbers)
print(sorted_numbers)

print(sorted(numbers, reverse=True))

vegetables = ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
print(vegetables)
print(min(vegetables))
print(max(vegetables))

mix_veg = ["carrot", 3, "tomato", 1.5, "spinach", -0.5]
print(mix_veg)
# print(min(mix_veg))
"""
# Ordered means
"""
+ve & -ve Index numbers of each element
Accessing through +ve or -ve index
slicing is exactly the same as it was in strings

print(numbers[3])
print(mix_veg[3])
print(numbers[2 : -2 : 2])
"""

# Mutable
# numbers[3] = 119.8
# print(numbers)

# list methods
# numbers.append(2000)

# numbers.append(3000)
# numbers.append(3000)
# numbers.append(3000)
# numbers.append(3000, 4000, 5000)


# numbers.clear()
# del numbers

# del numbers[3]
# print(numbers)

print(numbers.count(33))
# print(numbers.count(33, 2, 7))