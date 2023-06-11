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

