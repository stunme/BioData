##  Maximizing the Gap Symbols of an Optimal Alignment

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
            
seq = readFastaFileList("test.txt")

print(mgap(seq[0], seq[1]))

