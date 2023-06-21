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

    @property
    def mrp(self):
        return self._mrp
    
    @staticmethod
    def _updateMRP():   # protected method
        Products._mrp = float(input("New MRP: "))

    __costPrice = 95        # private variable
    
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
print(p1._mrp)