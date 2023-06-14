from employees import Employees

class Accountant(Employees):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.generateID("A")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

    def printDetails(self):
        super().printDetails()
        print("-----------X-----------X-----------")