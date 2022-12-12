from collections import defaultdict
import heapq

class MonkeyNode():
    def __init__(self, operation = None, test = None, truth = None, false = None) -> None:
        self.operation  = operation
        self.test = test
        self.truth = truth
        self.false = false

monkeysToItems = defaultdict(list)
monkeysToInspection = defaultdict(int)
NUM_ROUNDS = 20

def parseInput(filename):
    with open(filename) as f:
        line = f.readline()
        while 'Monkey' in line:
            line = line.replace('\n', '')
            _, idx = line.replace(':', '').split()
            monkeysToItems[idx] = [[]]
            monkeysToInspection[idx] = 0

            node = MonkeyNode()
            monkeysToItems[idx].append(node)

            line = f.readline()
            while line and 'Monkey' not in line:
                line = line.replace('\n', '')
                if 'Starting' in line:
                    startItems = line.replace(' ', '').split(':')
                    items = startItems[1].split(',')
                    monkeysToItems[idx][0] += items

                elif 'Operation' in line:
                    op = line.replace(' ', '').split('=')
                    operation = op[1]
                    node.operation = operation

                elif 'Test' in line:
                    test = line.split(' ')[-1]
                    node.test = test

                elif 'true' in line:
                    _truth = line.split(' ')[-1]
                    node.truth = _truth

                elif 'false' in line:
                    _false = line.split(' ')[-1]
                    node.false = _false

                line = f.readline()
            if 'Monkey' in line: continue
            line = f.readline()
        
def simulateMonkeyInTheMiddle():
    global NUM_ROUNDS
    for _ in range(NUM_ROUNDS):
        i = 0
        while str(i) in monkeysToItems:
            items = monkeysToItems[str(i)]
            operation = items[1].operation
            test = items[1].test
            truth = items[1].truth
            false = items[1].false
            while items[0]:
                worryLevel = int(items[0].pop(0))
                monkeysToInspection[str(i)] += 1
                if '+' in operation:
                    l, r = operation.split('+')
                    assert( l == 'old')
                    if r == 'old':
                        worryLevel *= 2
                    elif r.isdigit():
                        worryLevel += int(r)
                elif '*' in operation:
                    l, r = operation.split('*')
                    assert( l == 'old')
                    if r == 'old':
                        worryLevel = worryLevel**2
                    elif r.isdigit():
                        worryLevel *= int(r)
                worryLevel //= 3
                if (worryLevel % int(test) == 0):
                    monkeysToItems[truth][0].append(worryLevel)
                else:
                    monkeysToItems[false][0].append(worryLevel)
            i += 1

def getMonkeyBusiness():
    bus = list(monkeysToInspection.values())
    heapq.heapify(bus)
    res = heapq.nlargest(2, bus)
    return res[0]*res[1]

def main():
    parseInput('day-11.txt')
    simulateMonkeyInTheMiddle()
    print(getMonkeyBusiness())
main()