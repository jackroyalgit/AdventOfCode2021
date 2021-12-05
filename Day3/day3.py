""" Day 3 - Binary Diagnostic"""

with open('prac3.txt') as f:
    numbers = f.read().split("\n")

gamma = ""
epsilon=""
i = 0
width =len(numbers[0])
for i in range(0,width):
    countzero = 0
    countone = 0
    for num in numbers:
        if(num[i] == "0"):
            countzero += 1
        else:
            countone += 1
    
    if(countzero > countone):
        gamma+="0"
        epsilon+="1"
    else:
        gamma+="1"
        epsilon+="0"

    

print(int(gamma,2) * int(epsilon,2))

"""P2"""
oxygen = numbers
c02 = numbers

#print(numbers)
for i in range(0,width):
    oxynum1 = 0
    oxynum0 = 0
    oxygen1 = []
    oxygen0 = []
    
    c02num1 = 0
    c02num0 = 0
    c021 = []
    c020 = []
    
    if(len(oxygen) > 1):
        for num in oxygen:
            if(num[i] == "1"):
                oxynum1 += 1
                oxygen1.append(num)
            else:
                oxynum0+=1
                oxygen0.append(num)
        if(oxynum1 >= oxynum0):
            oxygen = oxygen1
        else:
            oxygen = oxygen0
    if(len(c02) > 1):
        for num in c02:
            if(num[i] == "1"):
                c02num1 += 1
                c021.append(num)
            else:
                c02num0+=1
                c020.append(num)
        if(c02num1 < c02num0):
            c02 = c021
        else:
            c02 = c020


print(int(oxygen[0],2) * int(c02[0],2))
