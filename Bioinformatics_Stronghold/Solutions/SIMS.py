##  Finding a Motif with Modifications

from utility import readFastaFileList

def sims(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for j in range(1,lenJ):
        arr[0][j] = -1*j

    for i in range(1,lenI):
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j-1],
                                 arr[i-1][j],
                                 arr[i][j-1])-1

    maxI = arr[i][j]
    pos = i
    while i > 0:
        i -= 1
        if arr[i][j]>maxI:
           maxI = arr[i][j]
           pos = i 
    i = pos
    
    alignI = ""
    alignJ = ""
        
    while i*j !=0:
        if seqI[i-1]==seqJ[j-1] or arr[i][j]+1 == arr[i-1][j-1]:
            i -=1
            j -=1
            alignI = seqI[i]+alignI
            alignJ = seqJ[j]+alignJ
        elif arr[i][j]+1 == arr[i-1][j]:
            i -=1
            alignI = seqI[i]+alignI
            alignJ = '-'+alignJ
        elif arr[i][j]+1 == arr[i][j-1]:
            j -=1
            alignI = '-'+alignI
            alignJ = seqJ[j]+alignJ
    with open("result.txt",'w') as f:
        f.write(f"{maxI}\n")
    return [alignI,alignJ]


seqList = readFastaFileList("test.txt")
with open("result.txt",'a') as f:
    f.write("\n".join(i for i in sims(seqList[0],seqList[1])))