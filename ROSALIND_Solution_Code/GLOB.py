##  Global Alignment with Scoring Matrix

from utility import readFastaFileList

## construct BLOSUM62 scoring dict
with open("BLOSUM62.txt","r") as f:
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

seq = readFastaFileList("test.txt")
print(glob(seq[0], seq[1] BLOSUM62))
