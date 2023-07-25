##  Genome Assembly with Perfect Coverage and Repeats


"""
Problem
Recall that a directed cycle is a cycle in a directed graph in which the head of one edge is equal to the tail of the following edge.

In a de Bruijn graph of k
-mers, a circular string s
 is constructed from a directed cycle s1→s2→...→si→s1
 is given by s1+s2[k]+...+si−k[k]+si−k+1[k]
. That is, because the final k−1
 symbols of s1
 overlap with the first k−1
 symbols of s2
, we simply tack on the k
-th symbol of s2
 to s
, then iterate the process.

For example, the circular string assembled from the cycle "AC" →
 "CT" →
 "TA" →
 "AC" is simply (ACT). Note that this string only has length three because the 2-mers "wrap around" in the string.

If every k
-mer in a collection of reads occurs as an edge in a de Bruijn graph cycle the same number of times as it appears in the reads, then we say that the cycle is "complete."

Given: A list Sk+1
 of error-free DNA (k+1)
-mers (k≤5
) taken from the same strand of a circular chromosome (of length ≤50
).

Return: All circular strings assembled by complete cycles in the de Bruijn graph Bk
 of Sk+1
. The strings may be given in any order, but each one should begin with the first (k+1)
-mer provided in the input.

Sample Dataset
CAG
AGT
GTT
TTT
TTG
TGG
GGC
GCG
CGT
GTT
TTC
TCA
CAA
AAT
ATT
TTC
TCA

Sample Output
CAGTTCAATTTGGCGTT
CAGTTCAATTGGCGTTT
CAGTTTCAATTGGCGTT
CAGTTTGGCGTTCAATT
CAGTTGGCGTTCAATTT
CAGTTGGCGTTTCAATT
"""

##  define function
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

##  import dataset
with open("../datasets/GREP_dataset.txt",'r') as f:
    seqList = [i.strip() for i in f.readlines()]

##  process dataset print result in function
seq = seqList[0]
addSeq(seq,seqList[1:],len(seq)-1)

