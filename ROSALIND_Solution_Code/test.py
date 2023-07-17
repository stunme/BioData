import itertools as it

with open("result.txt",'r') as f:
    seqList = [[]]
    for l in f.readlines():
        if "=" not in l:
            seqList[-1].append(l.strip())
        else:
            seqList.append([])

for sl in seqList:

    count = 0
    for a,b in it.combinations(sl[-2:],2):
        for x,y in zip(a,b):
            if x!=y:
                count -= 1
    print(count)