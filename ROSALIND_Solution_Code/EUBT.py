##  Enumerating Unrooted Binary Trees 

import itertools as it

class node(object):
    def __init__(self,taxas,parent) -> None:
        self.taxas = taxas
        self.childPairs = []
        self.parent = parent
        # self.idx = idx

with open("test.txt",'r') as f:
    taxaList = tuple(f.readline().strip().split())

# leaves = []
# end = []

def buildTree(taxaList, parent):
    cur = node(taxaList, parent)
    if len(cur.taxas) > 1:
        for i in range(1,len(cur.taxas)):
            for x in it.combinations(cur.taxas[1:],i):
                y = list(cur.taxas[:])
                for j in x:
                    y.remove(j)
                cur.childPairs.append([buildTree(x,cur),buildTree(tuple(y),cur)])
    # else:
    #     leaves.append(cur)
    return cur

root = node(taxaList,None)

import time

start = time.time()

checker = set()
for i in range(1,len(taxaList)):
    for x in it.combinations(taxaList[1:],i):
        tmp1 = [m for m in taxaList if m not in x]
        for j in range(1,len(tmp1)):
            for y in it.combinations(tmp1[1:],j):
                tmp2 = tuple([m for m in tmp1 if m not in y])
                ct = [""]*6
                for m in range(len(taxaList)):
                    if taxaList[m] in tmp2:
                        ct[0] += "1"
                        ct[1] += "0"
                    else:
                        ct[0] += "0"
                        ct[1] += "1"
                for m in range(len(taxaList)):
                    if taxaList[m] in y:
                        ct[2] += "1"
                        ct[3] += "0"
                    else:
                        ct[2] += "0"
                        ct[3] += "1"
                for m in range(len(taxaList)):
                    if taxaList[m] in x:
                        ct[4] += "1"
                        ct[5] += "0"
                    else:
                        ct[4] += "0"
                        ct[5] += "1"
                noFind = True
                for m in ct:
                    if m.count("0")<2 or m.count("1")<2:
                        continue
                    elif m in checker:
                        noFind = False
                        break
                if noFind:
                    for m in ct:
                        checker.add(m)
                    root.childPairs.append([buildTree(x,root),buildTree(tmp2,root),buildTree(y,root)])

print(time.time()-start)

def getNewick(node):
    strList = []
    if len(node.childPairs) == 0:
        strList.append(node.taxas[0])
    else:
        for c in node.childPairs:
            for x in getNewick(c[0]):
                for y in getNewick(c[1]):
                    if len(c)>2:
                        for z in getNewick(c[2]):
                            strList.append(f"({x},{y},{z})")
                    else:
                        strList.append(f"({x},{y})")
    return strList

import functools
start = time.time()
print(len(getNewick(root)),functools.reduce(lambda a, b: a*b % 10**6, range(2*len(taxaList)-5, 1, -2))) 
print(time.time()-start)
for i in getNewick(root):
    print(f"{i};")