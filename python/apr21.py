# Wrong way-
# import myPackage

"""
myPackage.func1()
myModule.func1()
func1()
myPackage.myModule.func1()
"""

# Correct way

# from myPackage import myModule
# myModule.func1()

# from myPackage import myModule as mm
# mm.func1()

# from myPackage.myModule import func1, longNameFunction as lnf
# func1()
# lnf()

# from myPackage.subPackage import subModule
# subModule.subFunc1()

# from myPackage.subPackage import subModule as sm
# sm.subFunc1()

# from myPackage.subPackage.subModule import subFunc1
# subFunc1()

from myPackage.subPackage.subModule import subFunc1 as sf1
sf1()