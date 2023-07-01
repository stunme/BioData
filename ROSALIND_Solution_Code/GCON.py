##  Global Alignment with Constant Gap Penalty

from utility import readFastaFileList

## construct BLOSUM62 scoring dict
with open("BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
BLOSUM62 = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      BLOSUM62[aa[i]+aa[j-1]] = int(m[i][j])
  
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
         
   # trace back
   seqI = ""
   seqJ = ""
   while i*j != 0:
      if arr[i][j]-BLOSUM62[seq1[i-1]+seq2[j-1]] == arr[i-1][j-1]:
         i -= 1
         j -= 1
         seqI = seq1[i]+seqI
         seqJ = seq2[j]+seqJ
      elif arrJ[i][j] == arrJ[i][j-1]:
         j -= 1
         seqI = '-'+seqI
         seqJ = seq2[j]+seqJ
      elif arrI[i][j] == arrI[i-1][j]:
         i -= 1
         seqI = seq1[i]+seqI
         seqJ = '-'+seqJ
   
   print("-"*j+seqI)
   print("-"*i+seqJ)

   return arr[lenI-1][lenJ-1]

seq = readFastaFileList("test.txt")
print(gcon(seq[0], seq[1], BLOSUM62))
