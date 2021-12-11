import numpy as np

def readData():
    with open('input', 'r') as f:
        data = [int(ff) for ff in f.readline().split(',')]
    return data 

def part1(data):
    # Find the median of the crabs and use this as the point where they meet.
    median = np.median(data).astype(int)
    diff = []
    for d in data:
        diff.append(np.abs(d - median).astype(int))

    return sum(diff)

def part2(data):
    # Get the average position of every crab.
    # As the crabs can only take on an integer position, get the floor value.
    mean = np.floor(np.mean(data)).astype(int)
    fuelUsage = 0
    diffArr = []
    for d in data:
        diff = np.round(np.abs(d - mean)).astype(int)
        # The fuel usage is a triangular number of the difference between the mean and position.
        # (n^2 + n) / 2
        fuelUsage += (diff**2 + diff) // 2

    return fuelUsage

data = readData()
print(f'Part 1: {part1(np.array(data, dtype=np.int64))}')
print(f'Part 2: {part2(np.array(data, dtype=np.int64))}')
