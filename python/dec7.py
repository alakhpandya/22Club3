"""
String-list examples:

1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
Example:
input: Alakh Janakkumar Pandya
output: A.J.Pandya
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13
3. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.
4. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.
5. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order. Now print both the lists.
6. Ask 10 numbers from the user and store them in a list. Now, ask user to enter a number between 1 to 10. Delete the element present at that index number and print the list. Now aks user to enter the number that he/she wants to delete. Delete that number itself from the list and print the resultant list.

"""
# 1.
'''
full_name = input("Enter your full name:")     # Alakh Janankkumar Pandya
first_letter = full_name[0]
first_space_index = full_name.index(" ")
second_letter = full_name[first_space_index + 1]
last_space_index = full_name.rindex(" ")
surname = full_name[last_space_index + 1 : ]
short_name = first_letter + "." + second_letter + "." + surname
print(short_name)
'''
# 3.
'''
input_string = input("Enter a sentence: ")
temp = input_string.replace('the ', '')
print(temp.replace('The ', ''))
'''
# 4.
input_string = input("Enter a sentence: ")
temp = input_string.replace(" ", "_", 1)
temp = temp[::-1]
temp = temp.replace(' ', '#', 1)
temp = temp[::-1]
print(temp)