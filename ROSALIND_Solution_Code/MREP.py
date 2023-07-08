##  Identifying Maximal Repeats


## generate max-repeats from suffix tree, not during build the tree up
#  

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



# def mrep(root,seq,n):
#     result = {}
#     def traceDown(node,upSeq):
#         endPos = node.seq[0]+node.seq[1]
#         # print(upSeq+seq[node.seq[0]:endPos])
#         if len(node.child)>0 and len(upSeq)+node.seq[1] >= n:
#             if (endPos in result) and result[endPos] < node.seq[0]-len(upSeq):
#                 return     
#             result[endPos] = node.seq[0]-len(upSeq)
#         selfSeq = upSeq+seq[node.seq[0]:endPos]
#         for c in node.child:
#            traceDown(node.child[c],selfSeq)
    
#     traceDown(root,"")
#     return result


def mrep(root,seq,n):
    result = []
    seqDict = {}
    def traceDown(node,upSeq):
        endPos = node.seq[0]+node.seq[1]
        selfSeq = upSeq+seq[node.seq[0]:endPos]
        for key,c in node.child.items():
            if len(selfSeq) >= n:
                if selfSeq in seqDict:
                    seqDict[selfSeq].add(seq[c.seq[0]-len(selfSeq)-1])    
                # result.append((c.seq[0]-len(selfSeq), c.seq[0]))
                else:
                     seqDict[selfSeq] = {seq[c.seq[0]-len(selfSeq)-1]}
            traceDown(c,selfSeq)
    
    traceDown(root,"")

    return seqDict




with open("test.txt",'r') as f:
    seq = f.readline().strip()

if seq[-1] != '$':
    seq += '$'

n = 20
nodes = suff(seq)

mrep(nodes[0],seq, n)
for key, value in mrep(nodes[0],seq, n).items():
    if len(value) > 1:
        print(key)