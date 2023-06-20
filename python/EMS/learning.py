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