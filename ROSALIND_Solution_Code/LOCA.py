##  Local Alignment with Scoring Matrix

from utility import readFastaFileList

def loca(seq1, seq2, scoreMatrixm, gap):
    lenI, lenJ = len(seq1)+1, len(seq2)+1
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for i in range(1, lenI):
        for j in range(1, lenJ):
            arr[i][j] = max(arr[i-1][j-1] + scoreMatrixm[seq1[i-1]+seq2[j-1]],
                            arr[i-1][j] + gap,
                            arr[i][j-1] + gap,
                            0
                            )

    #trace back
    end = (i,j)
    for x in range(lenI):
        for y in range(lenJ):
            if arr[end[0]][end[1]]<arr[x][y]:
                end = (x,y)
               
    i, j = end[0],end[1]
    while i * j != 0:
        tmp = max(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])
        if arr[i-1][j] == tmp:
            i -= 1
        elif arr[i][j-1] == tmp:
            j -= 1
        else:
            i -= 1
            j -= 1

    return arr[end[0]][end[1]], seq1[:end[0]],seq2[:end[1]]
    

## construct BLOSUM62 scoring dict
with open("PAM250.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrixm = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrixm[aa[i]+aa[j-1]] = int(m[i][j])

gap = -5

seq = readFastaFileList("test.txt")

result = loca(seq[0],seq[1],scoreMatrixm,gap)
print("\n".join(str(i) for i in result))