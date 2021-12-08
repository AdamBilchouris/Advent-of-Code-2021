import numpy as np

def readData():
    draws = []
    boards = []
    with open('input', 'r') as f:
        draws = np.array(f.readline().strip().split(','))
        ff = f.readlines()
        #replace the double space padding
        boards = [e.strip().replace('  ', ' ').split('\n\n') for e in ff if e != '\n']
        retBoards = []

        for i in range(0, int(len(boards)/5)):
            temp = boards[5*i:(i*5)+5]
            tempB = []
            for b in boards[5*i:(i*5)+5]:
                for bb in b:
                    bbl = [int(e) for e in bb.split(' ')]
                    tempB.append(bbl)
            if temp != []:
                #retBoards.append(np.array(temp))
                retBoards.append(np.array(tempB))
    return draws, np.array(retBoards)

def checkBingo(board):
    #rows
    bShape = board.shape
    for i in range(0, bShape[0]):
        comp = board[i] == (-1*np.ones(5, dtype=np.int64))
        if comp.all():
            return True
    #columns
    boardC = board.copy()
    boardC = boardC.transpose()
    for i in range(0, bShape[0]):
        comp = boardC[i] == (-1*np.ones(5, dtype=np.int64))
        if comp.all():
            return True
    return False

def part1(draws, boards):
    origBoard = boards.copy()
    bShape = boards.shape
    for d in draws:
        for i in range(0, bShape[0]):
            for j in range(0, 5):
                for k in range(0, 5):
                    if boards[i][j][k] == int(d):
                        boards[i][j][k] = -1
                    if checkBingo(boards[i]):
                        return d, boards[i]

def getScore(draw, board):
    bSum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] != -1:
                bSum += board[i][j]

    return (bSum * draw)

def part2(draws, boards):
    origBoard = boards.copy()
    bShape = boards.shape
    bingoCount = 0
    indices = []
    for d in draws:
        for i in range(0, bShape[0]):
            for j in range(0, 5):
                for k in range(0, 5):
                    if boards[i][j][k] == int(d):
                        boards[i][j][k] = -1
                    if checkBingo(boards[i]):
                        if i not in indices:
                            indices.append(i)
                            bingoCount += 1
                    if bingoCount == bShape[0]:
                        return d, boards[indices[-1]]

draws, boards = readData()
draw, winner = part1(draws, boards)
#print(f'{draw}\n{winner}')
print(f'Part 1: {getScore(int(draw), winner)}')
draw, loser = part2(draws, boards)
#print(f'{draw}\n{loser}')
print(f'Part 2: {getScore(int(draw), loser)}')
