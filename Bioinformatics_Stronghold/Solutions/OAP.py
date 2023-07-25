##  Overlap Alignment


"""
Problem
An overlap alignment between two strings s
 and t
 is a local alignment of a suffix of s
 with a prefix of t
. An optimal overlap alignment will therefore maximize an alignment score over all such substrings of s
 and t
.

The term "overlap alignment" has also been used to describe what Rosalind defines as a semiglobal alignment. See “Semiglobal Alignment” for details.

Given: Two DNA strings s
 and t
 in FASTA format, each having length at most 10 kbp.

Return: The score of an optimal overlap alignment of s
 and t
, followed by an alignment of a suffix s′
 of s
 and a prefix t′
 of t
 achieving this optimal score. Use an alignment score in which matching symbols count +1, substitutions count -2, and there is a linear gap penalty of 2. If multiple optimal alignments exist, then you may return any one.

Sample Dataset
>Rosalind_54
CTAAGGGATTCCGGTAATTAGACAG
>Rosalind_45
ATAGACCATATGTCAGTGACTGTGTAA

Sample Output
1
ATTAGAC-AG
AT-AGACCAT
"""

##  define functions
from utility import readFastaFileList

def oap(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for j in range(1,lenJ):
        arr[0][j] = -2*j

    for i in range(1,lenI):
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j-1],
                                 arr[i-1][j],
                                 arr[i][j-1])-2

    maxJ = arr[i][j]
    pos = j
    while j > 0:
        j -= 1
        if arr[i][j]>maxJ:
           maxJ = arr[i][j]
           pos = j 
    j = pos

    alignI = ""
    alignJ = ""
        
    while i*j !=0:
        if seqI[i-1]==seqJ[j-1] or arr[i][j]+2 == arr[i-1][j-1]:
            i -=1
            j -=1
            alignI = seqI[i]+alignI
            alignJ = seqJ[j]+alignJ
        elif arr[i][j]+2 == arr[i-1][j]:
            i -=1
            alignI = seqI[i]+alignI
            alignJ = '-'+alignJ
        elif arr[i][j]+2 == arr[i][j-1]:
            j -=1
            alignI = '-'+alignI
            alignJ = seqJ[j]+alignJ
    with open("result.txt",'w') as f:
        f.write(f"{maxJ}\n")
    return [alignI,alignJ]

##  import dataset
seqList = readFastaFileList("../datasets/OAP_dataset.txt")

##  output result to file
with open("result.txt",'a') as f:
    f.write("\n".join(i for i in oap(seqList[0],seqList[1])))