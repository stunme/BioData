##  Distances in Trees

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
        if i == "(":
            num += 1
            newChild = node(cur, num)
            cur.addChild(newChild)
            cur = newChild
        elif i == ")": 
            if name in items:
                if len(items) == 1:
                    break
                else:
                    items.remove(name)
                    tmp = cur
            name = ""
            cur = cur.parent
        elif i == ",":
            if name in items:
                if len(items) == 1:
                    break
                else:
                    items.remove(name)
                    tmp = cur 
            name = ""
            cur = cur.parent
            num += 1
            newChild = node(cur,num)
            cur.addChild(newChild)
            cur = newChild
        else:
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

with open("test.txt",'r') as f:
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

def nwck(filename):
    (n, tree, taxa) = stripLines(filename)
    taxa = taxa.split()
    tokens = iter(re.split('([(),])', tree))
    while next(tokens) not in taxa:
        pass
    climbs = 0
    descents = 0
    for token in tokens:
        if token in taxa:
        break
        if token in ',)':
        if descents > 0:
            descents -= 1
        else:
            climbs += 1
        if token in ',(':
        descents += 1
    print climbs + descents
