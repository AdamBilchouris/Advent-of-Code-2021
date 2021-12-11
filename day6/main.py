import numpy as np

def readData():
    with open('input', 'r') as f:
        data = [int(ff) for ff in f.readline().split(',')]
    return data 

# works for a small number of days.
def part1(data, NUMBER_DAYS):
    newData = data

    for i in range(1, NUMBER_DAYS+1):
        for j in range(0, len(newData)):
            if newData[j] == 0:
                newData[j] = 6
                newData.append(8)
            else:
                newData[j] -= 1
    return len(newData)

def part2(data, NUMBER_DAYS):
    # Keep track of the number of fish at each point in the lifecycle.
    # After each day, make all of the fish that have a timer of 0 re-appear at the end of the list.
    # These are the new fish. The same fish will also need to be added 6 as their timer is reset.
    newData = [0] * 9

    for d in data:
        newData[d] += 1

    for i in range(0, NUMBER_DAYS):
        fishZero = newData.pop(0)
        newData.append(fishZero)
        newData[6] += newData[8]

    return sum(newData)

data = readData()
print(f'Part 1: {part1(data.copy(), 80)}')
print(f'Part 2: {part2(data.copy(), 256)}')
