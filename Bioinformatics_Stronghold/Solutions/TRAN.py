##  Transitions and Transversions

"""
Problem
For DNA strings s1
 and s2
 having the same length, their transition/transversion ratio R(s1,s2)
 is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1
 and s2
 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2)
.

Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

Sample Output
1.21428571429
"""

##  define function
from utility import readFastaFileList

def TnT(seqList):
    dic = {'A':'G',
           'G':'A',
           'T':'C',
           'C':'T',
    }
    transitions, transversions = 0,0

    for i in range(len(seqList[0])):
        if seqList[0][i] == seqList[1][i]:
            continue
        elif dic[seqList[0][i]] == seqList[1][i]:
            transitions += 1
        else:
            transversions += 1
    return transitions/transversions

##  import dataset
##  print output
print(TnT(readFastaFileList("../datasets/TRAN_dataset.txt")))