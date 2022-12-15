from collections import defaultdict

STRENGHTS = [i + 20 for i in range(0, 221, 40)]
cyclesToValue = [1]*241

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
            cyclesToValue[cycle] = X
            if cycle in STRENGHTS:
                res += cycle * X

        elif 'addx' in ins:
            val = int(val)
            X += val
            cycle += 1
            cyclesToValue[cycle] = X - val

            if cycle in STRENGHTS:
                res += cycle * (X - val)

            cycle += 1
            cyclesToValue[cycle] = X

            if cycle in STRENGHTS:
                res += cycle * (X - val)

        else: 
            assert(False, "unknown token")
    return res

def printCRTImage():
    res = [[None] * 40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            round = 40 * row + col + 1
            if abs(cyclesToValue[round - 1] - col) <= 1:
                res[row][col] = "##"
            else:
                res[row][col] = "  "
    s = ""
    for row in res:
        s += ''.join(row)
        s += "\n"
    return s
    
def day10():
    filename = 'day-10.txt'
    lines = parseInput(filename)
    yield getRegisterValAtCycles(lines)
    yield printCRTImage()


def main():
    for sol in day10():
        print(sol)

main()