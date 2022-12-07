class FileNode:
    def __init__(self, val, parent = None, children = [], _type = None, size = 0):
        self.children = children
        self.size = size
        self.val = val
        self.parent = parent
        self.type = _type

def parseInput(filename, runner):
    with open(filename) as f:
        line = f.readline()
        while line:
            if '$' in line:
                CMD = line[2:4]
                ARG = line[5:]
                if CMD == 'cd':
                    if '..' in ARG:
                        runner = runner.parent

                    elif '/' not in ARG:
                        for node in runner.children:
                            if node.val == ARG.strip(' '):
                                runner = node
                                break

                elif CMD == 'ls':
                    line = f.readline()
                    while len(line) > 1 and '$' not in line:
                        a = line.split(' ')
                        if a[0] == 'dir':
                            runner.children.append(
                                FileNode(
                                    a[1],
                                    runner,
                                    [],
                                    'dir'
                                )
                            )
                        elif a[0].isdigit():
                            runner.children.append(
                                FileNode(
                                    a[1],
                                    runner,
                                    None,
                                    'file',
                                    int(a[0])
                                )
                            )
                        line = f.readline()
                    continue
            else:
                assert(False, "UNKNOWN TOKEN")
            line = f.readline()

def getSumDirs(Tree, res = [0]):
    if Tree.children == None or Tree.children == []:
        return
    for i in range(len(Tree.children)):
        node = Tree.children[i]
        if node.type == 'dir' and node.size < 100000:
            res[0] += node.size
        getSumDirs(Tree.children[i], res)

def smallestDirToFreeUpEnoughSpace(Tree, res, neededSpace):
    if Tree.children == None or Tree.children == []:
        return
    for i in range(len(Tree.children)):
        node = Tree.children[i]
        if node.type == 'dir':
            if node.size >= neededSpace:
                res[0] = min(res[0], node.size)
        smallestDirToFreeUpEnoughSpace(Tree.children[i], res, neededSpace)

def makeSizeForTreeDirs(Tree):
    if Tree.size > 0:
        return Tree.size

    if Tree.children == None or Tree.children == []:
        return 0

    res = 0
    for i in range(len(Tree.children)):
        res += makeSizeForTreeDirs(Tree.children[i])
        if Tree.type == 'dir':
            Tree.size = res
    return res

def day7():
    # Create parser and initialize TreeNode
    filename = 'day-7.txt'
    Tree = FileNode('*')
    Tree.type = 'dir'
    Root = Tree
    parseInput(filename, Root)

    # Compute size for all Dirs
    makeSizeForTreeDirs(Root)

    # Get size sum of Dirs
    sumOfDirs = [0]
    getSumDirs(Root, sumOfDirs)
    yield sumOfDirs[0]

    # Get smallest Dirs needed to be deleted
    neededSpace = 30000000 - (70000000 -  Root.size)
    smallestDir = [float('inf')]
    smallestDirToFreeUpEnoughSpace(Root, smallestDir, neededSpace)
    yield smallestDir[0]

def main():
    for sol in day7():
        print(sol)

main()