##  Linguistic Complexity of a Genome


## suffix tree solution. counting how many $ in the trees as sub(s)
def suff(seq):
    class node(object):
        def __init__(self) -> None:
            self.child = {}
            self.seq = (0,0)

    root = node()
    nodes = [root]
    
    for i in range(len(seq)):
        cur = root
        idx = 0
        for j in range(i,len(seq)):
            if idx == cur.seq[1]:
                if seq[j] in cur.child:
                    cur = cur.child[seq[j]]
                    idx = 1
                else:
                    cur.child[seq[j]] = node()
                    cur.child[seq[j]].seq = (j,len(seq)-j)
                    nodes.append(cur.child[seq[j]])
                    break
            else:
                if seq[j] == seq[cur.seq[0]+idx]:
                    idx += 1
                    continue
                else:
                    tmp = cur.child
                    tmpSeq = cur.seq
                    cur.seq = (tmpSeq[0],idx)
                    cur.child = {}
                    cur.child[seq[j]] = node()
                    cur.child[seq[j]].seq = (j,len(seq)-j)
                    nodes.append(cur.child[seq[j]])
                    cutPos = tmpSeq[0]+idx
                    cur.child[seq[cutPos]] = node()
                    cur.child[seq[cutPos]].seq = (cutPos,tmpSeq[1]-idx)
                    cur.child[seq[cutPos]].child = tmp
                    nodes.append(cur.child[seq[cutPos]])
                    break
    return nodes


import math

def ling(seq):
    n = len(seq)
    m = 0
    lg = int(math.log(n,4))
    for i in range(1,lg+1):
        m += 4**i
    for i in range(1,n-lg+1):
        m += i
    root = suff(seq)[0]

    def traceDown(node):
        count = node.seq[1]
        for k,v in node.child.items():
            count += traceDown(v)
        return count
    return traceDown(root)/m


with open("test.txt",'r') as f:
    seq = f.readline().strip()

print(ling(seq))
