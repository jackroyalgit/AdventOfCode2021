from os import truncate
import numpy as np

with open('input.txt') as f:
    numbers = f.read().split(",")
#part 1 - calculate median value

#part 2
numbers = np.array(numbers).astype(int)
numbermean = int(round(sum(numbers)/len(numbers)))+1000
numbermean = 1
# calculates fuel value for part 2
def calculate(positions, anchor):
    total = 0
    for i in positions:
        total+= sum(list(range(0,abs(anchor-i)+1)))
    return total

check = True
while(check):
    above = calculate(numbers, numbermean+1)
    value = calculate(numbers, numbermean)
    below = calculate(numbers, numbermean-1)

    if(above < value):
        numbermean = numbermean+1
    elif(below < value):
        numbermean = numbermean-1
    else:
        numbermean = numbermean
        check=False

print(value)