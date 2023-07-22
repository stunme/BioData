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
        self.parent = None
        self.seq = ''

## build up the tree, and fill up innerTaxa
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
            for c in root.child:
                c.parent = root
            cur = None

def rsub(cur_nd,pre_nd,n):
    if cur_nd.child:
        for c in cur_nd.child:
            if c.seq[n] == cur_nd.seq[n]:
                rsub(c,pre_nd,n)
            else:
                if c.seq[n] == pre_nd.parent.seq[n]:
                    with open("result.txt",'a') as f:
                        f.write(f"{pre_nd.taxa} {c.taxa} {n+1} {pre_nd.parent.seq[n]}->{cur_nd.seq[n]}->{c.seq[n]}\n")
                rsub(c,c,n)


with open("result.txt",'w') as f:
    f.write('')
for i in range(seqLen):
    for r in root.child:
        rsub(r,r,i)