##  Finding a Motif with Modifications

from utility import readFastaFileList
import time

def ksim(seqI, seqJ, k):
    k += 1
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    start = time.time()

    aligns = []

    cur = [j for j in range(lenJ)]
    curPos = [{j} for j in range(lenJ)]
    for i in range(1,lenI):
        pre = cur
        prePos = curPos
        cur = [0]+[k]*(lenJ-1)
        curPos = [{i}]
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                a = pre[j-1]
            else:
                a = pre[j-1] +1
            b = pre[j]+1
            c = cur[j-1]+1
            cur[j] = min(a,b,c)
            curPos.append(set())
            if cur[j]<k:
                if cur[j] == a:
                    curPos[j] |= prePos[j-1]
                if cur[j] == b:
                    curPos[j] |= prePos[j]
                if cur[j] == c:
                    curPos[j] |= curPos[j-1]
        if cur[j]<k:
            for m in curPos[j]:
                aligns.append([m+1,i-m])
    print(time.time()-start)

    return aligns


with open("test.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()

with open("result.txt",'w') as f:
    for i in ksim(genome,motif,k):
        f.write(' '.join(str(j) for j in i))
        f.write('\n')