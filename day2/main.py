def readData():
    with open('input', 'r') as f:
        data = [tuple(ff.strip().split(' ')) for ff in f]
    return data

def part1(data):
    x, y = 0, 0
    for d in data:
        if d[0] == 'forward':
            x += int(d[1])
        if d[0] == 'down':
            y += int(d[1])
        if d[0] == 'up':
            y -= int(d[1])
    return (x*y)

def part2(data):
    x, y, aim = 0, 0, 0
    for d in data:
        if d[0] == 'forward':
            x += int(d[1])
            y += (aim*int(d[1]))
        if d[0] == 'down':
            aim += int(d[1])
        if d[0] == 'up':
            aim -= int(d[1])
    return (x*y)

data = readData()
print(f'Part 1: {part1(data)}')
print(f'Part 2: {part2(data)}')
