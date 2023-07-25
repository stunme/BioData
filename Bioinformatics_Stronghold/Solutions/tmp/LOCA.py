##  Local Alignment with Scoring Matrix

from utility import readFastaFileList

def loca(seq1, seq2, scoreMatrixm, gap):
    lenI, lenJ = len(seq1)+1, len(seq2)+1
    arr = []
    tracker = []
    for i in range(lenI):
        arr.append([0]*lenJ)
        tracker.append([0]*lenJ)

    max_x, max_y = 0,0
    for i in range(1, lenI):
        for j in range(1, lenJ):
            tmp = [ arr[i-1][j-1] + scoreMatrixm[seq1[i-1]+seq2[j-1]],
                    arr[i-1][j] + gap,
                    arr[i][j-1] + gap,
                    0]
            arr[i][j] = max(tmp)
            tracker[i][j] = tmp.index(arr[i][j])
            if arr[max_x][max_y]<arr[i][j]:
                max_x, max_y = i,j

    i, j = max_x, max_y 
    while tracker[i][j] != 3 and i * j != 0:
        match tracker[i][j]:
            case 2:
                j -= 1
            case 1:
                i -= 1
            case 0:
                i -= 1
                j -= 1  
                
    return arr[max_x][max_y], seq1[i:max_x],seq2[j:max_y]
    

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
