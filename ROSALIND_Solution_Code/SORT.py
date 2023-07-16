##  Sorting by Reversals

## Park's Greedy


def score(seq):
    """return break points number"""
    seq = (-1,)+seq+(len(seq),)
    s = 0
    for i in range(1,len(seq)):
        if abs(seq[i]-seq[i-1]) != 1:
            s += 1
    return s

def reverse(seq,a,b):
    return tuple(seq[:a]+tuple([seq[i] for i in range(b,a-1,-1)])+seq[b+1:])

import itertools as it

def sort(seqTarget,seq):
    """Trace back to get Sorting by Reversals"""
    ## may reverse the seqTarget and seq roles below, then the return statement don't need [::-1]
    targetDict = {}
    for i in range(len(seq)):
        targetDict[seqTarget[i]] = i 
    tranSeq = tuple(targetDict[i] for i in seq)
    # count = 0
    stack = [{tranSeq:None}]
    minScore = len(seq)
    ## Greedy Algorithm, pushing seq with minimal break point(s) in stack
    while minScore > 0:
        stack.append(stack[-1].copy())
        for s in stack[-2]:
            for a,b in it.combinations(range(len(seq)),2):
                tmpSeq = reverse(s,a,b)
                if tmpSeq not in stack[-1]:
                    n = score(tmpSeq)
                    if minScore > n:
                        minScore = n
                        stack[-1] = {tmpSeq:(a,b)}
                    elif minScore == n:
                        stack[-1][tmpSeq] = (a,b)
    n = len(stack)-1
    curSeq = tuple(i for i in range(len(seq)))
    result = []
    while n>0:
        cur = stack[n][curSeq]
        curSeq = reverse(curSeq,cur[0],cur[1])
        result.append(tuple(i+1 for i in cur))
        n -= 1
    return result[::-1]
    
dataset = []
with open("test.txt","r") as f:
    for i in f.readlines():
        tmp = i.strip().split(" ")
        if len(tmp)>1:
            dataset.append(tmp)

sortResult = sort(dataset[1],dataset[0])
print(len(sortResult))
for i in sortResult:
    print(" ".join(str(j) for j in i))    
    