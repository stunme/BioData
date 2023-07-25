##  Genome Assembly Using Reads

def cyclic(dic):
    tmp = dic.popitem()
    cur = tmp[1]
    seq = cur[-1]
    for i in range(len(dic)):
        if cur not in dic:
            return ""
        seq += dic[cur][-1]
        if dic[cur] == tmp[0]:
            return seq
        cur = dic[cur]


def deBruijn(seqList):
    n = len(seqList[0])
    S = set([s.strip() for s in seqList])
    mapping = str.maketrans("ATGC","TACG")
    S |= set([s.translate(mapping)[::-1] for s in S])

    for k in range(n-1,0,-1):
        dic = {}
        for s in S:
            idx = n-k
            for i in range(idx):
                dic[s[i:i+k]] = s[i+1:i+k+1]
        tmp = cyclic(dic)
        if tmp != "":
            return tmp
    

with open("test.txt",'r') as f:
    seqList = [s.strip() for s in f.readlines()]
    

print(deBruijn(seqList))