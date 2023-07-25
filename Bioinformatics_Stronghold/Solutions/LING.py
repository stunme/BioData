##  Linguistic Complexity of a Genome
## suffix tree solution. counting how many $ in the trees as sub(s)

"""
Problem
Given a length n
 string s
 formed over an alphabet A
 of size a
, let the "substring count" sub(s)
 denote the total number of distinct substrings of s
. Furthermore, let the "maximum substring count" m(a,n)
 denote the maximum number of distinct substrings that could appear in a string of length n
 formed over A
.

The linguistic complexity of s
 (written lc(s)
) is equal to sub(s)m(a,n)
; in other words, lc(s)
 represents the percentage of observed substrings of s
 to the total number that are theoretically possible. Note that 0<lc(s)<1
, with smaller values of lc(s)
 indicating that s
 is more repetitive.

As an example, consider the DNA string (a=4
) s=ATTTGGATT
. In the following table, we demonstrate that lc(s)=3540=0.875
 by considering the number of observed and possible length k
 substrings of s
, which are denoted by subk(s)
 and m(a,k,n)
, respectively. (Observe that m(a,n)=∑nk=1m(a,k,n)=40
 and sub(s)=∑nk=1subk(s)=35
.)

k
subk(s)
m(a,k,n)
1	3	4
2	5	8
3	6	7
4	6	6
5	5	5
6	4	4
7	3	3
8	2	2
9	1	1
Total	35	40
Given: A DNA string s
 of length at most 100 kbp.

Return: The linguistic complexity lc(s)
.

Sample Dataset
ATTTGGATT

Sample Output
0.875
"""

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

##  import dataset
with open("../datasets/LING_dataset.txt",'r') as f:
    seq = f.readline().strip()

##  print result
print(ling(seq))
