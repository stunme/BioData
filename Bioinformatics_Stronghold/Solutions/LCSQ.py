##  Finding a Shared Spliced Motif

"""
Problem
A string u
 is a common subsequence of strings s
 and t
 if the symbols of u
 appear in order as a subsequence of both s
 and t
. For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".

Analogously to the definition of longest common substring, u
 is a longest common subsequence of s
 and t
 if there does not exist a longer common subsequence of the two strings. Continuing our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".

Given: Two DNA strings s
 and t
 (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s
 and t
. (If more than one solution exists, you may return any one.)

Sample Dataset
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA

Sample Output
AACTGG
"""

##  define function
from utility import readFastaFileList

def lcsq(seqI, seqJ):
    arr = []
    lenI,lenJ = len(seqI),len(seqJ)
    arr.append([0]*(lenJ+1))
    for i in range(lenI):
        arr.append([0]*(lenJ+1))
        for j in range(lenJ):
            if seqI[i] == seqJ[j]:
                arr[i+1][j+1] = arr[i][j]+1
            else:
                arr[i+1][j+1] = max(arr[i][j+1],arr[i+1][j])
                
    seq = ""
    i, j = lenI, lenJ
    while i*j != 0:
        if arr[i][j] == arr[i][j-1]:
            j -= 1
        elif arr[i][j] == arr[i-1][j]:
            i -= 1
        else:
            i -=1
            seq = seqI[i] + seq
            j -=1 
    
    return seq

##  import dataset
seq = readFastaFileList("../datasets/LCSQ_dataset.txt")

##  print result
print(lcsq(seq[0],seq[1]))