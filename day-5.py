import re
_map = {}
_max = [0]
def parseInput(filename):
    lines = []
    with open(filename) as f:
        line = f.readline()
        while line:
            a = line[:]
            if '[' in a:
                makeStackDictionary([line[i] for i in range(1, len(line), 4)])
            elif a[0] == 'm':
                move, _from, to = [int(s) for s in a.split() if s.isdigit()]
                # useMoveInstruction(move, _from, to)
                useMoveInstructionRetainOrder(move, _from, to)
            line = f.readline()
    f.close()

def makeStackDictionary(line):
    for ind, el in enumerate(line):
        if el != "" and el != " ":
            if ind + 1 not in _map:
                _map[ind + 1] = [el]
            else:
                _map[ind + 1].append(el)
        _max[0] = ind + 1

def useMoveInstruction(move, _from, to):
    print(_map)
    while move > 0:
        if _from in _map and to in _map and len(_map[_from]) > 0:
            _map[to].insert(0, _map[_from].pop(0))
        move -= 1

def useMoveInstructionRetainOrder(move, _from, to):
    print(_map)
    order = []
    while move > 0:
        if _from in _map and to in _map and len(_map[_from]) > 0:
            order.append(_map[_from].pop(0))
        move -= 1
    _map[to] = order + _map[to]

def extractResult():
    res, i = "", 1
    while i <= _max[0]:
        res += _map[i][0] if len(_map[i]) > 0 else ''
        i += 1
    return res
    

def main():
    filename = 'day-5.txt'
    parseInput(filename)
    res = extractResult()

main()