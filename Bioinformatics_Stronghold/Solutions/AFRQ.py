##  Counting Disease Carriers

"""
Problem
To model the Hardy-Weinberg principle, assume that we have a population of N
 diploid individuals. If an allele is in genetic equilibrium, then because mating is random, we may view the 2N
 chromosomes as receiving their alleles uniformly. In other words, if there are m
 dominant alleles, then the probability of a selected chromosome exhibiting the dominant allele is simply p=m2N
.

Because the first assumption of genetic equilibrium states that the population is so large as to be ignored, we will assume that N
 is infinite, so that we only need to concern ourselves with the value of p
.

Given: An array A
 for which A[k]
 represents the proportion of homozygous recessive individuals for the k
-th Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.

Return: An array B
 having the same length as A
 in which B[k]
 represents the probability that a randomly selected individual carries at least one copy of the recessive allele for the k
-th factor.

Sample Dataset
0.1 0.25 0.5

Sample Output
0.532 0.75 0.914
"""


import math

with open('../datasets/AFRQ_dataset.txt','r') as f:
    A = map(float,f.readline().strip().split(" "))
    

B = [round(2*math.sqrt(i)-i,3) for i in A]

print(' '.join(map(str,B)))

