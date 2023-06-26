##  Genome Assembly with Perfect Coverage and Repeats

def addSeq(seq, newList,n):
    cur = seq[-n:]
    ## find all potential next subseq
    nextSet = set()
    for i in newList:
        tmp = i[:-1]
        if tmp == cur:
            nextSet.add(i)
    ## if find next subseq add it to seq
    if len(nextSet) > 0:
        for i in nextSet:
            ## recursion here. 
            # add last nuelciotide to the seq
            # provide a new list by removing the current subseq
            newList.remove(i)
            addSeq(seq+i[-1],[k for k in newList],n)
            newList.append(i)   
    
    ## if not print whole seq, only print the seq with all subseq linked.
    else:
        if len(seq) == len(seqList)+n:
            print(seq[:-n])


with open("test.txt",'r') as f:
    seqList = [i.strip() for i in f.readlines()]

seq = seqList[0]
addSeq(seq,seqList[1:],len(seq)-1)
