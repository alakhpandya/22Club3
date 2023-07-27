import csv
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

def getObjectsFromCSV():
        with open('staff.csv', 'r') as f:
            data = list(csv.reader(f))

        data_dict = []
        for row in data:
            temp = {}
            for pair in row:
                key, value = pair.split(':')
                temp[key] = value
            data_dict.append(temp)
        # print(data_dict)
        for emp_dict in data_dict:
            role = emp_dict['_Employees__id'][-4]
            if role == "S":
                SalesExecutive(emp_dict['name'], int(emp_dict['age']), emp_dict['gender'], emp_dict['area'])
            elif role == "A":
                Accountant(emp_dict['name'], int(emp_dict['age']), emp_dict['gender'])
            elif role == "M":
                Manager(emp_dict['name'], int(emp_dict['age']), emp_dict['gender'], emp_dict['qualification'])
            elif role == 'P':
                Peon(emp_dict['name'], int(emp_dict['age']), emp_dict['gender'])
            elif role == 'G':
                GeneralManager(emp_dict['name'], int(emp_dict['age']), emp_dict['gender'], emp_dict['qualification'])
            else:
                print("Please update the program to avail this feature.")

def putObjectsToCSV():
    data = []
    for employee in Employees.all_employees:
        new_employee = []
        for key, value in employee.__dict__.items():
            new_employee.append(f"{key}:{value}")
        data.append(",".join(new_employee) + "\n")
    with open('staff.csv', 'w') as f:
        f.writelines(data)

printTitle()
getObjectsFromCSV()
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
        choice = Employees.selectEmployee()
        Employees.all_employees[choice].printDetails()

    elif op == 4:
        choice = Employees.selectEmployee()
        Employees.all_employees[choice].editDetails()

    elif op == 5:
        choice = Employees.selectEmployee()
        Employees.all_employees[choice].removeEmployees()

    elif op == 9:
        break
putObjectsToCSV()