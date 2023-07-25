##  Newick Format with Edge Weights

"""
Problem
In a weighted tree, each edge is assigned a (usually positive) number, called its weight. The distance between two nodes in a weighted tree becomes the sum of the weights along the unique path connecting the nodes.

To generalize Newick format to the case of a weighted tree T
, during our repeated "key step," if leaves v1,v2,…,vn
 are neighbors in T
, and all these leaves are incident to u
, then we replace u
 with (v1:d1,v2:d2,…,vn:dn)u
, where di
 is now the weight on the edge {vi,u}
.

Given: A collection of n
 weighted trees (n≤40
) in Newick format, with each tree containing at most 200 nodes; each tree Tk
 is followed by a pair of nodes xk
 and yk
 in Tk
.

Return: A collection of n
 numbers, for which the k
th number represents the distance between xk
 and yk
 in Tk
.

Sample Dataset
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant

Sample Output
75 136
"""

## define fuction

class node(object):

    def __init__(self,parent, num):
        self.num = num
        self.parent = parent
        self.child = set()
        self.edge = 0
        self.name = ""

    def addChild(self, child):
        self.child.add(child)

    def addEdge(self, edge):
        self.edge = edge

    def addName(self,name):
        self.name = name

def nkew(treeSeq, taxas):
    root= node(None,0)
    cur = root
    item = ""
    num = 0
    ##  build up the tree, break when two taxas found
    for i in treeSeq:
        if i in ",)": 
            name, edge = item.split(":")
            item = ""
            cur.addName(name)
            cur.addEdge(int(edge))
            if name in taxas:
                if len(taxas) == 1:
                    taxaB = cur
                else:
                    taxas.remove(name)
                    taxaA = cur
            cur = cur.parent
        if i in ",(":
            num += 1
            newChild = node(cur, num)
            cur.addChild(newChild)
            cur = newChild    
        if i not in ",()":
            item += i

    ## trace down
    dist = 0
    nodeDic = {}
    while taxaA!=None:
        nodeDic[taxaA.num] = dist
        dist += taxaA.edge
        taxaA = taxaA.parent
    dist = 0   
    while taxaB!=None:
        if taxaB.num in nodeDic:
            return nodeDic[taxaB.num]+dist
        else:
            dist +=taxaB.edge
            taxaB = taxaB.parent
    return 0


## import dataset
dataList = []
with open("../datasets/NKEW_dataset.txt",'r') as f:
    for l in f.readlines() :
        tmp = l.strip()
        if ";" in tmp:
            treeSeq = tmp.replace(";","")
        elif tmp == "":
            continue
        else:
            dataList.append([treeSeq,set(l.split())])

##  print result
print(" ".join(str(nkew(k,v)) for k,v in dataList))