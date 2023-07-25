from utility import readFastaFileList

"""
Problem
Given two strings s
 and t
 (of possibly different lengths), the edit distance dE(s,t)
 is the minimum number of edit operations needed to transform s
 into t
, where an edit operation is defined as the substitution, insertion, or deletion of a single symbol.

The latter two operations incorporate the case in which a contiguous interval is inserted into or deleted from a string; such an interval is called a gap. For the purposes of this problem, the insertion or deletion of a gap of length k
 still counts as k
 distinct edit operations.

Given: Two protein strings s
 and t
 in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t)
.

Sample Dataset
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY

Sample Output
5
"""

##  define function
def edit(seqI,seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for i in range(1,lenI):
        arr[i][0] = i
    for j in range(1,lenJ):
        arr[0][j] = j

    for i in range(1,lenI):
        for j in range(1, lenJ):
            if seqI[i-1] == seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j-1],arr[i][j-1],arr[i-1][j])+1


    return arr[lenI-1][lenJ-1]

##  import dataset
seq = readFastaFileList("../datasets/EDIT_dataset.txt")

##  print result
print(edit(seq[0],seq[1]))