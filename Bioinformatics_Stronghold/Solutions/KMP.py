##  Speeding Up Motif Finding 

"""
Problem
A prefix of a length n
 string s
 is a substring s[1:j]
; a suffix of s
 is a substring s[k:n]
.

The failure array of s
 is an array P
 of length n
 for which P[k]
 is the length of the longest substring s[j:k]
 that is equal to some prefix s[1:k−j+1]
, where j
 cannot equal 1
 (otherwise, P[k]
 would always equal k
). By convention, P[1]=0
.

Given: A DNA string s
 (of length at most 100 kbp) in FASTA format.

Return: The failure array of s
.

Sample Dataset
>Rosalind_87
CAGCATGGTATCACAGCAGAG

Sample Output
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

##  define function
from utility import readFastaFileList

def kmp(seq):
    result = [0]*len(seq)
    for i in range(1,len(seq)):
        j = result[i-1]
        while j>0 and seq[i]!=seq[j]:
            j = result[j-1]
        if seq[i] == seq[j]:
            j += 1
        result[i] = j
    return result

##  import dataset
seq = readFastaFileList("../datasets/KMP_dataset.txt")[0]

##  print result
print(kmp(seq))

