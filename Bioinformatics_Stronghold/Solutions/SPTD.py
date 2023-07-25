##  Phylogeny Comparison with Split Distance

#copy code from CTBL.py, get complete charTable for each taxaString, and caulcuate beased on the equation provided.

"""
Problem
Define the split distance between two unrooted binary trees as the number of nontrivial splits contained in one tree but not the other.

Formally, if s(T1,T2)
 denotes the number of nontrivial splits shared by unrooted binary trees T1
 and T2
, Then their split distance is dsplit(T1,T2)=2(n−3)−2s(T1,T2)
.

Given: A collection of at most 3,000 species taxa and two unrooted binary trees T1
 and T2
 on these taxa in Newick format.

Return: The split distance dsplit(T1,T2)
.

Sample Dataset
dog rat elephant mouse cat rabbit
(rat,(dog,cat),(rabbit,(elephant,mouse)));
(rat,(cat,dog),(elephant,(mouse,rabbit)));

Sample Output
2
"""

##  define functions
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
with open("../datasets/SPTD_dataset.txt",'r') as f:
    taxas = f.readline().strip().split()
    taxaTree1 = f.readline().strip().replace(";",'')
    taxaTree2 = f.readline().strip().replace(";",'')

ctbl1 = ctbl(taxaTree1)
ctbl2 = ctbl(taxaTree2)

set1 = set()
set2 = set()

for i in range(1,len(ctbl1[0])):
    set1.add("".join((j[i]) for j in ctbl1))
    set2.add("".join((j[i]) for j in ctbl2))

##  print result
print(2*(len(taxas)-3)-2*len(set1&set2))
