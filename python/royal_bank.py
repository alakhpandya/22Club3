# import section
import sys
# import csv

# Global variables & constants


# All the functions
def getData():
    f = open('royal_bank_database.csv', 'r')
    data = f.read().splitlines()
    f.close()
    # Removing the title
    data.pop(0) 
    return data

def putData(userName, password, balance):
    f = open('royal_bank_database.csv', 'a')
    f.write(f'\n{userName},{password},{balance}')
    f.close()

def searchData(term, value):
    try:
        assert term.lower() in ['username', 'password']
    except AssertionError:
        print("Term must be either 'username' or 'password', please try again...")
    ind = 0 if term.lower() == 'username' else 1
    data = getData()
    for line in data:
        userData = line.split(',')
        if value == userData[ind]:
            return userData
    return False

def createAccount():
    # Getting all the existing data from the file
    data = getData()
    
    # Taking username:
    while True:
        userName = input("Create your username: ")
        if searchData('username', userName):
            quit = input("Sorry, this username is already taken. Type 'x' to exit or any other key to try again: ").lower()
            if quit == 'x':
                return False
        else:
            break
    password = input("Set your password: ")

    # Taking opening balance
    while True:
        opening_balance = input("Opening Balance: ")
        if int(opening_balance) >= 25000:
            break
        quit = input("Opening balance must be atleast 25000. Type 'x' to exit or any other key to continue: ").lower()
        if quit == 'x':
            return False
        
    # Writing new username, password & opening balance into the file
    putData(userName, password, opening_balance)
    
    return True

def login(userName, password):
    userData = searchData("username", userName)
    if userData:
        if password == userData[1]:
            return True
    return False

def mainMenu():
    while True:
        print("Press:")
        print("1 to create account")
        print("2 to login")
        print("3 to quit")
        choice = int(input())
        if choice == 1:
            if createAccount():
                print("Account created successfully, now you may proceed to login...")
            else:
                print("Account creation failed. Please try again...")

        elif choice == 2:
            print("Enter the following details:")
            attempt = 1
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if login(username, password):
                    return True
                else:
                    print("Invalid username/password. Try again. Attempts left:", 3 - attempt)
                    attempt += 1
                    if attempt > 3:
                        return False
        
        elif choice == 3:
            return False
        
        else:
            print("This feature is not available right now. Please try again...")

# Main program
if not mainMenu():
    sys.exit()

while True:
    print("Enter your choice:")
    print("1. Deposit \n2. Withdraw \n3. Check Balance \n4. Log out")
    choice=int(input(""))
    if choice==1:
        balance=deposit(balance)
        # pass
    elif choice==2:
        print("︎Withdraw︎")
        print(f"Your account have {balance}Rs.")
        wd_amt=int(input("Enter withdraw amount"))
        balance-=wd_amt
        print(f"Now your Current Balance is {balance}")
        # pass
    elif choice==3:
        print(f"Your account have {balance}Rs.")              
        # pass
    elif choice==4:
        # Log out
        print("Logging out")
        break