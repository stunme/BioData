##  Counting Point Mutations

"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), 
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
.

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7

"""

## define function 
def countMutations(seq1, seq2):
    return sum(a!=b for a,b in zip(seq1,seq2))

##  input dataset
with open("../datasets/HAMM_dataset.txt",'r') as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()

##  print output
print(countMutations(seq1,seq2))
        