##  k-Mer Composition 
##  skip data validation

"""
Problem
For a fixed positive integer k
, order all possible k-mers taken from an underlying alphabet lexicographically.

Then the k-mer composition of a string s
 can be represented by an array A
 for which A[m]
 denotes the number of times that the m
th k-mer (with respect to the lexicographic order) appears in s
.

Given: A DNA string s
 in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s
.

Sample Dataset
>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG

Sample Output
4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1
"""

## define function
import itertools as it
from utility import readFastaFileList

def KMER(seq,k):
    dic = {}
    for i in it.product('ACGT',repeat=k):
        dic[''.join(j for j in i)] = 0
    for i in range(len(seq)-k+1):
        dic[seq[i:i+k]] += 1
    return dic


##  import dataset
seq = readFastaFileList("../datasets/KMER_dataset.txt")[0]

##  print result
print(" ".join(str(v) for k,v in KMER(seq,4).items()))