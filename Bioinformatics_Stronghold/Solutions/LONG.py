##  Genome Assembly as Shortest Superstring

"""
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC
"""

##   define function 
from utility import readFastaFileList

def long(seqList):
    n = len(seqList)
    L = len(seqList[0])
    l = int(L/2+1)

    dic = {}
    pathTree = {}
    leftSet = set([])
    for i in range(n):
        j = 0
        while j<n:
            if i == j:
                j += 1
                continue
            for k in range(L-1,l-1,-1):
                if seqList[j][:k] == seqList[i][-k:]:
                    dic[(i,j)] = -k
                    leftSet.add(i)
                    pathTree[j] = i
                    j = n
                    break
            j += 1
                    #   'i' is the left sequence
                    #   'j' is the right sequence 
                    ##  assume only a unique way to reconstruct
                    #   stop search other right sequence once left/right match found
    for i in range(n):
        if i not in leftSet:
            break
    seq = seqList[i]
    for j in range(n-1):
        left = pathTree[i]
        seq = seqList[left][:dic[(pathTree[i],i)]]+seq
        i = left   
    return seq

with open("result.txt","w") as f:
    f.write(long(readFastaFileList("../datasets/LONG_dataset.txt")))

