##Transcribing DNA into RNA

"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u  is formed by replacing all occurrences of 'T' in t  with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU

"""

## define function 
def transcribe(seq):
    return seq.replace("T","U")

##  input dataset
with open("../datasets/RNA_dataset.txt",'r') as f:
    seq = f.readline().strip()

##  print output
print(transcribe(seq))