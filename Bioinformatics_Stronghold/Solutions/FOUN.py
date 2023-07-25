##  The Founder Effect and Genetic Drift 
##  Copy the code from WFMD. only change the return of probability() 

"""
Problem
Given: Two positive integers N
 and m
, followed by an array A
 containing k
 integers between 0 and 2N
. A[j]
 represents the number of recessive alleles for the j
-th factor in a population of N
 diploid individuals.

Return: An m×k
 matrix B
 for which Bi,j
 represents the common logarithm of the probability that after i
 generations, no copies of the recessive allele for the j
-th factor will remain in the population. Apply the Wright-Fisher model.

Sample Dataset
4 3
0 1 2

Sample Output
0.0 -0.463935575821 -0.999509892866
0.0 -0.301424998891 -0.641668367342
0.0 -0.229066698008 -0.485798552456
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
                next[i] += binomial(n-1, i, j) * current[j]         
        current = next
    return current[-k]

##  import dataset
with open("../datasets/FOUN_dataset.txt",'r') as f:
    N,m = map(int,f.readline().split())
    A = [i for i in map(int,f.readline().split())]

##  print result
for x in range(1,m+1):
    print(" ".join(str(math.log(probability(N, y, x, 0),10)) for y in A))

