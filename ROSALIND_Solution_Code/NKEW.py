##  Newick Format with Edge Weights

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


## read input data

dataList = []

with open("test.txt",'r') as f:
    for l in f.readlines() :
        tmp = l.strip()
        if ";" in tmp:
            treeSeq = tmp.replace(";","")
        elif tmp == "":
            continue
        else:
            dataList.append([treeSeq,set(l.split())])


print(" ".join(str(nkew(k,v)) for k,v in dataList))