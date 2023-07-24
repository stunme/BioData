##  Global Alignment with Constant Gap Penalty

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
with open("BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrix = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrix[aa[i]+aa[j-1]] = int(m[i][j])

seq = readFastaFileList("test.txt")
print(gcon(seq[0], seq[1], scoreMatrix))
