from utility import readFastaFileList

def edit(seqI,seqJ):
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


    return arr[lenI-1][lenJ-1]


seq = readFastaFileList("test.txt")
print(edit(seq[0],seq[1]))