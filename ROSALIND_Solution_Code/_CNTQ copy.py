##  Counting Quartets

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
    n = int(f.readline().strip())
    taxaList = f.readline().strip().replace(";",'')

charTable = ctbl(taxaList)





import itertools as it

def qrt(seq):
    charOn = [i for i in range(len(seq)) if seq[i]=="1"]
    charOff = [i for i in range(len(seq)) if seq[i]=="0"]
    for x in it.combinations(charOn,2):
        for y in it.combinations(charOff,2):
            yield x,y

qrtSet = set()
count = 0

for i in range(1,len(charTable[0])):
        for x,y in qrt("".join((j[i]) for j in charTable)):
            if (x,y) not in qrtSet and (y,x) not in qrtSet:
                qrtSet.add((x,y))
                count+=1
                if count==10**6:
                    count = 0

print(count)