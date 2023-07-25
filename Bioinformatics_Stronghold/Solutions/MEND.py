##  Distances in Trees

"""
Problem

Figure 1. The rooted binary tree whose Newick format is (aa,((Aa,AA),AA)). Each leaf encodes the genotype of an ancestor for the given individual, which is represented by '?'.
A rooted binary tree can be used to model the pedigree of an individual. In this case, rather than time progressing from the root to the leaves, the tree is viewed upside down with time progressing from an individual's ancestors (at the leaves) to the individual (at the root).

An example of a pedigree for a single factor in which only the genotypes of ancestors are given is shown in Figure 1.

Given: A rooted binary tree T
 in Newick format encoding an individual's pedigree for a Mendelian factor whose alleles are A (dominant) and a (recessive).

Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root of T
 will exhibit the "AA", "Aa" and "aa" genotypes.

Sample Dataset
((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);

Sample Output
0.156 0.5 0.344
"""

##    define function
class node(object):
    nodes = {}
    def __init__(self,parent, num):
        self.num = num
        self.parent = parent
        self.child = set()
        self.poss={}
        self.genotype = ""

    def addChild(self, child):
        self.child.add(child)

    def calGenoType(self):
        if len(self.poss) > 0:
            return True
        nodeM, nodeF = [i for i in self.child]        
        if len(nodeM.poss) * len(nodeF.poss) !=0:
            mA = nodeM.poss["AA"]+nodeM.poss["Aa"]*0.5
            ma = nodeM.poss["aa"]+nodeM.poss["Aa"]*0.5
            fA = nodeF.poss["AA"]+nodeF.poss["Aa"]*0.5
            fa = nodeF.poss["aa"]+nodeF.poss["Aa"]*0.5
            self.poss["AA"] = mA*fA
            self.poss["Aa"] = mA*fa+ma*fA
            self.poss["aa"] = ma*fa
            return True
        return False

    def setGenoType(self, genotype):
        if genotype != "":
            self.genotype = genotype
            self.poss={"AA":0,"Aa":0,"aa":0}
            self.poss[genotype] = 1



##  build up the tree
def mendTree(treeSeq):
    root= node(None,0)
    cur = root
    genotype = ""
    num = 0
    for i in treeSeq:
        if i in ",)": 
            cur.setGenoType(genotype)
            genotype = ""
            cur = cur.parent
        if i in ",(":
            num += 1
            newChild = node(cur,num)
            root.nodes[num] = newChild
            cur.addChild(newChild)
            cur = newChild
        if i not in ",()":
            genotype += i
    return root
# recusive calculate the possilibity of genotype

def mend(node):
    while not node.calGenoType():
        for i in node.child:
            mend(i)
    return node.poss


## read input data

with open("../datasets/MEND_dataset.txt",'r') as f:
    treeSeq = f.readline().strip().replace(";","") 

root = mendTree(treeSeq)
print(" ".join(str(round(v,3)) for k,v in mend(root).items()))


##  Rosalind solution, without building the tree.
#   The order of the tokens of the Newick string is the algorithmic order of a depth-first-search in the tree. 
#   This means while parsing the tokens I can do the same operations I otherwise need a full-blown graph 
#       and a (recursive) depth-first-search function for. 
#   For this reason I prefer plain old parsing of the Newick string over the usage of external packages, 
#       which take the algorithmic order away, that is naturally provided by the Newick string.
#   Going without a recursive function requires explicitly creating a stack that is elsewise 
#       implicitly given in form of the function stack.

import re

def genotypes(newick):
    stack = [[]]
    for token in re.split('([(,)])', newick):
        if token == '(':
            stack += [[]]
        if token.isalpha():
            stack[-1] += [token.count('A') / 2]
        if token == ')':
            A = stack.pop()
            stack[-1] += [sum(A) / 2]
    a = 1 - A[0], 1 - A[1]
    return (A[0] * A[1],
             A[0] * a[1]
           + A[1] * a[0],
             a[0] * a[1])

with open("../datasets/MEND_dataset.txt",'r') as f:
    treeSeq = f.readline().strip().replace(";","") 

print(" ".join(str(round(i,3)) for i in genotypes(treeSeq)))