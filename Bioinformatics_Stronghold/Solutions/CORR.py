##  Error Correction in Reads 

"""
Problem
As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly.

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s
 in the dataset, one of the following applies:

s
 was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s
 is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

Sample Dataset
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC

Sample Output
TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA
"""

##  define function
from utility import readFastaFileList

def corr(seqList):
    n = len(seqList)
    rcList = [s.translate(str.maketrans("ATGC","TACG"))[::-1] for s in seqList]
    idxSet = set([i for i in range(n)])
    matchList = []
    
    ## obtain idxSet, which only contain unmatched seq
    i = 0
    while i< n: 
        if i in idxSet:
            for j in range(i+1,n):
                if j in idxSet:
                    if seqList[i] == seqList[j] or seqList[i] == rcList[j]:
                        if i in idxSet:
                            idxSet.remove(i)
                            matchList.append(i)
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
        for n in matchList:
            tmp = newSeq(m,n)
            if tmp!="":
                with open("result.txt",'a') as f:
                    f.write(f"{seqList[m]}->{tmp}\n")
                break

corr(readFastaFileList("../datasets/CORR_dataset.txt"))


##  ====================================================================================
##  more readable and shorter solution from Rosalind. But about 2.5 times slower. 


def revcomp(s):
    return s.translate(str.casefoldmaketrans('ACTG','TGAC'))[::-1]

def hamming(s,t):
    return len([x for x, y in zip(s,t) if x != y])

def include_revcomp(reads):
    return reads[:] + [ revcomp(read) for read in reads]

reads = readFastaFileList("../datasets/CORR_dataset.txt")
reads_and_revcomp = include_revcomp(reads)
correct_reads = set( include_revcomp( [ read for read in reads if reads_and_revcomp.count(read) > 1 ] ) )

res=""
for read in (set(reads) - correct_reads):
    with open("result.txt","w") as f:
        f.write(f"{read}->{[ r2 for r2 in correct_reads if hamming(r2,read) == 1 ][0]}")
