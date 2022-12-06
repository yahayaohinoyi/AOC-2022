_dict = {}
def parseInput(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close()
    return lines

# def getFirstStartOfPacket(buffer, n):
#     count = 0
#     for ind, el in enumerate(buffer):
#         print(_dict, count)
#         if el not in _dict:
#             count += 1
#             _dict[el] = ind
#             if count == n:
#                 return ind + 1
#         else:
#             if abs(_dict[el] - ind) >= n:
#                 count += 1
#                 if count == n:
#                     return ind + 1
#             else:
#                 count = abs(_dict[el] - ind)
#                 _dict[el] = ind

def getFirstStartOfPacket(buffer, n):
    Queue = []
    for i in range(n - 1):
        Queue.append(buffer[i])

    for i in range((n - 1), len(buffer)):
        Queue.append(buffer[i])
        if isDistinct(Queue):
            return i + 1
        Queue.pop(0)

def isDistinct(Queue):
    return len(list(set(Queue))) == len(Queue)

def main():
    filename = 'day-6.txt'
    lines = parseInput(filename)
    res = getFirstStartOfPacket(lines[0], 14)
    print(res)
main()