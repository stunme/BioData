##  Sex-Linked Inheritance

"""
Problem
The conditional probability of an event A
 given another event B
, written Pr(A∣B)
, is equal to Pr(A and B)
 divided by Pr(B)
.

Note that if A
 and B
 are independent, then Pr(A and B)
 must be equal to Pr(A)×Pr(B)
, which results in Pr(A∣B)=Pr(A)
. This equation offers an intuitive view of independence: the probability of A
, given the occurrence of event B
, is simply the probability of A
 (which does not depend on B
).

In the context of sex-linked traits, genetic equilibrium requires that the alleles for a gene k
 are uniformly distributed over the males and females of a population. In other words, the distribution of alleles is independent of sex.

Given: An array A
 of length n
 for which A[k]
 represents the proportion of males in a population exhibiting the k
-th of n
 total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n
 genes.

Return: An array B
 of length n
 in which B[k]
 equals the probability that a randomly selected female will be a carrier for the k
-th gene.

Sample Dataset
0.1 0.5 0.8

Sample Output
0.18 0.5 0.32
"""


with open('../datasets/DNA_dataset.txt') as f:
    A = map(float,f.readline().strip().split(" "))
    

B = [round(2*(x - x**2),3) for x in A]

print(' '.join(map(str,B)))
