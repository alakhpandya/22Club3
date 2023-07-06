# file handling
"""
# f = open('d:\\temp.txt')
f = open('temp.txt')

# print(f.read())
data = f.read(7)
data2 = f.read(10)
print(data)
print(data2)

f.close()
"""
"""
syntax:
file_pointer_name = open('file name with extension & full path', 'Mode1Mode2')
example: 
if we want to open temp.txt in write & text mode:
f = open('temp.txt', 'wt')
if we want to open file in d drive's temp folder with name image.png in append plus & binary mode:

f = open('d:\\temp\\image.png', 'a+b')
"""
"""
Mode1   Name    Description                                                 Mode2   Name
r       read    Opens the file for reading only                             t       text
                Does not create the file it does not exist
                Does not erase the content of the file
                Cursor is placed at the begining of the file
w       write   Opens the file for writing only                             b       binary
                Creates the file it does not exist
                Erases entire content of the file at the time of opening
                Cursor is placed at the begining of the file
a       append  Opens the file for writing only
                Creates the file it does not exist
                Does not erase the content of the file
                Cursor is placed at the end of the file
x  Exclusively  Create the file if it does not exist
    create      Rais FileExistsError if it is already created.
                Opens the file for writing only
                Cursor is placed at the begining of the file
r+  read plus   Opens the file for reading and writing both
                Does not create the file it does not exist
                Does not erase the content of the file
                Cursor is placed at the begining of the file
w+  write plus  Opens the file for reading and writing both
                Creates the file it does not exist
                Erases entire content of the file at the time of opening
                Cursor is placed at the begining of the file
a+ append plus  Opens the file for reading and writing both
                Creates the file it does not exist
                Does not erase the content of the file
                Cursor is placed at the end of the file
"""

# f = open('temp.txt', 'w')
# f = open('temp.txt', 'a')
# f.write("\nKrushnam")
# f.close()

# f = open('temp2.txt', 'x')
# f.write('Hi I am temp2!')
# f.close()

# f = open('temp.txt', 'r+')
# f.read()
# f.write('\nDhiraj')
# f.close()

# f = open('temp3.txt', 'r+')
# f.write('Hi, I am temp3!')
# f.close()

f = open('temp.txt', 'a+')
print(f.tell())
f.seek(0)
print(f.read())
f.close()

# More read & write operations, handling csv files to do data analysis