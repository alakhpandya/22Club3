# Unpacking of collections/Multiple Assignment
"""
# a = 10
# b = 20
a, b = 10, 20
print("a =", a)
print("b =", b)

# p, q, r = 5, 15, 25
# temp = b
# b = a
# a = temp

a, b = b, a
print("a =", a)
print("b =", b)
"""

# student_data = ("Aniket", 19, "Male")
# Method-1
"""
name = student_data[0]
age = student_data[1]
gender = student_data[2]
"""
# method-2
"""
name, age, gender = student_data[0], student_data[1], student_data[2]
"""
# method-3
"""
name, age, gender = student_data
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
"""
# student_data = ("Aniket", "24", "Male", "Germany", "M.Tech", "Data Scientist", "Swimming")
"""
name, age, gender, *other_details = student_data
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Other Details:", other_details)
"""
# modifying a tuple
"""
student_data[0] = "Neha"
student_data = ("Neha", 24, "Male", "Germany", "M.Tech", "Data Scientist", "Swimming")
student_data = list(student_data)
student_data = list(student_data)
student_data.sort()
student_data = tuple(student_data)
"""

student_data = ("Aniket", "24", "Male", "Germany", "M.Tech", "Data Scientist", "Swimming")
# *other_details, education, profession, hobby = student_data
# print(student_data)

# HW:
# Name, Education, other_details1, other_details