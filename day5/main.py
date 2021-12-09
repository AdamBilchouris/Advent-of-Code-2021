import numpy as np

def readData():
    with open('input', 'r') as f:
        data = [ff.strip() for ff in f]
        retData = []
        for d in data:
            if d == '':
                continue
            temp = []
            for dd in d.split(' -> '):
                temp.append([int(e) for e in dd.split(',')])
            retData.append(temp)
    return retData

def getGridSize(data):
    maxX, maxY = -1, -1
    for d in data:
        for dd in d:
            if maxX < dd[0]:
                maxX = dd[0]
            if maxY < dd[1]:
                maxY = dd[1]
    return (maxX, maxY)

def makeGrid(x, y):
    grid = []
    for i in range(0, x):
        grid.append([0 for j in range(0, y)])
    return grid

def checkHorizontal(y):
    if y[0] == y[1]:
        return True
    return False

def checkVertical(x):
    if x[0] == x[1]:
        return True
    return False

def checkDiagonal(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    if x == 0:
        return (False, -1, -1)
    m = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
    # it is diagonal if arctan(m) == pi/4 (or -pi/4)
    if m == 1 or m == -1:
        c = int(p1[1] - (m*p1[0]))
        return (True, m, c)
    return (False, -1, -1)

def getMinMax(data):
    return (min(data[0], data[1]), max(data[0], data[1]))

def part1(data):
    x, y = getGridSize(data)
    grid = np.array(makeGrid((x+1), (y+1)))

    for i in range(0, len(data)):
        if checkVertical((data[i][0][0], data[i][1][0])):
            lowY, highY = getMinMax((data[i][0][1], data[i][1][1]))
            grid = grid.transpose()
            for j in [k for k in range(lowY, highY + 1)]:
                grid[data[i][0][0]][j] += 1
            grid = grid.transpose()
        
        if checkHorizontal((data[i][0][1], data[i][1][1])):
            lowX, highX = getMinMax((data[i][0][0], data[i][1][0]))
            for j in [k for k in range(lowX, highX + 1)]:
                grid[data[i][0][1]][j] += 1

    score = 0
    for i in range(0, x+1):
        #score += sum(j > 1 for j in grid[i])
        for j in range(0, y+1):
            if grid[i][j] > 1:
               score += 1
    return score

def part2(data):
    x, y = getGridSize(data)
    grid = np.array(makeGrid((x+1), (y+1)))

    for i in range(0, len(data)):
        if checkVertical((data[i][0][0], data[i][1][0])):
            lowY, highY = getMinMax((data[i][0][1], data[i][1][1]))
            grid = grid.transpose()
            for j in [k for k in range(lowY, highY + 1)]:
                grid[data[i][0][0]][j] += 1
            grid = grid.transpose()
        
        if checkHorizontal((data[i][0][1], data[i][1][1])):
            lowX, highX = getMinMax((data[i][0][0], data[i][1][0]))
            for j in [k for k in range(lowX, highX + 1)]:
                grid[data[i][0][1]][j] += 1
        
        diag = checkDiagonal((data[i][0][0], data[i][0][1]), (data[i][1][0], data[i][1][1]))
        if diag[0]:
            m, c = diag[1], diag[2]
            points = [(data[i][0][0], data[i][0][1])]
            lowX, highX = getMinMax((data[i][0][0], data[i][1][0]))

            for j in [k for k in range(lowX + 1, highX)]:
                points.append((j, int(((m*j) + c))))
            points.append((data[i][1][0], data[i][1][1]))

            for (x1, y1) in points:
                grid[y1][x1] += 1

    score = 0
    for i in range(0, x+1):
        for j in range(0, y+1):
            if grid[i][j] > 1:
                score += 1
    return score


data = readData()
print(f'Part 1: {part1(data)}')
print(f'Part 2: {part2(data)}')
