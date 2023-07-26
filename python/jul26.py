# import csv

f = open('myCollection.csv', 'r')
data = f.readlines()
f.close()

sr_no = int(input("Sr no: "))
# print(data[sr_no])
movie = data[sr_no].split(',')
for i in movie:
    print(i)