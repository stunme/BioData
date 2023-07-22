##  Identifying Reversing Substitutions

import re

### parse input file
with open("test.txt",'r') as f:
    treeStr = f.readline().strip().replace(";","")
    taxas = {}
    cur = ""
    for i in f.readlines():
        i = i.strip()
        if ">" in i:
            cur = i.replace(">","")
            taxas[cur] = ""
        else:
            taxas[cur]+=i
    seqLen = len(taxas[cur])

## define node class
class node():
    def __init__(self, taxa) -> None:
        self.taxa = taxa
        self.child = None
        self.seq = ''


## build up the tree
tokens =re.split("([(),])",treeStr)
stack = [[]]
cur = None
for t in tokens:
    if t == '(':
        stack.append([])
    elif t == ')':
        cur = stack.pop()
    elif t not in ', ':
        root = node(t)
        root.seq = taxas[t]
        stack[-1].append(root)
        if cur:
            root.child = cur
            cur = None


