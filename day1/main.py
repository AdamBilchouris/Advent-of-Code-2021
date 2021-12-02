def readData():
    with open('input', 'r') as f:
        data = [int(ff.strip()) for ff in f]
    return data

def part1(data):
    inc = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            inc += 1
        prev = data[i]
    return inc

def part2(data):
    WINDOW_SIZE = 3
    sum_window = []
    for i in range(len(data)):
        sum_window.append(sum(data[i:i + WINDOW_SIZE]))

    inc = 0
    for i in range(1, len(sum_window)):
        if sum_window[i] > sum_window[i-1]:
            inc += 1

    return inc

data = readData()
print(f'Part 1: {part1(data)}')
print(f'Part 2: {part2(data)}')

