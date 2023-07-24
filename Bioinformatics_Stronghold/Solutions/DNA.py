## Counting DNA Nucleotides

"""
Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.

"""

## function define

def countDNA(seq):
    dic = {"A": 0,
           "C": 0,
           "G": 0,
           "T": 0,
           }
    for n in seq:
        dic[n] += 1
    return dic

##  input dataset
with open("../Dataset/DNA_dataset.txt",'r') as f:
    seq = f.readline().strip()

##  print output
print(" ".join(str(value) for key,value in countDNA(seq).items()))
