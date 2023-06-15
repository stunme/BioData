##  Overlap Graphs
from utility import readFastaFileDict

def overlap(seqDic, k =3):
    result = []
    for k1, v1 in seqDic.items():
        for k2,v2 in seqDic.items():
            if v1[-k:] == v2[:k] and k1 != k2:
                result.append([k1, k2])
    return result

for i in overlap(readFastaFileDict("test.txt")):
    print(" ".join(j for j in i))
