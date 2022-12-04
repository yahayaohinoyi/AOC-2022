def parseInput(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close()
    return lines

def isPairOverlap(sec_1, sec_2):
    return ((sec_1[0] <= sec_2[0] and sec_1[1] >= sec_2[1])
            or (sec_2[0] <= sec_1[0] and sec_2[1] >= sec_1[1]))

def isOverlappingSection(sec_1, sec_2):
    if (sec_1[0] <= sec_2[0] <= sec_1[1]):
        return True
    if (sec_2[0] <= sec_1[0] <= sec_2[1]):
        return True
    return False

def main():
    res = 0
    res2 = 0
    filename = 'day-4.txt'
    lines = parseInput(filename)
    for line in lines:
        sec_1, sec_2 = line.split(',')
        sec_1, sec_2 = sec_1.split('-'), sec_2.split('-')
        sec_1[0], sec_2[0], sec_1[1], sec_2[1] = int(sec_1[0]), int(sec_2[0]), int(sec_1[1]), int(sec_2[1])
        overlap = isPairOverlap(sec_1, sec_2)
        overlappinngSec = isOverlappingSection(sec_1, sec_2)
        res += overlap
        res2 += overlappinngSec
    print(res)
    print(res2)

main()