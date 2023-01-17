# int, floats, strings, list, tuples, set
"""
l1 = [5, 6.6]
print(l1)

t1 = ()

s1 = {}

# create multidimensional arrays in Python, need for frozenset
"""
# frozensets: Immutable sets
s1 = {1,2,3,4}
l1 = [4,5,6,7]
str1 = "Python"
fs1 = frozenset(s1)
fs2 = frozenset(l1)
fs3 = frozenset(str1)
print(fs1)
print(fs2)
print(fs3)
fs4 = frozenset({"a", "z", "q", "p"})
print(fs4)

fs5 = fs1.copy()
fs1.difference(fs2)
fs1.intersection(fs2)
fs1.union(fs2)
fs1.isdisjoint(fs2)
fs1.issuperset(fs2)
fs1.symmetric_difference(fs1)