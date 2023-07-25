##  Edit Distance Alignment

"""
Problem
An alignment of two strings s
 and t
 is defined by two strings s′
 and t′
 satisfying the following three conditions: 1. s′
 and t′
 must be formed from adding gap symbols "-" to each of s
 and t
, respectively; as a result, s
 and t
 will form subsequences of s′
 and t′
. 2. s′
 and t′
 must have the same length. 3. Two gap symbols may not be aligned; that is, if s′[j]
 is a gap symbol, then t′[j]
 cannot be a gap symbol, and vice-versa.

We say that s′
 and t′
 augment s
 and t
. Writing s′
 directly over t′
 so that symbols are aligned provides us with a scenario for transforming s
 into t
. Mismatched symbols from s
 and t
 correspond to symbol substitutions; a gap symbol s′[j]
 aligned with a non-gap symbol t′[j]
 implies the insertion of this symbol into t
; a gap symbol t′[j]
 aligned with a non-gap symbol s′[j]
 implies the deletion of this symbol from s
.

Thus, an alignment represents a transformation of s
 into t
 via edit operations. We define the corresponding edit alignment score of s′
 and t′
 as dH(s′,t′)
 (Hamming distance is used because the gap symbol has been introduced for insertions and deletions). It follows that dE(s,t)=mins′,t′dH(s′,t′)
, where the minimum is taken over all alignments of s
 and t
. We call such a minimum score alignment an optimal alignment (with respect to edit distance).

Given: Two protein strings s
 and t
 in FASTA format (with each string having length at most 1000 aa).

Return: The edit distance dE(s,t)
 followed by two augmented strings s′
 and t′
 representing an optimal alignment of s
 and t
.

Sample Dataset
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN

Sample Output
4
PRETTY--
PR-TTEIN
"""

##  define function
from utility import readFastaFileList

def edta(seqI,seqJ):
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
                arr[i][j] = min(arr[i-1][j-1]+1,arr[i][j-1]+1,arr[i-1][j]+1)
 
    sI = ""
    sJ = ""
    while i*j!=0:
        if arr[i][j] == arr[i-1][j]+1:
            sI = seqI[i-1]+sI
            sJ = '-'+sJ
            i-=1
        elif arr[i][j] == arr[i][j-1]+1:
            sJ = seqJ[j-1]+sJ
            sI = '-'+sI
            j -= 1
        elif arr[i][j] == arr[i-1][j-1]+1:
            sI = seqI[i-1]+sI
            sJ = seqJ[j-1]+sJ
            i-=1
            j -= 1
        else:
            sI = seqI[i-1]+sI
            sJ = seqJ[j-1]+sJ
            i-=1
            j -= 1

    print(arr[lenI-1][lenJ-1])
    print("-"*i+sI)
    print("-"*j+sJ)
    return arr

##  import dataset
seq = readFastaFileList("../datasets/EDTA_dataset.txt")

##  process data, result print at the end of the function
edta(seq[0],seq[1])