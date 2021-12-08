""" Day 4 Giant Squid """
import numpy as np
with open('input.txt') as f:
    numbers = f.read().split("\n\n")

numbers = list(map(lambda x:x.replace('\n',' '),numbers))
numbers = list(map(lambda x:x.replace('  ',' '),numbers))
inpnums = numbers[0].split(",")

for num in numbers[1:]:
    num = num.split(" ")
    
    print(num)
print(inpnums)
