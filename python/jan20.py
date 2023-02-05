"""
# We can not create mutable collections in unordered collections.
"""
"""
s1 = {
    frozenset({1,2,3}),
    (4,5,6)
}
print(s1)
"""
# Nesting of lists:
# 3 x 3 matrix:
"""
m1 = [
    [1,2,3],
    [-5,-6,2],
    [0,8,-9]
]

print(m1[0][2])
m1[2][1] = -18
print(m1)
"""
# Write a program that asks 9 numbers from user & create a 3x3 matrix using them.
"""
m = []
for y in range(3):
    row = []
    print(f"Enter 3 numbers for row-{y+1}:")
    for x in range(3):
        temp = float(input())
        row.append(temp)
    m.append(row)
print(m)
"""


# Dictionaries: Unordered & Mutable collections of key-value pairs
# result = {"Maths":88, "Science":92, "Computers":98}

result = {
    "Maths":88,
    "Science":92,
    "Computers":98
}
print(result)

# Dictionaries are unordered so, can't access by index numbers:
# result[0]

# Values can be accessed by keys:
print(result["Computers"])

# Changing value of an existing key:
result["Maths"] = 90
print(result)

# Adding a new key:value pair:
result["Python"] = 100
print(result)

# Rules for values:
celebration = {
    "Tithi" : "Paneer Tikka",
    "Dhiraj" : ("Bajri Rotlo", "Bengan Bharta", "Chhash"),
    "Khush" : ["Manchurian", "Pasta", "Thumbsup"],
    "Alakh" : {"Manchurian", "Pasta", "Thumbsup"},
    "Krushnam" : 23,
    "Kamal mam" : frozenset({"Khichdi", "Kadhi"}),
    "Dharmangi" : {
        "BF" : "Buffet",
        "Lunch" : "Punjabi",
        "Dinner" : "Italian"
    }
}

print(celebration)

# Write a program that takes name of the person from the user & print their food order. If the person name is Dhiraj, Khush, Kamal mam or Alakh then it should print each food item on seperate line. If person name is Dharmangi then the program should ask user which meal do they want to see. If user enters "BF" then it should print "Buffet", for "Lunch" it should print "Punjabi" and "Italian" for "Dinner".

# Rules for keys: