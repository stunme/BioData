##  Counting Optimal Alignments

"""
Problem
Recall from “Edit Distance Alignment” that if s′
 and t′
 are the augmented strings corresponding to an alignment of strings s
 and t
, then the edit alignment score of s′
 and t′
 was given by the Hamming distance dH(s′,t′)
 (because s′
 and t′
 have the same length and already include gap symbols to denote insertions/deletions).

As a result, we obtain dE(s,t)=mins′,t′dH(s′,t′)
, where the minimum is taken over all alignments of s
 and t
. Strings s′
 and t′
 achieving this minimum correspond to an optimal alignment with respect to edit alignment score.

Given: Two protein strings s
 and t
 in FASTA format, each of length at most 1000 aa.

Return: The total number of optimal alignments of s
 and t
 with respect to edit alignment score, modulo 134,217,727 (227-1).

Sample Dataset
>Rosalind_78
PLEASANTLY
>Rosalind_33
MEANLY

Sample Output
4
"""

## define function
from utility import readFastaFileList

def ctea(seq1, seq2):
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   
   for i in range(lenI):
      arr.append([0]*lenJ)

   for j in range(1, lenJ):
      arr[0][j] = j
   for i in range(1, lenI):
      arr[i][0] = i

   for i in range(1, lenI):
     for j in range(1, lenJ):
         if seq1[i-1] == seq2[j-1]:
            arr[i][j] = arr[i-1][j-1]
         else:
            arr[i][j] = min(arr[i-1][j-1],
                            arr[i-1][j],
                            arr[i][j-1]
                              )+1
    ##  trace back all potential route, but record sum of sub-routes
   traceDic = {}
   
   def traceDown(i,j):
      if (i,j) not in traceDic:
         if i*j == 0:
            traceDic[(i,j)] = 1
         else:
            traceDic[(i,j)] = 0
            if seq1[i-1] == seq2[j-1] or arr[i][j] == arr[i-1][j-1]+1:
               traceDic[(i,j)]+=traceDown(i-1,j-1)
            if arr[i][j] == arr[i-1][j]+1:
               traceDic[(i,j)]+=traceDown(i-1,j)
            if arr[i][j] == arr[i][j-1]+1:
               traceDic[(i,j)]+=traceDown(i,j-1)
            traceDic[(i,j)] %= 134217727
      return traceDic[(i,j)]
   
   return traceDown(i,j)


## import dataset           
seq = readFastaFileList("../datasets/CTEA_dataset.txt")

## print result
print(ctea(seq[0], seq[1]))

