##  Creating a Character Table

"""
Problem
Given a collection of n
 taxa, any subset S
 of these taxa can be seen as encoding a character that divides the taxa into the sets S
 and Sc
; we can represent the character by S∣Sc
, which is called a split. Alternately, the character can be represented by a character array A
 of length n
 for which A[j]=1
 if the j
th taxon belongs to S
 and A[j]=0
 if the j
th taxon belongs to Sc
 (recall the "ON"/"OFF" analogy from “Counting Subsets”).

At the same time, observe that the removal of an edge from an unrooted binary tree produces two separate trees, each one containing a subset of the original taxa. So each edge may also be encoded by a split S∣Sc
.

A trivial character isolates a single taxon into a group of its own. The corresponding split S∣Sc
 must be such that S
 or Sc
 contains only one element; the edge encoded by this split must be incident to a leaf of the unrooted binary tree, and the array for the character contains exactly one 0 or exactly one 1. Trivial characters are of no phylogenetic interest because they fail to provide us with information regarding the relationships of taxa to each other. All other characters are called nontrivial characters (and the associated splits are called nontrivial splits).

A character table is a matrix C
 in which each row represents the array notation for a nontrivial character. That is, entry Ci,j
 denotes the "ON"/"OFF" position of the i
th character with respect to the j
th taxon.

Given: An unrooted binary tree T
 in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T
. The columns of the character table should encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any given character, the particular subset of taxa to which 1s are assigned is arbitrary.

Sample Dataset
(dog,((elephant,mouse),robot),cat);

Sample Output
00110
00111
"""

##  define function
import re
def ctbl(treeStr):
    tokens = re.split('([(),])',treeStr)
    charTable = [['1']]
    stack = [[1]]
    curLeft = 1
    for t in tokens:
        if t == '(':
            stack += [[curLeft]]
        elif t not in ',()':
            stack[-1].append(t)
        elif t == ')':
            cur = stack.pop()
            left,cur = cur[0], cur[1:]
            for i in range(len(cur)):
                charTable += [['0']*len(charTable[-1])]
                charTable[-1][0] = cur[i]
            curLeft += len(cur)
            for i in range(left):
                charTable[i].append('0')
            for i in range(left,curLeft):
                charTable[i].append('1')
    charTable.sort()
    for i in charTable:
        i.pop()
    return charTable[1:]

##  import dataset
with open("../datasets/CTBL_dataset.txt",'r') as f:
    treeStr = f.readline().strip().replace(";",'')

ctbl_ = ctbl(treeStr)

##  output result to a file
with open("result.txt",'w') as f:
    for i in range(1,len(ctbl_[0])):
        f.write("".join((j[i]) for j in ctbl_))
        f.write("\n")
