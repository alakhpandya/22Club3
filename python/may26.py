class Car:
    seating_capacity = 5        # class variable
    allCars = []
    # def __init__(self, a, b, c):
    #     self.name = a
    #     self.price = b
    #     self.fuel = c

    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
        Car.allCars.append(self)

    # method
    def printDetails(self):
        print("Model name:", self.name)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel)
        print("Seating:", self.seating_capacity)
        print()

class Owner:
    pass

"""
c1 = Car()
c1.name = "Nexon EV"        # object variable
c1.price = 1500000
c1.fuel = "Electric"

# print("Model name:", c1.name)
# print("Price:", c1.price)
# print("Fuel Type:", c1.fuel)
# print("Seating:", c1.seating_capacity)
# print()
c1.printDetails()

c2 = Car()
c2.name = "XUV 700"
c2.price = 2500000
c2.fuel = "Diesel"
c2.seating_capacity = 7

# print("Model name:", c2.name)
# print("Price:", c2.price)
# print("Fuel Type:", c2.fuel)
# print("Seating:", c2.seating_capacity)
# print()
c2.printDetails()

c3 = Car()
c3.name = "Alto"
c3.price = 300000
c3.fuel = "CNG"


# print("Model name:", c3.name)
# print("Price:", c3.price)
# print("Fuel Type:", c3.fuel)
# print("Seating:", c3.seating_capacity)
# print()
c3.printDetails()

print(c2.__dict__)
print(c1.__dict__)

c4 = Car()
"""

c0 = Car("Nexon EV", 1500000, "Electric")
c1 = Car("XUV 700", 2500000, "Diesel")
c1.seating_capacity = 7
c2 = Car("Alto", 300000, "CNG")
# Car.allCars.append(c0)
# Car.allCars.append(c1)
# Car.allCars.append(c2)

# choice = int(input("car no: "))     # 1
# Car.allCars[choice].printDetails()

print(Car.allCars)