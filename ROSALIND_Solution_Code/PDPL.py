##  Creating a Restriction Map

from collections import Counter
def pdpl(cutDict):
    allPos = {0}
    endPos = max(cutDict)

    pairwise = lambda cut, Set: Counter(abs(cut-i) for i in Set)
    isSubDict = lambda a, b: all(a[i] <= b[i] for i in a)

    while len(cutDict) > 0:
        curPos = max(cutDict)
        ## check if all pairwises of a cut are all in the cutDict, if so, remove all cuts.
        if isSubDict(pairwise(curPos, allPos), cutDict):
            allPos |= {curPos}
            cutDict -= pairwise(curPos, allPos)
        else:
            allPos |= {endPos - curPos}
            cutDict -= pairwise(endPos - curPos, allPos)
    
    return list(allPos)


with open("test.txt",'r') as f:
    cutDict = Counter(int(i) for i in f.readline().strip().split())

cutList = pdpl(cutDict)
cutList.sort()
print(" ".join(str(i) for i in cutList))