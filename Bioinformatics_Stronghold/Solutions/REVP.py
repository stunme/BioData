##  Locating Restriction Sites

"""
Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""


## define function 
from utility import readFastaFileList

def findReversePalindrome(seq:str, short = 2, long = 6):
    dic = {'A':'T',
           'T':'A',
           'G':'C',
           'C':'G',
                 }
    result = []
    for p in range(short-1,len(seq)-short):
        cur, next = p, p+1
        if dic[seq[cur]] == seq[next]:
            i = 1
            while i<long:
                cur, next = cur-1, next+1
                if cur<0 or next>=len(seq):
                    break
                if dic[seq[cur]] == seq[next]:
                    i +=1
                    result.append([cur+1,i*2])
                    continue
                else:
                    break
    return result


##  input dataset
seq = readFastaFileList("../datasets/REVP_dataset.txt")[0]
short = 4
long = 12

##  print output
for i in findReversePalindrome(seq,int(short/2), int(long/2)):
    print(f"{i[0]} {i[1]}")
