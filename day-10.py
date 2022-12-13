from collections import defaultdict

STRENGHTS = [i + 20 for i in range(0, 221, 40)]

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def getRegisterValAtCycles(lines):
    X = 1 # initial value in ragister
    cycle = 0
    res = 0

    for line in lines:
        line = line.split(' ')
        ins = line[0]
        val = None if len(line) <= 1 else line[1].replace('\n', '')
        if 'noop' in ins:
            cycle += 1
            if cycle in STRENGHTS:
                res += cycle * X

        elif 'addx' in ins:
            val = int(val)
            X += val
            cycle += 1

            if cycle in STRENGHTS:
                res += cycle * (X - val)

            cycle += 1

            if cycle in STRENGHTS:
                res += cycle * (X - val)

        else: 
            assert(False, "unknown token")
    return res
    
def day10():
    filename = 'day-10.txt'
    lines = parseInput(filename)
    res = getRegisterValAtCycles(lines)
    yield res

def main():
    for sol in day10():
        print(sol)

main()