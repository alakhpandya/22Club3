# Uniform distribution, normal distribution

# print(dir(random))
# for i in range(20):
#     print(random.normalvariate(70, 5))

# Nihar
import random

def getRandomPath(pathLength):
    block=['up','down','left','right']
    x=0
    y=0

    for i in range(pathLength):
        choice1=random.choice(block)
        if choice1=='up':
            y+=1
        elif choice1=='down':
            y-=1
        elif choice1=='right':
            x+=1
        else:
            x-=1
    return x, y

noPay = 0
no_of_walks = 10000
pathLength = 8
for i in range(no_of_walks):
    x, y = getRandomPath(pathLength)
    distance = abs(x) + abs(y)
    if distance <= 4:
        noPay += 1

prob_of_noPay = noPay * 100/no_of_walks
print("Length\tProbability")
print(f"{pathLength}\t{prob_of_noPay}")

# Beautify this program