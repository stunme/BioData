##  Finding a Motif with Modifications

from utility import readFastaFileList
import time

def ksim(seqI, seqJ, k):
    k += 1

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    start = time.time()

    aligns = []

    cur = [j for j in range(lenJ)]
    curPos = [j for j in range(lenJ)]
    for i in range(1,lenI):
        pre = cur
        prePos = curPos
        cur = [0]+[k]*(lenJ-1)
        curPos = [i]+[0]*(lenJ-1)
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]
                curPos[j] = prePos[j-1]
            else:
                tmp = {pre[j-1]:prePos[j-1],pre[j]:prePos[j],cur[j-1]:curPos[j-1]}
                cur[j] = min(tmp)
                if cur[j]==k and curPos[j]>curPos[j-1]:
                    print(j)
                    break
                curPos[j] = tmp[cur[j]]
                cur[j] +=1
        # with open("result_1.txt",'a') as f:
        #     f.write("\t".join(str(m) for m in cur))
        #     f.write("\n")
        if cur[j]<k:
            aligns.append([curPos[j]+1,i-curPos[j]])
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