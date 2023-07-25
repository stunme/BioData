##  Finding a Motif with Modifications

"""
Problem

Figure 1. Global, local, and fitting alignments of strings v = GTAGGCTTAAGGTTA and w = TAGATA with respect to mismatch score. Note that in the fitting alignment, a substring of v must be aligned against all of w. Taken from Jones & Pevzner, An Introduction to Bioinformatics Algorithms
Given a string s
 and a motif t
, an alignment of a substring of s
 against all of t
 is called a fitting alignment. Our aim is to find a substring s′
 of s
 that maximizes an alignment score with respect to t
.

Note that more than one such substring of s
 may exist, depending on the particular strings and alignment score used. One candidate for scoring function is the one derived from edit distance; In this problem, we will consider a slightly different alignment score, in which all matched symbols count as +1 and all mismatched symbols (including insertions and deletions) receive a cost of -1. Let's call this scoring function the mismatch score. See Figure 1 for a comparison of global, local, and fitting alignments with respect to mismatch score.

Given: Two DNA strings s
 and t
, where s
 has length at most 10 kbp and t
 represents a motif of length at most 1 kbp.

Return: An optimal fitting alignment score with respect to the mismatch score defined above, followed by an optimal fitting alignment of a substring of s
 against t
. If multiple such alignments exist, then you may output any one.

Sample Dataset
>Rosalind_54
GCAAACCATAAGCCCTACGTGCCGCCTGTTTAAACTCGCGAACTGAATCTTCTGCTTCACGGTGAAAGTACCACAATGGTATCACACCCCAAGGAAAC
>Rosalind_46
GCCGTCAGGCTGGTGTCCG

Sample Output
5
ACCATAAGCCCTACGTG-CCG
GCCGTCAGGC-TG-GTGTCCG
"""

##  define functions
from utility import readFastaFileList

def sims(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for j in range(1,lenJ):
        arr[0][j] = -1*j

    for i in range(1,lenI):
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j-1],
                                 arr[i-1][j],
                                 arr[i][j-1])-1

    maxI = arr[i][j]
    pos = i
    while i > 0:
        i -= 1
        if arr[i][j]>maxI:
           maxI = arr[i][j]
           pos = i 
    i = pos
    
    alignI = ""
    alignJ = ""
        
    while i*j !=0:
        if seqI[i-1]==seqJ[j-1] or arr[i][j]+1 == arr[i-1][j-1]:
            i -=1
            j -=1
            alignI = seqI[i]+alignI
            alignJ = seqJ[j]+alignJ
        elif arr[i][j]+1 == arr[i-1][j]:
            i -=1
            alignI = seqI[i]+alignI
            alignJ = '-'+alignJ
        elif arr[i][j]+1 == arr[i][j-1]:
            j -=1
            alignI = '-'+alignI
            alignJ = seqJ[j]+alignJ
    with open("result.txt",'w') as f:
        f.write(f"{maxI}\n")
    return [alignI,alignJ]

##  import dataset
seqList = readFastaFileList("../datasets/SIMS_dataset.txt")

##  write output to file
with open("result.txt",'a') as f:
    f.write("\n".join(i for i in sims(seqList[0],seqList[1])))