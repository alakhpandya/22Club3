s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
s4 = {1,2,4,5,6,7,8,9}
s5 = {2,4,6,3,5,8}

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)
print("s5 =", s5)
# union = s1.union(s2)
# print(union)
# print(s2.union(s1))
# s1.update(s2)     # s1 = {1,2,3,4,5,6}    we have update() method instead of union_update()

# print(s1.intersection(s2))
# print(s2.intersection(s1))
# s1.intersection_update(s2)

# diff1 = s1.difference(s2)   # s1 - s2
# diff2 = s2.difference(s1)   # s2 - s1
# s1.difference_update(s2)    # s1 = s1 - s2

# print(diff1.union(diff2))   # symmetric difference of s1 & s2

# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))
# s1.symmetric_difference_update(s2)      # s1 = {1,2,5,6}
# print(s1)

# print(s1.issubset(s2))
# print(s1.issubset(s4))
# print(s2.issubset(s5))
# print(s5.issuperset(s2))

print(s1.isdisjoint(s3))

# Next Topic: frozenset()