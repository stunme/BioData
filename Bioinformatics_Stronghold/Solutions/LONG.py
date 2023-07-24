##  Genome Assembly as Shortest Superstring

from utility import readFastaFileList

def long(seqList):
    n = len(seqList)
    L = len(seqList[0])
    l = int(L/2+1)

    dic = {}
    pathTree = {}
    leftSet = set([])
    for i in range(n):
        j = 0
        while j<n:
            if i == j:
                j += 1
                continue
            for k in range(L-1,l-1,-1):
                if seqList[j][:k] == seqList[i][-k:]:
                    dic[(i,j)] = -k
                    leftSet.add(i)
                    pathTree[j] = i
                    j = n
                    break
            j += 1
                    #   'i' is the left sequence
                    #   'j' is the right sequence 
                    ##  assume only a unique way to reconstruct
                    #   stop search other right sequence once left/right match found
    for i in range(n):
        if i not in leftSet:
            break
    seq = seqList[i]
    for j in range(n-1):
        left = pathTree[i]
        seq = seqList[left][:dic[(pathTree[i],i)]]+seq
        i = left   
    return seq

def long2(seqList):
    n = len(seqList)
    

    dic = {}
    pathTree = {}
    leftSet = set([])
    for i in range(n):
        L = len(seqList[i])
        l = int(L/2)-1
        for j in range(n):
            if i == j:
                continue

            align = [0]*(L+1)

            # if seqList[i][0] == seqList[j][0]:
            #     align[0] = 1
            # else:
            #     align[0] = 0
            for x in range(1,L+1):
                y = align[x-1]
                while y>0 and seqList[i][x-1] != seqList[j][y]:
                    y = align[y-1]
                # print(len(seqList[i]),x-1,L)
                if seqList[i][x-1] == seqList[j][y]:
                    y += 1
                align[x] = y
            # if j ==12 and i ==1:
            #     print(" ".join([str(m) for m in align]))
            #     print(" ".join([m for m in seqList[i]]))
            #     print(" ".join([m for m in seqList[j]]))
                # print(i,j, align)
            if align[-1]>l:
                dic[(i,j)] = -align[-1]
                leftSet.add(i)
                pathTree[j] = i
                break
                    #   'i' is the left sequence
                    #   'j' is the right sequence 
                    ##  assume only a unique way to reconstruct
                    #   stop search other right sequence once left/right match found
    # for i in pathTree:
    #     print(i, pathTree[i])
    
    # print(leftSet)
    for i in range(n):
        if i not in leftSet:
            break
    seq = seqList[i]
    for j in range(n-1):
        tmp = pathTree[i]
        seq = seqList[tmp][:dic[(pathTree[i],i)]]+seq
        i = tmp   
    return seq


import time

start = time.time()
long(readFastaFileList("test.txt"))
print(time.time()-start) 


start = time.time()
long2(readFastaFileList("test.txt"))
print(time.time()-start)
# with open("result.txt","w") as f:
#     f.write(long(readFastaFileList("test.txt")))

