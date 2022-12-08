def parseInput(filename):
    lines = []
    with open(filename) as f:
        line = f.readline()
        while line:
            lines.append(line.replace('\n', ''))
            line = f.readline()
    f.close()
    return lines

def inBound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j <= len(grid[0])

    x, y = i, j
    res = True
    while i - 1 >= 0:
        res = res and (grid[x][y] > grid[i - 1][j])
        if not res: break
        i -= 1
    if res: return res

    res = True
    i, j = x, y
    while i + 1 < len(grid):
        res = res and (grid[x][y] > grid[i + 1][j])
        if not res: break
        i += 1
    if res: return res
    res = True

    i, j = x, y
    while j - 1 >= 0:
        res = res and (grid[x][y] > grid[i][j - 1])
        if not res: break
        j -= 1
    if res: return res
    res = True

    i, j = x, y
    while j + 1 < len(grid[0]):
        res = res and (grid[x][y] > grid[i][j + 1])
        if not res: break
        j += 1
    return res

def scoreForTree(grid, i, j):
    scores = 1
    count = 0
    x, y = i, j
    res = True
    while i - 1 >= 0:
        res = res and (grid[x][y] > grid[i - 1][j])
        count += 1
        if not res: break
        i -= 1
    scores *= max(count, 1)
    count = 0
    res = True
    i, j = x, y
    while i + 1 < len(grid):
        res = res and (grid[x][y] > grid[i + 1][j])
        count += 1
        if not res: break
        i += 1
    scores *= max(count, 1)

    count = 0
    res = True
    i, j = x, y
    while j - 1 >= 0:
        res = res and (grid[x][y] > grid[i][j - 1])
        count += 1
        if not res: break
        j -= 1
    scores *= max(count, 1)

    count = 0
    res = True
    i, j = x, y
    while j + 1 < len(grid[0]):
        res = res and (grid[x][y] > grid[i][j + 1])
        count += 1
        if not res: break
        j += 1
    scores *= max(count, 1)
    return scores

def computeNumberOfVisibleTrees(grid):
    count = len(grid) * 2 + (len(grid[0]) - 2) * 2
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if canBeSeen(grid, i, j):
                count += 1
    return count



def computeMaxScenicScore(grid):
    _max = float('-inf')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = scoreForTree(grid, i, j)
            _max = max(_max, score)
    return _max

def day8():
    filename = 'day-8.txt'
    lines = parseInput(filename)
    yield computeNumberOfVisibleTrees(lines)
    yield computeMaxScenicScore(lines)

def main():
    for i in day8():
        print(i)

main()