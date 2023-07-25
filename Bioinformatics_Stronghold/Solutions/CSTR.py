##  Creating a Character Table from Genetic Strings 

"""
Problem
A collection of strings is characterizable if there are at most two possible choices for the symbol at each position of the strings.

Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)

Sample Dataset
ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC

Sample Output
10110
10100
"""


##  define function
def cstr(seqList):
    result = set()
    for i in range(len(seqList[0])):
        cur = ""
        count = 0
        head = seqList[0][i]
        for s in seqList:
            if s[i] == head:
                cur += '1'
                count += 1
            else:
                cur += '0'
        if count>len(seqList)-2 or count<2:
            continue
        result.add(cur)

    return result


##  import dataset
with open("../datasets/CSTR_dataset.txt",'r') as f:
    seqList = [i.strip() for i in f.readlines()]

## output result to file
with open("result.txt",'w') as f:
    f.write('\n'.join(s for s in cstr(seqList)))
