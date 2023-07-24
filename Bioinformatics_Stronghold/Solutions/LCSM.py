##  Finding a Shared Motif

"""
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k
 (k≤100
) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
"""

## define function 
from utility import readFastaFileList

def sharedMotif(seqList):
    seqList = sorted(seqList,key = len)
    for l in range(len(seqList[0]),1,-1):
        ## start from the shortest seq of seqList
        ## check seq with length (l)
        for pos in range(len(seqList[0])-l+1):
            ## starting postion of seq with length(l) in the shortest seq of seqList
            findIt = True
            tmp = seqList[0][pos:pos+l]

            for i in seqList[1:]:
                if i.find(tmp) == -1:
                    findIt = False
                    break
            if findIt:
                return tmp
            
##  input dataset
##  print output
print(sharedMotif(readFastaFileList("../datasets/LCSM_dataset.txt")))
