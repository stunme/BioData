##  Local Alignment with Affine Gap Penalty

from utility import readFastaFileList

def laff(seq1, seq2, scoreMatrix, a,b):
    lenI, lenJ = len(seq1)+1, len(seq2)+1
    arr = []
    arrI = []
    arrJ = []
    tracker = []
    for i in range(lenI):
        arr.append([0]*lenJ)
        arrI.append([0]*lenJ)
        arrJ.append([0]*lenJ)
        tracker.append([0]*lenJ)
    
    max_x, max_y = 0, 0
    # instead of full map of arrI and arrJ used in GAFF. here only use tmp array to save memory and time
    arrI = [0]*lenJ
    arrII = [0]*lenJ
    arrJ = [0]*lenJ

    for i in range(1, lenI):        
        for j in range(1, lenJ):
            tmp = [ arr[i-1][j-1] + scoreMatrix[seq1[i-1]+seq2[j-1]],
                    arrI[j]-a,
                    arrJ[j-1]-a,
                    0]
            max_tmp = max(tmp)
            arr[i][j] = max_tmp
            arrII[j] = max(arrI[j]-b,max_tmp)
            arrI[j] = arrII[j]
            arrJ[j] = max(arrJ[j-1]-b,max_tmp)
            tracker[i][j] = tmp.index(max_tmp)
            if arr[i][j]>arr[max_x][max_y]:
                max_x, max_y = i,j

    i, j = max_x, max_y
    
    while tracker[i][j] != 3 and i * j != 0:
        match tracker[i][j]:
            case 2:
                j-=1
            case 1:
                i-=1
            case 0:
                i-=1
                j-=1
        
    return arr[max_x][max_y], seq1[i:max_x], seq2[j:max_y]
    
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

import time
start = time.time()
result = laff(seq[0], seq[1], scoreMatrix, a,b)
with open("result.txt",'w') as f:
    f.write("\n".join(str(x) for x in result))

print(time.time()-start)


