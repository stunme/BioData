##  Finding a Motif in DNA
##  For short motif, this works fine. For longer motif, might need ouse KMP searching or other

"""
Problem
Given two strings s
 and t
, t
 is a substring of s
 if t
 is contained as a contiguous collection of symbols in s
 (as a result, t
 must be no longer than s
).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
 of s
 is denoted by s[i]
.

A substring of s
 can be represented as s[j:k]
, where j
 and k
 represent the starting and ending positions of the substring in s
; for example, if s
 = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]
 = "UGCU".

The location of a substring s[j:k]
 is its beginning position j
; note that t
 will have multiple locations in s
 if it occurs more than once as a substring of s
 (see the Sample below).

Given: Two DNA strings s
 and t
 (each of length at most 1 kbp).

Return: All locations of t
 as a substring of s
.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
"""

## define function 

def subs(s,t):
    pos = []
    n = len(t)
    for i in range(len(s)-n+1):
        if s[i:i+n] == t:   
            pos.append(i+1)
    return pos

##  input dataset
with open("../datasets/SUBS_dataset.txt",'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

##  print output
print(' '.join(str(n) for n in subs(s,t)))