##  Identifying Maximal Repeats
#   This solution seems not working on some data with overlap repeat sequence, e.g. GAATCGAATCGA
#   Is GAATCGA a max-repeats? If Yes, it works on all dataset
#   The two repeats overlapped with GA, one end with GA and another use the same GA as start

## generate max-repeats from suffix tree, not during build the tree up
#  

"""
Problem
A maximal repeat of a string s
 is a repeated substring t
 of s
 having two occurrences t1
 and t2
 such that t1
 and t2
 cannot be extended by one symbol in either direction in s
 and still agree.

For example, "AG" is a maximal repeat in "TAGTTAGCGAGA" because even though the first two occurrences of "AG" can be extended left into "TAG", the first and third occurrences differ on both sides of the repeat; thus, we conclude that "AG" is a maximal repeat. Note that "TAG" is also a maximal repeat of "TAGTTAGCGAGA", since its only two occurrences do not still match if we extend them in either direction.

Given: A DNA string s
 of length at most 1 kbp.

Return: A list containing all maximal repeats of s
 having length at least 20.

Sample Dataset
TAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTATTATATAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTAT

Sample Output
TAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTAT
ATGGGTCCAGAGTTTTGTAATTT
"""

##  define functions
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
                else:
                     seqDict[selfSeq] = {seq[c.seq[0]-len(selfSeq)-1]}
            traceDown(c,selfSeq)
    
    traceDown(root,"")

    return seqDict

##  import dataset
with open("../datasets/MREP_dataset.txt",'r') as f:
    seq = f.readline().strip()

if seq[-1] != '$':
    seq += '$'

n = 20
nodes = suff(seq)

##  print result
for key, value in mrep(nodes[0],seq, n).items():
    if len(value) > 1:
        print(key)

