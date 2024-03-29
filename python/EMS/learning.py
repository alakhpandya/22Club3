"""
a = input("a: ")
# if type(a) == "<class 'str'>":
#     print("OK")
# else:
#     print("Not Ok")

# print(a.__class__.__name__)
if a.__class__.__name__ == "str":
    print("OK")
else:
    print("Not Ok")
"""

# Encapsulation
class Products():
    quantity = 10   # public variable

    @staticmethod
    def updateQuantity():   # public method
        Products.quantity = int(input("New Quantity: "))

    _mrp = 150       # protected variable

    @staticmethod
    def _updateMRP():   # protected method
        Products._mrp = float(input("New MRP: "))

    __costPrice = 95        # private variable

    # getter
    @property
    def dealerPrice(self):
        return self.__costPrice

    # setter
    @dealerPrice.setter
    def dealerPrice(self, newDealerPrice):
        self.__costPrice = newDealerPrice
        # return self.__costPrice

    @staticmethod
    def accessCostPrice():
        return Products.__costPrice

class Ketchup(Products):
    pass

# Products.quantity = 13
# print(Products.quantity)
# Products.updateQuantity()
# print("New quantity:", Products.quantity)

p1 = Products()
# print("Price =", p1._mrp)
# p1._updateMRP()
# print("New Price =", p1._mrp)

k1 = Ketchup()
# print("price of k1 =", k1._mrp)
# k1._updateMRP()
# print("New price of k1 =", k1._mrp)

# print("Cost price of products:", Products.__costPrice)
# print("Cost price of products:", Products.accessCostPrice())
# print("Cost price of p1:", p1.__costPrice)
# print("Cost price of p1:", p1.accessCostPrice())
# print("Cost price of k1:", k1.__costPrice)
# print("Cost price of k1:", k1.accessCostPrice())

# Name mangling
"""
print("Cost price of products:", Products._Products__costPrice)
print("Cost price of p1:", p1._Products__costPrice)
print("Cost price of k1:", k1._Products__costPrice)
"""
# print(p1._mrp)
print(p1.dealerPrice)
p1.dealerPrice = 105