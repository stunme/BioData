##  Fixing an Inconsistent Character Set

"""
Problem
A submatrix of a matrix M
 is a matrix formed by selecting rows and columns from M
 and taking only those entries found at the intersections of the selected rows and columns. We may also think of a submatrix as formed by deleting the remaining rows and columns from M
.

Given: An inconsistent character table C
 on at most 100 taxa.

Return: A submatrix of C′
 representing a consistent character table on the same taxa and formed by deleting a single row of C
. (If multiple solutions exist, you may return any one.)

Sample Dataset
100001
000110
111000
100111

Sample Output
000110
100001
100111
"""

##  define functions
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

##  import dataset
with open("../datasets/CSET_dataset.txt",'r') as f:
    charTableList = [i.strip() for i in f.readlines()]

##  output result to file
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

# with open("../datasets/CSET_dataset.txt",'r') as f:
#     charTableList = [i.strip() for i in f.readlines()]

# CSET(charTableList)