##  Reversal Distance

## Park's Greedy


def score(seq):
    """return break points number"""
    seq = (-1,)+seq+(len(seq),)
    s = 0
    for i in range(1,len(seq)):
        if abs(seq[i]-seq[i-1]) != 1:
            s += 1
    return s

import itertools as it

def rear(seqTarget,seq):
    """Calculate revesal distance"""
    if seqTarget == seq:
        return 0
    targetDict = {}
    for i in range(len(seq)):
        targetDict[seqTarget[i]] = i 
    tranSeq = tuple(targetDict[i] for i in seq)
    count = 0
    stack = {tranSeq}
    minScore = len(seq)
    ## Greedy Algorithm, pushing seq with minimal break point(s) in stack
    while True:
        tmpStack = stack.copy()
        for s in stack:
            for a,b in it.combinations(range(len(seq)),2):
                tmpSeq = tuple(s[:a]+tuple([s[i] for i in range(b,a-1,-1)])+s[b+1:])
                if tmpSeq not in tmpStack:
                    n = score(tmpSeq)
                    if minScore > n:
                        minScore = n
                        tmpStack = {tmpSeq}
                    elif minScore == n:
                        tmpStack.add(tmpSeq)
        count += 1
        if minScore == 0:
            return count
        stack = tmpStack.copy()
    
dataset = []
with open("test.txt","r") as f:
    for i in f.readlines():
        tmp = i.strip().split(" ")
        if len(tmp)>1:
            dataset.append(tmp)

print(" ".join(str(rear(dataset[i],dataset[i+1])) for i in range(0,len(dataset),2)))
    
    