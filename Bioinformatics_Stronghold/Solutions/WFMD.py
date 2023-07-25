##  The Wright-Fisher Model of Genetic Drift
##  idea and main code copied from https://github.com/timothymahajan/Project-Rosalind-Bioinformatics-Stronghold/blob/master/087_WFMD/WFMD.py

"""
Problem
Consider flipping a weighted coin that gives "heads" with some fixed probability p
 (i.e., p
 is not necessarily equal to 1/2).

We generalize the notion of binomial random variable from “Independent Segregation of Chromosomes” to quantify the sum of the weighted coin flips. Such a random variable X
 takes a value of k
 if a sequence of n
 independent "weighted coin flips" yields k
 "heads" and n−k
 "tails." We write that X∈Bin(n,p)
.

To quantify the Wright-Fisher Model of genetic drift, consider a population of N
 diploid individuals, whose 2N
 chromosomes possess m
 copies of the dominant allele. As in “Counting Disease Carriers”, set p=m2N
. Next, recall that the next generation must contain exactly N
 individuals. These individuals' 2N
 alleles are selected independently: a dominant allele is chosen with probability p
, and a recessive allele is chosen with probability 1−p
.

Given: Positive integers N
 (N≤7
), m
 (m≤2N
), g
 (g≤6
) and k
 (k≤2N
).

Return: The probability that in a population of N
 diploid individuals initially possessing m
 copies of a dominant allele, we will observe after g
 generations at least k
 copies of a recessive allele. Assume the Wright-Fisher model.

Sample Dataset
4 6 2 1

Sample Output
0.772
"""

import math

def binomial(n, i, m):
    return (math.factorial(n) / math.factorial(i) / math.factorial(n-i)) * ((m/n)**i * (1-(m/n))**(n-i))

def probability(N, m, g, k):
    n = N * 2+1
    current = [0]*(n)
    current[m] = 1
    for z in range(g):
        next = [0]*(n)
        for i in range(n):
            for j in range(n):
                next[i] += binomial(float(n-1), float(i), float(j)) * current[j]         
        current = next
    return sum(current[:-k])

##  import dataset
with open("../datasets/WFMD_dataset.txt",'r') as f:
    N,m,g,k = map(int,f.readline().strip().split())

##  print result
print(probability(N, m, g, k))
