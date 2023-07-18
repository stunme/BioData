##  Finding a Motif with Modifications

from utility import readFastaFileList

def smgb(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1

    tracker = []
    for i in range(lenI):
        tracker.append([0]*lenJ)
    cur = [0]*lenJ
    maxI = 0
    posi = i
    for i in range(1,lenI):
        pre = cur
        cur = [0]*lenJ
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]+1
                tracker[i][j] = 0
            else:
                cur[j] = max(pre[j-1],
                                 pre[j],
                                 cur[j-1])
                if cur[j] == pre[j-1]:
                    tracker[i][j] = 0
                elif cur[j] == pre[j]:
                    tracker[i][j] = 1
                elif cur[j] == cur[j-1]:
                    tracker[i][j] = 2
                cur[j]-=1
        if cur[j]>=maxI:
            maxI = cur[j]
            posi = i

    maxJ = maxI
    while j > 0:
        j -= 1
        if cur[j]>maxJ:
           maxJ = cur[j]
           posj = j 

    if maxJ>maxI:
        maxIJ = maxJ
        i = lenI-1
        j = posj
    else:
        maxIJ = maxI
        i = posi
        j = lenJ-1
        
    
    alignI = seqI[i:]+'-'*(lenJ-j-1)
    alignJ = seqJ[j:]+'-'*(lenI-i-1)
        
    while i*j !=0:
        if seqI[i-1]==seqJ[j-1] or tracker[i][j]==0:
            i -=1
            j -=1
            alignI = seqI[i]+alignI
            alignJ = seqJ[j]+alignJ
        elif tracker[i][j]==1:
            i -=1
            alignI = seqI[i]+alignI
            alignJ = '-'+alignJ
        elif tracker[i][j]==2:
            j -=1
            alignI = '-'+alignI
            alignJ = seqJ[j]+alignJ
    
    alignI = seqI[:i]+'-'*j+alignI
    alignJ = seqJ[:j]+'-'*i+alignJ
    with open("result.txt",'w') as f:
        f.write(f"{maxIJ}\n")
    return [alignI,alignJ]


seqList = readFastaFileList("test.txt")
with open("result.txt",'a') as f:
    f.write("\n".join(i for i in smgb(seqList[0],seqList[1])))