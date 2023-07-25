##  Creating a Distance Matrix

from utility import readFastaFileList

def pdst(seqList):
    B = []
    length = len(seqList)
    for i in seqList:
        tmp = []
        for j in seqList:
            D = 0
            for x in range(len(i)):
                if i[x]!=j[x]:
                    D += 1
            tmp.append(round(D/len(i),4))
        B.append(tmp)
    return B



seq = readFastaFileList("test.txt")
for i in pdst(seq):
    print(" ".join(str(j) for j in i))
