import json
def parseInput(filename):
    with open(filename) as f:
        lines = f.read().strip('\n').split('\n')
    f.close()
    return [json.loads(el) for el in lines if el != '']

def inBound(container, ind):
    return 0 <= ind < len(container)

# -1 -> False
# 1 -> True
# 0 -> Equal

def isLessThan(a, b):
    if a and not b:
        return -1

    if b and not a:
        return 1

    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        if b < a:
            return -1
        return 0

    if type(a) == list or type(b) == list:
        if type(a) == int:
            a = [a]

        if type(b) == int:
            b = [b]

        res = 0
        for p, q in zip(a, b):
            res = isLessThan(p, q)
            if res == 1: return 1
            elif res == -1: return -1
        if not res:
            # a ran out items first
            if len(a) < len(b):
                return 1
            if len(b) < len(a):
                return -1
    return 0

def countOrderedPackets(lines):
    count = 0
    i = 1
    while i < len(lines):
        res = isLessThan(lines[i-1], lines[i])
        if res == 1:
            count += i//2 + 1
        i += 2
    return count

def day13():
    filename = 'day-13.txt'
    lines = parseInput(filename)
    yield countOrderedPackets(lines)

def main():
    for sol in day13():
        print(sol)

main()
