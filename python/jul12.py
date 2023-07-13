# f = open('temp.txt', 'r')
# data = f.read()
# print(type(data))

# data = f.read(20)
# print(data)

# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

# print(f.readable())
# print(f.writable())

# f.close()

"""
path = input("Enter file name to open with path: ")
mode = input("Mode: ")
f = open(path, mode)

list_of_lines = f.readlines()
print(list_of_lines)

f.close()
"""

"""
f = open('temp2.txt', 'r+')

f.read()
data = input("Enter the text: ")
f.write(data)

f.close()
"""

"""
f = open('temp2.txt', 'w')

data = ['MD Sir\n', 'Dishant\n', 'Rahul\n', 'Kamal mam\n', 'DL Sir\n']
f.writelines(data)

f.close()
"""

# Create a banking app with 4 functionalities: deposit, withdraw, check balance, create a new account. 
"""
Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of her/his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()

Store all the information of every user (user name, password and balance) in a text file.
"""

# Exception Handling / Error Handling

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        z = x / y
        break
    # except ValueError:
    #     print("Please enter integers only... Try again!")
    # except ZeroDivisionError:
    #     print("'y' must be non-zero.")
    # except:
    # except Exception:
        # print("Oops, something went wrong, please try again...")
    except Exception as e:
        print(e)

while True:
    op = input("Operation (+, -, *, / or 'x' to quit): ")
    if op == '+':
        print(f"{x} + {y} = {x + y}")
    elif op == '-':
        print(f"{x} - {y} = {x - y}")
    elif op == '*':
        print(f"{x} * {y} = {x * y}")
    elif op == '/':
        try:
            print(f"{x} / {y} = {x / y}")
        except ZeroDivisionError:
            print("Cannot divide by zero! Please try again...")
    elif op == 'x':
        break
    else:
        print("Invalid operation. Please try again")


# i = 1
# while i <= 5:
#     print(i)

# x = int(input("x: "))
# y = 0
# print(x / y)

# Next Class: Resource Management, csv module