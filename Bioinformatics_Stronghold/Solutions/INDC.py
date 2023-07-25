##  Independent Segregation of Chromosomes

"""
Problem
Consider a collection of coin flips. One of the most natural questions we can ask is if we flip a coin 92 times, what is the probability of obtaining 51 "heads", vs. 27 "heads", vs. 92 "heads"?

Each coin flip can be modeled by a uniform random variable in which each of the two outcomes ("heads" and "tails") has probability equal to 1/2. We may assume that these random variables are independent (see “Independent Alleles”); in layman's terms, the outcomes of the two coin flips do not influence each other.

A binomial random variable X
 takes a value of k
 if n
 consecutive "coin flips" result in k
 total "heads" and n−k
 total "tails." We write that X∈Bin(n,1/2)
.

Given: A positive integer n≤50
.

Return: An array A
 of length 2n
 in which A[k]
 represents the common logarithm of the probability that two diploid siblings share at least k
 of their 2n
 chromosomes (we do not consider recombination for now).

Sample Dataset
5

Sample Output
0.000 -0.004 -0.024 -0.082 -0.206 -0.424 -0.765 -1.262 -1.969 -3.010
"""

import math

with open("../datasets/INDC_dataset.txt",'r') as f:
    n = int(f.readline().strip())

N = 2*n

prob = 0.5

tmp = [0]

for k in range(N,1,-1):
    tmp.append(prob**N*math.factorial(N)/math.factorial(k)/math.factorial(N-k)+tmp[N-k])

tmp.append(1)

B = [round(math.log10(i),3) for i in tmp[-1:0:-1]]

print(" ".join(str(i) for i in B))