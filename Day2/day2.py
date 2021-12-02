"""
Day 2 - Dive!
"""

import re

with open('input2.txt') as f:
    directions = f.read().split("\n")
#1
print(sum([int(re.search('forward (\d+)',d).group(1)) for d in directions if re.search('forward (\d+)',d)]) * (sum([int(re.search('down (\d+)',d).group(1)) for d in directions if re.search('down (\d+)',d)]) - sum([int(re.search('up (\d+)',d).group(1)) for d in directions if re.search('up (\d+)',d)])))

#2
f = 0
d = 0
u = 0
h = 0
a = 0
depth = 0
for direct in directions:
    if re.search('forward (\d+)',direct):
        f = int(re.search('forward (\d+)',direct).group(1))
        h += f
        depth += a*f
    if re.search('down (\d+)',direct):
        d = int(re.search('down (\d+)',direct).group(1))
        a += d
    if re.search('up (\d+)',direct):
        u = int(re.search('up (\d+)',direct).group(1))
        a -= u

print(h*depth)