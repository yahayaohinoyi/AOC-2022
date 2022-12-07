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
            if '$' in line or line[0] == '$':
                CMD = line[2:4]
                ARG = line[5:]
                # print(CMD, ARG)
                if CMD == 'cd':
                    if '..' in ARG:
                        runner = runner.parent
                    elif '/' in ARG:
                        line = f.readline()
                        continue
                    else:
                        for node in runner.children:
                            if node.val == ARG.strip(' '):
                                runner = node
                                break

                elif CMD == 'ls':
                    line = f.readline()
                    while '$' not in line:
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
                        if len(line) <= 1:
                            break
                    continue
            else:
                assert(False, "CODEPATH shouldn't be hit")
            
            line = f.readline()

def getSumDirs(Tree, res = [0]):
    if Tree.children == None or Tree.children == []:
        return
    for i in range(len(Tree.children)):
        size = Tree.children[i].size
        if Tree.children[i].type == 'dir' and size < 100000:
            res[0] += size
        getSumDirs(Tree.children[i], res)

def makeSizeForTreeDirs(Tree):
    if Tree.type == 'file':
        return Tree.size
    if Tree.children == None or Tree.children == []:
        return 0

    res = 0
    for i in range(len(Tree.children)):
        res += makeSizeForTreeDirs(Tree.children[i])
        if Tree.type == 'dir':
            Tree.size = res
    return 0

def main():
    filename = 'day-7.txt'
    Tree = FileNode('*')
    Root = Tree
    parseInput(filename, Tree)
    makeSizeForTreeDirs(Root)
    res = [0]
    getSumDirs(Root, res)
    # print(res)

main()