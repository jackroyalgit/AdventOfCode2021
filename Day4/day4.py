""" Day 4 Giant Squid """
import numpy as np
with open('input.txt') as f:
    numbers = f.read().split("\n\n")

numbers = list(map(lambda x:x.replace('\n',' '),numbers))
numbers = list(map(lambda x:x.replace('  ',' '),numbers))
inpnums = numbers[0].split(",")

clean = []
visit =[]
for num in numbers[1:]:
    num = num.split(" ")
    if "" in num:
        num.remove("")
    num = list(map(int, num))
    num2d = np.reshape(num, (5,5))
    visited = np.full((5, 5), False)
    clean.append(num2d)
    visit.append(visited)

def removearray(L,arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind],arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        raise ValueError('array not found in list.')
    
def column(matrix, i):
    return [row[i] for row in matrix]

def boardcheck(inputnumbers,cleanlist):
    marked = 0
    unmarked = 0
    inpnums = list(map(int, inputnumbers))
    for v in inpnums:
        for iy, ix in np.ndindex(5,5):
            for board,visited in zip(cleanlist,visit):
                if(board[iy, ix] == v):
                    visited[iy,ix] = True 
                    marked += v                   
                else:
                    unmarked += v
                i = 0
                for row in visited:
                    col = column(visited,i)
                    i+=1              
                    if(all(row == True) or all(col)):
                        result = np.where(visited == False)
                        coords = list(zip(result[0], result[1]))
                        total = 0
                        total = sum(board[x] for x in coords)
                        print(board[iy, ix]*total)
                        removearray(visit,visited)
                        removearray(cleanlist,board)
                        break
                        
boardcheck(inpnums,clean)




