##  Fixing an Inconsistent Character Set

import itertools as it

def cset(charTableList):
    ct = charTableList[:]
    conflit = set()
    ctSet = {}
    for i in range(len(ct)):
        ctSet[i] = [set(),set()]
        for x in range(len(ct[i])):
            if ct[i][x] == "0":
                ctSet[i][0].add(x)
            else:
                ctSet[i][1].add(x)
    
    for i, j in it.combinations(range(len(ct)),2):
        flag = True
        for x,y in it.product(ctSet[i],ctSet[j]):
            if len(x&y) ==0:
                flag = False
                break
        if flag:
            if i in conflit:
                del ct[i]
                return ct
            if j in conflit:
                del ct[j]
                return ct
            conflit.add(i)
            conflit.add(j)
    del ct[conflit.pop()]
    return ct


with open("test.txt",'r') as f:
    charTableList = [i.strip() for i in f.readlines()]

with open("result.txt",'w') as f:
    f.write("\n".join(cset(charTableList)))



## Compact solution from Rosalind. Slightly slower. 

# import itertools
# from collections import Counter

# def CSET(charTableList):
#     # characters = filter(None,data.splitlines())
#     inconsistent_set = Counter()
#     for A,B in itertools.combinations(charTableList,2):
#         if len(Counter(zip(A,B))) > 3:
#             inconsistent_set[A] += 1
#             inconsistent_set[B] += 1
#     X = inconsistent_set.most_common(1)[0][0]
#     assert 2 * inconsistent_set[X] == sum(inconsistent_set.values())    # X should present in all pairs of inconsistent set
#     with open("result.txt",'w') as f:
#         for C in charTableList:
#             if C != X:
#                 f.write(f"{C}\n")

# with open("test.txt",'r') as f:
#     charTableList = [i.strip() for i in f.readlines()]

# CSET(charTableList)