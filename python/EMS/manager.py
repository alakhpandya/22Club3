from employees import Employees

class Manager(Employees):
    team_size = 10
    dep_id = "M"

    def __init__(self, name, age, gender, qualification):
        super().__init__(name, age, gender)
        self.qualification = qualification

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

    def editDetails(self):
        super().editDetails()
        team_size = input("Team size: ")
        if team_size != "":
            self.team_size = int(team_size)
        qualification = input("Qualification: ")
        if qualification != "":
            self.qualification = qualification