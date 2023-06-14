from employees import Employees

class Manager(Employees):
    team_size = 10

    def __init__(self, name, age, gender, qualification):
        super().__init__(name, age, gender)
        self.qualification = qualification
        self.generateID("M")

    def printDetails(self):
        super().printDetails()
        print("Qualification:", self.qualification)
        print("Team Size:", self.team_size)
        print("-----------X-----------X-----------")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        qualification = input("Qualification: ")
        return cls(name, age, gender, qualification)
