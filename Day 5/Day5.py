""" Day 5 Hydrothermal Venture"""
import re
import numpy as np

with open('input.txt') as f:
    coords = f.read().split("\n")
x=[]
y=[]
for coord in coords:
    z = re.findall("^(\d+),(\d+) -> (\d+),(\d+)$", coord)
    x1 = int([c[0] for c in z][0])
    y1 = int([c[1] for c in z][0])
    x2 = int([c[2] for c in z][0])
    y2 = int([c[3] for c in z][0])
    x.extend([x1,x2])
    y.extend([y1,y2])

npzeros = np.zeros((max(x)+1,max(y)+1))
#For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

for coord in coords:
    z = re.findall("^(\d+),(\d+) -> (\d+),(\d+)$", coord)
    x1 = int([c[0] for c in z][0])
    y1 = int([c[1] for c in z][0])
    x2 = int([c[2] for c in z][0])
    y2 = int([c[3] for c in z][0])

    dy = y2-y1
    dx = x2-x1
    if((x1 == x2 or y1 == y2)):
        if(x2>x1):
            xs = [a for a in range(x1,x2+1)]
        else:
            xs = [a for a in range(x2,x1+1)]
        if(y2>y1):
            ys = [a for a in range(y1,y2+1)]
        else:
            ys = [a for a in range(y2,y1+1)]
    elif(dx == 0 or dy == 0 or abs(dx) == abs(dy)):
        if(x2>x1):
            xs = [a for a in range(x1,x2+1)]
        else:
            xs = [a for a in range(x2,x1+1)]
            xs = xs[::-1]
        if(y2>y1):
            ys = [a for a in range(y1,y2+1)]
        else:
            ys = [a for a in range(y2,y1+1)]
            ys = ys[::-1]
    
    else:
        xs = []
        ys=[]
    print(ys,xs)
    print(coord)
    npzeros[xs,ys] +=1
    print(npzeros)

print(npzeros)
print((npzeros>=2).sum())


