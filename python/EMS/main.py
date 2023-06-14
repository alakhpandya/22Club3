from employees import Employees
from accountant import Accountant
from general_manager import GeneralManager
from manager import Manager
from peon import Peon
from sales_executive import SalesExecutive

def printTitle():
    print("+" + "-"*100 + "+")
    print("|" + "Welcome to Employee Management.".center(100) + "|")
    print("+" + "-"*100 + "+")


printTitle()

while True:
    print("\nPress\n1 to see all details of employees:")
    print("2 to Add new employees:")
    print("3 to See details of particular employees:")
    print("4 to Edit a Employees details:")
    print("5 to Delete detail of a employees:")

    print("9 to exit")
    op=int(input())
    if op == 1:
        Employees.allEmployees()
    elif op == 2:
        print("Press:")
        print("\t1 to add a sales executive")
        print("\t2 to add a manager")
        print("\t3 to add an accountant")
        print("\t4 to add a peon")
        print("\t5 to add a general manager")
        role = int(input())
        options = {
            1 : SalesExecutive.addEmployee,
            2 : Manager.addEmployee,
            3 : Accountant.addEmployee,
            4 : Peon.addEmployee,
            5 : GeneralManager.addEmployee
        }
        options[role]()

    elif op == 3:
        Employees.allEmployees()
        choice = int(input("Enter sr no of the car you want view details of: "))
        Employees.all_employees[choice].printDetails()

    elif op == 4:
        Employees.allEmployees()
        choice = int(input("Enter sr no of the car you want view details of: "))
        Employees.all_employees[choice].editDetails()

    elif op == 5:
        pass
    elif op == 9:
        break
