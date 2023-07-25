##  Finding a Spliced Motif

"""
Problem
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s
 and t
 (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s
 in which the symbols of t
 appear as a subsequence of s
. If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample Output
3 8 10
"""

## define function
from utility import readFastaFileList

def splicedMotif(seq, motif):
    result = []
    cur = 0
    for n in motif:
        cur += seq[cur:].find(n)+1
        result.append(cur)
    return result

## import dataset
dataset = readFastaFileList("../datasets/SSEQ_dataset.txt")

## print output
print(" ".join(str(i) for i in splicedMotif(dataset[0],dataset[1])))
    
