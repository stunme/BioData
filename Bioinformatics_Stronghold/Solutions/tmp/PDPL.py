##  Creating a Restriction Map

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


with open("test.txt",'r') as f:
    cutDict = Counter(int(i) for i in f.readline().strip().split())

cutList = pdpl(cutDict)
cutList.sort()
print(" ".join(str(i) for i in cutList))