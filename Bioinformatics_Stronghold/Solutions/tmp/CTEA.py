##  Counting Optimal Alignments

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

            
seq = readFastaFileList("test.txt")

print(ctea(seq[0], seq[1]))

