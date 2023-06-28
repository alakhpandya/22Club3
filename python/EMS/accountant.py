from employees import Employees

class Accountant(Employees):
    dep_id = "A"
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

    def printDetails(self):
        super().printDetails()
        print("-----------X-----------X-----------")

    def editDetails(self):
        super().editDetails()
        