##  Finding a Shared Spliced Motif

from utility import readFastaFileList

seq = readFastaFileList("test.txt")


def lcsq(seqI, seqJ):
    arr = []
    lenI,lenJ = len(seqI),len(seqJ)
    arr.append([0]*(lenJ+1))
    for i in range(lenI):
        arr.append([0]*(lenJ+1))
        for j in range(lenJ):
            if seqI[i] == seqJ[j]:
                arr[i+1][j+1] = arr[i][j]+1
            else:
                arr[i+1][j+1] = max(arr[i][j+1],arr[i+1][j])
                
    seq = ""
    i, j = lenI, lenJ
    while i*j != 0:
        if arr[i][j] == arr[i][j-1]:
            j -= 1
        elif arr[i][j] == arr[i-1][j]:
            i -= 1
        else:
            i -=1
            seq = seqI[i] + seq
            j -=1 
    
    return seq

print(lcsq(seq[0],seq[1]))