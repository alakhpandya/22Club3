from datetime import datetime
from abc import ABC, abstractmethod
# abc: abstract base classes
# ABC: Abstract Base Class
# Abstraction
"""
Two purposes:
1. We want to restrict object creation in a particular class
2. We want to make some methods compulsory for every child class to have.
"""
class Employees(ABC): 
    all_employees=[]
    
    def __init__(self, name:str, age:int, gender:str):
        assert name.__class__.__name__ == 'str', f'Name must be a string'
        self.name = name
        assert age >= 18, f"We don't hire employees less than age 18. The age you entered ({age}) is too young to recruit"
        self.age = age
        self.gender = gender
        Employees.all_employees.append(self)
        self.generateID(self.dep_id)
    
    def generateID(self, code):
        joinDate = datetime.today()
        joinYear = str(joinDate.year)[2:]
        joinMonth = str(joinDate.month).zfill(2)
        srNo = str(len(Employees.all_employees) + 99)
        self.id = joinYear + joinMonth + code + srNo

    @abstractmethod
    def printDetails(self):
        print(f"---------Details of {self.name}---------")
        print("Employees ID:",self.id)
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
        # print(Employees.all_employees)
        print("-"*20)
        print("ID\tName")
        for employee in Employees.all_employees:
            print(f"{employee.id}\t{employee.name}")
        print("-"*20)
    
    @staticmethod
    @abstractmethod
    def addEmployee() -> object:
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return name, age, gender

    def __repr__(self) -> str:
        return f"({self.name}, {self.__class__.__name__})"

if __name__ == "__main__":
    e1 = Employees("Rahi", 18, "Female")
    # print(e1)
    # e1.printDetails()