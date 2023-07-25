##  Global Alignment with Scoring Matrix and Affine Gap Penalty 

"""
Problem
An affine gap penalty is written as a+b⋅(L−1)
, where L
 is the length of the gap, a
 is a positive constant called the gap opening penalty, and b
 is a positive constant called the gap extension penalty.

We can view the gap opening penalty as charging for the first gap symbol, and the gap extension penalty as charging for each subsequent symbol added to the gap.

For example, if a=11
 and b=1
, then a gap of length 1 would be penalized by 11 (for an average cost of 11 per gap symbol), whereas a gap of length 100 would have a score of 110 (for an average cost of 1.10 per gap symbol).

Consider the strings "PRTEINS" and "PRTWPSEIN". If we use the BLOSUM62 scoring matrix and an affine gap penalty with a=11
 and b=1
, then we obtain the following optimal alignment.

 PRT---EINS
 |||   |||
 PRTWPSEIN-
Matched symbols contribute a total of 32 to the calculation of the alignment's score, and the gaps cost 13 and 11 respectively, yielding a total score of 8.

Given: Two protein strings s
 and t
 in FASTA format (each of length at most 100 aa).

Return: The maximum alignment score between s
 and t
, followed by two augmented strings s′
 and t′
 representing an optimal alignment of s
 and t
. Use:

The BLOSUM62 scoring matrix.
Gap opening penalty equal to 11.
Gap extension penalty equal to 1.

Sample Dataset
>Rosalind_49
PRTEINS
>Rosalind_47
PRTWPSEIN

Sample Output
8
PRT---EINS
PRTWPSEIN-
"""


## define functions
from utility import readFastaFileList

def gaff(seq1, seq2, scoreMatrix, a, b):
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   arrI = []
   arrJ = []
   for i in range(lenI):
      arr.append([0]*lenJ)
      arrI.append([0]*lenJ)
      arrJ.append([0]*lenJ)
   for j in range(1, lenJ):
      gap = -a-b*(j-1)
      arr[0][j] = gap
      arrI[0][j] = gap
      arrJ[0][j] = gap
   for i in range(1, lenI):
      gap = -a-b*(i-1)
      arr[i][0] = gap
      arrI[i][0] = gap
      arrJ[i][0] = gap

   for i in range(1,lenI):
      for j in range(1, lenJ):
         arr[i][j] = max(arr[i-1][j-1]+scoreMatrix[seq1[i-1]+seq2[j-1]],
                         arrJ[i][j-1]-a,
                         arrI[i-1][j]-a
                         )
         arrJ[i][j] = max(arrJ[i][j-1]-b,arr[i][j])
         arrI[i][j] = max(arrI[i-1][j]-b,arr[i][j])

   # trace back, fill up the gap first
   seqI = ""
   seqJ = ""
   while i*j != 0:
      if arr[i][j] == arrJ[i][j-1]-a:
         while True:
            j -= 1
            seqI = '-'+seqI
            seqJ = seq2[j]+seqJ
            if arrJ[i][j] != arrJ[i][j-1]-b:
               break
      elif arr[i][j] == arrI[i-1][j]-a:
          while True:
            i -= 1
            seqI = seq1[i]+seqI
            seqJ = '-'+seqJ
            if arrI[i][j] != arrI[i-1][j]-b:
               break
      else:
         i -= 1
         j -= 1
         seqI = seq1[i]+seqI
         seqJ = seq2[j]+seqJ

   ## fill up the N-term   
   seqI = '-'*j+seq1[:i]+seqI
   seqJ = '-'*i+seq2[:j]+seqJ

   ## Calculate and print the global score, should same to arr[lenI-1][lenJ-1]

   # sum = 0
   # shortGap = True
   # for i in range(len(seqI)):
   #    if seqI[i] == "-" or seqJ[i] == "-":
   #       if shortGap:
   #          sum -= a
   #          shortGap = False
   #       else:
   #          sum -=b
   #    else:
   #       sum += scoreMatrix[seqI[i]+seqJ[i]]
   #       shortGap = True
   
   # print(sum)

   print(arr[lenI-1][lenJ-1])
   print(seqI)
   print(seqJ)

   return arr[lenI-1][lenJ-1]

## construct BLOSUM62 scoring dict
with open("./utility/BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrix = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrix[aa[i]+aa[j-1]] = int(m[i][j])

a,b =11,1

## import dataset
seq = readFastaFileList("../datasets/GAFF_dataset.txt")

## print result
gaff(seq[0], seq[1], scoreMatrix,a,b)
