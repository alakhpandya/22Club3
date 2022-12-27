# widest use of while loop: to create infinite loops
"""
# x = 0
# while x < 13.7596:
while True:
    n = int(input("Enter any number: "))    # 371
    str_of_n = str(n)
    no_of_digits = len(str_of_n)
    digits = []
    i = 0
    while i < no_of_digits:
        digits.append(int(str_of_n[i]) ** no_of_digits)
        i += 1
    # print(digits)
    # print(sum(digits))
    print("Armstrong.") if sum(digits) == n else print("Not Armstrong.")

    quit = input("Press 'x' to exit or 'r' to repeat: ")
    if quit == 'x':
        break
"""
"""
fruits = ["apple", "mango", "kiwi", "banana", "strawberry", "orange"]
i = 0
while i < len(fruits):      # i = 0,1,2,3,4,5,6
    print(fruits[i])
    # if fruits[i] == "banana":
    #     pass
    i += 1
"""


# for loop:
fruits = ["apple", "mango", "kiwi", "banana", "strawberry", "orange"]
for i in fruits:        # i = "apple", "mango", "kiwi", "banana", "strawberry", "orange"
    if i == "banana":
        # break
        pass
        # continue
    print(i)
print("The end")

# how we write for loop in real life (replacing 'i'), for loop in range, for-else