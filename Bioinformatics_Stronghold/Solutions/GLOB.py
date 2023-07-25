##  Global Alignment with Scoring Matrix

"""
Problem
To penalize symbol substitutions differently depending on which two symbols are involved in the substitution, we obtain a scoring matrix S
 in which Si,j
 represents the (negative) score assigned to a substitution of the i
th symbol of our alphabet A
 with the j
th symbol of A
.

A gap penalty is the component deducted from alignment score due to the presence of a gap. A gap penalty may be a function of the length of the gap; for example, a linear gap penalty is a constant g
 such that each inserted or deleted symbol is charged g
; as a result, the cost of a gap of length L
 is equal to gL
.

Given: Two protein strings s
 and t
 in FASTA format (each of length at most 1000 aa).

Return: The maximum alignment score between s
 and t
. Use:

The BLOSUM62 scoring matrix.
Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for each gap symbol).
Sample Dataset
>Rosalind_67
PLEASANTLY
>Rosalind_17
MEANLY

Sample Output
8
"""


from utility import readFastaFileList

## construct BLOSUM62 scoring dict
with open("../utility/BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
BLOSUM62 = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      BLOSUM62[aa[i]+aa[j-1]] = int(m[i][j])
  
def glob(seq1, seq2, scoreMatrix):
   gap= -5
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   for i in range(lenI):
      arr.append([0]*lenJ)
   for j in range(1, lenJ):
      arr[0][j] = gap*j
   for i in range(1, lenI):
      arr[i][0] = gap*i

   for i in range(1,lenI):
      for j in range(1, lenJ):
         arr[i][j] = max(
                           arr[i][j-1]+gap,
                           arr[i-1][j]+gap,
                           arr[i-1][j-1]+scoreMatrix[seq1[i-1]+seq2[j-1]]
               )
            
   return arr[i][j]

## import dataset
seq = readFastaFileList("../datasets/GLOB_dataset.txt")

## print result
print(glob(seq[0], seq[1],BLOSUM62))
