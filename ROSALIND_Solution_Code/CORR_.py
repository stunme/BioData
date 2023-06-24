##  Error Correction in Reads 

from utility import readFastaFileList

def corr(seqList):
    n = len(seqList)
    rcList = [s.translate(str.maketrans("ATGC","TACG"))[::-1] for s in seqList]
    idxSet = set([i for i in range(n)])
    matchSet = []
    
    ## obtain idxSet, which only contain unmatched seq
    i = 0
    while i< n: 
        if i in idxSet:
            for j in range(i+1,n):
                if j in idxSet:
                    if seqList[i] == seqList[j] or seqList[i] == rcList[j]:
                        if i in idxSet:
                            idxSet.remove(i)
                            matchSet.append(i)
                        idxSet.remove(j)  
        i += 1

    def humm(seq1,seq2):
        ## stop comparing once humming distance is 2 and above
        count = 0
        for s1, s2 in zip(seq1,seq2):
            if s1 != s2:
                if count == 1:
                    return False
                count += 1
        return True        

    def newSeq(m, n):
        if humm(seqList[m],seqList[n]):
            return seqList[n]
        if humm(seqList[m],rcList[n]):
            return rcList[n]
        return ""

    for m in idxSet:
        for n in matchSet:
            tmp = newSeq(m,n)
            if tmp!="":
                with open("result.txt",'a') as f:
                    f.write(f"{seqList[m]}->{tmp}\n")
                break

corr(readFastaFileList("test.txt"))


##  more readable and shorter solution from Rosalind. But about 2.5 times slower. 


def revcomp(s):
    return s.translate(str.casefoldmaketrans('ACTG','TGAC'))[::-1]

def hamming(s,t):
    return len([x for x, y in zip(s,t) if x != y])

def include_revcomp(reads):
    return reads[:] + [ revcomp(read) for read in reads]

# reads = readFastaFileList("test.txt")
# reads_and_revcomp = include_revcomp(reads)
# correct_reads = set( include_revcomp( [ read for read in reads if reads_and_revcomp.count(read) > 1 ] ) )

# res=""
# for read in (set(reads) - correct_reads):
#     with open("result.txt","w") as f:
#         f.write(f"{read}->{[ r2 for r2 in correct_reads if hamming(r2,read) == 1 ][0]}")
