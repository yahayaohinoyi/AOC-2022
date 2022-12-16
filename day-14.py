def parseInput(filename):
    with open(filename) as f:
        lines = f.read().strip('\n').split('\n')
    f.close()
    return lines

INIT_SAND_POS = (500, 0)
x_bound = [float('inf'), float('-inf')]
y_bound = [0, float('-inf')]

def inBound(coord):
    return x_bound[0] <= coord[0] <= x_bound[1] and y_bound[0] <= coord[1] <= y_bound[1]

def inBound2(coord):
    return 0 <= coord[1] <= y_bound[1] + 1

def doesUnitComeToRest(filled, coord = INIT_SAND_POS):
    down = (coord[0], coord[1] + 1)
    left = (coord[0] - 1, coord[1] + 1)
    right  = (coord[0] + 1, coord[1] + 1)

    for dir in [down, left, right]:
        if dir not in filled:
            if not inBound(dir): return False
            return doesUnitComeToRest(filled, dir)
    filled.add(coord)
    return True

def doesUnitComeToRest2(filled, coord = INIT_SAND_POS):
    if INIT_SAND_POS in filled: return False
    down = (coord[0], coord[1] + 1)
    left = (coord[0] - 1, coord[1] + 1)
    right  = (coord[0] + 1, coord[1] + 1)

    for dir in [down, left, right]:
        if dir not in filled and inBound2(dir):
            return doesUnitComeToRest2(filled, dir)
    filled.add(coord)
    return True


def simulateSand(lines, filled, part):
    def fillGridWithRocks(line, f, s, filled):
        x1, y1 = line[f].split(',')
        x2, y2 = line[s].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        x_bound[0] = min(x_bound[0], x1, x2)
        x_bound[1] = max(x_bound[1], x1, x2)
        y_bound[0] = min(y_bound[0], y1, y2)
        y_bound[1] = max(y_bound[1], y1, y2)

        filled.add((x1, y1))
        filled.add((x2, y2))
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            while dy > 0:
                y1 += 1
                dy = y2 - y1
                filled.add((x1, y1))

            while dy < 0:
                y1 -= 1
                dy = y2 - y1
                filled.add((x1, y1))

        elif dy == 0:
            while dx > 0:
                x1 += 1
                dx = x2 - x1
                filled.add((x1, y1))
            while dx < 0:
                x1 -= 1
                dx = x2 - x1
                filled.add((x1, y1))

    for line in lines:
        line = line.replace(' ', '').split('->')
        i = 1
        while i < len(line):
            fillGridWithRocks(line, i, i - 1, filled)
            i += 1
    #part 2
    global x_bound, y_bound
    if part == "2":
        units = 0
        while doesUnitComeToRest2(filled): units += 1
        return units

    else:
        units = 0
        while doesUnitComeToRest(filled): units += 1
        return units
    
def day14():
    filename = 'day-14.txt'
    lines = parseInput(filename)

    # part 1
    filled = set()
    yield simulateSand(lines, filled, "1")

    # part 2
    filled = set()
    yield simulateSand(lines, filled, "2")

def main():
    for sol in day14():
        print(sol)
main()