##  Finding a Motif with Modifications

from utility import readFastaFileList

def ksim(seqI, seqJ, k):
    k += 1
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    aligns = set()
    cur = [j for j in range(lenJ)]
    curPos = [{j} for j in range(lenJ)]
    for i in range(1,lenI):
        pre = cur.copy()
        prePos = curPos
        curPos = [{i}]
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]
                curPos.append(prePos[j-1].copy())
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
        # if cur[j]<k:
        for m in curPos[j]:
            aligns.add((m+1,i-m))
            for n in range(1,k-cur[j]):
                aligns.add((m+1+n,i-m-n))
                aligns.add((max(1,m+1-n),i-m+n))
    return aligns

import time
start = time.time()
with open("test.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()
    
with open("result.txt",'w') as f:
    for i in ksim(genome,motif,k):
        f.write(' '.join(str(j) for j in i))
        f.write('\n')
print(time.time()-start)


#Use more time, but works for all sample


# 2x faster and works for k > 3
def ksim_(seqI, seqJ, k):
    k += 1
    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    aligns = []
    tracker = []
    for i in range(lenI):
        tracker.append([0]*lenJ)
    cur = [j for j in range(lenJ)]
    for i in range(1,lenI):
        pre = cur
        cur = [0]+[k]*(lenJ-1)
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]

            else:
                cur[j] = min(pre[j-1],
                                 pre[j],
                                 cur[j-1])
                if cur[j] == k:
                    continue
                if cur[j] == pre[j]:
                    tracker[i][j] = 1
                elif cur[j] == cur[j-1]:
                    tracker[i][j] = 2
                cur[j] +=1
        if cur[j]<k:
            aligns.append((i,cur[j]))
    result = set()
    for a,b in aligns:
        i = a
        j = lenJ-1
        while i*j !=0:
            if tracker[i][j] == 0:
                i -=1
                j -=1
            elif tracker[i][j] == 1:
                i -=1
            elif tracker[i][j] == 2:
                j -=1
        result.add((i+1,a-i))
        for m in range(1,k-b):
                result.add((i+1+m,a-i-m))
                result.add((max(1,i+1-m),a-i+m))
    return result


# with open("result.txt",'w') as f:
#     for i in ksim_(genome,motif,k):
#         f.write(' '.join(str(j) for j in i))
#         f.write('\n')
