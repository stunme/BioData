##  Alignment-Based Phylogeny 

import re
import itertools as it

### parse input file
with open("test.txt",'r') as f:
    treeStr = f.readline().strip().replace(";","")
    outerTaxa = {}
    innerTaxa = {}
    cur = ""
    for i in f.readlines():
        i = i.strip()
        if ">" in i:
            cur = i.replace(">","")
            outerTaxa[cur] = ""
        else:
            outerTaxa[cur]+=i
    seqLen = len(outerTaxa[cur])

## define node class
class node():
    def __init__(self, taxa) -> None:
        self.taxa = taxa
        self.child = None

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
        stack[-1].append(root)
        if cur:
            root.child = cur
            innerTaxa[root.taxa]=''
            cur = None


## trace up to get the most common sequence, and trace down to get sequence for inner nodes
# use tracker to store the traceability
tracker = {}
def traceUp(nd,n):
    dic = {'A':[0,None],
           'C':[0,None],
           'G':[0,None],
           'T':[0,None],
           '-':[0,None]}
    if nd.child:
        left = traceUp(nd.child[0],n)
        right = traceUp(nd.child[1],n)
        maxdH = max(left[m] for m in left)[0] + max(right[m] for m in right)[0] + 3
        for k in dic:
            min = maxdH
            for a,b in it.product(left,right):
                tmp = left[a][0]+right[b][0]+(k!=a)+(k!=b) 
                if tmp<min:
                    min, dic[k] = tmp, [tmp,(a,b)]
    else:
        for k in dic:
            dic[k] = [int(k!=outerTaxa[nd.taxa][n]),None]
    if nd.taxa in innerTaxa:
        tracker[nd.taxa] = dic
    return dic 

def traceDown(nd,nt):
    if nd.child:
        innerTaxa[nd.taxa] += nt
        a, b = tracker[nd.taxa][nt][1]    
        traceDown(nd.child[0],a)
        traceDown(nd.child[1],b)

sum = 0
for i in range(seqLen):
    dic = traceUp(root,i)
    cur = min(dic,key=lambda x:dic[x])
    sum += dic[cur][0]
    traceDown(root,cur)

# output result
with open("result.txt",'w') as f:
    f.write(str(sum))
    f.write(''.join(f"\n>{k}\n{v}" for k,v in innerTaxa.items()))