##  Interleaving Two Motifs
## same mapping stratage to lcsq, but add seq at every step of traceback

"""
Problem
A string s
 is a supersequence of another string t
 if s
 contains t
 as a subsequence.

A common supersequence of strings s
 and t
 is a string that serves as a supersequence of both s
 and t
. For example, "GACCTAGGAACTC" serves as a common supersequence of "ACGTC" and "ATAT". A shortest common supersequence of s
 and t
 is a supersequence for which there does not exist a shorter common supersequence. Continuing our example, "ACGTACT" is a shortest common supersequence of "ACGTC" and "ATAT".

Given: Two DNA strings s
 and t
.

Return: A shortest common supersequence of s
 and t
. If multiple solutions exist, you may output any one.

Sample Dataset
ATCTGAT
TGCATA

Sample Output
ATGCATGAT
"""

##  define function
def scsp(seqI, seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    arr.append([0]*lenJ)
    for i in range(1,lenI):
        arr.append([0]*lenJ)
        for j in range(1,lenJ):
           if seqI[i-1] == seqJ[j-1]:
               arr[i][j] = arr[i-1][j-1]+1
           else:
               arr[i][j] = max(arr[i-1][j],arr[i][j-1])

    seq = ""
    while i*j!=0:
        if arr[i][j] == arr[i-1][j]:
            i -= 1
            seq = seqI[i]+seq
        elif arr[i][j] == arr[i][j-1]:
            j -= 1
            seq = seqJ[j]+seq
        else:
            i -=1
            seq = seqI[i]+seq
            j -=1
    
    return seqI[:i]+seqJ[:j]+seq

## import dataset
with open("../datasets/SCSP_dataset.txt",'r') as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()

##  print result
print(scsp(seq1,seq2))

