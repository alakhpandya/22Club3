# loop examples:
"""
1. Write a Python code that takes an integer from user and prints number of digits in that integer.
2. Write down a Python code that creates a user defined list
3. Write a Python code to print each of the elements of a given list in a new line
4. Write a Python program that prints whether the number given is a prime number or not.
5. Write a Python program that prints whether the number given is a perfect number or not.
6. Write a Python program that prints whether the number given is an Armstrong number or not.
7. Write a Python program that prints all the prime numbers between two integers given by user.
8. Write a Python program that prints all the perfect numbers between two integers given by user.
9. Write a Python program that prints all the Armstrong numbers between two integers given by user.
"""
"""
n = int(input("Enter n: "))
print(len(str(n)), "digits")
"""
"""
myList = []
n = int(input("Number of elements: "))  # 5
print(f"Enter {n} elements:")
i = 1
while i <= n:
    a = input(f"Number-{i}: ")
    myList.append(a)
    i += 1
print(myList)
"""
# cities = ["Ahmedabad", "Himmatnagar", "Dehgam", "Jamnagar", "Vadodara", "Bharuch"]
"""
n = int(input("Enter any number: "))    # 1003
i = 2
flag = 1
while i < n:
    if n % i == 0:
        print("Not Prime.")
        flag = 0
        break
    i += 1
if flag == 1:
    print("Prime.")
"""

# if - else
# while - else: break - else
"""
n = int(input("Enter any number: "))    # 97
i = 2
while i < n:
    if n % i == 0:
        print("Not Prime.")
        break
    i += 1
else:
    print("Prime.")
"""

# perfect no program:
"""
n = int(input("Enter any number: "))    # 6
i = 1
factor_sum = 0
while i < n:
    if n % i == 0:
        factor_sum = factor_sum + i
    i += 1
if factor_sum == n:
    print("Perfect.")
else:
    print("Not Perfect.")
"""

# Armstrong no program: 371: (3)^3 + (7)^3 + (1)^3: 27 + 343 + 1 = 371

n = int(input("Enter any number: "))    # 371
power = len(str(n))
temp = n
sum = 0
while temp > 0:
    last_digit = temp % 10
    sum = sum + last_digit ** power
    temp = temp // 10
if sum == n:
    print("Armstrong.")
else:
    print("Not Armstrong.")

# Next: Another approch to solve the above program