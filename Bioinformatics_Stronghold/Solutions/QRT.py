##  Quartets 

"""
Problem
A partial split of a set S
 of n
 taxa models a partial character and is denoted by A∣B
, where A
 and B
 are still the two disjoint subsets of taxa divided by the character. Unlike in the case of splits, we do not necessarily require that A∪B=S
; (A∪B)c
 corresponds to those taxa for which we lack conclusive evidence regarding the character.

We can assemble a collection of partial characters into a generalized partial character table C
 in which the symbol x
 is placed in Ci,j
 if we do not have conclusive evidence regarding the j
th taxon with respect to the i
th partial character.

A quartet is a partial split A∣B
 in which both A
 and B
 contain precisely two elements. For the sake of simplicity, we often will consider quartets instead of partial characters. We say that a quartet A∣B
 is inferred from a partial split C∣D
 if A⊆C
 and B⊆D
 (or equivalently A⊆D
 and B⊆C
). For example, {1,3}∣{2,4}
 and {3,5}∣{2,4}
 can be inferred from {1,3,5}∣{2,4}
.

Given: A partial character table C
.

Return: The collection of all quartets that can be inferred from the splits corresponding to the underlying characters of C
.

Sample Dataset
cat dog elephant ostrich mouse rabbit robot
01xxx00
x11xx00
111x00x

Sample Output
{elephant, dog} {rabbit, robot}
{cat, dog} {mouse, rabbit}
{mouse, rabbit} {cat, elephant}
{dog, elephant} {mouse, rabbit}
"""

##  define function
import itertools as it

def qrt(seq):
    charOn = [i for i in range(len(seq)) if seq[i]=="1"]
    charOff = [i for i in range(len(seq)) if seq[i]=="0"]
    for x in it.combinations(charOn,2):
        for y in it.combinations(charOff,2):
            yield x,y

##  parse dataset
with open("../datasets/QRT_dataset.txt",'r') as f:
    taxaList = f.readline().strip().split()
    charTable = [i.strip() for i in f.readlines()]

##  output result to file
qrtSet = set()
with open("result.txt",'w') as f:
    for c in charTable:
        for x,y in qrt(c):
            if (x,y) not in qrtSet and (y,x) not in qrtSet:
                f.write(f"{{{taxaList[x[0]]}, {taxaList[x[1]]}}} {{{taxaList[y[0]]}, {taxaList[y[1]]}}}\n")
                qrtSet.add((x,y))