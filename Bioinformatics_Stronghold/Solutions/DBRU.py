##  Constructing a De Bruijn Graph

"""
Problem
Consider a set S
 of (k+1)
-mers of some unknown DNA string. Let Src
 denote the set containing all reverse complements of the elements of S
. (recall from “Counting Subsets” that sets are not allowed to contain duplicate elements).

The de Bruijn graph Bk
 of order k
 corresponding to S∪Src
 is a digraph defined in the following way:

Nodes of Bk
 correspond to all k
-mers that are present as a substring of a (k+1)
-mer from S∪Src
.
Edges of Bk
 are encoded by the (k+1)
-mers of S∪Src
 in the following way: for each (k+1)
-mer r
 in S∪Src
, form a directed edge (r[1:k]
, r[2:k+1]
).
Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding to a set S
 of (k+1)
-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src
.

Sample Dataset
TGAT
CATG
TCAT
ATGC
CATC
CATC

Sample Output
(ATC, TCA)
(ATG, TGA)
(ATG, TGC)
(CAT, ATC)
(CAT, ATG)
(GAT, ATG)
(GCA, CAT)
(TCA, CAT)
(TGA, GAT)
"""


with open("../datasets/DBRU_dataset.txt",'r') as f:
    S = set([s.strip() for s in f.readlines()])

mapping = str.maketrans("ATGC","TACG")
S |= set([s.translate(mapping)[::-1] for s in S])

with open("result.txt",'a') as f:
    for s in S:
        f.write(f"({s[:-1]}, {s[1:]})\n")