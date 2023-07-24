##  Global Alignment with Scoring Matrix and Affine Gap Penalty 

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
with open("BLOSUM62.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrix = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrix[aa[i]+aa[j-1]] = int(m[i][j])

a,b =11,1

seq = readFastaFileList("test.txt")
gaff(seq[0], seq[1], scoreMatrix,a,b)
