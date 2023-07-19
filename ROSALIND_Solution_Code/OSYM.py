##  Isolating Symbols in Alignments 

from utility import readFastaFileList

def globalSUM(seqI, seqJ):

    lenI = len(seqI)+1
    lenJ = len(seqJ)+1
    
    total = 0

    cur = [j for j in range(0,-lenJ,-1)]

    for i in range(1,lenI):
        pre = cur
        total += sum(cur[:-1])
        cur = [-i]+[0]*(lenJ-1)
        for j in range(1,lenJ):
            if seqI[i-1]==seqJ[j-1]:
                cur[j] = pre[j-1]+1
            else:
                cur[j] = max(pre[j-1],
                             pre[j],
                             cur[j-1])-1
    print(cur[j])
    return total
    
I,J = readFastaFileList("test.txt")

total = 0
for i in I:
    for j in J:
        if i == j:
            total +=1
        else:
            total -=1

total += globalSUM(I,J) + globalSUM(I[::-1],J[::-1])
print(total)