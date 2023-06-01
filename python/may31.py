
class Car:
    seating_capacity = 5        # class variable
    allCars = []

    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
        Car.allCars.append(self)

    def printDetails(self):
        print("Model name:", self.name)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel)
        print("Seating:", self.seating_capacity)
        print()

    @staticmethod
    def showAllCars():
        print("-"*20)
        print("SrNo\tName")
        srNo = 0
        for car in Car.allCars:
            print(f"{srNo}\t{car.name}")
            srNo += 1
        print("-"*20)

    def editDetails(self):
        print("Enter updated details (Press Enter to skip that detail):")
        newName = input("Model name:")
        if newName != "":
            self.name = newName
        newPrice = input("Price:")
        if newPrice != "":
            self.price = int(newPrice)
        newFuel = input("Fuel Type:")
        if newFuel != "":
            self.fuel = newFuel
        newSeating_capacity = input("Seating:")
        if newSeating_capacity != "":
            self.seating_capacity = int(newSeating_capacity)

    @classmethod
    def addNewCar(cls):
        # Create new car object
        name = input("Model name:")
        price = int(input("Price:"))
        fuel = input("Fuel Type:")
        return cls(name, price, fuel)

def printTitle():
    print("+" + "-"*100 + "+")
    print("|" + "Welcome to Car Studio".center(100) + "|")
    print("+" + "-"*100 + "+")

"""
User can:
1. create new car objects
2. edit an existing object
3. see details of any object
4. delete an object
5. see all cars in a table format

9. exit
"""
printTitle()
c0 = Car("Nexon EV", 1500000, "Electric")
c1 = Car("XUV 700", 2500000, "Diesel")
c1.seating_capacity = 7
c2 = Car("Alto", 300000, "CNG")

while True:
    print("Type 1 to add new car")
    print("2 to view all cars in the inventory")
    print("3 to see details of a particular car")
    print("4 to edit a car")
    print("5 to delete a car")

    print("9 to exit")
    op = int(input())
    if op == 1:
        Car.addNewCar()
    
    elif op == 2:
        Car.showAllCars()

    elif op == 3:
        Car.showAllCars()
        choice = int(input("Enter sr no of the car you want view details of: "))
        Car.allCars[choice].printDetails()
    
    elif op == 4:
        Car.showAllCars()
        choice = int(input("Enter sr no of the car you want edit: "))
        Car.allCars[choice].editDetails()
    
    elif op == 5:
        Car.showAllCars()
        choice = int(input("Enter sr no of the car you want delete: "))
        removedCar = Car.allCars.pop(choice)
        print(f"Car {removedCar.name} has been removed successfully!")
        print()
    
    elif op == 6:
        pass
    
    elif op == 7:
        pass
    
    elif op == 8:
        pass
    
    elif op == 9:
        break

