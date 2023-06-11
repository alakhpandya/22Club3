from employees import Employees

class Accountant(Employees):
    
    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)
