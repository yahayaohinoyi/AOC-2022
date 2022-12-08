def parseInput(filename):
    lines = []
    with open(filename) as f:
        line = f.readline()
        while line:
            lines.append(line.replace('\n', ''))
            line = f.readline()
    f.close()
    return lines

def isInBound(grid, p, q):
    return 0 <= p < len(grid) and 0 <= q < len(grid[0])

def canBeSeen(grid, i, j, x, y, ACTION):
    if not isInBound(grid, x, y):
        return True

    initialCondition = (i == x) and (j == y)
    if not initialCondition and grid[i][j] <= grid[x][y]:
        return False

    if ACTION == "RIGHT":
        return canBeSeen(grid, i, j, x + 1, y, ACTION)
    elif ACTION == "LEFT":
        return canBeSeen(grid, i, j, x - 1, y, ACTION)
    elif ACTION == "UP":
        return canBeSeen(grid, i, j, x, y - 1, ACTION)
    else:
        return canBeSeen(grid, i, j, x, y + 1, ACTION)

def scoreForDirection(grid, i, j, x, y, ACTION, score = 0):
    if not isInBound(grid, x, y):
        if (i == 0 and x < 0) or (j == 0 and y < 0) or ((i == len(grid) - 1) and x >= len(grid)) or ((j == len(grid) - 1) and y >= len(grid)):
            return score
        return score - 1

    initialCondition = (i == x) and (j == y)
    if not initialCondition and grid[i][j] <= grid[x][y]:
        return score

    if ACTION == "RIGHT":
        return scoreForDirection(grid, i, j, x + 1, y, ACTION, score + 1)
    elif ACTION == "LEFT":
        return scoreForDirection(grid, i, j, x - 1, y, ACTION, score + 1)
    elif ACTION == "UP":
        return scoreForDirection(grid, i, j, x, y - 1, ACTION, score + 1)
    else:
        return scoreForDirection(grid, i, j, x, y + 1, ACTION, score + 1)

def computeNumberOfVisibleTrees(grid):
    count = len(grid) * 2 + (len(grid[0]) - 2) * 2
    DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

    def isTreeSeen(i, j):
        seen = False
        for dir in DIRECTIONS:
            seen = seen or canBeSeen(grid, i, j, i, j, dir)
        return seen

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            seen = isTreeSeen(i, j)
            if seen:
                count += 1
    return count

def computeMaxScenicScore(grid):
    DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
    _max = float('-inf')

    def getScenicScore(grid, i, j):
        score = 1
        for dir in DIRECTIONS:
            raw = scoreForDirection(grid, i, j, i, j, dir)
            score *= raw
        return score

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = getScenicScore(grid, i, j)
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