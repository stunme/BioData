##  Identifying Reversing Substitutions

"""
Problem
For a rooted tree T
 whose internal nodes are labeled with genetic strings, our goal is to identify reversing substitutions in T
. Assuming that all the strings of T
 have the same length, a reversing substitution is defined formally as two parent-child string pairs (s,t)
 and (v,w)
 along with a position index i
, where:

there is a path in T
 from s
 down to w
;
s[i]=w[i]≠v[i]=t[i]
; and
if u
 is on the path connecting t
 to v
, then t[i]=u[i]
.
In other words, the third condition demands that a reversing substitution must be contiguous: no other substitutions can appear between the initial and reversing substitution.

Given: A rooted binary tree T
 with labeled nodes in Newick format, followed by a collection of at most 100 DNA strings in FASTA format whose labels correspond to the labels of T
. We will assume that the DNA strings have the same length, which does not exceed 400 bp).

Return: A list of all reversing substitutions in T
 (in any order), with each substitution encoded by the following three items:

the name of the species in which the symbol is first changed, followed by the name of the species in which it changes back to its original state
the position in the string at which the reversing substitution occurs; and
the reversing substitution in the form original_symbol->substituted_symbol->reverted_symbol.
Sample Dataset
(((ostrich,cat)rat,mouse)dog,elephant)robot;
>robot
AATTG
>dog
GGGCA
>mouse
AAGAC
>rat
GTTGT
>cat
GAGGC
>ostrich
GTGTC
>elephant
AATTC

Sample Output
dog mouse 1 A->G->A
dog mouse 2 A->G->A
rat ostrich 3 G->T->G
rat cat 3 G->T->G
dog rat 3 T->G->T
"""

import re

### parse input file
with open("../datasets/RSUB_dataset.txt",'r') as f:
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


##  write result to file
with open("result.txt",'w') as f:
    f.write('')
for i in range(seqLen):
    for r in root.child:
        rsub(r,r,i)