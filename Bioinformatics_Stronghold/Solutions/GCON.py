##  Global Alignment with Constant Gap Penalty

"""
Problem
In a constant gap penalty, every gap receives some predetermined constant penalty, regardless of its length. Thus, the insertion or deletion of 1000 contiguous symbols is penalized equally to that of a single symbol.

Given: Two protein strings s
 and t
 in FASTA format (each of length at most 1000 aa).

Return: The maximum alignment score between s
 and t
. Use:

The BLOSUM62 scoring matrix.
Constant gap penalty equal to 5.

Sample Dataset
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

Sample Output
13
"""

## define functions
from utility import readFastaFileList
  
def gcon(seq1, seq2, scoreMatrix):
   gap= -5
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   arrI = []
   arrJ = []
   for i in range(lenI):
      arr.append([0]*lenJ)
      arrI.append([0]*lenJ)
      arrJ.append([0]*lenJ)
   for j in range(1, lenJ):
      arr[0][j] = gap
      arrI[0][j] = gap
      arrJ[0][j] = gap
   for i in range(1, lenI):
      arr[i][0] = gap
      arrI[i][0] = gap
      arrJ[i][0] = gap
      
   for i in range(1,lenI):
      for j in range(1, lenJ):
         arr[i][j] = max(arr[i-1][j-1]+scoreMatrix[seq1[i-1]+seq2[j-1]],
                         arrJ[i][j-1]+gap,
                         arrI[i-1][j]+gap
                         )
         arrJ[i][j] = max(arrJ[i][j-1],arr[i][j] )
         arrI[i][j] = max(arrI[i-1][j],arr[i][j] )
         
   return arr[lenI-1][lenJ-1]

## construct BLOSUM62 scoring dict
with open("../utility/BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrix = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrix[aa[i]+aa[j-1]] = int(m[i][j])

## import dataset
seq = readFastaFileList("../datasets/GCON_dataset.txt")

## print result
print(gcon(seq[0], seq[1], scoreMatrix))
