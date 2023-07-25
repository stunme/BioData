##  Reversal Distance

## Park's Greedy

"""
Problem
A reversal of a permutation creates a new permutation by inverting some interval of the permutation; (5,2,3,1,4)
, (5,3,4,1,2)
, and (4,1,2,3,5)
 are all reversals of (5,3,2,1,4)
. The reversal distance between two permutations π
 and σ
, written drev(π,σ)
, is the minimum number of reversals required to transform π
 into σ
 (this assumes that π
 and σ
 have the same length).

Given: A collection of at most 5 pairs of permutations, all of which have length 10.

Return: The reversal distance between each permutation pair.

Sample Dataset
1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

Sample Output
9 4 5 7 0
"""

## define fucntion
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


##  import dataset
dataset = []
with open("../datasets/REAR_dataset.txt","r") as f:
    for i in f.readlines():
        tmp = i.strip().split(" ")
        if len(tmp)>1:
            dataset.append(tmp)

##  print result
print(" ".join(str(rear(dataset[i],dataset[i+1])) for i in range(0,len(dataset),2)))
    
    