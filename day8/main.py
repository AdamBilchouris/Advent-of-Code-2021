import numpy as np

def readData():
    """
    with open('test', 'r') as f:
        data = [ff.strip().split('|') for ff in f.readlines()]
        for i in range(0, len(data)):
            data[i][0] = data[i][0].strip()
            data[i][1] = data[i][1].strip()
    return data
    """
    with open('input', 'r') as f:
        left = []
        right = []
        for ff in f:
            split = ff.strip().split(' | ')
            addL = split[0].split()
            left.append([''.join(sorted(s)) for s in addL])
            addR = split[1].split()
            right.append([''.join(sorted(s)) for s in addR])

        return left, right

# Only care about unique ones.
# 1 = 2, 4 = 4, 7 = 3, 8 = 7
def part1(left, right):
    i = 0
    for d in right:
        for dd in d:
            lenDD = len(dd)
            if lenDD in {2, 3, 4, 7}:
                i += 1
    return i

"""""""""
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
"""""""""
def part2(left, right):
    """
    # The known, unique, number of segments
    signalMap = {2: 1, 3: 7, 4: 4, 7: 8}
    resList = []
    known = {}
    knownLength = {}
    tempDict = {}

    for i in range(0, len(data)):
        for dd in data[i][0].split():
            lenDD = len(dd)
            dd = ''.join(sorted(dd))
            if lenDD in {2, 3, 4, 7}:
                known[dd] = signalMap[lenDD]
                knownLength[signalMap[lenDD]] = set(dd)
            else:
                tempDict[dd] = lenDD

        knownSet = set(known.keys())
        tempSet = set(tempDict.keys())
        print(tempSet)

    for d in tempDict.keys():
        d = ''.join(sorted(d))
        dSet = set(d)
        lenD = len(dSet)
        #0, 6, 9
        if lenD == 6:
            # Check if the the two sides which make up 1 (aa , bb) are not in the digit. This would be a 6 as it doesn't have aa.
            if not knownLength[1].issubset(dSet):
                known[d] = 6
            # Check if the sides of one exist, this will be the case for 0 and 9.
            # Then check if the dddd in 4 exists, if it does, then it will be 9, otherwise, 0
            elif knownLength[4].issubset(dSet):
                known[d] = 9
            else:
                known[d] = 0

        #2, 3, 5
        if lenD == 5:
            # Check if the the two sides which make up 1 (aa , bb) are in the digit. This would be a 3 as it has aa.
            if knownLength[1].issubset(dSet):
                known[d] = 3
            # If the union between 3 and the set cover every segment, then it is a 2 as 5 would be mssing the gg
            elif (knownLength[4].union(dSet)) == knownLength[8]:
                known[d] = 2
            else:
                known[d] = 5
    for j in range(0, len(data)):
        num = ''
        for dd in data[j][1].split():
            dd1 = ''.join(sorted(dd))
            num += str(known[dd1])
        resList.append(int(num))
        print(num)
    print(known)
    print(resList)

    return np.sum(resList)
    """
    # The known, unique, number of segments
    signalMap = {2: 1, 3: 7, 4: 4, 7: 8}
    known = {}
    knownLength = {}
    i = 0
    sumNum = 0
    #tempDict = {}
    for l in left:
        known = {}
        knownLength = {}

        for ll in l:
            lenLL = len(ll)
            if lenLL in {2, 3, 4, 7}:
                known[ll] = signalMap[lenLL]
                knownLength[signalMap[lenLL]] = set(ll)

        for ll in l:
            lenLL = len(ll)
            setLL = set(ll)

            #0, 6, 9
            if lenLL == 6:
                # Check if the the two sides which make up 1 (aa , bb) are not in the digit. This would be a 6 as it doesn't have aa.
                if not knownLength[1].issubset(setLL):
                    known[ll] = 6
                # Check if the sides of one exist, this will be the case for 0 and 9.
                # Then check if the dddd in 4 exists, if it does, then it will be 9, otherwise, 0
                elif knownLength[4].issubset(setLL):
                    known[ll] = 9
                else:
                    known[ll] = 0

            #2, 3, 5
            if lenLL == 5:
                # Check if the the two sides which make up 1 (aa , bb) are in the digit. This would be a 3 as it has aa.
                if knownLength[1].issubset(setLL):
                    known[ll] = 3
                # If the union between 4 and the set cover every segment, then it is a 2 as 5 would be mssing the gg
                elif (knownLength[4].union(setLL)) == knownLength[8]:
                    known[ll] = 2
                else:
                    known[ll] = 5

        num = ''
        for r in right[i]:
            num += str(known[r])
        num = int(num)
        sumNum += num
        i += 1

    return sumNum

            
left, right = readData()
print(f'Part 1: {part1(left, right)}')
print(f'Part 2: {part2(left, right)}')
