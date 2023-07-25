##  Alignment-Based Phylogeny 

"""
Problem
Say that we have n
 taxa represented by strings s1,s2,…,sn
 with a multiple alignment inducing corresponding augmented strings s¯¯¯1,s¯¯¯2,…,s¯¯¯n
.

Recall that the number of single-symbol substitutions required to transform one string into another is the Hamming distance between the strings (see “Counting Point Mutations”). Say that we have a rooted binary tree T
 containing s¯¯¯1,s¯¯¯2,…,s¯¯¯n
 at its leaves and additional strings s¯¯¯n+1,s¯¯¯n+2,…,s¯¯¯2n−1
 at its internal nodes, including the root (the number of internal nodes is n−1
 by extension of “Counting Phylogenetic Ancestors”). Define dH(T)
 as the sum of dH(s¯¯¯i,s¯¯¯j)
 over all edges {s¯¯¯i,s¯¯¯j}
 in T
:

dH(T)=∑{s¯¯¯i,s¯¯¯j}∈E(T)dH(s¯¯¯i,s¯¯¯j)

Thus, our aim is to minimize dH(T)
.

Given: A rooted binary tree T
 on n
 (n≤500
) species, given in Newick format, followed by a multiple alignment of m
 (m≤n
) augmented DNA strings having the same length (at most 300 bp) corresponding to the species and given in FASTA format.

Return: The minimum possible value of dH(T)
, followed by a collection of DNA strings to be assigned to the internal nodes of T
 that will minimize dH(T)
 (multiple solutions will exist, but you need only output one).

Sample Dataset
(((ostrich,cat)rat,(duck,fly)mouse)dog,(elephant,pikachu)hamster)robot;
>ostrich
AC
>cat
CA
>duck
T-
>fly
GC
>elephant
-T
>pikachu
AA

Sample Output
8
>rat
AC
>mouse
TC
>dog
AC
>hamster
AT
>robot
AC
"""


import re
import itertools as it

### parse input file
with open("../datasets/ALPH_dataset.txt",'r') as f:
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