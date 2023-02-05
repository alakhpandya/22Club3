from sys import getsizeof

result = {
    "Maths":88,
    "Science":92,
    "Computers":98,
    "Physics":65,
    "English":85,
    "Environment":100,
    "Chemistry":45
}

# print(result.get("Physics"))
# print(result["Physics"])
"""
obj = result.keys()

t1 = tuple(result.keys())

l1 = list(result.keys())

print(getsizeof(l1))
print(getsizeof(t1))
print(getsizeof(obj))
"""
# print(result.values())

# print(result.items())


# for loop in dictionaries:
"""
for subject in result.keys():
    print(subject)

for marks in result.values():
    print(marks)

for x, y in result.items():
    print(x)
    print(y)
    print()

for subject, marks in result.items():
    print(f"I got {marks} marks in {subject}.")

for x in result:        # this will give you keys by default
    print(x)
"""

# for loop with multiple variables:
"""
classResult = [
    ("Siddharth", "Computers", 98),
    ("Rupesh", "Maths", 55),
    ("Gautam", "Physics", 99),
    ("Nirav", "Chemistry", 82),
    ("Shweta", "Environment", 100)
]

for student, subject, marks in classResult:
    print(f"{student} got {marks} in {subject}.")
"""

# print(result.pop("Maths"))
# print(result)
"""
print(result.popitem())
print(result)

other_subjects = {
    "Python":100,
    "C":98,
    "javascript":99
}

result.update(other_subjects)
print(result)
"""
# fromkeys (on the basis of homework done or not) & setdefault