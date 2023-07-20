##  Finding a Motif with Modifications

from utility import readFastaFileList

def ksim(seqI, seqJ, k):
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
    result = []
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
        result.append([i+1,a-i])
        for m in range(1,k-b):
                result.append([i+1+m,a-i-m])
                result.append([i+1-m,a-i+m])
    return result

with open("test.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()
with open("result.txt",'w') as f:
    for i in ksim(genome,motif,k):
        f.write(' '.join(str(j) for j in i))
        f.write('\n')

