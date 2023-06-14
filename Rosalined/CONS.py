##  Consensus and Profile
##  skip data validation
from utility import readFastaFileList

def profile(seqList):
    result = []
    for i in range(len(seqList[0])):
        dic = { "A": 0,
                "C": 0,
                "G": 0,
                "T": 0,
                }
        for s in seqList:
            dic[s[i]] += 1
        result.append(dic)
    return result


tmp = profile(readFastaFileList("test.txt"))
print(''.join(max(i,key = i.get) for i in tmp))
for k,v in tmp[0].items():
    print(f"{k}: {' '.join(str(i[k]) for i in tmp)}")
