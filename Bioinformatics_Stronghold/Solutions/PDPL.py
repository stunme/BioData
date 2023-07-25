##  Creating a Restriction Map

"""
Problem

Figure 1. In the simplified figure above, we know that the dashed segments came from a chromosome; we desire a collection of numbers whose differences match the lengths of the dotted lines, which will correspond to the locations of restriction sites on the unknown chromosome. Taken from Jones & Pevzner, An Introduction to Bioinformatics Algorithms.
For a set X
 containing numbers, the difference multiset of X
 is the multiset ΔX
 defined as the collection of all positive differences between elements of X
. As a quick example, if X={2,4,7}
, then we will have that ΔX={2,3,5}
.

If X
 contains n
 elements, then ΔX
 will contain one element for each pair of elements from X
, so that ΔX
 contains (n2)
 elements (see combination statistic). You may note the similarity between the difference multiset and the Minkowski difference X⊖X
, which contains the elements of ΔX
 and their negatives. For the above set X
, X⊖X
 is {−5,−3,−2,2,3,5}
.

In practical terms, we can easily obtain a multiset L
 corresponding to the distances between restriction sites on a chromosome. If we can find a set X
 whose difference multiset ΔX
 is equal to L
, then X
 will represent possible locations of these restriction sites. For an example, consult Figure 1.

Given: A multiset L
 containing (n2)
 positive integers for some positive integer n
.

Return: A set X
 containing n
 nonnegative integers such that ΔX=L
.

Sample Dataset
2 2 3 3 4 5 6 7 8 10

Sample Output
0 2 4 7 10
"""

##  define function
from collections import Counter
def pdpl(cutDict):
    allPos = {0}
    endPos = max(cutDict)

    def counterCut(cut,posSet):
        return Counter(abs(cut-i) for i in posSet)
    
    def isSubDict(dicA, dicB):
        return all(dicA[i] <= dicB[i] for i in dicA)

    while len(cutDict) > 0:
        curPos = max(cutDict)
        ## check if all pairwises of a cut are all in the cutDict, if so, remove all cuts.
        if isSubDict(counterCut(curPos, allPos), cutDict):
            allPos |= {curPos}
            cutDict -= counterCut(curPos, allPos)
        else:
            allPos |= {endPos - curPos}
            cutDict -= counterCut(endPos - curPos, allPos)
    
    return list(allPos)

##  import dataset
with open("../datasets/PDPL_dataset.txt",'r') as f:
    cutDict = Counter(int(i) for i in f.readline().strip().split())

cutList = pdpl(cutDict)
cutList.sort()

##  print result
print(" ".join(str(i) for i in cutList))