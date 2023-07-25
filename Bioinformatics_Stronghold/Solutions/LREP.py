##  Finding the Longest Multiple Repeat

"""
Problem

Figure 1. The suffix tree for s = GTCCGAAGCTCCGG. Note that the dollar sign has been appended to a substring of the tree to mark the end of s. Every path from the root to a leaf corresponds to a unique suffix of GTCCGAAGCTCCGG, and each leaf is labeled with the location in s of the suffix ending at that leaf.
A repeated substring of a string s
 of length n
 is simply a substring that appears in more than one location of s
; more specifically, a k-fold substring appears in at least k distinct locations.

The suffix tree of s
, denoted T(s)
, is defined as follows:

T(s)
 is a rooted tree having exactly n
 leaves.
Every edge of T(s)
 is labeled with a substring of s∗
, where s∗
 is the string formed by adding a placeholder symbol $ to the end of s
.
Every internal node of T(s)
 other than the root has at least two children; i.e., it has degree at least 3.
The substring labels for the edges leading from a node to its children must begin with different symbols.
By concatenating the substrings along edges, each path from the root to a leaf corresponds to a unique suffix of s∗
.
See Figure 1 for an example of a suffix tree.

Given: A DNA string s
 (of length at most 20 kbp) with $ appended, a positive integer k
, and a list of edges defining the suffix tree of s
. Each edge is represented by four components:

the label of its parent node in T(s)
;
the label of its child node in T(s)
;
the location of the substring t
 of s∗
 assigned to the edge; and
the length of t
.
Return: The longest substring of s
 that occurs at least k
 times in s
. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
CATACATAC$
2
node1 node2 1 1
node1 node7 2 1
node1 node14 3 3
node1 node17 10 1
node2 node3 2 4
node2 node6 10 1
node3 node4 6 5
node3 node5 10 1
node7 node8 3 3
node7 node11 5 1
node8 node9 6 5
node8 node10 10 1
node11 node12 6 5
node11 node13 10 1
node14 node15 6 5
node14 node16 10 1

Sample Output
CATAC
"""


with open("../datasets/LREP_dataset.txt","r") as f:
    seq = f.readline().strip()
    k = int(f.readline().strip())
    nodeList = [i.strip().split() for i in f.readlines()]

childIdxDic = {}
childIdxDic["node1"] = {"parent":"","pos":0,"len":0, "sumN":0}
for i in nodeList:
    childIdxDic[i[1]] = {"parent":i[0],"pos":int(i[2])-1,"len":int(i[3]), "sumN":0}

for i in nodeList:
    if seq[int(i[2])+int(i[3])-2] == "$":
        cur = i[1]
        childIdxDic["node1"]["sumN"] += 1
        while childIdxDic[cur]["parent"] != "":
            childIdxDic[cur]["sumN"] += 1
            cur = childIdxDic[cur]["parent"]

maxLenSeq = ""
for i in childIdxDic:
    if childIdxDic[i]["sumN"]>=k:
        cur = i
        curLenSeq = ""
        while childIdxDic[cur]["parent"] != "":
            curLenSeq = seq[childIdxDic[cur]["pos"]:childIdxDic[cur]["pos"]+childIdxDic[cur]["len"]] +  curLenSeq
            if len(maxLenSeq)<len(curLenSeq):
                maxLenSeq = curLenSeq
            cur = childIdxDic[cur]["parent"]


##  print result
print(maxLenSeq)
