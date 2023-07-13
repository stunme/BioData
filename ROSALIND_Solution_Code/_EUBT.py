##  Enumerating Unrooted Binary Trees 

import itertools as it

allTrees = []

def eubt(taxaList):
    if len(taxaList)<3:
        return taxaList
    for i in range(len(taxaList)-2):
        for j in it.combinations(taxaList[1:],i):
            subSetA =set(taxaList[:1]+[x for x in j])
            subSetB = {x for x in taxaList if x not in subSetA}
            
            

with open("test.txt",'r') as f:
    taxaList = f.readline().strip().split()


taxaList = [1,2,3,4,5]
allTrees.append(taxaList)

eubt()
# for i in eubt(taxaList):
    # print(i)
# 