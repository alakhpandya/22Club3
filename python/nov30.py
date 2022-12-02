# s1 = "9876543210"
# s2 = "5⁴"
# s3 = "②⓪②②"
# s4 = "½"
# s5 = "二千二十二"

"""
The difference between isnumeric, isdigit & isdecimal
"""
"""
print(s4.isdecimal())   # only recognizes digits from 0 to 9 and nothing else.
print(s4.isdigit())     # also recognizes subscript, superscript, circled numbers
print(s4.isnumeric())   # also recognizes roman numerals, vulgar fractions, digits from other languages

print(s5.isnumeric())
"""

s6 = 'students of this batch are going to rock the indian software industry!\nBecause they are very sincere.\nThey also do their homework on time.'
# print(s6.split())
# print(s6.split("s"))
# print(s6.split("in"))
# print(s6.split(" ", 3))

# csv: comma separated values
# s7 = "Harsh,Vadhvana,987654321,harsh_v@gmail.com"
# contact = s7.split(",")
# print(contact)

# print(conatact[2])

# print(s6.rsplit(" ", 3))
# print(s6.rsplit(" "))

# print(s6)
# s6.split("\n")
# s6.splitlines()

# s7 = "Harsh is a good boy. 
# But, this sentence has an error."

# s8 = "||"
# s9 = s8.join(contact)
# print(s9)

# print(" ".join(contact))

s6 = 'students of this batch are going to rock the indian software industry!'
# print(s6.partition("rock"))
# print(s6.partition("are"))
# print(s6.rpartition("are"))

"""
s7 = "                                       Happy Birthday!                  "
print(s7)
print(s7.lstrip())
print(s7.rstrip())
print(s7.strip())
print(len(s7.strip()))

s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
print(s8.lstrip("$"))
print(s8.rstrip("$"))
print(s8.strip("$"))
"""

# print(s6.replace("indian", "Indian"))
# print(s6.removeprefix("students"))
# print(s6.removesuffix("try!"))
print("Please enter your date of birth (dd/mm/2000):")
date = input("Date:")
month = input("Month:")

print(f"Your date of birth is: {date.zfill(2)}/{month.zfill(2)}/2000")