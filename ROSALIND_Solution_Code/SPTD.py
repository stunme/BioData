##  Phylogeny Comparison with Split Distance

#copy code from CTBL.py, get complete charTable for each taxaString, and caulcuate beased on the equation provided.


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
    taxas = f.readline().strip().split()
    taxaTree1 = f.readline().strip().replace(";",'')
    taxaTree2 = f.readline().strip().replace(";",'')

ctbl1 = ctbl(taxaTree1)
ctbl2 = ctbl(taxaTree2)

set1 = set()
set2 = set()

with open("result.txt",'w') as f:
    for i in range(1,len(ctbl1[0])):
        set1.add("".join((j[i]) for j in ctbl1))
        set2.add("".join((j[i]) for j in ctbl2))

print(2*(len(taxas)-3)-2*len(set1&set2))
