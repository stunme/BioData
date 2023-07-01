##  Encoding Suffix Trees

with open("test.txt","r") as f:
    seq = f.readline().strip()



class node(object):
    num = 0
    pos = 0
    parent = None
    child = []   #{ collection of children }
    def __init__(self, parent, pos, num) -> None:
        self.num = num
        self.pos = pos
        self.parent = parent
    
    def addChild(self,child):
        self.child.append(child)
    
    def delChild(self,child):
        self.child.remove(child)

    def upEdge(self):
        return (self.parent.num,self.num)


class suffTree(object):
    sequence = ""
    root = None
    nodes = set()  # { node as child }
    edge = {}   #{(parent(int),child(int)) : (start(int), end(int))}

    def __init__(self,seq) -> None:
        self.sequence == seq
        self.root = node()
        self.tree(seq)

    def tree(self, seq):
        endNodes = {}   # {Node}
        cur = None    # [child(Node)]
        pos = 0       # position in current edge  
        num = 2
        for i in range(len(seq)):
            nt = seq[i]
            tmp = [self.root]
            if not cur:
                if pos == cur.pos-cur.parent.pos:
                    tmp.insert(0,cur)
                else:
                    if seq[cur.parent.pos+pos] == nt:
                        pos +=1
                    else:
                        newNode = node(cur.parent,cur.parent.pos+pos,num)
                        num +=1
                        cur.parent.delChild(cur)
                        cur.parent.addChild(newNode)
                        self.nodes.add(newNode)
                        newNode.addChild(cur)
                        cur.changeParent(newNode)
                        tmp.insert(0,newNode)
            for x in tmp:
                for y in x.child:
                    if seq[y.parent.pos+1] == nt:
                        cur = y
                        pos = 1
                        break
                ## add new 
            
            














## O(n^2)

root = {}

## build up the tree
for i in range(len(seq)):
   cur = root
   for c in seq[i:]:
       if c not in cur:
           cur[c] = {}
       cur = cur[c]

## recursion for edges collection
edge = {} 
num = 1
def traceBack(node, seq, parent):
    global num
    if len(node) == 1:
        for i in node:
            traceBack(node[i],seq+i, parent)
    else:
        if seq:
            edge[(parent,num)]=seq
        cur = num
        for i in node:
            num+=1
            traceBack(node[i],i,cur)

## start recursion
traceBack(root,"",1)

with open("result.txt","a") as f:
    for n,e in edge.items():
        f.write(f"{e}\n")