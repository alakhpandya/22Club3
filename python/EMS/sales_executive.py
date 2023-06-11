from employees import Employees

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

