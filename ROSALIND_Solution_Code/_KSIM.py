##  Finding a Motif with Modifications

from utility import readFastaFileList
import time

def ksim(seqI, seqJ, k):
    k += 1

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    start = time.time()

    aligns = []

    tracker = []
    for i in range(lenI):
        tracker.append([0]*lenJ)
    cur = [j for j in range(lenJ)]
    # with open("result.txt",'a') as f:
    #         f.write('\t'.join(str(m) for m in cur))
    #         f.write('\n')
    # print
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
                # if cur[j] == k:
                #     continue
                if cur[j] == pre[j-1]:
                    tracker[i][j] = 0
                elif cur[j] == pre[j]:
                    tracker[i][j] = 1
                elif cur[j] == cur[j-1]:
                    tracker[i][j] = 2
                cur[j] +=1
        # with open("result.txt",'a') as f:
        #     f.write('\t'.join(str(m) for m in cur))
        #     f.write('\n')
            # f.write(f"{i} lines, stop at {j}/{lenJ-1}\n")
        if cur[j]<k:
            aligns.append(i)
    # with open("result.txt",'w') as f:
    #     for m in arr:
    #         f.write('\t'.join(str(n) for n in m))
    #         f.write('\n')
    print(time.time()-start)
    # time.sleep(10000)
    start = time.time()
    print(len(aligns),aligns)

    result = []
    for a in aligns:
        i = a
        j = lenJ-1
        while i*j !=0:
            if seqI[i-1]==seqJ[j-1] or arr[i][j]-1 == arr[i-1][j-1]:
                i -=1
                j -=1
            elif arr[i][j]-1 == arr[i-1][j]:
                i -=1
            elif arr[i][j]-1 == arr[i][j-1]:
                j -=1
        result.append([i+1,a-i])

        # print(result[-1])
       

    # with open("result.txt",'w') as f:
    #     f.write(f"{minIJ}\n")
    # print(f"{minIJ}")
    print(time.time()-start)
    return result


with open("test.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()
# sims(genome,motif,k)
with open("result.txt",'w') as f:
    for i in ksim(genome,motif,k):
        f.write(' '.join(str(j) for j in i))
        f.write('\n')