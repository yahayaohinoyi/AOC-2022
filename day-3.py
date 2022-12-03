
import string
from collections import defaultdict
dictionary = {ch: n for n, ch in enumerate(string.ascii_letters)}
# def findCommonItemsPriority(line):
#     _map = {}
#     sumOfRuckCommonSackItems = 0
#     for ind, el in enumerate(line):
#         if ind < len(line)//2 :
#             _map[el] = True
#         else:
#             if el in _map:
#                 print(el, line)
#                 sumOfRuckCommonSackItems += dictionary[el] + 1
#                 break
    
#     return sumOfRuckCommonSackItems

def findCommonItemsPriorityInGroups(group):
    _map = {}
    for ind, row in enumerate(group):
        for el in list(set(row)):
            if el not in _map and el != '\n':
                print(el)
                _map[el] = 1
            elif el != '\n':
                _map[el] += 1
                if _map[el] == 3:
                    return dictionary[el] + 1

def ruckSackOrganization(filename):
    res = 0
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            # res += findCommonItemsPriority(line)
            res += findCommonItemsPriorityInGroups(lines[i:i+3])
            i += 3
    return res
        

res = ruckSackOrganization('day-3.txt')
print(res)
