##  Finding a Shared Motif
##  skip data validation

from utility import readFastaFileList

def sharedMotif(seqList):
    seqList = sorted(seqList,key = len)
    for l in range(len(seqList[0]),1,-1):
        ## start from the shortest seq of seqList
        ## check seq with length (l)
        for pos in range(len(seqList[0])-l+1):
            ## starting postion of seq with length(l) in the shortest seq of seqList
            findIt = True
            tmp = seqList[0][pos:pos+l]

            for i in seqList[1:]:
                if i.find(tmp) == -1:
                    findIt = False
                    break
            if findIt:
                return tmp
            

print(sharedMotif(readFastaFileList("test.txt")))
