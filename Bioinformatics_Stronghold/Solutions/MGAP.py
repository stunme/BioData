##  Maximizing the Gap Symbols of an Optimal Alignment

"""
Problem
For the computation of an alignment score generalizing the edit alignment score, let m
 denote the score assigned to matched symbols, d
 denote the score assigned to mismatched non-gap symbols, and g
 denote the score assigned a symbol matched to a gap symbol '-' (i.e., g
 is a linear gap penalty).

Given: Two DNA strings s
 and t
 in FASTA format (each of length at most 5000 bp).

Return: The maximum number of gap symbols that can appear in any maximum score alignment of s
 and t
 with score parameters satisfying m>0
, d<0
, and g<0
.

Sample Dataset
>Rosalind_92
AACGTA
>Rosalind_47
ACACCTA

Sample Output
3
"""

## define functions
from utility import readFastaFileList

def mgap(seq1, seq2):
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   
   for i in range(lenI):
      arr.append([0]*lenJ)

   for i in range(1, lenI):
     for j in range(1, lenJ):
         if seq1[i-1] == seq2[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
         else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])

   return len(seq1)+len(seq2)- 2*arr[lenI-1][lenJ-1]

## import dataseet    
seq = readFastaFileList("../datasets/MGAP_dataset.txt")

## print result
print(mgap(seq[0], seq[1]))

