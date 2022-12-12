from collections import defaultdict

STRENGHTS = [i + 20 for i in range(0, 221, 40)]
X = 1 # initial value in ragister
cycle = 1
strength = 1
Queue = []
res = 0

def parseInput(filename):
    with open(filename) as f:
        line = f.readline()
        while line:
            getRegisterValAtCycles(line)
            line = f.readline()

def getRegisterValAtCycles(line):
    global cycle, X, res, Queue, strength
    line = line.split(' ')
    ins, val = None, None
    if len(line) == 2:
        ins, val = line[0].strip('\n'), line[1]
    elif len(line) == 1:
        ins, val = line[0].strip('\n'), str(0)

    # store new instruction
    if 'addx' in ins:
        Queue.append([2, int(val)])

    print(cycle, X, Queue[0])
    if cycle in STRENGHTS:
        res += X * cycle

    # process existing instruction
    if Queue:
        Queue[0][0] -= 1
        if Queue[0][0] <= 0:
            X += Queue[0][1]
            Queue.pop(0)

    cycle += 1

        
def resolveQueue():
    global cycle, res, X, Queue , strength
    while Queue:
        if cycle in STRENGHTS:
            res += X * cycle
        print(cycle, X, X*cycle)
        Queue[0][0] -= 1
        if Queue[0][0] <= 0:
            X += Queue[0][1]
            Queue.pop(0)

        cycle += 1
    
def day10():
    global res
    filename = 'day-10.txt'
    parseInput(filename)
    resolveQueue()
    yield None

def main():
    for sol in day10():
        print(sol)

main()