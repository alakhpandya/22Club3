"""
result = {
    "Maths":88,
    "Science":92,
    "Computers":98,
    "Maths":35
}

# Methods of dictionaries:
# print(result.clear())

yourResult = result.copy()
myResult = result
# result.clear()
print(result)
print(yourResult)
print(myResult)

consumers = ["Tithi", "Dharmangi", "Vedangi", "Khush", "Alakh"]
transfer = {}
# Write your code here


print(transfer)
# output:
{"Tithi":100000, "Dharmangi":100000, "Vedangi":100000, "Khush":100000, "Alakh":100000}
"""





"""
Advanced examples of List and Dictionary:
1. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

3. Ask user to give name and marks of 10 different students. Store them in dictionary.

4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it. 

5. Sort the dictionary in Example-3 by the names of students.

6. Sort the dictionary in Example-3 by the marks.

7. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

8. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""

# Example of the way if a question is asked in a technical coding round (Please note that they will NEVER ask such an easy question, this is just to show you how would they describe any question)
"""
Q1. Categorize the person

Problem Description
Write a program to in input from the user a float value(A) representing the height of person. You have to print the category of that person.

If the height is greater than or equal to 195 then that person is "abnormal".
If the height is in the range of [165 -195) then that person is "taller".
If the height is in the range of [150 -165) then that person is "average".
If the height is smaller than 150 then that person is a "dwarf".

Problem Constraints:
50 <= A <= 250

Input Format:
One line containing a float value A. 

Output Format:
A string representing the category of the person.

Example Input:
Input 1:
165

Input 2:
205.8

Input 3:
155

Example Output:
Output 1:
taller

Output 2:
abnormal

Output 3:
average
"""
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    return 0

if __name__ == '__main__':
    main()
"""