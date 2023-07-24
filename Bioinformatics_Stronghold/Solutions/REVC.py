##	Complementing a Strand of DNA

"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s
.

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT

"""


## define function 
def reverseComplement(seq):
    dic = {'A':'T',
           'T':'A',
           'G':'C',
           'C':'G',
           }
    return ''.join(dic[n] for n in seq[::-1])

##  input dataset
with open("../datasets/REVC_dataset.txt",'r') as f:
    seq = f.readline().strip()

##  print output
print(reverseComplement(seq))