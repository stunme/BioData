##  Wobble Bonding and RNA Secondary Structures

"""
Problem

Figure 1. A valid matching of basepair edges in the bonding graph of an RNA string, followed by a diagram of how this bonding will induce the resulting folded RNA.

Figure 2. All 12 possible valid basepair matchings in the bonding graph corresponding to the string s = CGAUGCUAG (including the trivial matching in which no edges are matched.) Courtesy Brian Tjaden.
Given an RNA string s
, we will augment the bonding graph of s
 by adding basepair edges connecting all occurrences of 'U' to all occurrences of 'G' in order to represent possible wobble base pairs.

We say that a matching in the bonding graph for s
 is valid if it is noncrossing (to prevent pseudoknots) and has the property that a basepair edge in the matching cannot connect symbols sj
 and sk
 unless k≥j+4
 (to prevent nearby nucleotides from base pairing).

See Figure 1 for an example of a valid matching if we allow wobble base pairs. In this problem, we will wish to count all possible valid matchings in a given bonding graph; see Figure 2 for all possible valid matchings in a small bonding graph, assuming that we allow wobble base pairing.

Given: An RNA string s
 (of length at most 200 bp).

Return: The total number of distinct valid matchings of basepair edges in the bonding graph of s
. Assume that wobble base pairing is allowed.

Sample Dataset
AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU

Sample Output
284850219977421
"""

## define function
dicAll ={}

def rnas(seq):
    if seq not in dicAll:
        if len(seq) < 5:
            return 1   
        sum =rnas(seq[1:])
        for i in range(4,len(seq)):
            if seq[0]+seq[i] in ["AU","UA","GU","UG","GC","CG"]:
                sum += rnas(seq[1:i])*rnas(seq[i+1:])
        dicAll[seq] = sum
    return dicAll[seq]

## import dataset
with open("../datasets/RNAS_dataset.txt","r") as f:
  seq = f.readline().strip()

## print result
print(rnas(seq))



