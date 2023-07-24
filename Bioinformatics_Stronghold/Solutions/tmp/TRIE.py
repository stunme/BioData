## Introduction to Pattern Matching

with open("test.txt",'r') as f:
    seqList = [i.strip() for i in f.readlines()]

### save nodes in T

T = [0]
T.append({"A":False,"C":False,"G":False,"T":False})

for i in seqList:
    cur = 1
    for j in i:
        if not T[cur][j]:
            T.append({"A":False,"C":False,"G":False,"T":False})
            T[cur][j]=(cur,len(T)-1, j)
            cur = len(T)-1
            # turple here store the (parrent node, child node, edge char)
        else:
            cur = T[cur][j][1]

## sort adjacency by adding sequence

result = {}
for i in range(1,len(T)):
    for k, v in T[i].items():
        if v:
            result[v[1]] = v

with open("result.txt","w") as f:
    for i in range(2,len(T)):
        f.write(" ".join(str(j) for j in result[i]))
        f.write('\n')
