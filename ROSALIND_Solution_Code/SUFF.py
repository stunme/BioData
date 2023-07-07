##  Encoding Suffix Trees


## merge every substring (n-1) to current tree. 
#   Space effiecnt can be improved by store list position instead save String,see LING.py

def suff(seq):
    class node(object):
        def __init__(self) -> None:
            self.child = {}
            self.seq = ""

    root = node()
    nodes = [root]

    for i in range(len(seq)):
        cur = root
        idx = 0
        for j in range(i,len(seq)):
            if idx == len(cur.seq):
                if seq[j] in cur.child:
                    cur = cur.child[seq[j]]
                    idx = 1
                else:
                    cur.child[seq[j]] = node()
                    cur.child[seq[j]].seq = seq[j:]
                    nodes.append(cur.child[seq[j]])
                    break
            else:
                if seq[j] == cur.seq[idx]:
                    idx += 1
                    continue
                else:
                    tmp = cur.child
                    tmpSeq = cur.seq
                    cur.seq = tmpSeq[:idx]
                    cur.child = {}
                    cur.child[seq[j]] = node()
                    cur.child[seq[j]].seq = seq[j:]
                    nodes.append(cur.child[seq[j]])
                    cur.child[tmpSeq[idx]] = node()
                    cur.child[tmpSeq[idx]].seq = tmpSeq[idx:]
                    cur.child[tmpSeq[idx]].child = tmp
                    nodes.append(cur.child[tmpSeq[idx]])
                    break
    return nodes

import time
start = time.time()

with open("test.txt","r") as f:
    seq = f.readline().strip()

nodes = suff(seq)

with open("result.txt","a") as f:
    for n in nodes:
        if n.seq == "":
            continue
        f.write(f"{n.seq}\n")

print(time.time()-start)        

    


## O(n^2) solution. 

start = time.time()

root = {}

## build up the tree
for i in range(len(seq)):
   cur = root
   for c in seq[i:]:
       if c not in cur:
           cur[c] = {}
       cur = cur[c]

## recursion for edges collection
edge = {} 
num = 1
def traceBack(node, seq, parent):
    global num
    if len(node) == 1:
        for i in node:
            traceBack(node[i],seq+i, parent)
    else:
        if seq:
            edge[(parent,num)]=seq
        cur = num
        for i in node:
            num+=1
            traceBack(node[i],i,cur)

## start recursion
traceBack(root,"",1)

with open("result.txt","a") as f:
    setB = []
    for n,e in edge.items():
        f.write(f"{e}\n")
        setB.append(e)

print(time.time()-start)


