import csv

"""
f = open('myCollection.csv', 'r')
data = f.readlines()
f.close()

sr_no = int(input("Sr no: "))
# print(data[sr_no])
movie = data[sr_no].split(',')
for i in movie:
    print(i)
"""

# print(dir(csv))

f = open('myCollection.csv', 'r')
# data = csv.reader(f)
# print(data)
# title = next(data)
# for raw in data:
#     print(raw)
# print(title)

data = csv.reader(f)
title = next(data)
data = list(data)
sr_no = int(input("Sr no: ")) - 1
movie = data[sr_no]
f.close()

for i in range(len(movie)):
    print(f"{title[i]}: {movie[i]}")

# Analyse google stock data and answer the following questions:
"""
1. If a person buys 100 shares of google on 19/8/2004 when the stock price was least and sells it on 19/8/2004 when the stock prize was the max. How much profit/loss will she make?
2. Another investor purchases 10 shares of google every day when the market opens and sells it when the stock price gets highest on that day. She continues this for 10 years. How much profit/loss whill she make after 10 years?
3. A college student decides to invest his pocket money into share market and decides to follow a simple strategy: Purchase 5 shares of google everyday when market opens & sell them all when market closes on the same day. What will be his experience of the stock market? Profitable or making loss?
"""