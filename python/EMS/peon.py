from employees import Employees

class Peon(Employees):
    
    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)
