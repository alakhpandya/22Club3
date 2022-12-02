s1 = 'students of this batch are going to rock the INDIAN software industry!'
"""
print(s1.find("D"))
print(s1.find("e"))
print(s1.find("rock"))

a = s1.find("e")
print(s1.find("e", a+1))

print(s1.find("e", 5))
print(s1.find("e", 5, 30))

print(s1.find("e", 5, -5))
print(s1.find("Python"))

print()

print(s1.index("D"))
print(s1.index("e"))
print(s1.index("rock"))

a = s1.index("e")
print(s1.index("e", a+1))

print(s1.index("e", 5))
print(s1.index("e", 5, 30))

print(s1.index("e", 5, -5))
print(s1.index("Python"))


print(s1.rfind("e"))
print(s1.rfind("are", 20, -3))
print(s1.rindex("D"))
print(s1.rindex("r", 20, -20))
"""

# methods starting from is: All these methods return True or False

# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())

s2 = "AlakhPandya"
s3 = "9876543210"
s4 = "AlakhPandya9876543210"
# print(s2.isnumeric())
# print(s3.isnumeric())
# print(s2.isalpha())
# print(s4.isalpha())
# print(s4.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())

# s3.isnumeric()
# s3.isdecimal()
# s3.isdigit()

# s1.isascii()
s5 = "₹5000"
s6 = "forwhileisinelseifelif"
# print(s6.isidentifier())

# print(s1.isprintable())

s7 = "       \t\t\n            \n            "
# print(s7.isspace())
print(s7.isprintable())

# Next class: Methods starting from 'j'