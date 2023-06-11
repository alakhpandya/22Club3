
# Abstraction
"""
Two purposes:
1. We want to restrict object creation in a particular class
2. We want to make some methods compulsory for every child class to have.
"""
class Employees:
    all_employees=[]
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        Employees.all_employees.append(self)
    
    def printDetails(self):
        print(f"---------Details of {self.name}---------")
        print("Employees name:",self.name)
        print("Employees age:",self.age)
        print("Employees gender:",self.gender)
    
    def editDetails(self):
        print("Enter new details (Press 'Enter' to keep the same detail):")
        name = input("Name: ")
        age = input("Age: ")
        gender = input("Gender: ")
        return {"name" : name, "age" : age, "gender" : gender}
    
    def removeEmployees(self):
        Employees.all_employees()
        choice = int(input("Enter sr no of the Employees you want delete: "))
        removedEmp = Employees.allEmployees.pop(choice)
        print(f"Employees {removedEmp.name} has been removed successfully!")
        print()

    @staticmethod
    def allEmployees():
        print("-"*20)
        print("SrNo\tName")
        srNo = 0
        for employee in Employees.all_employees:
            print(f"{srNo}\t{employee.name}")
            srNo +=1
        print("-"*20)
    
    @staticmethod
    def addEmployee():
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return name, age, gender


class SalesExecutive(Employees):
    target = 1000000
    def __init__(self, name, age, gender, area):
        super().__init__(name, age, gender)
        self.area = area

    def printDetails(self):
        super().printDetails()
        print("Target:", self.target)

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        area = input("Area: ")
        return cls(name, age, gender, area)

    def editDetails(self):
        details = super().editDetails()
        area = input("Area: ")
        target = input("Target: ")
        details.update({"area" : area, "target" : target})
        details_mapping = {"name" : self.name, "age" : self.age, "gender" : self.gender, "area" : self.area, "target" : self.target}
        for detail in details:
            if details[detail] != "":
                if detail == "target" or detail == "age":
                    details_mapping[detail] = int(details[detail])
                else:
                    details_mapping[detail] = details[detail]

class Manager(Employees):
    team_size = 10

    def __init__(self, name, age, gender, qualification):
        super().__init__(name, age, gender)
        self.qualification = qualification

    def printDetails(self):
        super().printDetails()
        print("Qualification:", self.qualification)
        print("Team Size:", self.team_size)

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        qualification = input("Qualification: ")
        return cls(name, age, gender, qualification)

class Accountant(Employees):
    
    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class Peon(Employees):
    
    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class GeneralManager(Manager):
    team_size = 100

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
        pass
