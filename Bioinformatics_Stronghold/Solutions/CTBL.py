##  Creating a Character Table

import re
def ctbl(treeStr):
    tokens = re.split('([(),])',treeStr)
    charTable = [['1']]
    stack = [[1]]
    curLeft = 1
    for t in tokens:
        if t == '(':
            stack += [[curLeft]]
        elif t not in ',()':
            stack[-1].append(t)
        elif t == ')':
            cur = stack.pop()
            left,cur = cur[0], cur[1:]
            for i in range(len(cur)):
                charTable += [['0']*len(charTable[-1])]
                charTable[-1][0] = cur[i]
            curLeft += len(cur)
            for i in range(left):
                charTable[i].append('0')
            for i in range(left,curLeft):
                charTable[i].append('1')
    charTable.sort()
    for i in charTable:
        i.pop()
    return charTable[1:]

with open("test.txt",'r') as f:
    treeStr = f.readline().strip().replace(";",'')

ctbl_ = ctbl(treeStr)


with open("result.txt",'w') as f:
    for i in range(1,len(ctbl_[0])):
        f.write("".join((j[i]) for j in ctbl_))
        f.write("\n")
