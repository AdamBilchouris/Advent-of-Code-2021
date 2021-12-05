def readData():
    with open('input', 'r') as f:
        data = [ff.strip() for ff in f]
    return data

def part1(data):
    size = len(data[0])
    nums = [{0:0, 1:0} for i in range(0, size)]
    for i in range(0, size):
        for d in data:
            if int(d[i]) == 0:
                nums[i][0] += 1
            else:
                nums[i][1] += 1

    gamma, epsilon = '', ''
    for i in range(0, size):
        gamma += str(max(nums[i], key=nums[i].get))
        epsilon += str(min(nums[i], key=nums[i].get))

    return (int(gamma, base=2) * int(epsilon, base=2))

def part2(data):
    size = len(data[0])
    dataMin, dataMax = list(zip(*data)), list(zip(*data))
    co2 = ''

    for i in range(0, size):
        colMin = dataMin[i]
        count0, count1 = 0, 0
        toKeep = []

        if len(colMin) == 1:
            break

        for c in colMin:
            if int(c) == 0:
                count0 += 1
            else:
                count1 += 1

        if count0 <= count1:
            toKeep = [i for i, item in enumerate(colMin) if item == '0']
        if count0 > count1:
            toKeep = [i for i, item in enumerate(colMin) if item == '1']

        for j in range(0, size):
            dataMin[j] = tuple([x for i, x in enumerate(dataMin[j]) if i in toKeep])

    co2 = ''.join([''.join(x) for x in dataMin])

    for i in range(0, size):
        colMax = dataMax[i]
        count0, count1 = 0, 0
        toKeep = []

        if len(colMax) == 1:
            break

        for c in colMax:
            if int(c) == 0:
                count0 += 1
            else:
                count1 += 1

        if count0 > count1:
            toKeep = [i for i, item in enumerate(colMax) if item == '0']
        if count0 <= count1:
            toKeep = [i for i, item in enumerate(colMax) if item == '1']

        for j in range(0, size):
            dataMax[j] = tuple([x for i, x in enumerate(dataMax[j]) if i in toKeep])

    o2 = ''.join([''.join(x) for x in dataMax])
    return (int(co2, base=2) * int(o2, base=2))

data = readData()
print(f'Part 1: {part1(data)}')
print(f'Part 2: {part2(data)}')
