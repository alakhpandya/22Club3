# result = {
#     "Maths":88,
#     "Science":92,
#     "Computers":98,
#     "Physics":65,
#     "English":85,
#     "Environment":100,
#     "Chemistry":45
# }

"""
result.setdefault("Java", 89)
print(result)

result["C"] = 80
result["English"] = 80

result.setdefault("English", 50)
print(result)
"""
# return_value = result.setdefault("Java", 89)
# return_value = result.setdefault("English", 70)
# print(return_value)

"""
write a program that uses the 'result' dictionary given below & asks name of a subject & marks from user to add in the dictionary. If the subject does not exist in the 'result', add the subject and the marks as new key : value pair in the dictionary. If the subject already exists, tell user that the subject already exists with ____ marks and ask for the confirmation to overwrite it. If user confirms to overwrite, then replace the previous subject & marks with new ones. If user does not want to overwrite, print a message on the screen "Subject could not be added." At the end, print the result dictionary.

result = {
    "Maths":88,
    "Science":92,
    "Computers":98,
    "Physics":65,
    "English":85,
    "Environment":100,
    "Chemistry":45
}

# Your code goes here


print(result)

Test inputs - 1:
java
89

Output - 1:
result = {
    "Maths":88,
    "Science":92,
    "Computers":98,
    "Physics":65,
    "English":85,
    "Environment":100,
    "Chemistry":45,
    "Java":89
}

Test inputs - 2:
English
80

Output - 2:
Subject English already exists with 85 marks. Do you want to overwrite, Y/N?
    2nd input: N
    Final Output:
    Subject could not be added.
    result = {
        "Maths":88,
        "Science":92,
        "Computers":98,
        "Physics":65,
        "English":85,
        "Environment":100,
        "Chemistry":45,
    }

    2nd input: Y
    Final Ouput:
    result = {
        "Maths":88,
        "Science":92,
        "Computers":98,
        "Physics":65,
        "English":80,
        "Environment":100,
        "Chemistry":45,
    }
"""
"""
a = 15
b = 30

print(a + b)
print(a.__add__(b)) # magical methods/dunder methods

c = "Surat"
d = "City"

print(c + d)
print(c.__add__(d))
"""