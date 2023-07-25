##  Ordering Strings of Varying Length Lexicographically

"""
Problem
Say that we have strings s=s1s2⋯sm
 and t=t1t2⋯tn
 with m<n
. Consider the substring t′=t[1:m]
. We have two cases:

If s=t′
, then we set s<Lext
 because s
 is shorter than t
 (e.g., APPLE<APPLET
).
Otherwise, s≠t′
. We define s<Lext
 if s<Lext′
 and define s>Lext
 if s>Lext′
 (e.g., APPLET<LexARTS
 because APPL<LexARTS
).
Given: A permutation of at most 12 symbols defining an ordered alphabet A
 and a positive integer n
 (n≤4
).

Return: All strings of length at most n
 formed from A
, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

Sample Dataset
D N A
3

Sample Output
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA
"""

##  define function
def generate(n, seq, item=""):
    if item !="":
        seq.append(item)
    if n == 0:
        return
    for s in symbol:
        generate(n-1, seq, item+s)

##  import dataset
with open("../datasets/LEXV_dataset.txt",'r') as f:
    symbol = [i for i in f.readline().strip().split(' ')]
    n = int(f.readline())

##  print result
seq = []
generate(n, seq)
print(len(seq))
print('\n'.join(i for i in seq))