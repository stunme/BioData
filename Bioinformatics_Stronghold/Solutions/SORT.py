##  Sorting by Reversals

## Park's Greedy

"""
Problem
A reversal of a permutation can be encoded by the two indices at the endpoints of the interval that it inverts; for example, the reversal that transforms (4,1,2,6,3,5)
 into (4,1,3,6,2,5)
 is encoded by [3,5]
.

A collection of reversals sorts π
 into γ
 if the collection contains drev(π,γ)
 reversals, which when successively applied to π
 yield γ
.

Given: Two permutations π
 and γ
, each of length 10.

Return: The reversal distance drev(π,γ)
, followed by a collection of reversals sorting π
 into γ
. If multiple collections of such reversals exist, you may return any one.

Sample Dataset
1 2 3 4 5 6 7 8 9 10
1 8 9 3 2 7 6 5 4 10

Sample Output
2
4 9
2 5
"""

##  define function
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
    
##  import dataset
dataset = []
with open("../datasets/SORT_dataset.txt","r") as f:
    for i in f.readlines():
        tmp = i.strip().split(" ")
        if len(tmp)>1:
            dataset.append(tmp)

##  print result
sortResult = sort(dataset[1],dataset[0])
print(len(sortResult))
for i in sortResult:
    print(" ".join(str(j) for j in i))    
    