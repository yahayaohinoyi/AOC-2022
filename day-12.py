def parseInput(filename):
    lines = []
    with open(filename) as f:
        line = f.readline()
        while line:
            line = line.strip()
            lines.append(list(line))
            line = f.readline()
    f.close()
    return lines

def findStartPos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return [i, j]

    assert (False, "No start position found")

def inBound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def isMinimumElevation(grid, i, j, x, y):
    l = ord(grid[i][j]) if grid[i][j] != 'S' else ord('a')
    h = ord(grid[x][y]) if grid[x][y] != 'E' else ord('z')
    return l - h >= -1

def getFewestStepsToReachHill(grid, i = 0, j = 0, visited = {}):
    Queue = []
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Queue.append((i, j))
    visited[(i, j)] = 1
    res = 0

    while Queue:
        size = len(Queue)
        while size > 0:
            node = Queue.pop(0)
            i, j = node[0], node[1]
            if grid[i][j] == 'E':
                return res
            for x, y in dirs:
                if inBound(grid, i + x, j + y) and (i + x, j + y) not in visited and isMinimumElevation(grid, i, j, i + x, j + y):
                    Queue.append((i + x, j + y)) 
                    visited[(i + x, j + y)] = 1
            size -= 1
        res += 1
    return res

def main():
    lines = parseInput('day-12.txt')
    x, y = findStartPos(lines)
    res = getFewestStepsToReachHill(lines, x, y, {})
    print(res)

main()