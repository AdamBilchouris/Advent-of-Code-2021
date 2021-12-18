import numpy as np

def readData():
    with open('input', 'r') as f:
        data = [ff.strip() for ff in f]
    return data

def part1(data):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = []
    for d in data:
        s = []
        for dd in d:
            isGt, isCy, isSq, isBr = False, False, False, False
            if len(s) > 0:
                isGt = dd == '>' and s[-1] == '<' 
                isCy = dd == '}' and s[-1] == '{'
                isSq = dd == ']' and s[-1] == '['
                isBr = dd == ')' and s[-1] == '('

            if isGt or isCy or isSq or isBr:
                s.pop()
            elif dd in ('(', '[', '{', '<'):
                s.append(dd)
            else:
                score.append(points[dd])
                break
    return sum(score)

def part2(data):
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    matching = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = []
    for d in data:
        isCorrupt = False
        s = []
        for dd in d:
            isGt, isCy, isSq, isBr = False, False, False, False
            if len(s) > 0:
                isGt = dd == '>' and s[-1] == '<' 
                isCy = dd == '}' and s[-1] == '{'
                isSq = dd == ']' and s[-1] == '['
                isBr = dd == ')' and s[-1] == '('

            if isGt or isCy or isSq or isBr:
                s.pop()
            elif dd in ('(', '[', '{', '<'):
                s.append(dd)
            else:
                isCorrupt = True
                break
        #only care about incomplete lines
        if isCorrupt:
            continue

        s.reverse()

        score = 0
        for ss in s:
            score = (5 * score) + points[matching[ss]]
        scores.append(score)

    scores.sort()
    return np.median(scores).astype(int)

data = readData()
print(f'Part 1: {part1(data)}')
print(f'Part 2: {part2(data)}')
