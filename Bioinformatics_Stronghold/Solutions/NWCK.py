##  Distances in Trees

"""
Problem

Figure 1. This tree can be represented in Newick format in a number of ways, including (C, D, (A, B)); (A, (D, C), B); and (((A, B), C), D);.
Newick format is a way of representing trees even more concisely than using an adjacency list, especially when dealing with trees whose internal nodes have not been labeled.

First, consider the case of a rooted tree T
. A collection of leaves v1,v2,…,vn
 of T
 are neighbors if they are all adjacent to some internal node u
. Newick format for T
 is obtained by iterating the following key step: delete all the edges {vi,u}
 from T
 and label u
 with (v1,v2,…,vn)u
. This process is repeated all the way to the root, at which point a semicolon signals the end of the tree.

A number of variations of Newick format exist. First, if a node is not labeled in T
, then we simply leave blank the space occupied by the node. In the key step, we can write (v1,v2,…,vn)
 in place of (v1,v2,…,vn)u
 if the vi
 are labeled; if none of the nodes are labeled, we can write (,,…,)
.

A second variation of Newick format occurs when T
 is unrooted, in which case we simply select any internal node to serve as the root of T
. A particularly peculiar case of Newick format arises when we choose a leaf to serve as the root.

Note that there will be a large number of different ways to represent T
 in Newick format; see Figure 1.

Given: A collection of n
 trees (n≤40
) in Newick format, with each tree containing at most 200 nodes; each tree Tk
 is followed by a pair of nodes xk
 and yk
 in Tk
.

Return: A collection of n
 positive integers, for which the k
th integer represents the distance between xk
 and yk
 in Tk
.

Sample Dataset
(cat)dog;
dog cat

(dog,cat);
dog cat

Sample Output
1 2
"""


class node(object):

   def __init__(self,parent, num):
      self.num = num
      self.parent = parent
      self.child = set()

   def addChild(self, child):
      self.child.add(child)


def nwck(treeSeq, items):
    root= node(None,0)
    cur = root
    name = ""
    num = 0
    ##  build up the tree, break when two items found
    for i in treeSeq:
        if i in ",)": 
            if name in items:
                if len(items) == 1:
                    break
                else:
                    items.remove(name)
                    tmp = cur
            name = ""
            cur = cur.parent
        if i in ",(":
            num += 1
            newChild = node(cur,num)
            cur.addChild(newChild)
            cur = newChild
        if i not in ",()":
            name += i

    # track back return distance
    if name in items:
        dist = 0
        nodeDic = {}
        while tmp!=None:
            nodeDic[tmp.num] = dist
            tmp = tmp.parent
            dist += 1
        dist = 0   
        while cur!=None:
            if cur.num in nodeDic:
                return nodeDic[cur.num]+dist
            else:
                cur = cur.parent
                dist += 1
    
    return 0


## read input data

dataList = []

with open("../datasets/NWCK_dataset.txt",'r') as f:
    for l in f.readlines() :
        tmp = l.strip()
        if ";" in tmp:
            treeSeq = tmp.replace(";","")
        elif tmp == "":
            continue
        else:
            dataList.append([treeSeq,set(l.split())])


print(" ".join(str(nwck(k,v)) for k,v in dataList))


##  Rosalind resolution
# No need to even build a tree--just traverse the notation as if it were a tree, 
# keeping track of unbalanced climbs and descents between the two desired strings. 
# The only trick is that "," is both a climb and a descent.

import re

def nwck1(treeSeq, taxas):
    items = iter(re.split('([(),])',treeSeq))
    while next(items) not in taxas:
        pass
    climbs = 0
    descents = 0
    for i in items:
        if i in taxas:
            break
        if i in ',)':
            if descents > 0:
                descents -= 1
            else:
                climbs += 1
        if i in ',(':
            descents += 1
    return climbs + descents


dataList=[]
with open("../datasets/NWCK_dataset.txt",'r') as f:
    for l in f.readlines() :
        tmp = l.strip()
        if ";" in tmp:
            treeSeq = tmp.replace(";","")
        elif tmp == "":
            continue
        else:
            dataList.append([treeSeq,set(l.split())])

print(" ".join(str(nwck1(k,v)) for k,v in dataList))