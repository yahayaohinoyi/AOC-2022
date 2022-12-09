from collections import defaultdict
tPositionToOcc = defaultdict(int)
posForKnots = [{'x': 0, 'y': 0} for _ in range(10)]

def parseInput(filename):
    with open(filename) as f:
        line = f.readline()
        while line:
            simulateRopeMotion(line)
            line = f.readline()

def simulateRopeMotion(line):
    def makeFollowerKnots(ind):
        f, s = ind - 1, ind
        dx = posForKnots[f]['x'] - posForKnots[s]['x']
        dy = posForKnots[f]['y'] - posForKnots[s]['y']

        if abs(dx) <= 1 and abs(dy) <= 1:
            return

        if dx > 0:
            posForKnots[s]['x'] += 1
        elif dx < 0:
            posForKnots[s]['x'] -= 1

        if dy > 0:
            posForKnots[s]['y'] += 1
        elif dy < 0:
            posForKnots[s]['y'] -= 1

    dir, mag = line.split(' ')
    for _ in range(int(mag)):
        if dir == 'U':
            posForKnots[0]['y'] += 1
        elif dir == 'D':
            posForKnots[0]['y'] -= 1
        elif dir == 'L':
            posForKnots[0]['x'] -= 1
        elif dir == 'R':
            posForKnots[0]['x'] += 1

        for ind in range(1, len(posForKnots)):
            makeFollowerKnots(ind)
        tPositionToOcc[(posForKnots[len(posForKnots) - 1]['x'], posForKnots[len(posForKnots) - 1]['y'])] += 1

def numberOfTailVisits():
    return len(tPositionToOcc.keys())

def day9():
    filename = 'day-9.txt'
    parseInput(filename)
    yield numberOfTailVisits()

def main():
    for sol in day9():
        print(sol)

main()