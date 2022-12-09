from collections import defaultdict
tPositionToOcc = defaultdict(int)
posForTwoKnots = [[0, 0], [0, 0]]
tPositionToOcc[(posForTwoKnots[0][0], posForTwoKnots[0][0])] = 1
# posForTenKnots = [[0, 0] for _ in range(10)]

def parseInput(filename):
    with open(filename) as f:
        line = f.readline()
        while line:
            ind = len(posForTwoKnots) - 1
            while ind > 0:
                simulateRopeForTwoKnots(line, posForTwoKnots[ind], posForTwoKnots[ind - 1])
                ind -= 1
            line = f.readline()

def simulateRopeForTwoKnots(line, hp, tp):
    def tailDivergeFromHead(hp, tp):
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            if tp[0] + x == hp[0] and tp[1] + y == hp[1]:
                return False

        return True

    dir, mag = line.split(' ')
    if dir == 'R':
        for _ in range(int(mag)):
            hp[0] += 1
            if not tailDivergeFromHead(hp, tp):
                pass

            if hp[1] == tp[1] and abs(hp[0] - tp[0]) > 1:
                tp[0] = hp[0] - 1 if hp[0] > tp[0] else hp[0] + 1

            elif abs(hp[1] - tp[1]) >= 1 and tailDivergeFromHead(hp, tp):
                tp[1] = hp[1]
                tp[0] = hp[0] - 1 if hp[0] > tp[0] else hp[0] + 1
            tPositionToOcc[(posForTwoKnots[0][0], posForTwoKnots[0][1])] += 1
            
    elif dir == 'L':
        for _ in range(int(mag)):
            hp[0] -= 1

            if not tailDivergeFromHead(hp, tp):
                pass

            if hp[1] == tp[1] and abs(hp[0] - tp[0]) > 1:
                tp[0] = hp[0] - 1 if hp[0] > tp[0] else hp[0] + 1

            elif abs(hp[1] - tp[1]) >= 1 and tailDivergeFromHead(hp, tp):
                tp[1] = hp[1]
                tp[0] = hp[0] - 1 if hp[0] > tp[0] else hp[0] + 1
            tPositionToOcc[(posForTwoKnots[0][0], posForTwoKnots[0][1])] += 1

    elif dir == 'U':
        for _ in range(int(mag)):
            hp[1] += 1
            if not tailDivergeFromHead(hp, tp):
                pass

            if hp[0] == tp[0] and abs(hp[1] - tp[1]) > 1:
                tp[1] = hp[1] - 1 if hp[1] > tp[1] else hp[1] + 1

            elif abs(hp[0] - tp[0]) >= 1 and tailDivergeFromHead(hp, tp):
                tp[0] = hp[0]
                tp[1] = hp[1] - 1 if hp[1] > tp[1] else hp[1] -+1
            tPositionToOcc[(posForTwoKnots[0][0], posForTwoKnots[0][1])] += 1

    elif dir == 'D':
        for _ in range(int(mag)):
            hp[1] -= 1
            if not tailDivergeFromHead(hp, tp):
                pass

            if hp[0] == tp[0] and abs(hp[1] - tp[1]) > 1:
                tp[1] = hp[1] - 1 if hp[1] > tp[1] else hp[1] + 1

            elif abs(hp[0] - tp[0]) >= 1 and tailDivergeFromHead(hp, tp):
                tp[0] = hp[0]
                tp[1] = hp[1] - 1 if hp[1] > tp[1] else hp[1] + 1
            tPositionToOcc[(posForTwoKnots[0][0], posForTwoKnots[0][1])] += 1

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