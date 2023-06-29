##  Edit Distance Alignment

from utility import readFastaFileList

def edta(seqI,seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for i in range(1,lenI):
        arr[i][0] = i
    for j in range(1,lenJ):
        arr[0][j] = j

    for i in range(1,lenI):
        for j in range(1, lenJ):
            if seqI[i-1] == seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j-1]+1,arr[i][j-1]+1,arr[i-1][j]+1)
 
    sI = ""
    sJ = ""
    while i*j!=0:
        if arr[i][j] == arr[i-1][j]+1:
            sI = seqI[i-1]+sI
            sJ = '-'+sJ
            i-=1
        elif arr[i][j] == arr[i][j-1]+1:
            sJ = seqJ[j-1]+sJ
            sI = '-'+sI
            j -= 1
        elif arr[i][j] == arr[i-1][j-1]+1:
            sI = seqI[i-1]+sI
            sJ = seqJ[j-1]+sJ
            i-=1
            j -= 1
        else:
            sI = seqI[i-1]+sI
            sJ = seqJ[j-1]+sJ
            i-=1
            j -= 1

    print(arr[lenI-1][lenJ-1])
    print("-"*i+sI)
    print("-"*j+sJ)
    return arr

seq = readFastaFileList("test.txt")
edta(seq[0],seq[1])