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
    if len(buffer) < n:
        return 0
    i = n - 1
    while i < len(buffer):
        a = [buffer[i - n] for n in range(n)]
        print(a)
        if len(list(set(a))) == len(a):
            return i
        i += 1
    return 0

def main():
    filename = 'day-6.txt'
    lines = parseInput(filename)
    res = getFirstStartOfPacket(lines[0], 14)
    print(res)
main()