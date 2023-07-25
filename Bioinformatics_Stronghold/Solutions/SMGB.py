##  Finding a Motif with Modifications

"""
Problem
A semiglobal alignment of strings s
 and t
 is an alignment in which any gaps appearing as prefixes or suffixes of s
 and t
 do not contribute to the alignment score.

Semiglobal alignment has sometimes also been called "overlap alignment". Rosalind defines overlap alignment differently (see “Overlap Alignment”).

Given: Two DNA strings s
 and t
 in FASTA format, each having length at most 10 kbp.

Return: The maximum semiglobal alignment score of s
 and t
, followed by an alignment of s
 and t
 achieving this maximum score. Use an alignment score in which matching symbols count +1, substitutions count -1, and there is a linear gap penalty of 1. If multiple optimal alignments exist, then you may return any one.

Sample Dataset
>Rosalind_79
CAGCACTTGGATTCTCGG
>Rosalind_98
CAGCGTGG

Sample Output
4
CAGCA-CTTGGATTCTCGG
---CAGCGTGG--------
"""

##  define functions
from utility import readFastaFileList

def smgb(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1

    tracker = []
    for i in range(lenI):
        tracker.append([0]*lenJ)
    cur = [0]*lenJ
    maxI = 0
    posi = i
    for i in range(1,lenI):
        pre = cur
        cur = [0]*lenJ
        for j in range(1,lenJ):
            j_ = j-1
            if seqI[i-1]==seqJ[j_]:
                cur[j] = pre[j_]+1
                tracker[i][j] = 0
            else:
                cur[j] = max(pre[j_],
                             pre[j],
                             cur[j_])
                if cur[j] == pre[j_]:
                    tracker[i][j] = 0
                elif cur[j] == pre[j]:
                    tracker[i][j] = 1
                elif cur[j] == cur[j_]:
                    tracker[i][j] = 2
                cur[j]-=1
        if cur[j]>=maxI:
            posi = i
            maxI = cur[j]

    posj = max(range(lenJ),key=lambda x:cur[x])
    maxJ = cur[j]

    if maxJ>maxI:
        maxIJ = maxJ
        i = lenI-1
        j = posj
    else:
        maxIJ = maxI
        i = posi
        j = lenJ-1
    
    alignI = seqI[i:]+'-'*(lenJ-j-1)
    alignJ = seqJ[j:]+'-'*(lenI-i-1)
        
    while i*j !=0:
        if seqI[i-1]==seqJ[j-1] or tracker[i][j]==0:
            i -=1
            j -=1
            alignI = seqI[i]+alignI
            alignJ = seqJ[j]+alignJ
        elif tracker[i][j]==1:
            i -=1
            alignI = seqI[i]+alignI
            alignJ = '-'+alignJ
        elif tracker[i][j]==2:
            j -=1
            alignI = '-'+alignI
            alignJ = seqJ[j]+alignJ
    
    alignI = seqI[:i]+'-'*j+alignI
    alignJ = seqJ[:j]+'-'*i+alignJ
    with open("result.txt",'w') as f:
        f.write(f"{maxIJ}\n")
    return [alignI,alignJ]


import time
start = time.time()

##  import dataset
seqList = readFastaFileList("../datasets/SMGB_dataset.txt")

##  write result to file
with open("result.txt",'a') as f:
    f.write("\n".join(i for i in smgb(seqList[0],seqList[1])))
print(time.time()-start)