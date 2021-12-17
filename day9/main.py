import numpy as np

def readData():
    with open('input', 'r') as f:
        data = [ff.strip() for ff in f]
    return data

def readData2():
    with open('input', 'r') as f:
        data = [ff.strip() for ff in f]
    ret = []
    for d in data:
        l = []
        for dd in d:
            l.append(int(dd))
        ret.append(l)
    return ret

def checkLow(data, i, j, row, col):
    curr = int(data[i][j])
    above, below, left, right= 100000, 100000, 100000, 100000

    if i > 0:
        above = int(data[i-1][j])
    if i < row - 1:
        below = int(data[i+1][j])
    if j > 0:
        left = int(data[i][j-1])
    if j < col - 1: 
        right = int(data[i][j+1])

    if curr < above and curr < below and curr < left and curr < right:
        return (True, curr)
    return (False, -1)

def part1(data):
    risk = 0
    for i in range(row):
        for j in range(col):
            isLow = checkLow(data, i, j, row, col)
            if isLow[0]:
                risk += (isLow[1] + 1)
    return risk

groups = []
def findNeighbour(data, i, j, row, col):
    #bounds
    if i < 0 or i > (row - 1) or j < 0 or j > (col - 1):
        return 
    #ignore 9
    if data[i][j] == 9:
        return
    #if the sample has already been seen, ignore it
    if data[i][j] == -1:
        return

    data[i][j] = -1
    groups[len(groups) - 1] += 1
    #above
    findNeighbour(data, i + 1, j, row, col)
    #below
    findNeighbour(data, i - 1, j, row, col)
    #left
    findNeighbour(data, i, j - 1, row, col)
    #right
    findNeighbour(data, i, j + 1, row, col)

def part2(data):
    for i in range(row):
        for j in range(col):
            if data[i][j] < 9:
                groups.append(0)
                findNeighbour(data, i, j, row, col)
    return (np.prod(sorted(groups)[-3:]))

data = readData()
row, col = len(data), len(data[0])
print(f'Part 1: {part1(data)}')
data = readData2()
print(f'Part 2: {part2(data)}')
