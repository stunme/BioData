### RNA Splicing

"""
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""

##  input dataset
##  print output
from utility import readFastaFileList
from DNASeq import DNASeq

seq = readFastaFileList("../datasets/SPLC_dataset.txt")
cDNA = seq[0]
for s in seq[1:]:
    cDNA = cDNA.replace(s,'')

print(DNASeq(cDNA).findOpenFrame()['Foward_0'][:-1])



