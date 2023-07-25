##  Bioinformatics_Stronghold/Solutions/tmp/RNAS.py

"""
Problem
Given three strings s
, t
, and u
, we say that t
 and u
 can be interwoven into s
 if there is some substring of s
 made up of t
 and u
 as disjoint subsequences.

For example, the strings "ACAG
" and "CCG
" can be interwoven into "GACCACGGTT
". However, they cannot be interwoven into "GACCACAAAAGGTT
" because of the appearance of the four 'A's in the middle of the subsequences. Similarly, even though both "ACACG
" is a shortest common supersequence of ACAG
 and CCG
, it is not possible to interweave these two strings into "ACACG
" because the two desired subsequences must be disjoint; see “Interleaving Two Motifs” for details on finding a shortest common supersequence of two strings.

Given: A text DNA string s
 of length at most 10 kbp, followed by a collection of n
 (n≤10
) DNA strings of length at most 10 bp acting as patterns.

Return: An n×n
 matrix M
 for which Mj,k=1
 if the j
th and k
th pattern strings can be interwoven into s
 and Mj,k=0
 otherwise.

Sample Dataset
GACCACGGTT
ACAG
GT
CCG

Sample Output
0 0 1
0 1 0
1 0 0
"""

##  define function, credit belong to Aleksandar Dimitriev, on Rosalind
def itwv(s, t1, t2):
    if len(t1) + len(t2) == 0:
        return True
    elif len(t1) == 0:
        return t2[0] == s[0] and itwv(s[1:], t1, t2[1:])
    elif len(t2) == 0:
        return t1[0] == s[0] and itwv(s[1:], t1[1:], t2)
    else:
        return t1[0] == s[0] and itwv(s[1:], t1[1:], t2) or t2[0] == s[0] and itwv(s[1:], t1, t2[1:])

##  import data
with open("../datasets/ITWV_dataset.txt","r") as f:
    s = f.readline().strip()
    seqList = [i.strip() for i in f.readlines()]

##  print result
for i in seqList:
    print(" ".join(str(int(itwv(s,i,j))) for j in seqList))
