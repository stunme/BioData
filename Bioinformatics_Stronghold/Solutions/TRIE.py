## Introduction to Pattern Matching

"""
Problem

Figure 1. The trie corresponding to the strings 'apple', 'apropos', 'banana', 'bandana', and 'orange'. Each path from root to leaf encodes one of these strings.
Given a collection of strings, their trie (often pronounced "try" to avoid ambiguity with the general term tree) is a rooted tree formed as follows. For every unique first symbol in the strings, an edge is formed connecting the root to a new vertex. This symbol is then used to label the edge.

We may then iterate the process by moving down one level as follows. Say that an edge connecting the root to a node v
 is labeled with 'A'; then we delete the first symbol from every string in the collection beginning with 'A' and then treat v
 as our root. We apply this process to all nodes that are adjacent to the root, and then we move down another level and continue. See Figure 1 for an example of a trie.

As a result of this method of construction, the symbols along the edges of any path in the trie from the root to a leaf will spell out a unique string from the collection, as long as no string is a prefix of another in the collection (this would cause the first string to be encoded as a path terminating at an internal node).

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.

Return: The adjacency list corresponding to the trie T
 for these patterns, in the following format. If T
 has n
 nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n
 in any order you like. Each edge of the adjacency list of T
 will be encoded by a triple containing the integer representing the edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the edge.

Sample Dataset
ATAGA
ATC
GAT

Sample Output
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T
"""

with open("../datasets/TRIE_dataset.txt",'r') as f:
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

##  write result to a file
with open("result.txt","w") as f:
    for i in range(2,len(T)):
        f.write(" ".join(str(j) for j in result[i]))
        f.write('\n')
