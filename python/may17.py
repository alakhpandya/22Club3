'''
import datetime
# strptime: string parse time
# strftime: string format time

# print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

lamya = datetime.datetime(2024, 2, 4)
"Feb 4th, 2024, Thu"
"2024, 4th February, Thursday"
"4th Feb, 2024 (Thursday)"
"""
dob = datetime.datetime.strftime(lamya, f"{lamya.day}th %b, %Y (%A)")
print(f"Lamya's next birthdate is going to be on {dob} but, if she wishes, she can give party immediately after she comes back!")
"""

input_string = "Chandrayaan-2 was launched on 22nd July 2019 from Satish Dhawan Space Center, Sriharikota."
chandrayaan2_date_string = "22nd July 2019, 2:30pm"
chandrayaan2_launch_datetime = datetime.datetime.strptime(chandrayaan2_date_string, "%dnd %B %Y, %I:%M%p")
print(chandrayaan2_launch_datetime)
'''

import random

# print(dir(random))
# print(random.__doc__)
"""
# Ceaser's cypher
"lect cancel" = "ohfw fdqfho"
000000
to
999999

# RSA Encryption: prime numbers: 300 to 600 digits
"""
# for i in range(20):
#     print(random.random())      # generates random fraction in the interval [0, 1)

# How to get random fraction between 6 to 7
# for i in range(20):
#     print(random.random() + 6)

# How to get random fraction between 0 to 10
"""
0.7636588946110 * 10

smallest: 0 * 10 = 0
largest: 0.9999 * 10 = 9.9999
"""
# for i in range(20):
    # print(random.random() * 10)
    # print(random.random() * 15)


# How to get random fraction between 15 to 25
# for i in range(20):
#     print((random.random() * 10) + 15)

# Ask two integers a & b from user and print 20 random fractions in the interval [a, b)
"""
a = int(input("a: "))
b = int(input("b: "))
gap = b - a
for i in range(20):
    print(random.random() * gap + a)
"""

# Simulating rolling of a dice
"""
for i in range(20):
    print(int(random.random() * 6 + 1))
"""

# 
"""
options = ["Rock", "Paper", "Scissors"]
# simulate an opponent (computer) guessing any one of the above three twenty times.
for i in range(20):
    index = int(random.random() * 3)
    print(options[index])
"""

# Sample output:
"""
Rock: ______ times
Paper: ______ times
Scissors: ______ times
"""
options = ["Rock", "Paper", "Scissors"]
for i in range(20):
    # print(random.uniform(13, 30))
    # print(random.randint(1, 6))
    # print(random.randrange(1, 7))
    print(random.choice(options))

# Simulate Rock-Paper-Scissors game:
"""
In every turn ask a choice of user, guess a choice from computer record score of both. Take 20 turns and declare final result.
"""