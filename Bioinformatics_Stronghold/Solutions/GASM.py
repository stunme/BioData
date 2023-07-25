##  Genome Assembly Using Reads

"""
Problem
A directed cycle is simply a cycle in a directed graph in which the head of one edge is equal to the tail of the next (so that every edge in the cycle is traversed in the same direction).

For a set of DNA strings S
 and a positive integer k
, let Sk
 denote the collection of all possible k
-mers of the strings in S
.

Given: A collection S
 of (error-free) reads of equal length (not exceeding 50 bp). In this dataset, for some positive integer k
, the de Bruijn graph Bk
 on Sk+1∪Srck+1
 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its reverse complement.

Sample Dataset
AATCT
TGTAA
GATTA
ACAGA

Sample Output
GATTACA
"""

##  define functions
def cyclic(dic):
    tmp = dic.popitem()
    cur = tmp[1]
    seq = cur[-1]
    for i in range(len(dic)):
        if cur not in dic:
            return ""
        seq += dic[cur][-1]
        if dic[cur] == tmp[0]:
            return seq
        cur = dic[cur]


def deBruijn(seqList):
    n = len(seqList[0])
    S = set([s.strip() for s in seqList])
    mapping = str.maketrans("ATGC","TACG")
    S |= set([s.translate(mapping)[::-1] for s in S])

    for k in range(n-1,0,-1):
        dic = {}
        for s in S:
            idx = n-k
            for i in range(idx):
                dic[s[i:i+k]] = s[i+1:i+k+1]
        tmp = cyclic(dic)
        if tmp != "":
            return tmp
    
##  import dataset
with open("../datasets/GASM_dataset.txt",'r') as f:
    seqList = [s.strip() for s in f.readlines()]
    
##  print result
print(deBruijn(seqList))