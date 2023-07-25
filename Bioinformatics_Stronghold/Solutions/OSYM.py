##  Isolating Symbols in Alignments 

"""
Problem
Say that we have two strings s
 and t
 of respective lengths m
 and n
 and an alignment score. Let's define a matrix M
 corresponding to s
 and t
 by setting Mj,k
 equal to the maximum score of any alignment that aligns s[j]
 with t[k]
. So each entry in M
 can be equal to at most the maximum score of any alignment of s
 and t
.

Given: Two DNA strings s
 and t
 in FASTA format, each having length at most 1000 bp.

Return: The maximum alignment score of a global alignment of s
 and t
, followed by the sum of all elements of the matrix M
 corresponding to s
 and t
 that was defined above. Apply the mismatch score introduced in “Finding a Motif with Modifications”.

Sample Dataset
>Rosalind_35
ATAGATA
>Rosalind_5
ACAGGTA

Sample Output
3
-139
"""

##  define functions
from utility import readFastaFileList

def globalSUM(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    
    total = 0

    cur = [j for j in range(0,-lenJ,-1)]

    for i in range(1,lenI):
        pre = cur
        total += sum(cur[:-1])
        cur = [-i]+[0]*(lenJ-1)
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]+1
            else:
                cur[j] = max(pre[j-1],
                             pre[j],
                             cur[j-1])-1
    print(cur[j])
    return total


##  import dataset
I,J = readFastaFileList("../datasets/OSYM_dataset.txt")


##  process data and print result
total = 0
for i in I:
    for j in J:
        if i == j:
            total +=1
        else:
            total -=1

total += globalSUM(I,J) + globalSUM(I[::-1],J[::-1])

print(total)